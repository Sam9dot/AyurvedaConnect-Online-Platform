@echo off
echo ========================================
echo   AyurvedaConnect - Starting Frontend
echo ========================================
echo.

cd frontend

echo Starting frontend server on http://localhost:8080
echo.
echo Open your browser and go to:
echo   http://localhost:8080/index.html
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python -m http.server 8080
