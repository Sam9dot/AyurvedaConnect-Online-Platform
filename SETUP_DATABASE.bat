@echo off
echo ========================================
echo   AyurvedaConnect - Database Setup
echo ========================================
echo.

cd backend

echo Activating virtual environment...
call venv\Scripts\activate

echo.
echo Step 1: Creating database tables...
python migrate_db.py

echo.
echo Step 2: Seeding Excel data...
python seed_data_excel.py

echo.
echo ========================================
echo   Database setup complete!
echo ========================================
echo.
echo You can now start the backend server.
echo.
pause
