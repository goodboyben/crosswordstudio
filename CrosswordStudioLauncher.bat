@echo off
:: 1. Force the script to look in the correct folder
cd /d "%~dp0"

:: 2. Start Python in a MINIMIZED window
:: "CrosswordEngine" is just the title of the window
start /min "CrosswordEngine" python server.py

:: 3. Wait 2 seconds for Python to wake up
timeout /t 2 >nul

:: 4. Open the browser
start http://localhost:8000/CrosswordStudio.html

:: 5. Exit this launcher (The Python window stays running in taskbar)
exit