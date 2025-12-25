"""
Deployment wrapper that avoids 'src' imports.

This file is placed at the root of backend/ and uses direct imports
to avoid the 'src' module import issue with cloudpickle.
"""
import sys
import os
from pathlib import Path

# Add current directory to path
_backend_dir = Path(__file__).parent
if str(_backend_dir) not in sys.path:
    sys.path.insert(0, str(_backend_dir))

# Now import using direct path manipulation
# We'll import everything we need here and re-export
import importlib.util

# Import config
config_spec = importlib.util.spec_from_file_location(
    "config", _backend_dir / "src" / "config.py"
)
config = importlib.util.module_from_spec(config_spec)
sys.modules["config"] = config
config_spec.loader.exec_module(config)

# Import orchestrator
orchestrator_spec = importlib.util.spec_from_file_location(
    "orchestrator", _backend_dir / "src" / "graph" / "orchestrator.py"
)
orchestrator = importlib.util.module_from_spec(orchestrator_spec)
sys.modules["orchestrator"] = orchestrator
orchestrator_spec.loader.exec_module(orchestrator)

# Import logging utils
logging_utils_spec = importlib.util.spec_from_file_location(
    "logging_utils", _backend_dir / "src" / "utils" / "logging_utils.py"
)
logging_utils = importlib.util.module_from_spec(logging_utils_spec)
sys.modules["logging_utils"] = logging_utils
logging_utils_spec.loader.exec_module(logging_utils)

# Now we can use these modules
get_project_id = config.get_project_id
get_location = config.get_location
get_staging_bucket = config.get_staging_bucket
GEMINI_MODEL_NAME = config.GEMINI_MODEL_NAME
build_langgraph_app = orchestrator.build_langgraph_app
get_logger = logging_utils.get_logger
setup_logging = logging_utils.setup_logging

# Rest of deployment code
from typing import Dict, Any, Optional
import vertexai
from vertexai import agent_engines

logger = get_logger(__name__)
setup_logging()


def create_agent_engine(
    display_name: str = "resume-matcher-langgraph",
    model_name: Optional[str] = None,
    temperature: float = 0.1,
    max_output_tokens: int = 2048,
) -> Any:
    """Create and deploy a LangGraph agent to Vertex AI Agent Engine."""
    project_id = get_project_id()
    location = get_location()
    model_name = model_name or GEMINI_MODEL_NAME
    staging_bucket = get_staging_bucket()
    
    if not staging_bucket:
        raise ValueError(
            "STAGING_BUCKET environment variable must be set for deployment."
        )
    
    logger.info(f"Initializing Vertex AI: project={project_id}, location={location}")
    
    vertexai.init(
        project=project_id,
        location=location,
        staging_bucket=staging_bucket
    )
    
    def runnable_builder(model: Any, **kwargs: Any) -> Any:
        """Builder function that returns the LangGraph app."""
        # Ensure path is set up
        if str(_backend_dir) not in sys.path:
            sys.path.insert(0, str(_backend_dir))
        
        # Build the graph
        return build_langgraph_app()
    
    try:
        logger.info(f"Creating LanggraphAgent with model: {model_name}")
        agent = agent_engines.LanggraphAgent(
            model=model_name,
            runnable_builder=runnable_builder,
            model_kwargs={
                "temperature": temperature,
                "max_output_tokens": max_output_tokens,
            },
        )
        
        logger.info(f"Deploying agent engine: {display_name}")
        
        requirements = [
            "google-cloud-aiplatform[agent_engines]>=1.60.0",
            "langgraph>=0.2.0",
            "langchain-core>=0.3.0",
            "pydantic>=2.0.0",
            "python-dotenv>=1.0.0",
            "typing-extensions>=4.8.0",
        ]
        
        # Include the entire backend directory
        extra_packages = [str(_backend_dir)]
        
        engine = agent_engines.create(
            agent_engine=agent,
            display_name=display_name,
            requirements=requirements,
            extra_packages=extra_packages,
        )
        
        logger.info(f"Agent Engine deployed successfully!")
        logger.info(f"Resource name: {engine.resource_name}")
        
        return engine
        
    except Exception as e:
        logger.error(f"Failed to deploy agent engine: {e}")
        raise


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "deploy":
        try:
            engine = create_agent_engine()
            print(f"\n✅ Deployment successful!")
            print(f"Resource name: {engine.resource_name}")
        except Exception as e:
            print(f"\n❌ Deployment failed: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    else:
        print("Usage: python deploy_wrapper.py deploy")

