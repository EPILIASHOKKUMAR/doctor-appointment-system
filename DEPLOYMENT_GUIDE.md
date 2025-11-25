# 🚀 SmartClinic Deployment Guide

## Overview
This guide covers deploying SmartClinic to various platforms.

---

## 📋 Pre-Deployment Checklist

### **1. Prepare Your Project**
- [ ] All features tested locally
- [ ] Database migrations complete
- [ ] Environment variables configured
- [ ] API keys ready
- [ ] Requirements.txt updated

### **2. Security Checklist**
- [ ] Change SECRET_KEY in production
- [ ] Set DEBUG=False
- [ ] Configure allowed hosts
- [ ] Use HTTPS
- [ ] Secure database credentials
- [ ] API keys in environment variables

---

## 🌐 Deployment Options

### **Option 1: Heroku (Easiest - Recommended)**
### **Option 2: PythonAnywhere (Free Tier Available)**
### **Option 3: AWS/DigitalOcean (Advanced)**
### **Option 4: Render (Modern Alternative)**

---

## 🎯 Option 1: Heroku Deployment (Recommended)

### **Why Heroku?**
- ✅ Easy deployment
- ✅ Free tier available
- ✅ Automatic HTTPS
- ✅ Good for beginners
- ✅ PostgreSQL included

### **Step 1: Install Heroku CLI**
Download from: https://devcenter.heroku.com/articles/heroku-cli

### **Step 2: Login to Heroku**
```bash
heroku login
```

### **Step 3: Create Heroku App**
```bash
cd doctor-appointment-system-main
heroku create smartclinic-app
```

### **Step 4: Add PostgreSQL**
```bash
heroku addons:create heroku-postgresql:mini
```

### **Step 5: Set Environment Variables**
```bash
heroku config:set GEMINI_API_KEY=your_gemini_key
heroku config:set GOOGLE_MAPS_API_KEY=your_maps_key
heroku config:set SECRET_KEY=your_secret_key_here
```

### **Step 6: Deploy**
```bash
git add .
git commit -m "Prepare for deployment"
git push heroku main
```

### **Step 7: Initialize Database**
```bash
heroku run python
>>> from app import app, db
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
```

### **Step 8: Open Your App**
```bash
heroku open
```

**Your app is live!** 🎉

---

## 🐍 Option 2: PythonAnywhere (Free Tier)

### **Why PythonAnywhere?**
- ✅ Free tier available
- ✅ Easy Python hosting
- ✅ Good for students
- ✅ No credit card required

### **Step 1: Create Account**
Go to: https://www.pythonanywhere.com/registration/

### **Step 2: Upload Files**
1. Go to "Files" tab
2. Upload your project folder
3. Or use Git:
```bash
git clone https://github.com/yourusername/smartclinic.git
```

### **Step 3: Create Virtual Environment**
```bash
mkvirtualenv --python=/usr/bin/python3.10 smartclinic
pip install -r requirements.txt
```

### **Step 4: Configure Web App**
1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python 3.10

### **Step 5: Configure WSGI File**
Edit `/var/www/yourusername_pythonanywhere_com_wsgi.py`:
```python
import sys
path = '/home/yourusername/smartclinic/doctor-appointment-system-main'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

### **Step 6: Set Environment Variables**
In WSGI file, add:
```python
import os
os.environ['GEMINI_API_KEY'] = 'your_key'
os.environ['GOOGLE_MAPS_API_KEY'] = 'your_key'
```

### **Step 7: Reload Web App**
Click "Reload" button on Web tab

**Your app is live!** 🎉

---

## ☁️ Option 3: Render (Modern Platform)

### **Why Render?**
- ✅ Modern platform
- ✅ Free tier
- ✅ Automatic HTTPS
- ✅ Easy deployment
- ✅ Good performance

### **Step 1: Create Account**
Go to: https://render.com/

### **Step 2: Connect GitHub**
1. Push your code to GitHub
2. Connect Render to GitHub

### **Step 3: Create Web Service**
1. Click "New +"
2. Select "Web Service"
3. Connect your repository

### **Step 4: Configure Service**
```
Name: smartclinic
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

### **Step 5: Add Environment Variables**
In Render dashboard:
- GEMINI_API_KEY
- GOOGLE_MAPS_API_KEY
- SECRET_KEY
- DATABASE_URL (auto-provided)

### **Step 6: Deploy**
Click "Create Web Service"

**Your app is live!** 🎉

---

## 🔧 Production Configuration

### **Update app.py for Production**

Add this at the top of app.py:
```python
import os

# Production configuration
if os.environ.get('PRODUCTION'):
    app.config['DEBUG'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    # Fix for Heroku PostgreSQL
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('postgres://'):
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace('postgres://', 'postgresql://', 1)
else:
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinic.db'
```

### **Create requirements.txt**
Already exists, but verify it includes:
```
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
python-dotenv==1.0.0
google-generativeai==0.3.1
gunicorn==21.2.0
psycopg2-binary==2.9.9
```

### **Create Procfile (for Heroku)**
Already exists, verify:
```
web: gunicorn app:app
```

### **Create runtime.txt (for Heroku)**
Already exists, verify:
```
python-3.11.0
```

---

## 🔒 Security Best Practices

### **1. Change SECRET_KEY**
```python
# In production, use environment variable
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(16))
```

### **2. Use HTTPS**
All platforms provide automatic HTTPS

### **3. Secure Database**
Use PostgreSQL in production, not SQLite

### **4. Environment Variables**
Never commit .env file to Git!

Add to .gitignore:
```
.env
*.db
__pycache__/
*.pyc
```

### **5. Rate Limiting**
Consider adding Flask-Limiter:
```python
from flask_limiter import Limiter
limiter = Limiter(app, key_func=lambda: request.remote_addr)
```

---

## 📊 Post-Deployment

### **1. Test Everything**
- [ ] User registration
- [ ] Login/logout
- [ ] Appointment booking
- [ ] Emergency features
- [ ] AI chatbot
- [ ] Maps and location

### **2. Monitor Performance**
- Check response times
- Monitor error logs
- Track user activity

### **3. Set Up Backups**
- Database backups
- Regular snapshots
- Disaster recovery plan

---

## 🐛 Troubleshooting

### **Issue: Database Not Found**
```bash
# Heroku
heroku run python
>>> from app import app, db
>>> with app.app_context(): db.create_all()

# PythonAnywhere
python manage.py
```

### **Issue: Static Files Not Loading**
```python
# Add to app.py
app.config['STATIC_FOLDER'] = 'static'
app.config['STATIC_URL_PATH'] = '/static'
```

### **Issue: API Keys Not Working**
```bash
# Check environment variables
heroku config
# or
echo $GEMINI_API_KEY
```

### **Issue: 500 Internal Server Error**
```bash
# Check logs
heroku logs --tail
# or check platform-specific logs
```

---

## 💰 Cost Estimates

### **Heroku:**
- Free tier: $0/month (limited hours)
- Hobby: $7/month
- Professional: $25/month

### **PythonAnywhere:**
- Free tier: $0/month (limited)
- Hacker: $5/month
- Web Developer: $12/month

### **Render:**
- Free tier: $0/month
- Starter: $7/month
- Standard: $25/month

### **Recommended for Students:**
PythonAnywhere Free Tier or Render Free Tier

---

## 🎓 Quick Deploy Commands

### **Heroku Quick Deploy:**
```bash
# One-time setup
heroku login
heroku create smartclinic-app
heroku addons:create heroku-postgresql:mini
heroku config:set GEMINI_API_KEY=your_key
heroku config:set GOOGLE_MAPS_API_KEY=your_key

# Deploy
git add .
git commit -m "Deploy"
git push heroku main

# Initialize DB
heroku run python -c "from app import app, db; app.app_context().push(); db.create_all()"

# Open app
heroku open
```

### **Render Quick Deploy:**
```bash
# Push to GitHub
git add .
git commit -m "Deploy"
git push origin main

# Then in Render dashboard:
# 1. Connect GitHub repo
# 2. Add environment variables
# 3. Click Deploy
```

---

## 📱 Domain Setup (Optional)

### **Custom Domain:**
1. Buy domain (Namecheap, GoDaddy)
2. Add to platform:
   - Heroku: `heroku domains:add www.smartclinic.com`
   - Render: Add in dashboard
3. Update DNS records
4. Wait for propagation (24-48 hours)

---

## 🔄 Continuous Deployment

### **GitHub Actions (Auto-deploy):**

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy to Heroku

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: akhileshns/heroku-deploy@v3.12.12
        with:
          heroku_api_key: ${{secrets.HEROKU_API_KEY}}
          heroku_app_name: "smartclinic-app"
          heroku_email: "your@email.com"
```

---

## ✅ Deployment Checklist

### **Before Deployment:**
- [ ] Test all features locally
- [ ] Update requirements.txt
- [ ] Set up .gitignore
- [ ] Prepare environment variables
- [ ] Choose deployment platform

### **During Deployment:**
- [ ] Create account on platform
- [ ] Configure database
- [ ] Set environment variables
- [ ] Deploy code
- [ ] Initialize database

### **After Deployment:**
- [ ] Test all features
- [ ] Check logs for errors
- [ ] Set up monitoring
- [ ] Configure backups
- [ ] Share with users!

---

## 🎉 Success!

Your SmartClinic is now live and accessible to users worldwide!

**Next Steps:**
1. Share your URL
2. Gather user feedback
3. Monitor performance
4. Plan improvements
5. Scale as needed

---

## 📞 Support

**Platform Documentation:**
- Heroku: https://devcenter.heroku.com/
- PythonAnywhere: https://help.pythonanywhere.com/
- Render: https://render.com/docs

**Project Documentation:**
- EMERGENCY_FEATURES.md
- TESTING_GUIDE.md
- README.md

---

**Last Updated:** November 25, 2025
**Version:** 3.0
**Status:** Ready for Deployment ✅
