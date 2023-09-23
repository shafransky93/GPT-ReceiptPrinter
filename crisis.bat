@echo off
start "Check Brain" check_brain.bat

:loop
start "You Pass the Butter" python you_pass_the_butter.py
timeout /t 100
taskkill /f /im python.exe
python brain_print.py
goto loop
