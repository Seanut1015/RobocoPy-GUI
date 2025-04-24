@echo off
call .\.venv\Scripts\activate.bat

where pyinstaller >nul 2>nul
if errorlevel 1 (
    echo [ERROR] pyinstaller NOT install : pip install pyinstaller
    pause
    exit /b 1
)

for %%i in (%cd%) do set "APP_NAME=%%~ni"
pyinstaller app.py -w --onefile --name %APP_NAME%