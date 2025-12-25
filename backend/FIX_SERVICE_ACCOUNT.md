# Fix Service Account for Cloud Run

## Step 1: Find the Correct Service Account

Run this to see what service account Cloud Run is currently using:

```bash
gcloud run services describe resume-matcher-api \
  --region us-central1 \
  --format 'value(spec.template.spec.serviceAccountName)'
```

If it returns empty, Cloud Run is using the default Compute Engine service account, which has a different format.

## Step 2: Get the Default Compute Engine Service Account

```bash
# Get the project number first
PROJECT_NUMBER=$(gcloud projects describe edifyai-2737f --format='value(projectNumber)')

# The default service account format is:
# PROJECT_NUMBER-compute@developer.gserviceaccount.com
echo "Default service account: ${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"
```

## Step 3: Grant Permissions to the Correct Service Account

Once you have the correct service account email, grant permissions:

```bash
# Replace SERVICE_ACCOUNT_EMAIL with the actual email from Step 1 or 2
gcloud projects add-iam-policy-binding edifyai-2737f \
  --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
  --role="roles/aiplatform.user"
```

## Alternative: Create and Use a Custom Service Account (Recommended)

```bash
# Create a new service account
gcloud iam service-accounts create vertex-ai-runner \
  --display-name="Vertex AI Cloud Run Service Account" \
  --project=edifyai-2737f

# Grant Vertex AI permissions
gcloud projects add-iam-policy-binding edifyai-2737f \
  --member="serviceAccount:vertex-ai-runner@edifyai-2737f.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

# Update Cloud Run to use this service account
gcloud run services update resume-matcher-api \
  --region us-central1 \
  --service-account="vertex-ai-runner@edifyai-2737f.iam.gserviceaccount.com"
```

