@echo off
echo Starting Professional GUI Application...
echo.

:: Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher.
    pause
    exit /b 1
)

:: Check if PySide6 is installed
python -c "import PySide6" >nul 2>&1
if errorlevel 1 (
    echo PySide6 is not installed.
    echo Installing PySide6...
    pip install PySide6
    if errorlevel 1 (
        echo Failed to install PySide6.
        pause
        exit /b 1
    )
)

:: Run the application
echo Running application...
python main.py

:: Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Application exited with an error.
    pause
)
