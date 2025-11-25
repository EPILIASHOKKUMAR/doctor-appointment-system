#!/bin/bash

# SmartClinic Heroku Deployment Script
# Run this script to deploy to Heroku

echo "🚀 SmartClinic Heroku Deployment"
echo "================================"

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null
then
    echo "❌ Heroku CLI not found. Please install it first:"
    echo "   https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi

echo "✓ Heroku CLI found"

# Login to Heroku
echo ""
echo "📝 Logging in to Heroku..."
heroku login

# Create app (or use existing)
echo ""
read -p "Enter your Heroku app name (e.g., smartclinic-app): " APP_NAME

if heroku apps:info -a $APP_NAME &> /dev/null; then
    echo "✓ Using existing app: $APP_NAME"
else
    echo "Creating new app: $APP_NAME"
    heroku create $APP_NAME
fi

# Add PostgreSQL
echo ""
echo "📊 Setting up PostgreSQL..."
if heroku addons -a $APP_NAME | grep -q "heroku-postgresql"; then
    echo "✓ PostgreSQL already configured"
else
    heroku addons:create heroku-postgresql:mini -a $APP_NAME
    echo "✓ PostgreSQL added"
fi

# Set environment variables
echo ""
echo "🔑 Setting environment variables..."
read -p "Enter your Gemini API Key: " GEMINI_KEY
read -p "Enter your Google Maps API Key: " MAPS_KEY

heroku config:set GEMINI_API_KEY=$GEMINI_KEY -a $APP_NAME
heroku config:set GOOGLE_MAPS_API_KEY=$MAPS_KEY -a $APP_NAME
heroku config:set PRODUCTION=true -a $APP_NAME
heroku config:set SECRET_KEY=$(openssl rand -hex 32) -a $APP_NAME

echo "✓ Environment variables set"

# Deploy
echo ""
echo "📦 Deploying to Heroku..."
git add .
git commit -m "Deploy to Heroku" || echo "No changes to commit"
git push heroku main

# Initialize database
echo ""
echo "🗄️  Initializing database..."
heroku run python -c "from app import app, db; app.app_context().push(); db.create_all()" -a $APP_NAME

echo ""
echo "✅ Deployment complete!"
echo ""
echo "🌐 Your app is live at: https://$APP_NAME.herokuapp.com"
echo ""
echo "📊 View logs: heroku logs --tail -a $APP_NAME"
echo "🔧 Open dashboard: heroku open -a $APP_NAME"
echo ""
echo "🎉 Happy deploying!"
