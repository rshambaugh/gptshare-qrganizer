#!/bin/bash

# Define paths
PROJECT_DIR="$HOME/projects/qrganizer"
CODE_UPDATE_SCRIPT="$PROJECT_DIR/codeupdate.sh"

# Step 1: Run codeupdate.sh
echo "Running codeupdate.sh..."
if [ -f "$CODE_UPDATE_SCRIPT" ]; then
  bash "$CODE_UPDATE_SCRIPT"
else
  echo "Error: codeupdate.sh not found at $CODE_UPDATE_SCRIPT."
  exit 1
fi

# Step 2: Extract commit message from codeupdate.sh
echo "Extracting commit message from codeupdate.sh..."
COMMIT_MESSAGE=$(grep -m 1 "^# Commit Message:" "$CODE_UPDATE_SCRIPT" | sed 's/# Commit Message: //')

if [ -z "$COMMIT_MESSAGE" ]; then
  echo "Error: Commit message not found in codeupdate.sh. Please add a '# Commit Message: <your message>' comment at the top."
  exit 1
fi

# Debugging: Print the extracted commit message
echo "Extracted Commit Message: $COMMIT_MESSAGE"

# Step 3: Stage, commit, and push changes
echo "Staging and committing changes..."
cd "$PROJECT_DIR" || exit
git add .
git commit -m "$COMMIT_MESSAGE"
git push origin master

echo "Code update, commit, and push complete!"
