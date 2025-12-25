# Deploy Python Backend to Google Cloud Run

## Prerequisites

1. **Install Google Cloud SDK** (if not already installed):
   ```bash
   # macOS
   brew install google-cloud-sdk
   
   # Or download from: https://cloud.google.com/sdk/docs/install
   ```

2. **Authenticate with Google Cloud**:
   ```bash
   gcloud auth login
   gcloud auth application-default login
   ```

3. **Set your project**:
   ```bash
   gcloud config set project edifyai-2737f
   ```

4. **Enable required APIs**:
   ```bash
   gcloud services enable cloudbuild.googleapis.com
   gcloud services enable run.googleapis.com
   gcloud services enable aiplatform.googleapis.com
   ```

## Deployment Steps

### Option 1: Using the Deployment Script (Recommended)

```bash
cd backend
chmod +x deploy_cloud_run.sh
./deploy_cloud_run.sh
```

### Option 2: Manual Deployment

1. **Build the container image**:
   ```bash
   cd backend
   gcloud builds submit --tag gcr.io/edifyai-2737f/resume-matcher-api
   ```

2. **Deploy to Cloud Run**:
   ```bash
   gcloud run deploy resume-matcher-api \
     --image gcr.io/edifyai-2737f/resume-matcher-api \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars "GOOGLE_CLOUD_PROJECT=edifyai-2737f,VERTEX_AI_LOCATION=us-central1,GEMINI_MODEL_NAME=gemini-2.5-flash" \
     --memory 2Gi \
     --cpu 2 \
     --timeout 300 \
     --port 8080
   ```

3. **Get the service URL**:
   ```bash
   gcloud run services describe resume-matcher-api \
     --region us-central1 \
     --format 'value(status.url)'
   ```

## Update Frontend Environment

After deployment, update your Next.js `.env.local` file:

```env
PYTHON_BACKEND_URL=https://resume-matcher-api-xxxxx.run.app
```

Replace `xxxxx` with your actual Cloud Run service URL.

## Verify Deployment

1. **Health check**:
   ```bash
   curl https://your-service-url.run.app/health
   ```

2. **Test analysis endpoint**:
   ```bash
   curl -X POST https://your-service-url.run.app/ \
     -H "Content-Type: application/json" \
     -d '{"resume_text": "test", "job_description": "test"}'
   ```

## Troubleshooting

- **Build fails**: Check that all dependencies are in `requirements.txt`
- **Deployment timeout**: Increase timeout in deployment command
- **Memory issues**: Increase memory allocation (currently 2Gi)
- **Authentication errors**: Run `gcloud auth application-default login`

