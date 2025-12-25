# Fix 429 Error in Cloud Run Deployment

## Problem
Getting 429 "Resource exhausted" error when calling from deployed frontend, but works locally.

## Root Cause
Cloud Run service account doesn't have proper Vertex AI permissions or quota limits are being hit.

## Solution

### Step 1: Get the Cloud Run Service Account

```bash
# Get the default compute service account email
PROJECT_ID=edifyai-2737f
SERVICE_ACCOUNT="${PROJECT_ID}@appspot.gserviceaccount.com"

# Or get the actual service account used by Cloud Run
gcloud run services describe resume-matcher-api \
  --region us-central1 \
  --format 'value(spec.template.spec.serviceAccountName)'
```

### Step 2: Grant Vertex AI Permissions

```bash
PROJECT_ID=edifyai-2737f
SERVICE_ACCOUNT="${PROJECT_ID}@appspot.gserviceaccount.com"

# Grant Vertex AI User role
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${SERVICE_ACCOUNT}" \
  --role="roles/aiplatform.user"

# Grant Service Account User role (if needed)
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:${SERVICE_ACCOUNT}" \
  --role="roles/iam.serviceAccountUser"
```

### Step 3: Update Cloud Run Service with Proper Service Account

```bash
gcloud run services update resume-matcher-api \
  --region us-central1 \
  --service-account="${PROJECT_ID}@appspot.gserviceaccount.com"
```

### Step 4: Verify Environment Variables

Make sure these are set in Cloud Run:

```bash
gcloud run services update resume-matcher-api \
  --region us-central1 \
  --update-env-vars "GOOGLE_CLOUD_PROJECT=edifyai-2737f,VERTEX_AI_LOCATION=us-central1,GEMINI_MODEL_NAME=gemini-2.5-flash"
```

### Step 5: Check Quota Limits

If still getting 429, check and request quota increase:

1. Go to: https://console.cloud.google.com/iam-admin/quotas?project=edifyai-2737f
2. Filter by "Vertex AI API" or "Generative Language API"
3. Look for "Requests per minute" or "Requests per day"
4. Request quota increase if needed

### Alternative: Use a Custom Service Account (Recommended for Production)

```bash
# Create a custom service account
gcloud iam service-accounts create vertex-ai-runner \
  --display-name="Vertex AI Cloud Run Service Account" \
  --project=edifyai-2737f

# Grant permissions
gcloud projects add-iam-policy-binding edifyai-2737f \
  --member="serviceAccount:vertex-ai-runner@edifyai-2737f.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

# Update Cloud Run to use custom service account
gcloud run services update resume-matcher-api \
  --region us-central1 \
  --service-account="vertex-ai-runner@edifyai-2737f.iam.gserviceaccount.com"
```

## Verify Fix

After applying fixes, test the endpoint:

```bash
curl https://resume-matcher-api-721055312482.us-central1.run.app/health
```

Then test with a small request to see if 429 error is resolved.

