@echo off
call ..\.venv\Scripts\activate.bat

cd UI_files

where pyuic5 >nul 2>nul
if errorlevel 1 (
    echo [ERROR] NOT install pyuic5 : pip install pyqt5
    pause
    exit /b 1
)

pyuic5 untitled.ui -o UI.py

