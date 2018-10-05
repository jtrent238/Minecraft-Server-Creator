@echo off
cls

If NOT exist "Temp" (
	mkdir "Temp"
) 

SET TEMP_PYTHONVERSION=%random%.temp

python -V>>Temp\%TEMP_PYTHONVERSION%
echo %TEMP_PYTHONVERSION%
echo Current Python version: <Temp\%TEMP_PYTHONVERSION%

::pip install wget
::pip install raven --upgrade
::python Main.py
pause>nul