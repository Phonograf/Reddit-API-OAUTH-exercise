@echo off
color 0a
::This is the
echo 1. Create a virtual environment
mkdir .venv
python -m venv .venv
echo 2. Activate the virtual environment
::Script should be executed inside bat
call .venv\Scripts\activate
echo 3. Install dependencies
pip install -r requirements.txt
echo Finished. You can proceed with launch.bat
pause