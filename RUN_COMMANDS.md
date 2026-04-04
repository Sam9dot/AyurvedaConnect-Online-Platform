# 🌿 AyurvedaConnect - Quick Start Commands

## Terminal Commands to Run the Application

### Step 1: Setup Backend (First Terminal)

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create database tables
python migrate_db.py

# Seed Excel data into database
python seed_data_excel.py

# Start backend server
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

**Backend will run at:** http://127.0.0.1:8000

---

### Step 2: Setup Frontend (Second Terminal)

```bash
# Navigate to frontend folder
cd frontend

# Start HTTP server (choose one option)

# Option A: Python 3
python -m http.server 8080

# Option B: Python 2
python -m SimpleHTTPServer 8080

# Option C: Node.js (if installed)
npx http-server -p 8080

# Option D: PHP (if installed)
php -S localhost:8080
```

**Frontend will run at:** http://localhost:8080

---

## Quick Access URLs

- **Home Page:** http://localhost:8080/index.html
- **Login:** http://localhost:8080/login.html
- **Signup:** http://localhost:8080/signup.html
- **Doctors:** http://localhost:8080/doctors.html
- **Wellness Centres:** http://localhost:8080/wellness.html
- **Products:** http://localhost:8080/products.html
- **API Docs:** http://127.0.0.1:8000/docs

---

## Database Configuration

Before running, edit `backend/.env`:

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ayurveda_db
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
```

Create the database in MySQL:
```sql
CREATE DATABASE ayurveda_db;
```

---

## What Gets Seeded

When you run `python seed_data_excel.py`, the following data from your Excel sheet is added:

### Doctors (8 total):
1. Dr. Shubhangi Kulkarni - 10+ yrs exp, 20-40 daily footfall
2. Dr. Nilesh Patil - 6-10 yrs exp, 10-20 daily footfall
3. Dr. Swati Deshpande - 6-10 yrs exp, 20-40 daily footfall
4. Dr. Amol Jadhav - 3-5 yrs exp, 10-20 daily footfall
5. Dr. Priyanka More - 3-5 yrs exp, 10-20 daily footfall
6. Dr. Rahul Pawar - 10+ yrs exp, 20-40 daily footfall
7. Dr. Sneha Bhosale - 0-2 yrs exp, 0-10 daily footfall
8. Dr. Mahesh Shinde - 10+ yrs exp, 40+ daily footfall

### Yoga Centres (7 total):
1. Omkar Yoga & Meditation Centre - 6-10 yrs exp
2. Prana Yog Wellness Studio - 3-5 yrs exp
3. Dhankawadi Yoga Sadhana Kendra - 10+ yrs exp
4. Shree Yoga & Fitness Hub - 0-2 yrs exp
5. Aarogyam Yoga Centre - 6-10 yrs exp
6. Surya Namaskar Yoga Academy - 10+ yrs exp
7. MindBody Yoga Studio - 3-5 yrs exp

### Wellness Centres (7 total):
1. Arogyam Ayurvedic Wellness Centre - 6-10 yrs exp
2. Panchamrit Panchakarma Clinic - 10+ yrs exp
3. Jeevan Ayurveda & Wellness - 3-5 yrs exp
4. Sattva Holistic Healing Centre - 6-10 yrs exp
5. AyurSparsh Therapy Centre - 3-5 yrs exp
6. Tridosha Wellness Studio - 0-2 yrs exp
7. Prakruti Natural Healing Centre - 10+ yrs exp

---

## User Roles & Features

### 1. Patient (Default)
- Browse doctors and wellness centres
- Book appointments
- Purchase products
- View order history

### 2. Doctor
- Create/update profile (appears in doctors list automatically)
- View appointments
- Manage availability
- Update bio and specialization

### 3. Seller
- Add/edit products
- View orders
- Manage inventory
- Track sales

### 4. Wellness Centre
- Manage centre information
- View bookings
- Update facilities and services
- Manage schedules

### 5. Admin
- View all users, doctors, centres
- Delete any entity
- View system statistics
- Full platform control

---

## Testing the Application

### Create Test Accounts:
1. Go to http://localhost:8080/signup.html
2. Select user type (patient/doctor/seller/wellness/admin)
3. Enter email and password (min 8 characters)
4. Click "Create Account"

### Test Doctor Flow:
1. Signup as "doctor"
2. Login → redirects to doctor dashboard
3. Create profile with specialization, experience, location
4. Profile automatically appears in doctors list
5. View appointments from patients

### Test Admin Flow:
1. Signup as "admin"
2. Login → redirects to admin dashboard
3. View statistics (total users, doctors, centres)
4. Manage all entities
5. Delete users/doctors/centres

---

## Troubleshooting

### Backend won't start:
```bash
# Check if MySQL is running
# Verify .env file has correct credentials
# Try: pip install --upgrade -r requirements.txt
```

### Frontend can't connect:
```bash
# Ensure backend is running on port 8000
# Check browser console for errors (F12)
# Clear browser cache and cookies
```

### Database errors:
```bash
# Re-run migrations
python migrate_db.py

# Check MySQL connection
mysql -u your_username -p -e "SHOW DATABASES;"
```

### Port already in use:
```bash
# Backend: Change port in uvicorn command
uvicorn app.main:app --reload --port 8001

# Frontend: Change port in http.server command
python -m http.server 8081
```

---

## Development Tips

### Auto-reload on changes:
- Backend: Already enabled with `--reload` flag
- Frontend: Just refresh browser (F5)

### View API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

### Check database:
```bash
mysql -u your_username -p ayurveda_db

# View tables
SHOW TABLES;

# View doctors
SELECT * FROM doctors;

# View wellness centres
SELECT * FROM wellness_centers;
```

### Clear all data and reseed:
```bash
# Drop and recreate database
mysql -u your_username -p -e "DROP DATABASE ayurveda_db; CREATE DATABASE ayurveda_db;"

# Re-run migrations and seed
python migrate_db.py
python seed_data_excel.py
```

---

## Production Deployment Notes

For production deployment:
1. Use environment variables for sensitive data
2. Set up proper WSGI server (gunicorn)
3. Use nginx/Apache for frontend
4. Enable HTTPS with SSL certificates
5. Set up database backups
6. Configure proper CORS origins
7. Use production-grade database (not localhost)

---

## Key Improvements Made

### Backend:
✅ Admin routes for full system control
✅ Doctor profile creation and update endpoints
✅ Excel data seeding directly to database
✅ Enhanced authentication and authorization
✅ Better error handling

### Frontend:
✅ Center-aligned dashboards
✅ Enhanced Ayurveda aesthetics (natural colors, patterns)
✅ Better images with Ayurveda feel
✅ Improved UI components (cards, buttons, forms)
✅ Responsive design for all screen sizes
✅ Role-specific dashboards

### Features:
✅ Doctors can create profiles that auto-appear in listings
✅ Admin can manage all entities
✅ Sellers can manage products
✅ Wellness centres can manage bookings
✅ All data from Excel sheet in database

---

## Need Help?

Check the logs:
- Backend: Terminal where uvicorn is running
- Frontend: Browser console (F12 → Console tab)
- Database: MySQL error logs

Happy coding! 🌿
