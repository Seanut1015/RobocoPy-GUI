@echo off
cd ..
python -m venv .venv
call .venv\Scripts\activate.bat
pip install -r .\requirements.txt"
pip list
pause