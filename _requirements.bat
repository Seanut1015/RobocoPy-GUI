@echo off
call .\.venv\Scripts\activate.bat
pip freeze > requirements.txt
