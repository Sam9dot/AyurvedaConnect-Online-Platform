"""
Seed script — populates doctors and wellness centres from the Excel data.
Run: python seed_data.py
"""
from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(dotenv_path=BASE_DIR / ".env", override=False)

if os.getenv("DATABASE_URL"):
    DATABASE_URL = os.environ["DATABASE_URL"]
else:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "ayurvedaconnect")
    DB_USER = os.getenv("DB_USER", "USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "PASSWORD")
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# ======= EXCEL DATA =======

DOCTORS = [
    {"name": "Dr. Shubhangi Kulkarni", "specialization": "Ayurvedic Doctor", "experience": "10+", "daily_footfall": "20-40", "location": "Koregaon Park, Pune", "phone": "+91 20 2567 1234", "image_url": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=800&q=80", "bio": "Expert in Panchakarma therapy and chronic disease management with over a decade of experience.", "rating": 4.9},
    {"name": "Dr. Nilesh Patil", "specialization": "Ayurvedic Doctor", "experience": "6-10", "daily_footfall": "10-20", "location": "Shivajinagar, Pune", "phone": "+91 20 2553 4567", "image_url": "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=800&q=80", "bio": "Specializes in digestive health and Ayurvedic nutrition counseling.", "rating": 4.7},
    {"name": "Dr. Swati Deshpande", "specialization": "Ayurvedic Doctor", "experience": "6-10", "daily_footfall": "20-40", "location": "Baner, Pune", "phone": "+91 20 2445 6789", "image_url": "https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&w=800&q=80", "bio": "Renowned for women's wellness, prenatal care, and stress management therapies.", "rating": 4.8},
    {"name": "Dr. Amol Jadhav", "specialization": "Ayurvedic Doctor", "experience": "3-5", "daily_footfall": "10-20", "location": "Aundh, Pune", "phone": "+91 20 2612 3456", "image_url": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=800&q=80", "bio": "Young practitioner focused on sports injuries and musculoskeletal Ayurveda.", "rating": 4.5},
    {"name": "Dr. Priyanka More", "specialization": "Ayurvedic Doctor", "experience": "3-5", "daily_footfall": "10-20", "location": "Hadapsar, Pune", "phone": "+91 20 2567 8901", "image_url": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=800&q=80", "bio": "Pediatric Ayurveda specialist with a gentle approach to child wellness.", "rating": 4.6},
    {"name": "Dr. Rahul Pawar", "specialization": "Ayurvedic Doctor", "experience": "10+", "daily_footfall": "20-40", "location": "Deccan Gymkhana, Pune", "phone": "+91 20 2443 2211", "image_url": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=800&q=80", "bio": "Senior Ayurvedic physician known for detox and rejuvenation programs.", "rating": 4.9},
    {"name": "Dr. Sneha Bhosale", "specialization": "Ayurvedic Doctor", "experience": "0-2", "daily_footfall": "0-10", "location": "Viman Nagar, Pune", "phone": "+91 20 2556 7788", "image_url": "https://images.unsplash.com/photo-1643297654416-05795d62e39c?auto=format&fit=crop&w=800&q=80", "bio": "Fresh graduate passionate about integrating modern diagnostics with traditional Ayurveda.", "rating": 4.3},
    {"name": "Dr. Mahesh Shinde", "specialization": "Ayurvedic Doctor", "experience": "10+", "daily_footfall": "40+", "location": "Kothrud, Pune", "phone": "+91 20 2423 9900", "image_url": "https://images.unsplash.com/photo-1582750433449-648ed127bb54?auto=format&fit=crop&w=800&q=80", "bio": "Most experienced practitioner with mastery in rare Ayurvedic formulations and Netra Chikitsa.", "rating": 4.9},
]

YOGA_CENTRES = [
    {"name": "Omkar Yoga & Meditation Centre", "experience": "6-10", "location": "Koregaon Park, Pune", "phone": "+91 20 2615 1100", "services": "Hatha Yoga, Meditation, Pranayama, Yoga Therapy", "image_url": "https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=800&q=80", "rating": 4.7},
    {"name": "Prana Yog Wellness Studio", "experience": "3-5", "location": "Baner, Pune", "phone": "+91 20 2729 2200", "services": "Ashtanga Yoga, Power Yoga, Restorative Yoga", "image_url": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80", "rating": 4.5},
    {"name": "Dhankawadi Yoga Sadhana Kendra", "experience": "10+", "location": "Dhankawadi, Pune", "phone": "+91 20 2436 3300", "services": "Traditional Yoga, Kriyas, Shatkarma, Meditation Retreats", "image_url": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?auto=format&fit=crop&w=800&q=80", "rating": 4.8},
    {"name": "Shree Yoga & Fitness Hub", "experience": "0-2", "location": "Wakad, Pune", "phone": "+91 20 2687 4400", "services": "Yoga for Beginners, Flexibility Training, Fitness Yoga", "image_url": "https://images.unsplash.com/photo-1575052814086-f385e2e2ad33?auto=format&fit=crop&w=800&q=80", "rating": 4.3},
    {"name": "Aarogyam Yoga Centre", "experience": "6-10", "location": "Kalyani Nagar, Pune", "phone": "+91 20 2668 5500", "services": "Therapeutic Yoga, Prenatal Yoga, Senior Yoga, Workshops", "image_url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=800&q=80", "rating": 4.6},
    {"name": "Surya Namaskar Yoga Academy", "experience": "10+", "location": "Camp, Pune", "phone": "+91 20 2614 6600", "services": "Teacher Training, Advanced Asanas, Yoga Philosophy", "image_url": "https://images.unsplash.com/photo-1588286840104-8957b019727f?auto=format&fit=crop&w=800&q=80", "rating": 4.9},
    {"name": "MindBody Yoga Studio", "experience": "3-5", "location": "Hinjawadi, Pune", "phone": "+91 20 2293 7700", "services": "Vinyasa Flow, Yin Yoga, Sound Healing, Corporate Yoga", "image_url": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=800&q=80", "rating": 4.5},
]

WELLNESS_CENTRES = [
    {"name": "Arogyam Ayurvedic Wellness Centre", "experience": "6-10", "location": "Kothrud, Pune", "phone": "+91 20 2546 1100", "services": "Panchakarma, Abhyanga, Shirodhara, Ayurvedic Detox", "image_url": "https://images.unsplash.com/photo-1600334089648-b0d9d3028eb2?auto=format&fit=crop&w=800&q=80", "rating": 4.7},
    {"name": "Panchamrit Panchakarma Clinic", "experience": "10+", "location": "Sadashiv Peth, Pune", "phone": "+91 20 2447 2200", "services": "Nasya, Vamana, Virechana, Basti, Full Panchakarma", "image_url": "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=800&q=80", "rating": 4.8},
    {"name": "Jeevan Ayurveda & Wellness", "experience": "3-5", "location": "Magarpatta, Pune", "phone": "+91 20 4000 3300", "services": "Herbal Therapy, Nutrition Consult, Online Consultations", "image_url": "https://images.unsplash.com/photo-1540555700478-4be289fbec6d?auto=format&fit=crop&w=800&q=80", "rating": 4.5},
    {"name": "Sattva Holistic Healing Centre", "experience": "6-10", "location": "Baner Road, Pune", "phone": "+91 20 2729 4400", "services": "Kerala Treatments, Oil Therapy, Pizhichil, Herbal Bath", "image_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=800&q=80", "rating": 4.6},
    {"name": "AyurSparsh Therapy Centre", "experience": "3-5", "location": "Tilak Road, Pune", "phone": "+91 20 2447 5500", "services": "Stress Relief, Joint Care, Skin Therapy, Hair Treatment", "image_url": "https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&w=800&q=80", "rating": 4.4},
    {"name": "Tridosha Wellness Studio", "experience": "0-2", "location": "Aundh, Pune", "phone": "+91 20 4920 6600", "services": "Dosha Balancing, Diet Plans, Lifestyle Coaching, Marma", "image_url": "https://images.unsplash.com/photo-1552693673-1bf958298935?auto=format&fit=crop&w=800&q=80", "rating": 4.3},
    {"name": "Prakruti Natural Healing Centre", "experience": "10+", "location": "Koregaon Park, Pune", "phone": "+91 20 2612 7700", "services": "Naturopathy, Ayurveda, Mud Therapy, Hydrotherapy, Fasting", "image_url": "https://images.unsplash.com/photo-1600334089648-b0d9d3028eb2?auto=format&fit=crop&w=800&q=80", "rating": 4.9},
]

def main():
    print(f"Connecting to: {DATABASE_URL.split('@')[-1]}")
    session = Session()
    try:
        # Clear existing seeded data
        session.execute(text("DELETE FROM doctors WHERE user_id IS NULL"))
        session.execute(text("DELETE FROM wellness_centers"))
        session.commit()
        print("  Cleared existing seed data.")

        # Seed doctors
        for d in DOCTORS:
            session.execute(text(
                "INSERT INTO doctors (name, specialization, experience, phone, location, image_url, daily_footfall, bio, rating) "
                "VALUES (:name, :specialization, :experience, :phone, :location, :image_url, :daily_footfall, :bio, :rating)"
            ), d)
        session.commit()
        print(f"  Seeded {len(DOCTORS)} doctors.")

        # Seed yoga centres
        for y in YOGA_CENTRES:
            session.execute(text(
                "INSERT INTO wellness_centers (name, location, center_type, experience, phone, services, image_url, rating) "
                "VALUES (:name, :location, 'yoga', :experience, :phone, :services, :image_url, :rating)"
            ), y)
        session.commit()
        print(f"  Seeded {len(YOGA_CENTRES)} yoga centres.")

        # Seed wellness centres
        for w in WELLNESS_CENTRES:
            session.execute(text(
                "INSERT INTO wellness_centers (name, location, center_type, experience, phone, services, image_url, rating) "
                "VALUES (:name, :location, 'wellness', :experience, :phone, :services, :image_url, :rating)"
            ), w)
        session.commit()
        print(f"  Seeded {len(WELLNESS_CENTRES)} wellness centres.")

        print("Seeding complete!")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    main()
