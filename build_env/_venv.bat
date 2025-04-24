@echo off
cd ..
set CUR_DIR=%cd%
cd ..
python -m venv .venv
call .venv\Scripts\activate.bat
pip install -r "%CUR_DIR%\requirements.txt"
pip list
pause