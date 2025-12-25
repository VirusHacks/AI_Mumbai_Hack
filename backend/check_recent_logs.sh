#!/bin/bash

# Script to check the most recent Agent Engine deployment logs

PROJECT_ID=${GOOGLE_CLOUD_PROJECT:-"edifyai-2737f"}

echo "Fetching most recent Agent Engine error logs..."
echo "Project: $PROJECT_ID"
echo ""

# Get the most recent reasoning engine errors
gcloud logging read \
  "resource.type=aiplatform.googleapis.com/ReasoningEngine AND severity>=ERROR" \
  --project="$PROJECT_ID" \
  --limit=20 \
  --format="table(timestamp,severity,textPayload,jsonPayload.message)" \
  --freshness=30m \
  2>/dev/null | head -40

echo ""
echo ""
echo "For detailed logs in console, visit:"
echo "https://console.cloud.google.com/logs/query?project=$PROJECT_ID"
echo ""
echo "Filter by: resource.type=\"aiplatform.googleapis.com/ReasoningEngine\""

