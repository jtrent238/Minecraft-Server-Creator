@echo off
cls

If NOT exist "Temp" (
	mkdir "Temp"
) 

SET TEMP_PYTHONVERSION=%random%.temp

SET wget_NotInstalled=false
SET raven_NotInstalled=false

python -V>>Temp\%TEMP_PYTHONVERSION%
echo %TEMP_PYTHONVERSION%
echo Current Python version: <Temp\%TEMP_PYTHONVERSION%

If %wget_NotInstalled% "false" (
	pip install wget
	SET wget_NotInstalled=true
}

If %raven_NotInstalled% "false" (
	pip install raven --upgrade
	SET raven_NotInstalled=true
)

python Main.py
pause>nul