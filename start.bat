@echo off
TITLE SmartERP - Enterprise Platform Launcher
cls
echo ============================================================================
echo                      Starting SmartERP Enterprise Platform
echo  Modules: Auth & RBAC, HR, CRM, Inventory, Sales, Procurement, Finance
echo ============================================================================
echo.

SET "ROOT_DIR=%~dp0"
cd /d "%ROOT_DIR%"

:: Check if Node is in PATH, if not fallback to portable location
where node >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    if exist "C:\Users\DELL\nodejs\node-v20.18.0-win-x64" (
        set "PATH=C:\Users\DELL\nodejs\node-v20.18.0-win-x64;%PATH%"
    )
)

:: Locate Python Virtualenv (.venv in root or backend\.venv)
set "VENV_ACTIVATE="
if exist "%ROOT_DIR%.venv\Scripts\activate.bat" (
    set "VENV_ACTIVATE=%ROOT_DIR%.venv\Scripts\activate.bat"
) else if exist "%ROOT_DIR%backend\.venv\Scripts\activate.bat" (
    set "VENV_ACTIVATE=%ROOT_DIR%backend\.venv\Scripts\activate.bat"
)

if "%VENV_ACTIVATE%"=="" (
    echo [INFO] Creating Python virtual environment in .venv...
    python -m venv "%ROOT_DIR%.venv"
    echo [INFO] Installing backend dependencies...
    "%ROOT_DIR%.venv\Scripts\pip" install -r "%ROOT_DIR%backend\requirements.txt"
    set "VENV_ACTIVATE=%ROOT_DIR%.venv\Scripts\activate.bat"
)

:: Check Frontend node_modules
if not exist "%ROOT_DIR%frontend\node_modules" (
    echo [INFO] Installing frontend dependencies...
    cd /d "%ROOT_DIR%frontend"
    call npm.cmd install
    cd /d "%ROOT_DIR%"
)

echo [1/2] Launching FastAPI Backend (Uvicorn on Port 8000)...
start "SmartERP Backend (FastAPI)" cmd /k "cd /d "%ROOT_DIR%backend" && call "%VENV_ACTIVATE%" && python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000"

echo [2/2] Launching React Vite Frontend (Port 5173)...
start "SmartERP Frontend (Vite)" cmd /k "cd /d "%ROOT_DIR%frontend" && call npm.cmd run dev"

echo.
echo ============================================================================
echo SmartERP servers are starting up in separate windows!
echo.
echo - Web Application: http://localhost:5173
echo - API Server:      http://localhost:8000
echo - Swagger Docs:    http://localhost:8000/docs
echo.
echo Demo Credentials:
echo   Administrator: admin / Admin@123
echo   Sales Manager: salesmgr / Manager@123
echo   HR Manager:    hrmanager / Hr@123
echo   Staff:         staff / Staff@123
echo ============================================================================
echo.
pause
