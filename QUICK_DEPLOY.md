# ⚡ Quick Deploy Guide

## 🚀 Deploy in 5 Minutes!

### **Option 1: Heroku (Easiest)**

#### **Windows Users:**
```cmd
1. Double-click: deploy_heroku.bat
2. Follow the prompts
3. Done!
```

#### **Mac/Linux Users:**
```bash
chmod +x deploy_heroku.sh
./deploy_heroku.sh
```

#### **Manual Steps:**
```bash
# 1. Install Heroku CLI
# Download from: https://devcenter.heroku.com/articles/heroku-cli

# 2. Login
heroku login

# 3. Create app
heroku create smartclinic-app

# 4. Add database
heroku addons:create heroku-postgresql:mini

# 5. Set environment variables
heroku config:set GEMINI_API_KEY=your_gemini_key
heroku config:set GOOGLE_MAPS_API_KEY=your_maps_key
heroku config:set PRODUCTION=true

# 6. Deploy
git push heroku main

# 7. Initialize database
heroku run python -c "from app import app, db; app.app_context().push(); db.create_all()"

# 8. Open app
heroku open
```

---

### **Option 2: Render (Modern)**

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Go to Render**
   - Visit: https://render.com
   - Sign up/Login
   - Click "New +" → "Web Service"

3. **Connect Repository**
   - Connect your GitHub account
   - Select your repository

4. **Configure**
   ```
   Name: smartclinic
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   ```

5. **Add Environment Variables**
   - GEMINI_API_KEY
   - GOOGLE_MAPS_API_KEY
   - PRODUCTION=true

6. **Deploy**
   - Click "Create Web Service"
   - Wait 5 minutes
   - Done!

---

### **Option 3: PythonAnywhere (Free)**

1. **Create Account**
   - Go to: https://www.pythonanywhere.com
   - Sign up (free tier available)

2. **Upload Code**
   - Go to "Files" tab
   - Upload your project
   - Or clone from Git

3. **Install Dependencies**
   ```bash
   mkvirtualenv smartclinic
   pip install -r requirements.txt
   ```

4. **Configure Web App**
   - Go to "Web" tab
   - Add new web app
   - Manual configuration
   - Python 3.10

5. **Edit WSGI File**
   ```python
   import sys
   path = '/home/yourusername/smartclinic/doctor-appointment-system-main'
   sys.path.append(path)
   
   from app import app as application
   ```

6. **Reload**
   - Click "Reload" button
   - Done!

---

## 🔑 Required Information

Before deploying, have these ready:

1. **Gemini API Key**
   - Get from: https://makersuite.google.com/app/apikey
   - Your key: `AIzaSyD8kNsrTkg_G6XrszzVfe5nWhu94SUH9ZA`

2. **Google Maps API Key**
   - Get from: https://console.cloud.google.com/
   - Your key: `AIzaSyBUDDfyKeJuCeuIYufm0fBUX7uoaAPdGHQ`

3. **GitHub Account** (for Render)
   - Create at: https://github.com

---

## ✅ Post-Deployment Checklist

After deployment, test:

- [ ] Homepage loads
- [ ] User registration works
- [ ] Login works
- [ ] Appointment booking works
- [ ] Emergency page works
- [ ] Maps show correctly
- [ ] AI chatbot responds
- [ ] All features functional

---

## 🐛 Troubleshooting

### **Issue: App won't start**
```bash
# Check logs
heroku logs --tail
# or check platform-specific logs
```

### **Issue: Database error**
```bash
# Initialize database
heroku run python
>>> from app import app, db
>>> with app.app_context(): db.create_all()
```

### **Issue: Environment variables not working**
```bash
# Check variables
heroku config
# Set again if needed
heroku config:set KEY=value
```

---

## 💰 Cost

### **Free Tiers:**
- **Heroku:** Free (with limitations)
- **Render:** Free (with limitations)
- **PythonAnywhere:** Free (with limitations)

### **Paid Plans (if needed):**
- **Heroku Hobby:** $7/month
- **Render Starter:** $7/month
- **PythonAnywhere Hacker:** $5/month

**Recommendation:** Start with free tier!

---

## 🎉 Success!

Once deployed, your app will be live at:
- **Heroku:** `https://smartclinic-app.herokuapp.com`
- **Render:** `https://smartclinic.onrender.com`
- **PythonAnywhere:** `https://yourusername.pythonanywhere.com`

Share the link with users and start helping patients! 🏥

---

## 📞 Need Help?

- **Full Guide:** DEPLOYMENT_GUIDE.md
- **Heroku Docs:** https://devcenter.heroku.com/
- **Render Docs:** https://render.com/docs
- **PythonAnywhere Help:** https://help.pythonanywhere.com/

---

**Last Updated:** November 25, 2025
**Status:** Ready to Deploy ✅
