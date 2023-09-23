@echo off
:loop
cls
echo Inside of the brain is:
type "brain.txt"
ping -n 2 127.0.0.1 > nul
goto loop