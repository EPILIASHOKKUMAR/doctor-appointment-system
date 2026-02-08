#!/bin/bash

# Quick script to push SmartClinic AI to GitHub

echo "========================================"
echo "Push SmartClinic AI to GitHub"
echo "========================================"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "[INFO] Initializing Git repository..."
    git init
    echo ""
fi

# Add all files
echo "[INFO] Adding all files..."
git add .
echo ""

# Commit
echo "[INFO] Committing changes..."
git commit -m "Initial commit - SmartClinic AI ready for deployment"
echo ""

# Get GitHub username and repo name
echo "[INPUT] Please provide your GitHub details:"
echo ""
read -p "Enter your GitHub username: " GITHUB_USERNAME
read -p "Enter repository name (default: smartclinic-ai): " REPO_NAME

# Set default repo name if empty
if [ -z "$REPO_NAME" ]; then
    REPO_NAME="smartclinic-ai"
fi

echo ""
echo "[INFO] Repository will be: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
echo ""

# Check if remote exists
if git remote get-url origin &> /dev/null; then
    echo "[INFO] Remote 'origin' already exists. Removing..."
    git remote remove origin
fi

# Add remote
echo "[INFO] Adding remote repository..."
git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
echo ""

# Set branch to main
echo "[INFO] Setting branch to main..."
git branch -M main
echo ""

# Push to GitHub
echo "[INFO] Pushing to GitHub..."
echo "[NOTE] You may be prompted for authentication"
echo "[NOTE] Use your Personal Access Token as password (not your GitHub password)"
echo ""
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "[SUCCESS] Pushed to GitHub successfully!"
    echo "========================================"
    echo ""
    echo "Your repository: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
    echo ""
    echo "[NEXT STEPS]"
    echo "1. Visit your repository on GitHub"
    echo "2. Verify all files are uploaded"
    echo "3. Open RENDER_DEPLOY.md to deploy your app"
    echo ""
else
    echo ""
    echo "========================================"
    echo "[ERROR] Failed to push to GitHub"
    echo "========================================"
    echo ""
    echo "[TROUBLESHOOTING]"
    echo "1. Make sure the repository exists on GitHub"
    echo "2. Check your authentication (use Personal Access Token)"
    echo "3. See PUSH_TO_GITHUB.md for detailed help"
    echo ""
fi
