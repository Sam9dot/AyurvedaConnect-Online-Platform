"""
Seed database with data from Excel spreadsheet
Run this after migrate_db.py to populate the database with initial data
"""
import sys
from pathlib import Path

# Add parent directory to path to import app modules
sys.path.insert(0, str(Path(__file__).parent))

from app.database import SessionLocal, engine
from app.models.ayurveda_models import Doctors, WellnessCenters, Base
from sqlalchemy.exc import IntegrityError

def seed_excel_data():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Check if data already exists
        existing_doctors = db.query(Doctors).count()
        existing_centres = db.query(WellnessCenters).count()
        
        if existing_doctors > 0 or existing_centres > 0:
            print(f"⚠️  Database already has data ({existing_doctors} doctors, {existing_centres} centres)")
            response = input("Do you want to add more data anyway? (yes/no): ")
            if response.lower() not in ['yes', 'y']:
                print("Skipping seed operation.")
                return
        
        # Doctors from Excel - with Indian images
        doctors_data = [
            {
                "name": "Dr. Shubhangi Kulkarni",
                "specialization": "Ayurvedic Doctor",
                "experience": "10+",
                "daily_footfall": "20-40",
                "phone": "+91 20 2567 1234",
                "location": "Koregaon Park, Pune",
                "bio": "Expert in Panchakarma therapy and chronic disease management.",
                "rating": 4.9,
                "image_url": "https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&w=800&q=80"
            },
            {
                "name": "Dr. Nilesh Patil",
                "specialization": "Ayurvedic Doctor",
                "experience": "6-10",
                "daily_footfall": "10-20",
                "phone": "+91 20 2553 4567",
                "location": "Shivajinagar, Pune",
                "bio": "Specializes in digestive health and Ayurvedic nutrition.",
                "rating": 4.7,
                "image_url": "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=800&q=80"
            },
            {
                "name": "Dr. Swati Deshpande",
                "specialization": "Ayurvedic Doctor",
                "experience": "6-10",
                "daily_footfall": "20-40",
                "phone": "+91 20 2445 6789",
                "location": "Baner, Pune",
                "bio": "Renowned for women's wellness and stress management.",
                "rating": 4.8,
                "image_url": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=800&q=80"
            },
            {
                "name": "Dr. Amol Jadhav",
                "specialization": "Ayurvedic Doctor",
                "experience": "3-5",
                "daily_footfall": "10-20",
                "phone": "+91 20 2612 3456",
                "location": "Aundh, Pune",
                "bio": "Focused on sports injuries and musculoskeletal Ayurveda.",
                "rating": 4.5,
                "image_url": "https://images.unsplash.com/photo-1582750433449-648ed127bb54?auto=format&fit=crop&w=800&q=80"
            },
            {
                "name": "Dr. Priyanka More",
                "specialization": "Ayurvedic Doctor",
                "experience": "3-5",
                "daily_footfall": "10-20",
                "phone": "+91 20 2567 8901",
                "location": "Hadapsar, Pune",
                "bio": "Pediatric Ayurveda specialist with a gentle approach.",
                "rating": 4.6,
                "image_url": "https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=800&q=80"
            },
            {
                "name": "Dr. Rahul Pawar",
                "specialization": "Ayurvedic Doctor",
                "experience": "10+",
                "daily_footfall": "20-40",
                "phone": "+91 20 2443 2211",
                "location": "Deccan Gymkhana, Pune",
                "bio": "Senior physician known for detox and rejuvenation programs.",
                "rating": 4.9,
                "image_url": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=800&q=80"
            },
            {
                "name": "Dr. Sneha Bhosale",
                "specialization": "Ayurvedic Doctor",
                "experience": "0-2",
                "daily_footfall": "0-10",
                "phone": "+91 20 2556 7788",
                "location": "Viman Nagar, Pune",
                "bio": "Integrating modern diagnostics with traditional Ayurveda.",
                "rating": 4.3,
                "image_url": "https://images.unsplash.com/photo-1643297654416-05795d62e39c?auto=format&fit=crop&w=800&q=80"
            },
            {
                "name": "Dr. Mahesh Shinde",
                "specialization": "Ayurvedic Doctor",
                "experience": "10+",
                "daily_footfall": "40+",
                "phone": "+91 20 2423 9900",
                "location": "Kothrud, Pune",
                "bio": "Mastery in rare Ayurvedic formulations and Netra Chikitsa.",
                "rating": 4.9,
                "image_url": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=800&q=80"
            }
        ]
        
        print("📋 Seeding doctors from Excel data...")
        doctors_added = 0
        for doc_data in doctors_data:
            # Check if doctor already exists by name
            existing = db.query(Doctors).filter(Doctors.name == doc_data["name"]).first()
            if not existing:
                doctor = Doctors(**doc_data)
                db.add(doctor)
                doctors_added += 1
        
        # Yoga Centres from Excel
        yoga_centres = [
            {
                "name": "Omkar Yoga & Meditation Centre",
                "center_type": "yoga",
                "location": "Koregaon Park, Pune",
                "services": "Hatha Yoga, Meditation, Pranayama, Yoga Therapy",
                "phone": "+91 20 2615 1100",
                "experience": "6-10",
                "rating": 4.7,
                "image_url": "https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=800&q=80",
                "amenities": "Yoga Hall, Meditation Room, Pranayama Zone, Herbal Tea Lounge"
            },
            {
                "name": "Prana Yog Wellness Studio",
                "center_type": "yoga",
                "location": "Baner, Pune",
                "services": "Ashtanga Yoga, Power Yoga, Restorative Yoga",
                "phone": "+91 20 2729 2200",
                "experience": "3-5",
                "rating": 4.5,
                "image_url": "https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80",
                "amenities": "Practice Studio, Props Room, Changing Rooms, Juice Bar"
            },
            {
                "name": "Dhankawadi Yoga Sadhana Kendra",
                "center_type": "yoga",
                "location": "Dhankawadi, Pune",
                "services": "Traditional Yoga, Kriyas, Shatkarma, Retreats",
                "phone": "+91 20 2436 3300",
                "experience": "10+",
                "rating": 4.8,
                "image_url": "https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?auto=format&fit=crop&w=800&q=80",
                "amenities": "Open-Air Shala, Meditation Garden, Library, Dormitory"
            },
            {
                "name": "Shree Yoga & Fitness Hub",
                "center_type": "yoga",
                "location": "Wakad, Pune",
                "services": "Yoga for Beginners, Flexibility, Fitness Yoga",
                "phone": "+91 20 2687 4400",
                "experience": "0-2",
                "rating": 4.3,
                "image_url": "https://images.unsplash.com/photo-1575052814086-f385e2e2ad33?auto=format&fit=crop&w=800&q=80",
                "amenities": "AC Studio, Fitness Zone, Consultation Desk"
            },
            {
                "name": "Aarogyam Yoga Centre",
                "center_type": "yoga",
                "location": "Kalyani Nagar, Pune",
                "services": "Therapeutic Yoga, Prenatal Yoga, Workshops",
                "phone": "+91 20 2668 5500",
                "experience": "6-10",
                "rating": 4.6,
                "image_url": "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=800&q=80",
                "amenities": "Therapy Room, Prenatal Suite, Workshop Hall, Garden"
            },
            {
                "name": "Surya Namaskar Yoga Academy",
                "center_type": "yoga",
                "location": "Camp, Pune",
                "services": "Teacher Training, Advanced Asanas, Philosophy",
                "phone": "+91 20 2614 6600",
                "experience": "10+",
                "rating": 4.9,
                "image_url": "https://images.unsplash.com/photo-1588286840104-8957b019727f?auto=format&fit=crop&w=800&q=80",
                "amenities": "Training Hall, Philosophy Library, Exam Centre, Canteen"
            },
            {
                "name": "MindBody Yoga Studio",
                "center_type": "yoga",
                "location": "Hinjawadi, Pune",
                "services": "Vinyasa, Yin Yoga, Sound Healing, Corporate Yoga",
                "phone": "+91 20 2293 7700",
                "experience": "3-5",
                "rating": 4.5,
                "image_url": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=800&q=80",
                "amenities": "Heated Studio, Sound Room, Corporate Lounge, Resting Area"
            }
        ]
        
        # Wellness Centres from Excel
        wellness_centres = [
            {
                "name": "Arogyam Ayurvedic Wellness Centre",
                "center_type": "wellness",
                "location": "Kothrud, Pune",
                "services": "Panchakarma, Abhyanga, Shirodhara, Detox",
                "phone": "+91 20 2546 1100",
                "experience": "6-10",
                "rating": 4.7,
                "image_url": "https://images.unsplash.com/photo-1600334089648-b0d9d3028eb2?auto=format&fit=crop&w=800&q=80",
                "amenities": "Panchakarma Suite, Steam Room, Herbal Garden, Consultation"
            },
            {
                "name": "Panchamrit Panchakarma Clinic",
                "center_type": "wellness",
                "location": "Sadashiv Peth, Pune",
                "services": "Nasya, Vamana, Virechana, Basti, Full Panchakarma",
                "phone": "+91 20 2447 2200",
                "experience": "10+",
                "rating": 4.8,
                "image_url": "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=800&q=80",
                "amenities": "5 Therapy Rooms, Preparation Lab, Recovery Suite, Herbal Store"
            },
            {
                "name": "Jeevan Ayurveda & Wellness",
                "center_type": "wellness",
                "location": "Magarpatta, Pune",
                "services": "Herbal Therapy, Nutrition Consult, Online Consults",
                "phone": "+91 20 4000 3300",
                "experience": "3-5",
                "rating": 4.5,
                "image_url": "https://images.unsplash.com/photo-1540555700478-4be289fbec6d?auto=format&fit=crop&w=800&q=80",
                "amenities": "Tele-Consult Room, Treatment Wing, Diet Lab, Dispensary"
            },
            {
                "name": "Sattva Holistic Healing Centre",
                "center_type": "wellness",
                "location": "Baner Road, Pune",
                "services": "Kerala Treatments, Oil Therapy, Pizhichil, Herbal Bath",
                "phone": "+91 20 2729 4400",
                "experience": "6-10",
                "rating": 4.6,
                "image_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=800&q=80",
                "amenities": "Abhyanga Room, Pizhichil Chamber, Herbal Bath, Ayurvedic Kitchen"
            },
            {
                "name": "AyurSparsh Therapy Centre",
                "center_type": "wellness",
                "location": "Tilak Road, Pune",
                "services": "Stress Relief, Joint Care, Skin Therapy",
                "phone": "+91 20 2447 5500",
                "experience": "3-5",
                "rating": 4.4,
                "image_url": "https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&w=800&q=80",
                "amenities": "Therapy Rooms, Relaxation Lounge, Herbal Pharmacy"
            },
            {
                "name": "Tridosha Wellness Studio",
                "center_type": "wellness",
                "location": "Aundh, Pune",
                "services": "Dosha Balancing, Diet Plans, Lifestyle Coaching",
                "phone": "+91 20 4920 6600",
                "experience": "0-2",
                "rating": 4.3,
                "image_url": "https://images.unsplash.com/photo-1552693673-1bf958298935?auto=format&fit=crop&w=800&q=80",
                "amenities": "Consultation Room, Diet Planning Lab, Marma Therapy"
            },
            {
                "name": "Prakruti Natural Healing Centre",
                "center_type": "wellness",
                "location": "Koregaon Park, Pune",
                "services": "Naturopathy, Ayurveda, Mud Therapy, Hydrotherapy",
                "phone": "+91 20 2612 7700",
                "experience": "10+",
                "rating": 4.9,
                "image_url": "https://images.unsplash.com/photo-1600334089648-b0d9d3028eb2?auto=format&fit=crop&w=800&q=80",
                "amenities": "Mud Therapy Room, Hydro Pool, Fasting Suite, Nature Garden, Yoga Deck"
            }
        ]
        
        print("🧘 Seeding wellness centres from Excel data...")
        centres_added = 0
        for centre_data in yoga_centres + wellness_centres:
            # Check if centre already exists by name
            existing = db.query(WellnessCenters).filter(WellnessCenters.name == centre_data["name"]).first()
            if not existing:
                centre = WellnessCenters(**centre_data)
                db.add(centre)
                centres_added += 1
        
        db.commit()
        
        print("\n" + "="*60)
        print("✅ Excel data seeded successfully!")
        print("="*60)
        print(f"📊 Summary:")
        print(f"   • Doctors added: {doctors_added}")
        print(f"   • Wellness centres added: {centres_added}")
        print(f"   • Total doctors in DB: {db.query(Doctors).count()}")
        print(f"   • Total centres in DB: {db.query(WellnessCenters).count()}")
        print("="*60)
        
    except IntegrityError as e:
        db.rollback()
        print(f"❌ Database integrity error: {e}")
        print("Some data may already exist in the database.")
    except Exception as e:
        db.rollback()
        print(f"❌ Error seeding data: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🌿 AyurvedaConnect - Database Seeding")
    print("="*60)
    print("This will populate your database with:")
    print("  • 8 Ayurvedic Doctors")
    print("  • 7 Yoga Centres")
    print("  • 7 Wellness Centres")
    print("="*60 + "\n")
    
    seed_excel_data()
