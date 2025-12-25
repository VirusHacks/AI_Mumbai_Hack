# Quick Start: Deploy to Vertex AI Agent Engine

## Prerequisites Checklist

- [ ] Google Cloud Project with billing enabled
- [ ] Vertex AI API enabled
- [ ] IAM permissions (`roles/aiplatform.user` or `roles/aiplatform.admin`)
- [ ] Authentication configured (service account key OR `gcloud auth`)
- [ ] Python 3.10+ with virtual environment
- [ ] All dependencies installed

## 5-Minute Deployment

### 1. Configure Environment

Create `.env` file in `backend/` directory with **required** variables:

```env
GOOGLE_CLOUD_PROJECT=your-project-id
VERTEX_AI_LOCATION=us-central1
GEMINI_MODEL_NAME=gemini-2.0-flash-exp
```

### 2. Enable APIs

```bash
gcloud services enable aiplatform.googleapis.com --project=YOUR_PROJECT_ID
```

### 3. Authenticate (Choose ONE method)

**Option A: Service Account (Recommended for Production)**
- Create service account in Google Cloud Console
- Download JSON key file
- Add to `.env`:
  ```env
  GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
  ```

**Option B: gcloud CLI (Easier for Development)**
```bash
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```
*No `.env` changes needed for this option*

### 4. Install Dependencies

```bash
cd backend
source venv/bin/activate  # or: venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 5. Test Locally (Optional but Recommended)

```bash
python main_local_test.py samples/resume.txt samples/jd.txt
```

### 6. Deploy

**Option A: Using the script (Recommended)**
```bash
./deploy.sh
```

**Option B: Manual deployment**
```bash
python -m src.deploy.agent_engine_deploy deploy
```

### 7. Save Resource Name

After deployment, you'll see:
```
✅ Deployment successful!
Resource name: projects/123456789/locations/us-central1/agentEngines/987654321
```

**Save this resource name!** You'll need it to query the agent.

### 8. Test Deployment

```bash
export VERTEX_AGENT_ENGINE_RESOURCE="projects/.../agentEngines/..."
python -m src.deploy.agent_engine_deploy test
```

## Using the Deployed Agent

### Python Example

```python
from vertexai import agent_engines
import vertexai
from src.config import get_project_id, get_location

# Initialize
project_id = get_project_id()
location = get_location()
vertexai.init(project=project_id, location=location)

# Get agent engine
resource_name = "projects/YOUR_PROJECT/locations/us-central1/agentEngines/RESOURCE_ID"
engine = agent_engines.get_agent_engine(resource_name=resource_name)

# Query
response = engine.query({
    "resume_text": "Your resume text...",
    "job_description": "Job description..."
})

print(f"Score: {response['final_score']['overall_score']}")
```

## Common Issues

| Issue | Solution |
|-------|----------|
| "GOOGLE_CLOUD_PROJECT not set" | Check `.env` file exists and has correct values |
| "Credentials not found" | Run `gcloud auth application-default login` or set `GOOGLE_APPLICATION_CREDENTIALS` |
| "Permission denied" | Check IAM roles: `gcloud projects get-iam-policy YOUR_PROJECT_ID` |
| "API not enabled" | Run: `gcloud services enable aiplatform.googleapis.com` |
| Deployment takes long | Normal! Can take 5-15 minutes. Check logs if stuck. |

## Next Steps

- Read full guide: `DEPLOYMENT.md`
- Integrate with frontend: See `INTEGRATION.md`
- Monitor usage: Google Cloud Console → Vertex AI → Agent Engines

## Need Help?

1. Check `DEPLOYMENT.md` for detailed troubleshooting
2. Review Google Cloud logs
3. Verify all prerequisites are met

