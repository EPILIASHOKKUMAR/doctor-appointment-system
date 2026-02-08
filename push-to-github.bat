@echo off
REM Quick script to push SmartClinic AI to GitHub

echo ========================================
echo Push SmartClinic AI to GitHub
echo ========================================
echo.

REM Check if git is initialized
if not exist .git (
    echo [INFO] Initializing Git repository...
    git init
    echo.
)

REM Add all files
echo [INFO] Adding all files...
git add .
echo.

REM Commit
echo [INFO] Committing changes...
git commit -m "Initial commit - SmartClinic AI ready for deployment"
echo.

REM Get GitHub username and repo name
echo [INPUT] Please provide your GitHub details:
echo.
set /p GITHUB_USERNAME="Enter your GitHub username: "
set /p REPO_NAME="Enter repository name (default: smartclinic-ai): "

REM Set default repo name if empty
if "%REPO_NAME%"=="" set REPO_NAME=smartclinic-ai

echo.
echo [INFO] Repository will be: https://github.com/%GITHUB_USERNAME%/%REPO_NAME%
echo.

REM Check if remote exists
git remote get-url origin >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [INFO] Remote 'origin' already exists. Removing...
    git remote remove origin
)

REM Add remote
echo [INFO] Adding remote repository...
git remote add origin https://github.com/%GITHUB_USERNAME%/%REPO_NAME%.git
echo.

REM Set branch to main
echo [INFO] Setting branch to main...
git branch -M main
echo.

REM Push to GitHub
echo [INFO] Pushing to GitHub...
echo [NOTE] You may be prompted for authentication
echo [NOTE] Use your Personal Access Token as password (not your GitHub password)
echo.
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo [SUCCESS] Pushed to GitHub successfully!
    echo ========================================
    echo.
    echo Your repository: https://github.com/%GITHUB_USERNAME%/%REPO_NAME%
    echo.
    echo [NEXT STEPS]
    echo 1. Visit your repository on GitHub
    echo 2. Verify all files are uploaded
    echo 3. Open RENDER_DEPLOY.md to deploy your app
    echo.
) else (
    echo.
    echo ========================================
    echo [ERROR] Failed to push to GitHub
    echo ========================================
    echo.
    echo [TROUBLESHOOTING]
    echo 1. Make sure the repository exists on GitHub
    echo 2. Check your authentication (use Personal Access Token)
    echo 3. See PUSH_TO_GITHUB.md for detailed help
    echo.
)

pause
