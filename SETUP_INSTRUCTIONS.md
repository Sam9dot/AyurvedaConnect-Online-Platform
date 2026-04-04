# AyurvedaConnect - Setup & Run Instructions

## Prerequisites
- Python 3.8+
- MySQL database
- pip (Python package manager)

## Backend Setup

### 1. Navigate to backend directory
```bash
cd backend
```

### 2. Create and activate virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Linux/Mac)
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure database
Edit `backend/.env` file with your MySQL credentials:
```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ayurveda_db
DB_USER=your_username
DB_PASSWORD=your_password
```

### 5. Create database
```bash
# Login to MySQL
mysql -u your_username -p

# Create database
CREATE DATABASE ayurveda_db;
EXIT;
```

### 6. Run migrations (create tables)
```bash
python migrate_db.py
```

### 7. Seed database with Excel data (Doctors & Wellness Centres)
```bash
python seed_data_excel.py
```
This will add:
- 8 Ayurvedic Doctors from the Excel sheet
- 7 Yoga Centres
- 7 Wellness Centres

### 8. Start backend server
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Backend will be running at: http://127.0.0.1:8000

## Frontend Setup

### 1. Open new terminal and navigate to frontend directory
```bash
cd frontend
```

### 2. Start a simple HTTP server

**Option A: Using Python**
```bash
# Python 3
python -m http.server 8080

# Python 2
python -m SimpleHTTPServer 8080
```

**Option B: Using Node.js (if installed)**
```bash
npx http-server -p 8080
```

**Option C: Using PHP (if installed)**
```bash
php -S localhost:8080
```

Frontend will be running at: http://localhost:8080

## Access the Application

1. **Home Page**: http://localhost:8080/index.html
2. **Login**: http://localhost:8080/login.html
3. **Signup**: http://localhost:8080/signup.html

## Default Test Accounts

After seeding, you can create accounts with these roles:
- **Patient**: Regular user account
- **Doctor**: Can create profile, manage appointments
- **Seller**: Can manage products
- **Wellness**: Can manage wellness center
- **Admin**: Full system access

## Key Features Implemented

### For Doctors:
- Create and update profile
- View appointments
- Profile automatically appears in doctors list
- Manage availability

### For Sellers:
- Add/edit products
- View orders
- Manage inventory

### For Wellness Centers:
- Manage center information
- View bookings
- Update facilities

### For Admin:
- View all users, doctors, centers
- Delete any entity
- View system statistics
- Full control over platform

### UI Improvements:
- Center-aligned dashboards
- Enhanced Ayurveda aesthetics
- Better color scheme with natural tones
- Improved images and icons
- Responsive design

## API Documentation

Once backend is running, visit:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Troubleshooting

### Backend won't start:
- Check MySQL is running
- Verify database credentials in `.env`
- Ensure all dependencies are installed

### Frontend can't connect to backend:
- Verify backend is running on port 8000
- Check CORS settings in `backend/app/main.py`
- Clear browser cache

### Database errors:
- Run `python migrate_db.py` again
- Check MySQL user permissions
- Verify database exists

## Development Workflow

1. Make changes to backend code
2. Backend auto-reloads (if using `--reload` flag)
3. Make changes to frontend code
4. Refresh browser to see changes

## Production Deployment

For production:
1. Set `DEBUG=False` in backend
2. Use proper WSGI server (gunicorn, uvicorn)
3. Set up proper database with backups
4. Use nginx/Apache for frontend
5. Enable HTTPS
6. Set proper CORS origins

## Support

For issues or questions, check:
- API documentation at `/docs`
- Console logs in browser (F12)
- Backend logs in terminal
