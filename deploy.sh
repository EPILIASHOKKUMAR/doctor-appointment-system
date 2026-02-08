#!/bin/bash

# SmartClinic AI - Quick Deployment Script
# This script helps you deploy to Heroku quickly

echo "🚀 SmartClinic AI - Deployment Script"
echo "======================================"
echo ""

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null
then
    echo "❌ Heroku CLI not found!"
    echo "📥 Please install from: https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi

echo "✅ Heroku CLI found"
echo ""

# Login to Heroku
echo "🔐 Logging in to Heroku..."
heroku login

# Get app name
echo ""
read -p "Enter your app name (e.g., smartclinic-ai-yourname): " APP_NAME

# Create Heroku app
echo ""
echo "📦 Creating Heroku app: $APP_NAME"
heroku create $APP_NAME

# Add MySQL database
echo ""
echo "🗄️ Adding MySQL database (ClearDB)..."
heroku addons:create cleardb:ignite -a $APP_NAME

# Generate and set SECRET_KEY
echo ""
echo "🔑 Generating SECRET_KEY..."
SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')
heroku config:set SECRET_KEY=$SECRET_KEY -a $APP_NAME

# Set Flask environment
echo ""
echo "⚙️ Setting Flask environment..."
heroku config:set FLASK_ENV=production -a $APP_NAME

# Optional: Set API keys
echo ""
read -p "Do you have a Gemini API key? (y/n): " HAS_GEMINI
if [ "$HAS_GEMINI" = "y" ]; then
    read -p "Enter Gemini API key: " GEMINI_KEY
    heroku config:set GEMINI_API_KEY=$GEMINI_KEY -a $APP_NAME
fi

echo ""
read -p "Do you have a Google Maps API key? (y/n): " HAS_MAPS
if [ "$HAS_MAPS" = "y" ]; then
    read -p "Enter Google Maps API key: " MAPS_KEY
    heroku config:set GOOGLE_MAPS_API_KEY=$MAPS_KEY -a $APP_NAME
fi

# Initialize git if needed
if [ ! -d .git ]; then
    echo ""
    echo "📝 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit for deployment"
fi

# Add Heroku remote
echo ""
echo "🔗 Adding Heroku remote..."
heroku git:remote -a $APP_NAME

# Deploy to Heroku
echo ""
echo "🚀 Deploying to Heroku..."
git push heroku main || git push heroku master

# Setup database
echo ""
echo "🗄️ Setting up database..."
heroku run python backend/setup_db.py -a $APP_NAME

# Open the app
echo ""
echo "✅ Deployment complete!"
echo ""
echo "🌐 Opening your app..."
heroku open -a $APP_NAME

echo ""
echo "📊 View logs with: heroku logs --tail -a $APP_NAME"
echo "🔄 Restart app with: heroku restart -a $APP_NAME"
echo ""
echo "🎉 Your SmartClinic AI is now live!"
