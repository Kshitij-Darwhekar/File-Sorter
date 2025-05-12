@echo off
REM Get the directory where the batch file is located
set SCRIPT_DIR=%~dp0

REM Change to that directory
cd /d "%SCRIPT_DIR%"

REM Run the Python script
python sorter.py

REM Display beautiful completion message
echo.
echo ┌─────────────────────────────────────────────┐
echo │     ✅ Sorting completed successfully!      │
echo └─────────────────────────────────────────────┘
echo        Press any key to exit...
pause >nul
