# Troubleshooting Agent Engine Deployment

## Deployment Failed to Start

If you see: `Reasoning Engine resource failed to start and cannot serve traffic`

### Step 1: Check Logs

1. **View logs in Google Cloud Console:**
   - Go to: https://console.cloud.google.com/logs/query?project=edifyai-2737f
   - Filter by: `resource.type="aiplatform.googleapis.com/ReasoningEngine"`
   - Look for ERROR level logs

2. **Or use gcloud CLI:**
   ```bash
   gcloud logging read "resource.type=aiplatform.googleapis.com/ReasoningEngine" \
     --project=edifyai-2737f \
     --limit=50 \
     --format=json
   ```

### Step 2: Common Issues

#### Issue: Import Errors

**Symptoms:** Logs show `ModuleNotFoundError` or `ImportError`

**Solution:** Ensure all source code is included. The deployment should automatically package your code, but verify:
- All `src/` modules are present
- No circular imports
- All dependencies in `requirements.txt`

#### Issue: Missing Dependencies

**Symptoms:** Logs show missing packages

**Solution:** Add missing packages to requirements list in `agent_engine_deploy.py`

#### Issue: Serialization Errors

**Symptoms:** Logs show `pickle` or `cloudpickle` errors

**Solution:** 
- Avoid capturing non-serializable objects in closures
- Ensure logger is properly configured
- Check that all functions are at module level (not nested)

#### Issue: Authentication Errors

**Symptoms:** Logs show permission denied or auth errors

**Solution:**
- Verify service account has correct permissions
- Check that `GOOGLE_APPLICATION_CREDENTIALS` is set correctly
- Ensure Vertex AI API is enabled

### Step 3: Verify Local Execution

Before deploying, ensure everything works locally:

```bash
python main_local_test.py samples/resume.txt samples/jd.txt
```

If this fails, fix local issues first.

### Step 4: Test with Minimal Example

Create a minimal LangGraph app to test deployment:

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    message: str

def hello_node(state: State) -> State:
    return {"message": f"Hello, {state.get('message', 'World')}!"}

def build_minimal_app():
    workflow = StateGraph(State)
    workflow.add_node("hello", hello_node)
    workflow.set_entry_point("hello")
    workflow.add_edge("hello", END)
    return workflow.compile()
```

If minimal example works, the issue is in your specific code.

### Step 5: Check Resource Limits

Verify your project has sufficient quota:
- Go to: https://console.cloud.google.com/iam-admin/quotas
- Check Vertex AI quotas
- Request increase if needed

## Getting Help

1. **Check official docs:**
   - https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/troubleshooting/deploy

2. **Review logs carefully:**
   - Look for the first ERROR
   - Check stack traces
   - Note any missing modules or permissions

3. **Common fixes:**
   - Re-deploy with updated code
   - Check Python version (must be 3.9-3.13)
   - Verify all environment variables are set
   - Ensure staging bucket exists and is accessible

