#!/bin/bash

# Script to check Agent Engine deployment logs

PROJECT_ID=${GOOGLE_CLOUD_PROJECT:-"edifyai-2737f"}

echo "Fetching recent Agent Engine logs..."
echo "Project: $PROJECT_ID"
echo ""

gcloud logging read "resource.type=aiplatform.googleapis.com/ReasoningEngine" \
  --project="$PROJECT_ID" \
  --limit=20 \
  --format="table(timestamp,severity,textPayload,jsonPayload.message)" \
  --freshness=1h

echo ""
echo "For more detailed logs, visit:"
echo "https://console.cloud.google.com/logs/query?project=$PROJECT_ID"

