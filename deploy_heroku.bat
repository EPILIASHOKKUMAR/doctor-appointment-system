@echo off
REM SmartClinic Heroku Deployment Script for Windows
REM Run this script to deploy to Heroku

echo.
echo ========================================
echo   SmartClinic Heroku Deployment
echo ========================================
echo.

REM Check if Heroku CLI is installed
where heroku >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Heroku CLI not found!
    echo Please install it from: https://devcenter.heroku.com/articles/heroku-cli
    pause
    exit /b 1
)

echo [OK] Heroku CLI found
echo.

REM Login to Heroku
echo Logging in to Heroku...
call heroku login
echo.

REM Get app name
set /p APP_NAME="Enter your Heroku app name (e.g., smartclinic-app): "
echo.

REM Check if app exists
heroku apps:info -a %APP_NAME% >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    echo [OK] Using existing app: %APP_NAME%
) else (
    echo Creating new app: %APP_NAME%
    call heroku create %APP_NAME%
)
echo.

REM Add PostgreSQL
echo Setting up PostgreSQL...
heroku addons -a %APP_NAME% | findstr "heroku-postgresql" >nul
if %ERRORLEVEL% EQU 0 (
    echo [OK] PostgreSQL already configured
) else (
    call heroku addons:create heroku-postgresql:mini -a %APP_NAME%
    echo [OK] PostgreSQL added
)
echo.

REM Set environment variables
echo Setting environment variables...
set /p GEMINI_KEY="Enter your Gemini API Key: "
set /p MAPS_KEY="Enter your Google Maps API Key: "
echo.

call heroku config:set GEMINI_API_KEY=%GEMINI_KEY% -a %APP_NAME%
call heroku config:set GOOGLE_MAPS_API_KEY=%MAPS_KEY% -a %APP_NAME%
call heroku config:set PRODUCTION=true -a %APP_NAME%

echo [OK] Environment variables set
echo.

REM Deploy
echo Deploying to Heroku...
git add .
git commit -m "Deploy to Heroku"
git push heroku main
echo.

REM Initialize database
echo Initializing database...
call heroku run python -c "from app import app, db; app.app_context().push(); db.create_all()" -a %APP_NAME%
echo.

echo ========================================
echo   Deployment Complete!
echo ========================================
echo.
echo Your app is live at: https://%APP_NAME%.herokuapp.com
echo.
echo View logs: heroku logs --tail -a %APP_NAME%
echo Open app: heroku open -a %APP_NAME%
echo.
echo Happy deploying!
echo.
pause
