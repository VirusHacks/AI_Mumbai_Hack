# Python LangGraph Multi-Agent Resume Matching Backend

A production-ready multi-agent system for resume-JD matching using LangGraph and Vertex AI Agent Engine. This system extracts structured information from resumes, scores multiple sections against job descriptions, and provides comprehensive matching analysis.

## Features

- **Resume Extraction Agent**: Extracts structured data from resume text using Vertex AI structured output
- **Section Scoring Agents**: Five specialized agents scoring:
  - Skills
  - Work Experience
  - Education
  - Projects
  - Meta Information (seniority, domains, languages)
- **LangGraph Orchestration**: Parallel execution of scoring agents with weighted aggregation
- **Vertex AI Agent Engine Deployment**: Deploy as a production-ready agent on Google Cloud

## Project Structure

```
backend/
├── src/
│   ├── config.py              # Vertex AI configuration
│   ├── models/
│   │   └── schemas.py         # Pydantic models for structured data
│   ├── agents/
│   │   ├── resume_extractor.py
│   │   ├── skills_agent.py
│   │   ├── experience_agent.py
│   │   ├── education_agent.py
│   │   ├── projects_agent.py
│   │   └── meta_agent.py
│   ├── graph/
│   │   └── orchestrator.py    # LangGraph workflow
│   ├── deploy/
│   │   └── agent_engine_deploy.py
│   └── utils/
│       ├── logging_utils.py
│       └── text_utils.py
├── main_local_test.py         # Local testing entrypoint
├── requirements.txt
├── pyproject.toml
└── samples/                    # Sample resume and JD files
```

## Setup

### Prerequisites

1. **Python 3.10+**
2. **Google Cloud Account** with:
   - Vertex AI API enabled
   - Agent Engine API enabled (if deploying)
   - Application Default Credentials configured

### Installation

1. **Clone and navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your Google Cloud project details
   ```

   Required variables:
   ```env
   GOOGLE_CLOUD_PROJECT=your-project-id
   VERTEX_AI_LOCATION=us-central1
   GEMINI_MODEL_NAME=gemini-2.0-flash-exp
   ```

5. **Authenticate with Google Cloud (choose one method):**

   **Option A: Using Service Account Key File (Recommended if gcloud CLI not installed)**
   
   1. Create a service account in Google Cloud Console
   2. Download the JSON key file
   3. Add to `.env`:
      ```env
      GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account-key.json
      ```
   
   **Option B: Using gcloud CLI (Requires installation)**
   
   1. Install Google Cloud SDK: https://cloud.google.com/sdk/docs/install
   2. Run:
      ```bash
      gcloud auth application-default login
      gcloud config set project your-project-id
      ```

## Usage

### Running the API Server

To integrate with the Next.js frontend, start the HTTP API server:

```bash
# From the backend directory
python api_server.py --port 8000
```

Or with environment variables:
```bash
PYTHON_BACKEND_URL=http://localhost:8000 python api_server.py
```

The server will be available at `http://localhost:8000` and accepts POST requests with:
```json
{
  "resume_text": "extracted resume text...",
  "job_description": "job description text..."
}
```

**Note:** Make sure to set `PYTHON_BACKEND_URL` in your Next.js `.env.local`:
```env
PYTHON_BACKEND_URL=http://localhost:8000
```

### Local Testing

Test the system locally without deploying to Agent Engine:

```bash
python main_local_test.py [resume.txt] [jd.txt]
```

If no arguments are provided, it will look for sample files in `samples/` directory.

Example:
```bash
python main_local_test.py samples/resume.txt samples/jd.txt
```

The output will include:
- Overall weighted score (0-100)
- Individual section scores with reasons
- Missing requirements for each section
- Overall comments and recommendations

### Running as a Python Module

You can also import and use the system programmatically:

```python
from src.graph.orchestrator import build_langgraph_app

# Build the app
app = build_langgraph_app()

# Prepare input
initial_state = {
    "resume_text": "...",
    "job_description": "..."
}

# Invoke
result = app.invoke(initial_state)
final_score = result["final_score"]
```

## Deployment to Vertex AI Agent Engine

**📖 For detailed deployment instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md)**

**⚡ For quick start, see [QUICK_START.md](./QUICK_START.md)**

### Quick Deployment Steps

1. **Prerequisites:**
   - Google Cloud Project with billing enabled
   - Vertex AI API enabled
   - IAM permissions (`roles/aiplatform.user`)
   - Authentication configured

2. **Configure `.env` file:**
   ```env
   GOOGLE_CLOUD_PROJECT=your-project-id
   VERTEX_AI_LOCATION=us-central1
   GEMINI_MODEL_NAME=gemini-2.0-flash-exp
   ```

3. **Deploy:**
   ```bash
   # Option 1: Using deployment script
   ./deploy.sh
   
   # Option 2: Manual deployment
   python -m src.deploy.agent_engine_deploy deploy
   ```

4. **Save the resource name** from the deployment output

5. **Test deployment:**
   ```bash
   export VERTEX_AGENT_ENGINE_RESOURCE="projects/.../agentEngines/..."
   python -m src.deploy.agent_engine_deploy test
   ```

### Calling the Deployed Agent

```python
from vertexai import agent_engines
import vertexai
from src.config import get_project_id, get_location

# Initialize
project_id = get_project_id()
location = get_location()
vertexai.init(project=project_id, location=location)

# Get deployed engine
resource_name = "projects/YOUR_PROJECT/locations/us-central1/agentEngines/RESOURCE_ID"
engine = agent_engines.get_agent_engine(resource_name=resource_name)

# Query
response = engine.query({
    "resume_text": "...",
    "job_description": "..."
})

final_score = response["final_score"]
```

For complete deployment guide, troubleshooting, and best practices, see [DEPLOYMENT.md](./DEPLOYMENT.md).

## Scoring Weights

The system uses weighted aggregation for the final score:

- **Skills**: 35%
- **Experience**: 35%
- **Education**: 15%
- **Projects**: 10%
- **Meta**: 5%

These weights can be adjusted in `src/graph/orchestrator.py`.

## Scoring Rubric

Each section is scored 0-100:

- **90-100**: Strong match on most key requirements
- **60-89**: Partial match, some gaps
- **30-59**: Weak match, many important gaps
- **0-29**: Almost no alignment

## Development

### Project Structure

- **`src/config.py`**: Configuration and Vertex AI client setup
- **`src/models/schemas.py`**: Pydantic models for type safety
- **`src/agents/`**: Individual agent implementations
- **`src/graph/orchestrator.py`**: LangGraph workflow definition
- **`src/utils/`**: Utility functions for text processing and logging

### Adding New Agents

1. Create a new agent file in `src/agents/`
2. Implement a node function following the pattern of existing agents
3. Add the node to the orchestrator in `src/graph/orchestrator.py`
4. Add appropriate edges in the graph

### Testing

Run local tests:
```bash
python main_local_test.py
```

Check logs for debugging:
```bash
# Set log level in main_local_test.py or use environment variable
LOG_LEVEL=DEBUG python main_local_test.py
```

## Troubleshooting

### Common Issues

1. **"GOOGLE_CLOUD_PROJECT environment variable must be set"**
   - Ensure `.env` file exists and contains `GOOGLE_CLOUD_PROJECT`
   - Or set the environment variable directly

2. **Authentication errors**
   - Run `gcloud auth application-default login`
   - Verify your project ID is correct

3. **Vertex AI API not enabled**
   - Enable it: `gcloud services enable aiplatform.googleapis.com`

4. **Import errors**
   - Ensure you're in the virtual environment
   - Reinstall dependencies: `pip install -r requirements.txt`

## License

This project is part of the gen-ed hackathon project.

## Contributing

This is a hackathon project. For improvements, please follow the existing code structure and patterns.

