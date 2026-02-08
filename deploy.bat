@echo off
REM SmartClinic AI - Quick Deployment Script for Windows
REM This script helps you deploy to Heroku quickly

echo ========================================
echo SmartClinic AI - Deployment Script
echo ========================================
echo.

REM Check if Heroku CLI is installed
where heroku >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Heroku CLI not found!
    echo [INFO] Please install from: https://devcenter.heroku.com/articles/heroku-cli
    pause
    exit /b 1
)

echo [OK] Heroku CLI found
echo.

REM Login to Heroku
echo [INFO] Logging in to Heroku...
call heroku login

REM Get app name
echo.
set /p APP_NAME="Enter your app name (e.g., smartclinic-ai-yourname): "

REM Create Heroku app
echo.
echo [INFO] Creating Heroku app: %APP_NAME%
call heroku create %APP_NAME%

REM Add MySQL database
echo.
echo [INFO] Adding MySQL database (ClearDB)...
call heroku addons:create cleardb:ignite -a %APP_NAME%

REM Generate and set SECRET_KEY
echo.
echo [INFO] Generating SECRET_KEY...
for /f "delims=" %%i in ('python -c "import secrets; print(secrets.token_hex(32))"') do set SECRET_KEY=%%i
call heroku config:set SECRET_KEY=%SECRET_KEY% -a %APP_NAME%

REM Set Flask environment
echo.
echo [INFO] Setting Flask environment...
call heroku config:set FLASK_ENV=production -a %APP_NAME%

REM Optional: Set API keys
echo.
set /p HAS_GEMINI="Do you have a Gemini API key? (y/n): "
if /i "%HAS_GEMINI%"=="y" (
    set /p GEMINI_KEY="Enter Gemini API key: "
    call heroku config:set GEMINI_API_KEY=%GEMINI_KEY% -a %APP_NAME%
)

echo.
set /p HAS_MAPS="Do you have a Google Maps API key? (y/n): "
if /i "%HAS_MAPS%"=="y" (
    set /p MAPS_KEY="Enter Google Maps API key: "
    call heroku config:set GOOGLE_MAPS_API_KEY=%MAPS_KEY% -a %APP_NAME%
)

REM Initialize git if needed
if not exist .git (
    echo.
    echo [INFO] Initializing Git repository...
    git init
    git add .
    git commit -m "Initial commit for deployment"
)

REM Add Heroku remote
echo.
echo [INFO] Adding Heroku remote...
call heroku git:remote -a %APP_NAME%

REM Deploy to Heroku
echo.
echo [INFO] Deploying to Heroku...
git push heroku main
if %ERRORLEVEL% NEQ 0 (
    git push heroku master
)

REM Setup database
echo.
echo [INFO] Setting up database...
call heroku run python backend/setup_db.py -a %APP_NAME%

REM Open the app
echo.
echo [OK] Deployment complete!
echo.
echo [INFO] Opening your app...
call heroku open -a %APP_NAME%

echo.
echo [INFO] View logs with: heroku logs --tail -a %APP_NAME%
echo [INFO] Restart app with: heroku restart -a %APP_NAME%
echo.
echo [SUCCESS] Your SmartClinic AI is now live!
echo.
pause
