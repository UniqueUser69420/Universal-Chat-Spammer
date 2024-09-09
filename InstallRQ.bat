@echo off
pip install keyboard tk selenium scipy pytesseract pillow pil
if %errorlevel% neq 0 (
    echo Installation failed. Please check your internet connection and pip installation.
) else (
    echo Installation successful!
)
pause