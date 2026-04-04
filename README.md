# 🌿 AyurvedaConnect - Complete Wellness Platform

A comprehensive Ayurveda and wellness platform connecting patients with doctors, yoga centres, and wellness facilities. Features role-based dashboards, appointment booking, product marketplace, and admin controls.

![Version](https://img.shields.io/badge/version-2.0-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-teal)
![License](https://img.shields.io/badge/license-MIT-yellow)

---

## ✨ Features

### 👥 Multi-Role System
- **Patients**: Browse doctors, book appointments, purchase products
- **Doctors**: Create profiles, manage appointments, appear in listings
- **Sellers**: Manage products, track orders, view analytics
- **Wellness Centres**: Manage facilities, bookings, services
- **Admins**: Full platform control, user management, statistics

### 🎨 Beautiful UI
- Authentic Ayurveda aesthetics with natural colors
- Center-aligned, responsive dashboards
- Smooth animations and transitions
- Mobile-friendly design
- Professional card layouts

### 📊 Complete Data
- 8 Ayurvedic Doctors from Excel sheet
- 7 Yoga Centres with facilities
- 7 Wellness Centres with services
- All data includes ratings, experience, contact info

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- MySQL database
- Web browser

### Option 1: Using Batch Files (Windows - Easiest!)

1. **Setup Database** (First time only)
   ```
   Double-click: SETUP_DATABASE.bat
   ```

2. **Start Backend** (Terminal 1)
   ```
   Double-click: START_BACKEND.bat
   ```

3. **Start Frontend** (Terminal 2)
   ```
   Double-click: START_FRONTEND.bat
   ```

4. **Open Browser**
   ```
   http://localhost:8080/index.html
   ```

### Option 2: Manual Commands

#### Backend Setup:
```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/Mac
pip install -r requirements.txt
python migrate_db.py
python seed_data_excel.py
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

#### Frontend Setup:
```bash
cd frontend
python -m http.server 8080
```

---

## 📁 Project Structure

```
AyurvedaConnect/
├── backend/
│   ├── app/
│   │   ├── models/          # Database models
│   │   ├── routes/          # API endpoints
│   │   ├── services/        # Business logic
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── dependencies/    # Auth & dependencies
│   │   ├── database.py      # DB configuration
│   │   └── main.py          # FastAPI app
│   ├── migrate_db.py        # Create tables
│   ├── seed_data_excel.py   # Seed Excel data
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Database config
├── frontend/
│   ├── css/
│   │   └── styles.css       # Enhanced Ayurveda styles
│   ├── js/
│   │   └── app.js           # Frontend logic
│   ├── assets/              # Images and assets
│   ├── index.html           # Home page
│   ├── login.html           # Login page
│   ├── signup.html          # Registration
│   ├── doctors.html         # Doctors listing
│   ├── wellness.html        # Wellness centres
│   ├── products.html        # Product marketplace
│   ├── dashboard.html       # Patient dashboard
│   ├── doctor-dashboard.html    # Doctor panel
│   ├── seller-dashboard.html    # Seller panel
│   ├── wellness-dashboard.html  # Centre panel
│   └── admin-dashboard.html     # Admin panel
├── START_BACKEND.bat        # Quick start backend
├── START_FRONTEND.bat       # Quick start frontend
├── SETUP_DATABASE.bat       # Setup database
├── RUN_COMMANDS.md          # Detailed commands
├── SETUP_INSTRUCTIONS.md    # Full setup guide
├── IMPROVEMENTS_SUMMARY.md  # All improvements
└── README.md                # This file
```

---

## 🗄️ Database Configuration

Edit `backend/.env`:
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ayurveda_db
DB_USER=your_username
DB_PASSWORD=your_password
```

Create database in MySQL:
```sql
CREATE DATABASE ayurveda_db;
```

---

## 👤 User Roles & Capabilities

### Patient
- Browse doctors and wellness centres
- View detailed profiles with ratings
- Book appointments
- Purchase Ayurvedic products
- Track orders
- View appointment history

### Doctor
- Create professional profile
- Update specialization, experience, bio
- Profile automatically appears in doctors list
- View patient appointments
- Manage availability
- Update contact information

### Seller
- Add new products
- Edit product details
- View all orders
- Track inventory
- Manage product categories
- View sales analytics

### Wellness Centre
- Manage centre information
- Update services and facilities
- View bookings
- Manage schedules
- Update contact details
- Track visitor statistics

### Admin
- View all users by type
- System statistics dashboard
- Delete users, doctors, centres
- Full platform management
- Monitor activity
- Access all features

---

## 🎨 UI Highlights

### Color Scheme
- **Forest Green**: #1b5e20, #2e7d32 (Primary)
- **Gold**: #c9a227 (Accent)
- **Cream**: #fafdf6 (Background)
- **Peach**: #ffe5d9 (Warm accent)

### Design Elements
- Organic leaf pattern backgrounds
- Lotus flower decorations
- Smooth gradients
- Soft shadows
- Rounded corners
- Hover animations
- Responsive grids

### Typography
- **Headings**: Playfair Display (elegant, traditional)
- **Body**: Poppins (modern, readable)

---

## 📊 Excel Data Included

### Doctors (8):
All with experience, daily footfall, ratings, specializations, and contact info

### Yoga Centres (7):
Complete with facilities, services, experience, and ratings

### Wellness Centres (7):
Full details including therapies, amenities, and contact information

---

## 🔗 Important URLs

### Frontend:
- Home: http://localhost:8080/index.html
- Login: http://localhost:8080/login.html
- Signup: http://localhost:8080/signup.html
- Doctors: http://localhost:8080/doctors.html
- Wellness: http://localhost:8080/wellness.html

### Backend:
- API Base: http://127.0.0.1:8000
- Swagger Docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

## 🧪 Testing

### Create Test Accounts:
1. Go to signup page
2. Choose role (patient/doctor/seller/wellness/admin)
3. Enter email and password (min 8 chars)
4. Login and explore role-specific features

### Test Doctor Flow:
1. Signup as "doctor"
2. Login → doctor dashboard
3. Create profile
4. Check doctors list → your profile appears
5. Update profile anytime

### Test Admin Flow:
1. Signup as "admin"
2. Login → admin dashboard
3. View statistics
4. Manage all entities
5. Delete test data

---

## 🛠️ Tech Stack

### Backend:
- **Framework**: FastAPI
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Auth**: JWT (python-jose)
- **Validation**: Pydantic
- **Password**: bcrypt

### Frontend:
- **HTML5**: Semantic markup
- **CSS3**: Custom styles, animations
- **JavaScript**: Vanilla JS (no frameworks)
- **Icons**: SVG (Lucide-style)

---

## 📝 API Endpoints

### Authentication:
- `POST /auth/register` - Create account
- `POST /auth/login` - Login
- `GET /auth/me` - Get current user

### Doctors:
- `GET /doctors` - List all doctors
- `GET /doctors/{id}` - Get doctor details
- `POST /doctors` - Create profile (auth)
- `PUT /doctors/{id}` - Update profile (auth)
- `GET /doctors/my/profile` - Get my profile (auth)

### Wellness:
- `GET /wellness` - List centres
- `GET /wellness/{id}` - Get centre details

### Admin:
- `GET /admin/users` - List all users (admin)
- `GET /admin/stats` - System statistics (admin)
- `DELETE /admin/users/{id}` - Delete user (admin)
- `DELETE /admin/doctors/{id}` - Delete doctor (admin)
- `DELETE /admin/wellness/{id}` - Delete centre (admin)

---

## 🐛 Troubleshooting

### Backend won't start:
- Check MySQL is running
- Verify `.env` credentials
- Run: `pip install --upgrade -r requirements.txt`

### Frontend can't connect:
- Ensure backend is on port 8000
- Check browser console (F12)
- Clear cache and cookies

### Database errors:
- Re-run: `python migrate_db.py`
- Check MySQL permissions
- Verify database exists

### Port already in use:
- Change backend port: `--port 8001`
- Change frontend port: `8081`

---

## 📚 Documentation

- **Setup Guide**: `SETUP_INSTRUCTIONS.md`
- **Quick Commands**: `RUN_COMMANDS.md`
- **Improvements**: `IMPROVEMENTS_SUMMARY.md`
- **API Docs**: http://127.0.0.1:8000/docs

---

## 🔐 Security

- JWT authentication
- Password hashing (bcrypt)
- Role-based access control
- Protected admin routes
- Input validation
- SQL injection prevention
- CORS configuration

---

## 🚀 Deployment

For production:
1. Use environment variables
2. Set up WSGI server (gunicorn)
3. Configure nginx/Apache
4. Enable HTTPS
5. Set up database backups
6. Configure proper CORS
7. Use production database

---

## 📄 License

MIT License - feel free to use for personal or commercial projects

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

---

## 📞 Support

For issues or questions:
- Check documentation files
- Review API docs at `/docs`
- Check browser console (F12)
- Review backend terminal logs

---

## ✅ What's New in v2.0

- ✨ Complete Excel data integration
- 🎨 Enhanced Ayurveda aesthetics
- 📱 Center-aligned responsive dashboards
- 👨‍⚕️ Doctor profile creation
- 🛡️ Admin control panel
- 🏪 Seller product management
- 🧘 Wellness centre management
- 🔐 Enhanced security
- 📊 System statistics
- 🎯 Role-based features

---

## 🌟 Key Highlights

✅ **Production Ready** - Clean code, proper architecture
✅ **Fully Functional** - All roles working perfectly
✅ **Beautiful UI** - Authentic Ayurveda design
✅ **Complete Data** - All Excel data in database
✅ **Responsive** - Works on all devices
✅ **Secure** - JWT auth, role-based access
✅ **Well Documented** - Comprehensive guides
✅ **Easy Setup** - Batch files for Windows

---

**Built with 💚 for the Ayurveda community**

**Version**: 2.0  
**Last Updated**: April 3, 2026  
**Status**: ✅ Production Ready
