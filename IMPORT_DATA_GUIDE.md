# 📥 Import Data to Production - Complete Guide

## ✅ Step 1: Data Already Exported!

Your local data has been successfully exported to:
```
backend/production_data.sql
```

**What was exported:**
- ✅ 5 Hospitals
- ✅ 9 Doctors  
- ✅ 19 Users

---

## 🚀 Step 2: Push Code to GitHub

First, we need to push the import endpoint and data file to GitHub:

```bash
cd backend
git add production_data.sql import_to_production.py export_data.py
cd ..
git add backend/app.py IMPORT_DATA_GUIDE.md
git commit -m "Add data import functionality for production"
git push origin main
```

**Wait 3-5 minutes** for Render to automatically deploy the new code.

---

## 🔧 Step 3: Configure Environment Variables on Render

Before importing data, make sure you've added the Gemini API key:

1. Go to https://dashboard.render.com/
2. Click on your **smartcinicai** service
3. Click **"Environment"** in the left sidebar
4. Add this variable if not already added:
   - **Key:** `GEMINI_API_KEY`
   - **Value:** `AIzaSyCs8z32-0heiYZnL9ngU3PmIYJaTKC7Nos`
5. Click **"Save Changes"**
6. Wait for automatic redeploy

---

## 📤 Step 4: Import Data to Production

You have 2 options:

### Option A: Using Python Script (Easiest)

1. **Install requests library** (if not already installed):
   ```bash
   pip install requests
   ```

2. **Run the import script:**
   ```bash
   cd backend
   python import_to_production.py
   ```

3. **Confirm when prompted:**
   - Type `yes` and press Enter
   - Wait for the import to complete

4. **Check the results:**
   - You'll see a success message with statistics
   - Visit https://smartcinicai.onrender.com to verify

### Option B: Using cURL or Postman (Manual)

1. **Wait for Render to deploy** (check logs for "Build succeeded")

2. **Send POST request:**
   ```bash
   curl -X POST https://smartcinicai.onrender.com/import-production-data \
     -H "Content-Type: application/json" \
     -d '{"secret":"import-data-2026"}'
   ```

3. **Check the response** for success message

---

## 🔍 Step 5: Verify the Import

1. **Visit your production site:**
   ```
   https://smartcinicai.onrender.com
   ```

2. **Login as hospital admin:**
   - Email: `2@gmail.com` (or any admin from your data)
   - Password: (the password you set locally)

3. **Check if your hospitals are there:**
   - Go to "Hospitals" page
   - You should see:
     - ADITHYA HOSPITALS
     - ASHOK HOSPITAL
     - Aditya Hospitals
     - ESI HOSPITAL
     - Test General Hospital

4. **Test the chatbot:**
   - Click the chatbot button (🤖)
   - Type "I have a headache"
   - Should get detailed AI response

---

## ⚠️ Important Notes

### About Duplicate Entries
- The import script will skip duplicate entries automatically
- If you run it twice, it won't create duplicates
- Existing data will be preserved

### About Passwords
- All passwords are hashed and will work as they did locally
- Use the same passwords you set on your local system

### About IDs
- The script preserves the original IDs from your local database
- This ensures relationships between users, hospitals, and doctors remain intact

---

## 🐛 Troubleshooting

### Problem: "Cannot connect to production server"
**Solution:** 
- Check if Render deployment is running
- Visit https://smartcinicai.onrender.com in browser first
- Wait a few minutes and try again

### Problem: "production_data.sql file not found"
**Solution:**
- Make sure you pushed the file to GitHub
- Check Render logs to see if deployment succeeded
- The file should be in `backend/production_data.sql`

### Problem: "Unauthorized: Invalid secret key"
**Solution:**
- The secret key in `import_to_production.py` must match `app.py`
- Both should be: `import-data-2026`
- If you changed it, update both files

### Problem: Import succeeds but data not showing
**Solution:**
- Clear your browser cache
- Try logging in with different admin accounts
- Check Render logs for any database errors

### Problem: "Duplicate entry" errors
**Solution:**
- This is normal if data already exists
- The script will skip duplicates automatically
- Check the final count to see what was imported

---

## 📊 Expected Results

After successful import, you should have:

**Hospitals:**
1. Test General Hospital
2. ADITHYA HOSPITALS
3. ASHOK HOSPITAL
4. Aditya Hospitals
5. ESI HOSPITAL

**Doctors:**
- 9 doctors across different specializations
- Orthopedic, Cardiologist, Dermatologist, General Physician, Neurologist

**Users:**
- 19 total users
- Multiple hospital admins
- Multiple doctors
- Multiple patients

---

## 🎯 Next Steps After Import

1. **Test all functionality:**
   - Login with different user types
   - Book appointments
   - Test chatbot
   - Search hospitals

2. **Update production data:**
   - Add more hospitals through the website
   - Update doctor information
   - Add patient records

3. **Monitor the deployment:**
   - Check Render logs regularly
   - Monitor API usage for Gemini
   - Watch for any errors

---

## 🔐 Security Notes

**The import endpoint is protected by a secret key:**
- Secret: `import-data-2026`
- Only requests with this secret can import data
- Change this secret in production for better security

**To change the secret:**
1. Edit `backend/app.py` - line with `if secret != 'import-data-2026':`
2. Edit `backend/import_to_production.py` - line with `SECRET_KEY = "import-data-2026"`
3. Use a strong, random secret
4. Push changes to GitHub

---

## ✅ Success Checklist

- [ ] Code pushed to GitHub
- [ ] Render deployment completed
- [ ] GEMINI_API_KEY added to Render environment
- [ ] production_data.sql file exists on server
- [ ] Import script executed successfully
- [ ] Can see hospitals on production site
- [ ] Can login with local credentials
- [ ] Chatbot is working
- [ ] Can book appointments

---

## 📞 Need Help?

If you encounter issues:

1. **Check Render Logs:**
   - Go to Render dashboard
   - Click "Logs" tab
   - Look for error messages

2. **Check Browser Console:**
   - Press F12 in browser
   - Look for JavaScript errors

3. **Test the endpoint manually:**
   ```bash
   curl https://smartcinicai.onrender.com/import-production-data
   ```

4. **Verify the file exists:**
   - Check GitHub repository
   - Look for `backend/production_data.sql`

---

**Good luck with your import! 🚀**
