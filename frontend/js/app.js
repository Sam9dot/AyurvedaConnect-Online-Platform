/**
 * AyurvedaConnect — Full-Featured App (SVG Icons, No Emojis)
 */
(function () {
  "use strict";

  var API_BASE = "http://127.0.0.1:8000";
  var token = localStorage.getItem("token");
  var userRole = localStorage.getItem("userRole") || "";
  var userName = localStorage.getItem("userName") || "";
  if(userRole === "admin") userName = "Admin";

  // SVG Icon helpers (Lucide-style)
  var IC = {
    home:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    wellness:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>',
    doctor:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4.8 2.3A.3.3 0 105 2H4a2 2 0 00-2 2v5a6 6 0 006 6 6 6 0 006-6V4a2 2 0 00-2-2h-1a.2.2 0 10.3.3"/><path d="M8 15v1a6 6 0 006 6 6 6 0 006-6v-4"/><circle cx="20" cy="10" r="2"/></svg>',
    products:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2L3 6v14a2 2 0 002 2h14a2 2 0 002-2V6l-3-4z"/><line x1="3" y1="6" x2="21" y2="6"/><path d="M16 10a4 4 0 01-8 0"/></svg>',
    cart:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 002 1.61h9.72a2 2 0 002-1.61L23 6H6"/></svg>',
    dashboard:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    logout:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>',
    yoga:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="4" r="2"/><path d="M12 6v6"/><path d="M6 18l3-6h6l3 6"/></svg>',
    order:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',
    calendar:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
    heart:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>',
    users:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>',
    clock:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    check:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
    shield:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    plus:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>',
    activity:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',
    star:'<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    starEmpty:'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    pin:'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    phone:'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72 12.84 12.84 0 00.7 2.81 2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45 12.84 12.84 0 002.81.7A2 2 0 0122 16.92z"/></svg>',
    building:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M12 6h.01"/><path d="M12 10h.01"/><path d="M12 14h.01"/><path d="M16 10h.01"/><path d="M16 14h.01"/><path d="M8 10h.01"/><path d="M8 14h.01"/></svg>',
    spa:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    zap:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
  };

  function stars(r){var s="";for(var i=0;i<5;i++)s+=(i<Math.round(r))?IC.star:IC.starEmpty;return s;}

  // DATA — from Excel spreadsheet
  window.__FALLBACK_DOCTORS__ = [
    { id:1, name:"Dr. Shubhangi Kulkarni", spec:"Ayurvedic Doctor", exp:"10+ yrs", phone:"+91 20 2567 1234", location:"Koregaon Park, Pune", rating:4.9, reviews:128, footfall:"20-40", img:"https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=800&q=80", bio:"Expert in Panchakarma therapy and chronic disease management." },
    { id:2, name:"Dr. Nilesh Patil", spec:"Ayurvedic Doctor", exp:"6-10 yrs", phone:"+91 20 2553 4567", location:"Shivajinagar, Pune", rating:4.7, reviews:95, footfall:"10-20", img:"https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=800&q=80", bio:"Specializes in digestive health and Ayurvedic nutrition." },
    { id:3, name:"Dr. Swati Deshpande", spec:"Ayurvedic Doctor", exp:"6-10 yrs", phone:"+91 20 2445 6789", location:"Baner, Pune", rating:4.8, reviews:213, footfall:"20-40", img:"https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&w=800&q=80", bio:"Renowned for women's wellness and stress management." },
    { id:4, name:"Dr. Amol Jadhav", spec:"Ayurvedic Doctor", exp:"3-5 yrs", phone:"+91 20 2612 3456", location:"Aundh, Pune", rating:4.5, reviews:76, footfall:"10-20", img:"https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&w=800&q=80", bio:"Focused on sports injuries and musculoskeletal Ayurveda." },
    { id:5, name:"Dr. Priyanka More", spec:"Ayurvedic Doctor", exp:"3-5 yrs", phone:"+91 20 2567 8901", location:"Hadapsar, Pune", rating:4.6, reviews:54, footfall:"10-20", img:"https://images.unsplash.com/photo-1551836022-d5d88e9218df?auto=format&fit=crop&w=800&q=80", bio:"Pediatric Ayurveda specialist with a gentle approach." },
    { id:6, name:"Dr. Rahul Pawar", spec:"Ayurvedic Doctor", exp:"10+ yrs", phone:"+91 20 2443 2211", location:"Deccan Gymkhana, Pune", rating:4.9, reviews:340, footfall:"20-40", img:"https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=800&q=80", bio:"Senior physician known for detox and rejuvenation programs." },
    { id:7, name:"Dr. Sneha Bhosale", spec:"Ayurvedic Doctor", exp:"0-2 yrs", phone:"+91 20 2556 7788", location:"Viman Nagar, Pune", rating:4.3, reviews:42, footfall:"0-10", img:"https://images.unsplash.com/photo-1643297654416-05795d62e39c?auto=format&fit=crop&w=800&q=80", bio:"Integrating modern diagnostics with traditional Ayurveda." },
    { id:8, name:"Dr. Mahesh Shinde", spec:"Ayurvedic Doctor", exp:"10+ yrs", phone:"+91 20 2423 9900", location:"Kothrud, Pune", rating:4.9, reviews:412, footfall:"40+", img:"https://images.unsplash.com/photo-1582750433449-648ed127bb54?auto=format&fit=crop&w=800&q=80", bio:"Mastery in rare Ayurvedic formulations and Netra Chikitsa." },
  ];

  window.__FALLBACK_PRODUCTS__ = [
    { id:1, name:"Ashwagandha Capsules", desc:"Adaptogenic root extract for stress relief and vitality.", price:"899", img:"https://www.arlakayurveda.com/wp-content/uploads/2023/03/Ashwagandha-Bottle-3D-scaled.jpg", category:"Supplements" },
    { id:2, name:"Triphala Powder", desc:"Classic three-fruit blend supporting gentle daily detox.", price:"549", img:"https://www.gaviayurveda.com/wp-content/uploads/2023/10/Triphala-Powder.jpg", category:"Powders" },
    { id:3, name:"Brahmi Hair Oil", desc:"Cold-pressed herbal oil for scalp nourishment.", price:"649", img:"https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?auto=format&fit=crop&w=800&q=80", category:"Oils" },
    { id:4, name:"Turmeric Golden Milk Mix", desc:"Anti-inflammatory haldi doodh blend with black pepper.", price:"450", img:"https://ayuspa.co.nz/wp-content/uploads/2022/01/t-golden-milk.jpg", category:"Drinks" },
    { id:5, name:"Neem Face Wash", desc:"Purifying herbal cleanser with neem and tulsi extracts.", price:"350", img:"https://www.healthwithherbal.com/wp-content/uploads/2016/05/neem-tulsi-face-wash-1.jpg", category:"Skincare" },
    { id:6, name:"Amla Vitamin C Tablets", desc:"Natural immunity booster from Indian gooseberry.", price:"299", img:"https://assets.hyugalife.com/catalog/product/h/s/hsky66b0_2__1.jpg", category:"Supplements" },
    { id:7, name:"Chyawanprash (500g)", desc:"Traditional herbal jam with amla, honey, and 40+ herbs.", price:"599", img:"https://img3.exportersindia.com/product_images/bc-full/2023/1/11356419/dabur-chyawanprash-1674801653-6736207.jpeg", category:"Tonics" },
    { id:8, name:"Kumkumadi Face Oil", desc:"Saffron-infused night oil for radiant, glowing skin.", price:"1299", img:"https://img1.exportersindia.com/product_images/bc-full/2024/4/4190081/kumkumadi-tailam-face-serum-1712816494-7379236.jpeg", category:"Skincare" },
    { id:9, name:"Shatavari Capsules", desc:"Women's wellness herb for hormonal balance.", price:"799", img:"https://assets.hyugalife.com/catalog/product/h/s/hsbp58n5_1.jpg", category:"Supplements" },
    { id:10, name:"Moringa Leaf Powder", desc:"Nutrient-dense superfood from drumstick leaves.", price:"399", img:"https://ilavanam.com/wp-content/uploads/2024/01/moringa-packagingv2.png", category:"Powders" },
  ];

  window.__FALLBACK_WELLNESS__ = [
    // Yoga Centres (from Excel)
    { name:"Omkar Yoga & Meditation Centre", type:"yoga", address:"Koregaon Park, Pune", services:"Hatha Yoga, Meditation, Pranayama, Yoga Therapy", phone:"+91 20 2615 1100", rating:4.7, exp:"6-10", img:"https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=800&q=80", facilities:["Yoga Hall","Meditation Room","Pranayama Zone","Herbal Tea Lounge"] },
    { name:"Prana Yog Wellness Studio", type:"yoga", address:"Baner, Pune", services:"Ashtanga Yoga, Power Yoga, Restorative Yoga", phone:"+91 20 2729 2200", rating:4.5, exp:"3-5", img:"https://images.unsplash.com/photo-1506126613408-eca07ce68773?auto=format&fit=crop&w=800&q=80", facilities:["Practice Studio","Props Room","Changing Rooms","Juice Bar"] },
    { name:"Dhankawadi Yoga Sadhana Kendra", type:"yoga", address:"Dhankawadi, Pune", services:"Traditional Yoga, Kriyas, Shatkarma, Retreats", phone:"+91 20 2436 3300", rating:4.8, exp:"10+", img:"https://images.unsplash.com/photo-1599901860904-17e6ed7083a0?auto=format&fit=crop&w=800&q=80", facilities:["Open-Air Shala","Meditation Garden","Library","Dormitory"] },
    { name:"Shree Yoga & Fitness Hub", type:"yoga", address:"Wakad, Pune", services:"Yoga for Beginners, Flexibility, Fitness Yoga", phone:"+91 20 2687 4400", rating:4.3, exp:"0-2", img:"https://images.unsplash.com/photo-1575052814086-f385e2e2ad33?auto=format&fit=crop&w=800&q=80", facilities:["AC Studio","Fitness Zone","Consultation Desk"] },
    { name:"Aarogyam Yoga Centre", type:"yoga", address:"Kalyani Nagar, Pune", services:"Therapeutic Yoga, Prenatal Yoga, Workshops", phone:"+91 20 2668 5500", rating:4.6, exp:"6-10", img:"https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=800&q=80", facilities:["Therapy Room","Prenatal Suite","Workshop Hall","Garden"] },
    { name:"Surya Namaskar Yoga Academy", type:"yoga", address:"Camp, Pune", services:"Teacher Training, Advanced Asanas, Philosophy", phone:"+91 20 2614 6600", rating:4.9, exp:"10+", img:"https://images.unsplash.com/photo-1588286840104-8957b019727f?auto=format&fit=crop&w=800&q=80", facilities:["Training Hall","Philosophy Library","Exam Centre","Canteen"] },
    { name:"MindBody Yoga Studio", type:"yoga", address:"Hinjawadi, Pune", services:"Vinyasa, Yin Yoga, Sound Healing, Corporate Yoga", phone:"+91 20 2293 7700", rating:4.5, exp:"3-5", img:"https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=800&q=80", facilities:["Heated Studio","Sound Room","Corporate Lounge","Resting Area"] },
    // Wellness Centres (from Excel)
    { name:"Arogyam Ayurvedic Wellness Centre", type:"wellness", address:"Kothrud, Pune", services:"Panchakarma, Abhyanga, Shirodhara, Detox", phone:"+91 20 2546 1100", rating:4.7, exp:"6-10", img:"https://images.unsplash.com/photo-1600334089648-b0d9d3028eb2?auto=format&fit=crop&w=800&q=80", facilities:["Panchakarma Suite","Steam Room","Herbal Garden","Consultation"] },
    { name:"Panchamrit Panchakarma Clinic", type:"wellness", address:"Sadashiv Peth, Pune", services:"Nasya, Vamana, Virechana, Basti, Full Panchakarma", phone:"+91 20 2447 2200", rating:4.8, exp:"10+", img:"https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=800&q=80", facilities:["5 Therapy Rooms","Preparation Lab","Recovery Suite","Herbal Store"] },
    { name:"Jeevan Ayurveda & Wellness", type:"wellness", address:"Magarpatta, Pune", services:"Herbal Therapy, Nutrition Consult, Online Consults", phone:"+91 20 4000 3300", rating:4.5, exp:"3-5", img:"https://images.unsplash.com/photo-1540555700478-4be289fbec6d?auto=format&fit=crop&w=800&q=80", facilities:["Tele-Consult Room","Treatment Wing","Diet Lab","Dispensary"] },
    { name:"Sattva Holistic Healing Centre", type:"wellness", address:"Baner Road, Pune", services:"Kerala Treatments, Oil Therapy, Pizhichil, Herbal Bath", phone:"+91 20 2729 4400", rating:4.6, exp:"6-10", img:"https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=800&q=80", facilities:["Abhyanga Room","Pizhichil Chamber","Herbal Bath","Ayurvedic Kitchen"] },
    { name:"AyurSparsh Therapy Centre", type:"wellness", address:"Tilak Road, Pune", services:"Stress Relief, Joint Care, Skin Therapy", phone:"+91 20 2447 5500", rating:4.4, exp:"3-5", img:"https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&w=800&q=80", facilities:["Therapy Rooms","Relaxation Lounge","Herbal Pharmacy"] },
    { name:"Tridosha Wellness Studio", type:"wellness", address:"Aundh, Pune", services:"Dosha Balancing, Diet Plans, Lifestyle Coaching", phone:"+91 20 4920 6600", rating:4.3, exp:"0-2", img:"https://images.unsplash.com/photo-1552693673-1bf958298935?auto=format&fit=crop&w=800&q=80", facilities:["Consultation Room","Diet Planning Lab","Marma Therapy"] },
    { name:"Prakruti Natural Healing Centre", type:"wellness", address:"Koregaon Park, Pune", services:"Naturopathy, Ayurveda, Mud Therapy, Hydrotherapy", phone:"+91 20 2612 7700", rating:4.9, exp:"10+", img:"https://images.unsplash.com/photo-1600334089648-b0d9d3028eb2?auto=format&fit=crop&w=800&q=80", facilities:["Mud Therapy Room","Hydro Pool","Fasting Suite","Nature Garden","Yoga Deck"] },
  ];

  // CART
  function getCart(){try{return JSON.parse(localStorage.getItem("cart"))||[];}catch(e){return[];}}
  function saveCart(c){localStorage.setItem("cart",JSON.stringify(c));}
  function addToCart(p){var c=getCart(),found=false;for(var i=0;i<c.length;i++)if(c[i].name===p.name){c[i].qty=(c[i].qty||1)+1;found=true;break;}if(!found){p.qty=1;c.push(p);}saveCart(c);showToast(p.name+" added to cart!");updateCartBadge();}
  function removeFromCart(i){var c=getCart();c.splice(i,1);saveCart(c);}
  function updateQty(i,d){var c=getCart();if(c[i]){c[i].qty=Math.max(1,(c[i].qty||1)+d);saveCart(c);}}
  function getCartTotal(){var c=getCart(),t=0;for(var i=0;i<c.length;i++)t+=parseFloat(c[i].price)*(c[i].qty||1);return t;}

  function showToast(msg){var t=document.createElement("div");t.className="toast-msg";t.textContent=msg;document.body.appendChild(t);setTimeout(function(){t.classList.add("toast-msg--show");},10);setTimeout(function(){t.classList.remove("toast-msg--show");setTimeout(function(){t.remove();},400);},2500);}

  function getLikes(){try{return JSON.parse(localStorage.getItem("likes"))||{};}catch(e){return{};}}
  function toggleLike(type,id){var l=getLikes();var k=type+"-"+id;l[k]=!l[k];localStorage.setItem("likes",JSON.stringify(l));return l[k];}
  function isLiked(type,id){return!!getLikes()[type+"-"+id];}
  function getReviews(){try{return JSON.parse(localStorage.getItem("reviews"))||{};}catch(e){return{};}}
  function addReview(type,id,text,rating){var r=getReviews();var k=type+"-"+id;if(!r[k])r[k]=[];r[k].push({text:text,rating:rating,user:userName||"User",date:new Date().toLocaleDateString()});localStorage.setItem("reviews",JSON.stringify(r));return r[k];}
  function getReviewsFor(type,id){return(getReviews()[type+"-"+id])||[];}

  // NAV TOGGLE
  var navToggle=document.querySelector(".nav-toggle");
  var navMenu=document.querySelector(".site-header .nav");
  if(navToggle&&navMenu){navToggle.addEventListener("click",function(){var o=navMenu.classList.toggle("is-open");navToggle.setAttribute("aria-expanded",o?"true":"false");});}
  var path=window.location.pathname.split("/").pop()||"index.html";

  // SIDEBAR
  var sidebar=document.getElementById("sidebar");
  var sidebarToggle=document.getElementById("sidebar-toggle");
  var mainContent=document.getElementById("main-content");
  if(sidebar&&token){
    sidebar.classList.add("sidebar--visible");
    if(mainContent)mainContent.classList.add("has-sidebar");
    var sidebarNav=sidebar.querySelector(".sidebar__nav");
    if(sidebarNav){
      var links='<a href="index.html" class="sidebar__link">'+IC.home+' Home</a>';
      if(userRole==="patient"||userRole===""||userRole==="admin")links+='<a href="wellness.html" class="sidebar__link">'+IC.wellness+' Wellness Centres</a>';
      if(userRole==="patient"||userRole===""||userRole==="admin")links+='<a href="doctors.html" class="sidebar__link">'+IC.doctor+' Doctors</a>';
      if(userRole==="patient"||userRole===""||userRole==="seller"||userRole==="admin")links+='<a href="products.html" class="sidebar__link">'+IC.products+' Products</a>';
      if(userRole==="patient"||userRole==="")links+='<a href="cart.html" class="sidebar__link">'+IC.cart+' Cart <span id="sidebar-cart-count"></span></a>';
      if(userRole==="patient"||userRole==="")links+='<a href="dashboard.html" class="sidebar__link">'+IC.dashboard+' Dashboard</a>';
      if(userRole==="doctor")links+='<a href="doctor-dashboard.html" class="sidebar__link">'+IC.dashboard+' Doctor Panel</a>';
      if(userRole==="seller")links+='<a href="seller-dashboard.html" class="sidebar__link">'+IC.dashboard+' Seller Panel</a>';
      if(userRole==="wellness")links+='<a href="wellness-dashboard.html" class="sidebar__link">'+IC.dashboard+' Centre Panel</a>';
      if(userRole==="admin")links+='<a href="admin-dashboard.html" class="sidebar__link">'+IC.shield+' Admin Panel</a>';
      links+='<a href="#" class="sidebar__link sidebar__logout">'+IC.logout+' Logout</a>';
      sidebarNav.innerHTML=links;
      sidebarNav.querySelectorAll("a").forEach(function(a){var h=a.getAttribute("href");if(h===path)a.classList.add("sidebar__link--active");});
      var logoutBtn=sidebarNav.querySelector(".sidebar__logout");
      if(logoutBtn)logoutBtn.addEventListener("click",function(e){e.preventDefault();if(!confirm("Are you sure you want to log out?"))return;localStorage.removeItem("token");localStorage.removeItem("userRole");localStorage.removeItem("userName");localStorage.removeItem("cart");showToast("Logged out!");setTimeout(function(){window.location.href="login.html";},500);});
    }
    if(sidebarToggle)sidebarToggle.addEventListener("click",function(){sidebar.classList.toggle("sidebar--collapsed");if(mainContent)mainContent.classList.toggle("sidebar-collapsed");});
  }

  // PUBLIC TOP NAV
  var navEl=document.getElementById("main-nav");
  if(navEl){
    if(!navEl.querySelector('a[href="wellness.html"]')){var wl=document.createElement("a");wl.href="wellness.html";wl.textContent="Wellness Centres";var hl=navEl.querySelector('a[href="index.html"]');if(hl&&hl.nextSibling)navEl.insertBefore(wl,hl.nextSibling);else navEl.appendChild(wl);}
    if(userRole!=="patient"&&userRole!==""&&userRole!=="admin"){var pw=navEl.querySelector('a[href="wellness.html"]');if(pw)pw.remove();}
    if(userRole!=="patient"&&userRole!==""&&userRole!=="admin"){var doc=navEl.querySelector('a[href="doctors.html"]');if(doc)doc.remove();}
    if(userRole==="doctor"||userRole==="wellness"){var prod=navEl.querySelector('a[href="products.html"]');if(prod)prod.remove();}

    if(token){
      if(userRole==="patient"||userRole===""){
        var cc=getCart().reduce(function(s,it){return s+(it.qty||1);},0);
        var cl=document.createElement("a");cl.href="cart.html";cl.textContent="Cart"+(cc>0?" ("+cc+")":"");cl.id="nav-cart-link";
        var ll=navEl.querySelector('a[href="login.html"]');if(ll)navEl.insertBefore(cl,ll);else navEl.appendChild(cl);
      }
      var ll2=navEl.querySelector('a[href="login.html"]');if(ll2)ll2.remove();
      var dl=document.createElement("a");dl.href=userRole==="admin"?"admin-dashboard.html":userRole==="doctor"?"doctor-dashboard.html":userRole==="seller"?"seller-dashboard.html":userRole==="wellness"?"wellness-dashboard.html":"dashboard.html";
      dl.textContent="Dashboard";navEl.appendChild(dl);
      var lo=document.createElement("a");lo.href="#";lo.textContent="Logout";
      lo.addEventListener("click",function(e){e.preventDefault();if(!confirm("Are you sure you want to log out?"))return;localStorage.removeItem("token");localStorage.removeItem("userRole");localStorage.removeItem("userName");localStorage.removeItem("cart");window.location.href="login.html";});
      navEl.appendChild(lo);
    }
    navEl.querySelectorAll("a").forEach(function(a){var h=a.getAttribute("href");if(h===path)a.setAttribute("aria-current","page");});
  }
  function updateCartBadge(){var cc=getCart().reduce(function(s,it){return s+(it.qty||1);},0);var el=document.getElementById("nav-cart-link");if(el)el.textContent="Cart"+(cc>0?" ("+cc+")":"");var sb=document.getElementById("sidebar-cart-count");if(sb)sb.textContent=cc>0?"("+cc+")":"";}

  // Enhanced Dashboard Helper Functions
  function createCircularProgress(containerId, percentage, label) {
    var container = document.getElementById(containerId);
    if (!container) return;
    
    var circumference = 2 * Math.PI * 45;
    var offset = circumference - (percentage / 100) * circumference;
    
    container.innerHTML = '<div class="circular-progress">' +
      '<svg viewBox="0 0 100 100">' +
      '<circle class="bg-circle" cx="50" cy="50" r="45"></circle>' +
      '<circle class="progress-circle" cx="50" cy="50" r="45" style="stroke-dashoffset: ' + offset + '"></circle>' +
      '</svg>' +
      '<div class="progress-text">' + percentage + '%</div>' +
      '</div>' +
      '<div class="progress-ring__label">' + label + '</div>';
  }

  function createActivityTimeline() {
    var container = document.getElementById("activity-timeline");
    if (!container) return;
    
    var activities = [
      { title: "Morning Yoga Session", time: "2 hours ago", type: "wellness" },
      { title: "Ashwagandha Capsules Taken", time: "4 hours ago", type: "supplement" },
      { title: "Meditation Completed", time: "1 day ago", type: "mindfulness" },
      { title: "Ayurvedic Consultation", time: "2 days ago", type: "consultation" },
      { title: "Triphala Powder Ordered", time: "3 days ago", type: "order" }
    ];
    
    container.innerHTML = '<div class="activity-timeline">' +
      activities.map(function(activity) {
        return '<div class="timeline-item">' +
          '<h4>' + activity.title + '</h4>' +
          '<p class="time">' + activity.time + '</p>' +
          '</div>';
      }).join('') +
      '</div>';
  }

  

  function createMiniCalendar() {
    var container = document.getElementById("mini-calendar");
    if (!container) return;
    
    var today = new Date();
    var currentMonth = today.getMonth();
    var currentYear = today.getFullYear();
    var firstDay = new Date(currentYear, currentMonth, 1).getDay();
    var daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    
    var monthNames = ["January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"];
    
    var calendarHTML = '<div class="appointment-calendar">' +
      '<div class="calendar-header">' +
      '<h3>' + monthNames[currentMonth] + ' ' + currentYear + '</h3>' +
      '</div>' +
      '<div class="calendar-grid">';
    
    // Add day headers
    var dayHeaders = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    dayHeaders.forEach(function(day) {
      calendarHTML += '<div class="calendar-day" style="font-weight: 600; background: rgba(46,125,50,0.1)">' + day + '</div>';
    });
    
    // Add empty cells for days before month starts
    for (var i = 0; i < firstDay; i++) {
      calendarHTML += '<div class="calendar-day"></div>';
    }
    
    // Add days of the month
    for (var day = 1; day <= daysInMonth; day++) {
      var isToday = day === today.getDate();
      var hasAppointment = [5, 12, 18, 25].includes(day); // Mock appointments
      var classes = 'calendar-day';
      if (isToday) classes += ' today';
      if (hasAppointment) classes += ' has-appointment';
      
      calendarHTML += '<div class="' + classes + '">' + day + '</div>';
    }
    
    calendarHTML += '</div></div>';
    container.innerHTML = calendarHTML;
  }

  function createAdminCharts() {
    createCircularProgress("admin-user-growth", 78, "User Growth");
    createCircularProgress("admin-revenue-growth", 65, "Revenue Growth");
    createCircularProgress("admin-satisfaction", 92, "User Satisfaction");
  }

  function createUserTypeDistribution() {
    var container = document.getElementById("user-type-chart");
    if (!container) return;
    
    var userTypes = [
      { type: "Patients", count: 45, color: "var(--color-forest)" },
      { type: "Doctors", count: 12, color: "var(--color-gold)" },
      { type: "Sellers", count: 8, color: "var(--color-teal)" },
      { type: "Wellness Centers", count: 6, color: "var(--color-violet)" }
    ];
    
    var total = userTypes.reduce(function(sum, type) { return sum + type.count; }, 0);
    
    container.innerHTML = '<div class="chart-container">' +
      '<div class="chart-header">' +
      '<h3 class="chart-title">User Distribution</h3>' +
      '<span class="chart-period">Total: ' + total + '</span>' +
      '</div>' +
      '<div class="mini-stats">' +
      userTypes.map(function(type) {
        var percentage = Math.round((type.count / total) * 100);
        return '<div class="mini-stat">' +
          '<div class="mini-stat__value" style="color: ' + type.color + '">' + type.count + '</div>' +
          '<div class="mini-stat__label">' + type.type + ' (' + percentage + '%)</div>' +
          '</div>';
      }).join('') +
      '</div>' +
      '</div>';
  }

  function createRevenueChart() {
    var container = document.getElementById("revenue-chart");
    if (!container) return;
    
    var monthlyRevenue = [
      { month: "Jan", amount: 4500 },
      { month: "Feb", amount: 4800 },
      { month: "Mar", amount: 3900 },
      { month: "Apr", amount: 4100 },
      { month: "May", amount: 4600 },
      { month: "Jun", amount: 4900 }
    ];
    
    var maxRevenue = Math.max.apply(Math, monthlyRevenue.map(function(m) { return m.amount; }));
    
    container.innerHTML = '<div class="chart-container">' +
      '<div class="chart-header">' +
      '<h3 class="chart-title">Monthly Revenue</h3>' +
      '<span class="chart-period">Last 6 months</span>' +
      '</div>' +
      '<div style="display: flex; align-items: end; gap: 1rem; height: 200px; padding: 1rem 0;">' +
      monthlyRevenue.map(function(data) {
        var height = (data.amount / maxRevenue) * 160;
        return '<div style="flex: 1; display: flex; flex-direction: column; align-items: center;">' +
          '<div style="width: 100%; background: linear-gradient(to top, var(--color-forest), var(--color-teal)); height: ' + height + 'px; border-radius: 4px 4px 0 0; margin-bottom: 0.5rem;"></div>' +
          '<span style="font-size: 0.8rem; color: var(--color-text-muted);">' + data.month + '</span>' +
          '<span style="font-size: 0.75rem; color: var(--color-forest); font-weight: 600;">₹' + (data.amount/1000) + 'k</span>' +
          '</div>';
      }).join('') +
      '</div>' +
      '</div>';
  }

  function createDoctorMetrics() {
    var container = document.getElementById("doctor-metrics");
    if (!container) return;
    
    var metrics = [
      { icon: IC.users, value: "24", label: "Patients Today", trend: "+3", trendDir: "up" },
      { icon: IC.calendar, value: "18", label: "Appointments", trend: "+2", trendDir: "up" },
      { icon: IC.star, value: "4.8", label: "Rating", trend: "+0.1", trendDir: "up" },
      { icon: IC.clock, value: "6.5h", label: "Consultation Time", trend: "+30m", trendDir: "up" }
    ];
    
    container.innerHTML = '<div class="health-metrics">' +
      metrics.map(function(metric) {
        return '<div class="health-metric">' +
          '<div class="health-metric__icon">' + metric.icon + '</div>' +
          '<div class="health-metric__value">' + metric.value + '</div>' +
          '<div class="health-metric__label">' + metric.label + '</div>' +
          '<div class="health-metric__trend ' + metric.trendDir + '">' + metric.trend + '</div>' +
          '</div>';
      }).join('') +
      '</div>';
  }

  

  function createAppointmentCalendar() {
    var container = document.getElementById("appointment-calendar");
    if (!container) return;
    
    var appointments = [
      { time: "09:00", patient: "Priya Sharma", type: "Consultation" },
      { time: "10:30", patient: "Raj Patel", type: "Follow-up" },
      { time: "11:45", patient: "Anita Singh", type: "New Patient" },
      { time: "14:00", patient: "Vikram Kumar", type: "Consultation" },
      { time: "15:30", patient: "Meera Joshi", type: "Treatment Review" }
    ];
    
    container.innerHTML = '<div class="dashboard-card">' +
      '<h3>Today\'s Schedule</h3>' +
      '<div class="activity-timeline">' +
      appointments.map(function(apt) {
        return '<div class="timeline-item">' +
          '<h4>' + apt.time + ' - ' + apt.patient + '</h4>' +
          '<p>' + apt.type + '</p>' +
          '</div>';
      }).join('') +
      '</div>' +
      '</div>';
  }

  // Enhanced Dashboard Features
  window.createCircularProgress = createCircularProgress;
  window.createActivityTimeline = createActivityTimeline;
  window.createMiniCalendar = createMiniCalendar;
  window.createAdminCharts = createAdminCharts;
  window.createUserTypeDistribution = createUserTypeDistribution;
  window.createRevenueChart = createRevenueChart;
  window.createDoctorMetrics = createDoctorMetrics;
  window.createAppointmentCalendar = createAppointmentCalendar;

  
  // Dashboard Brand Customization
  if (sidebar && userName) {
    if (path === 'wellness-dashboard.html') {
      let title = document.querySelector('.dashboard-welcome h1');
      if(title) title.textContent = userName;
    }
    if (path === 'seller-dashboard.html') {
      let title = document.querySelector('.dashboard-welcome h1');
      if(title) title.textContent = userName;
    }
    if (path === 'admin-dashboard.html') {
      let title = document.querySelector('.dashboard-welcome h1');
      if(title) title.textContent = "Admin - " + userName;
    }
  }

  if (userName) {
    if (path === 'wellness.html' && userRole === 'wellness') {
      let intro = document.querySelector('.section__intro');
      if (intro) intro.textContent = "Welcome back, " + userName + ". These are our verified centres.";
    }
    if (path === 'products.html' && userRole === 'seller') {
      let intro = document.querySelector('.section__intro');
      if (intro) intro.textContent = "Welcome back, " + userName + ". View and manage these products in your dashboard.";
    }
  }

  
  // ===== DYNAMIC FALLBACK VARIABLES =====
  let DOCTORS = window.__FALLBACK_DOCTORS__ || [];
  let PRODUCTS = window.__FALLBACK_PRODUCTS__ || [];
  let WELLNESS = window.__FALLBACK_WELLNESS__ || [];


  // Async loader
  window.loadPlatformData = function() {
    return Promise.all([
      fetch(API_BASE + '/doctors').then(function(res){ return res.ok ? res.json() : []; }).catch(function(){ return []; }),
      fetch(API_BASE + '/products').then(function(res){ return res.ok ? res.json() : []; }).catch(function(){ return []; }),
      fetch(API_BASE + '/wellness').then(function(res){ return res.ok ? res.json() : []; }).catch(function(){ return []; })
    ]).then(function(results) {
      var fetchedDoctors = results[0];
      var fetchedProducts = results[1];
      var fetchedWellness = results[2];
      
      if (fetchedDoctors && fetchedDoctors.length > 0) {
        DOCTORS = fetchedDoctors.map(function(d) {
          return {
            id: d.doctor_id || d.id,
            name: d.name,
            spec: d.specialization || "Ayurvedic Doctor",
            exp: d.experience || "5+ yrs",
            phone: d.phone || "",
            location: d.location || "Pune",
            rating: d.rating || 4.5,
            reviews: 50,
            footfall: d.daily_footfall || "10-20",
            img: d.image_url || window.__FALLBACK_DOCTORS__[0].img,
            bio: d.bio || "Ayurveda practitioner."
          };
        });
      }

      if (fetchedProducts && fetchedProducts.length > 0) {
        var newProducts = fetchedProducts.map(function(p) {
          var genericImg = "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?auto=format&fit=crop&w=800&q=80";
          return {
            id: p.product_id || p.id,
            name: p.name,
            desc: p.desc || "A natural ayurvedic product.",
            price: p.price,
            img: p.image_url || genericImg,
            category: p.category || "General"
          };
        });
        PRODUCTS = window.__FALLBACK_PRODUCTS__.concat(newProducts);
      }

      if (fetchedWellness && fetchedWellness.length > 0) {
        WELLNESS = fetchedWellness.map(function(w) {
          return {
            name: w.name,
            type: w.center_type || "wellness",
            address: w.location || "Pune",
            services: w.services || "Wellness, Spa",
            phone: w.phone || "",
            rating: w.rating || 4.5,
            exp: w.experience || "3-5",
            img: w.image_url || window.__FALLBACK_WELLNESS__[0].img,
            facilities: w.amenities ? w.amenities.split(',') : ["Consultation"]
          };
        });
      }
    });
  };

  // === PAGE HANDLERS (continued in next section) ===
  // LOGIN
  var loginForm=document.getElementById("login-form");
  var globalLoginEmail = "";
  if(loginForm){loginForm.addEventListener("submit",function(e){e.preventDefault();var email=document.getElementById("email").value,pw=document.getElementById("password").value;
  globalLoginEmail = email;
  fetch(API_BASE+"/auth/login",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({email:email,password:pw})}).then(function(r){if(!r.ok)return r.json().then(function(e){throw new Error(e.detail||"Invalid credentials.")});return r.json()}).then(function(d){
    if(d.status === "otp_required") {
        showToast(d.message || "OTP sent to your phone");
        document.getElementById("login-form").style.display = "none";
        document.getElementById("otp-form").style.display = "flex";
        if(document.getElementById("otp-msg")) document.getElementById("otp-msg").innerText = d.message;
    } else {
        // Fallback or previously valid non-OTP flow
        localStorage.setItem("token",d.access_token);var actualRole=d.user_type||role;localStorage.setItem("userRole",actualRole);if(d.user_name)localStorage.setItem("userName",d.user_name);showToast("Login successful!");var dest=actualRole==="admin"?"admin-dashboard.html":actualRole==="doctor"?"doctor-dashboard.html":actualRole==="seller"?"seller-dashboard.html":actualRole==="wellness"?"wellness-dashboard.html":"dashboard.html";setTimeout(function(){window.location.href=dest;},600);
    }
  }).catch(function(e){alert("Login failed: "+e.message);});});}

  var otpForm=document.getElementById("otp-form");
  if(otpForm) {
    document.querySelectorAll(".btn-back-login").forEach(function(btn) {
      btn.addEventListener("click", function() {
        document.getElementById("otp-form").style.display = "none";
        document.getElementById("login-form").style.display = "flex";
      });
    });

    var btnSendOtp = document.getElementById("btn-send-otp");
    if(btnSendOtp) {
      btnSendOtp.addEventListener("click", function() {
        var phone = document.getElementById("otp-phone").value.trim();
        if(phone.length < 10) { alert("Please enter a valid mobile number"); return; }
        fetch(API_BASE+"/auth/send-otp", {
          method: "POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify({email: globalLoginEmail, phone: phone})
        }).then(function(r){
          if(!r.ok) return r.json().then(function(e){throw new Error(e.detail||"Error sending OTP.")});
          return r.json();
        }).then(function(d){
          showToast("OTP sent to " + phone + "!");
          document.getElementById("otp-phone-step").style.display = "none";
          document.getElementById("otp-code-step").style.display = "block";
        }).catch(function(e){ alert(e.message); });
      });
    }

    document.getElementById("btn-verify-otp").addEventListener("click", function() {
      var code = document.getElementById("otp-code").value.trim();
      if(code.length < 4) { alert("Please enter the OTP"); return; }
      fetch(API_BASE+"/auth/verify-otp", {
        method: "POST", headers:{"Content-Type":"application/json"}, body: JSON.stringify({email: globalLoginEmail, otp: code})
      }).then(function(r){
        if(!r.ok) return r.json().then(function(e){throw new Error(e.detail||"Verification failed.")});
        return r.json();
      }).then(function(d){
        localStorage.setItem("token",d.access_token);
        var actualRole=d.user_type;
        localStorage.setItem("userRole",actualRole);
        if(d.user_name) localStorage.setItem("userName",d.user_name);
        showToast("Verified and logged in successfully!");
        var dest=actualRole==="admin"?"admin-dashboard.html":actualRole==="doctor"?"doctor-dashboard.html":actualRole==="seller"?"seller-dashboard.html":actualRole==="wellness"?"wellness-dashboard.html":"dashboard.html";
        setTimeout(function(){window.location.href=dest;},600);
      }).catch(function(e){ alert(e.message); });
    });
  }

  // SIGNUP
  var signupForm=document.getElementById("signup-form");
  if(signupForm){signupForm.addEventListener("submit",function(e){e.preventDefault();var email=document.getElementById("email").value;var phone=document.getElementById("phone").value;var pw=document.getElementById("password").value;var userTypeEl=document.getElementById("user-type");var userType=userTypeEl?userTypeEl.value:"patient";if(pw.length<8){alert("Password must be at least 8 characters.");return;}fetch(API_BASE+"/auth/register",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({email:email,password:pw,phone:phone,user_type:userType})}).then(function(r){if(!r.ok)return r.json().then(function(e){var d=e.detail;if(typeof d==="object")d=JSON.stringify(d);throw new Error(d||"Signup failed.")});return r.json()}).then(function(){showToast("Account created! Please log in.");setTimeout(function(){window.location.href="login.html";},600);}).catch(function(e){alert("Signup error: "+e.message);});});}

  // DOCTORS PAGE
  var doctorsGrid=document.getElementById("doctors-grid");
  if(doctorsGrid){
    doctorsGrid.innerHTML='<p class="note" style="grid-column:1/-1;text-align:center">Loading doctors...</p>';
    var docSort="rating";
    function renderDoctors(docs){if(!docs.length){doctorsGrid.innerHTML='<p class="note" style="grid-column:1/-1">No doctors found.</p>';return;}doctorsGrid.innerHTML=docs.map(function(d){var liked=isLiked("doctor",d.id);return '<article class="doctor-card" data-id="'+d.id+'"><div style="position:relative"><img class="doctor-card__image" src="'+d.img+'" alt="'+d.name+'" loading="lazy" /><button class="like-btn'+(liked?' like-btn--active':'')+'" data-type="doctor" data-id="'+d.id+'" title="Like">'+(liked?IC.heart:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>')+'</button></div><div class="doctor-card__body"><h2 class="doctor-card__name"><a href="doctor-detail.html?id='+d.id+'" style="color:inherit;text-decoration:none">'+d.name+'</a></h2><p class="doctor-card__spec">'+d.spec+' · '+d.exp+(d.footfall?' <span class="doctor-card__footfall">'+IC.users+' '+d.footfall+' patients/day</span>':'')+'</p>'+(d.bio?'<p style="margin:0.25rem 0 0;font-size:0.82rem;color:#4a5c4a;line-height:1.4">'+d.bio+'</p>':'')+'<p style="margin:0.25rem 0 0;font-size:0.85rem;color:#4a5c4a">'+IC.pin+' '+d.location+'</p><div style="display:flex;align-items:center;gap:0.5rem;margin-top:0.5rem"><span style="color:var(--color-amber)">'+stars(d.rating)+'</span><span style="font-weight:600;font-size:0.9rem">'+d.rating+'</span><span style="font-size:0.8rem;color:#4a5c4a">('+d.reviews+' reviews)</span></div></div></article>';}).join("");document.querySelectorAll(".like-btn").forEach(function(b){b.addEventListener("click",function(e){e.stopPropagation();var type=b.getAttribute("data-type"),id=parseInt(b.getAttribute("data-id"),10);var now=toggleLike(type,id);b.innerHTML=now?IC.heart:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>';b.classList.toggle("like-btn--active",now);showToast(now?"Added to favorites!":"Removed from favorites.");});});}
    var docSearch=document.getElementById("doctor-search");
    var docSortSel=document.getElementById("doctor-sort");
    if(docSearch)docSearch.addEventListener("input",function(){filterDoctors();});
    if(docSortSel)docSortSel.addEventListener("change",function(){docSort=docSortSel.value;filterDoctors();});
    function filterDoctors(){var customDocs=JSON.parse(localStorage.getItem("customDoctors")||"[]");var allDoctors=DOCTORS.slice();customDocs.forEach(function(cd){allDoctors.push({id:100+allDoctors.length,name:cd.name,spec:cd.specialization||"Ayurvedic Doctor",exp:cd.experience||"",phone:cd.phone||"",location:cd.location||"",rating:4.5,reviews:0,footfall:"New",img:cd.image_url||"https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&w=800&q=80",bio:cd.bio||""});});var q=(docSearch?docSearch.value:"").toLowerCase();var filtered=allDoctors.filter(function(d){return !q||d.name.toLowerCase().includes(q)||d.spec.toLowerCase().includes(q)||d.location.toLowerCase().includes(q);});if(docSort==="rating")filtered.sort(function(a,b){return b.rating-a.rating;});else if(docSort==="name")filtered.sort(function(a,b){return a.name.localeCompare(b.name);});else if(docSort==="exp")filtered.sort(function(a,b){return parseInt(b.exp)-parseInt(a.exp);});renderDoctors(filtered);}
    window.loadPlatformData().then(function(){filterDoctors();});
  }

  // DOCTOR DETAIL
  var doctorProfile=document.getElementById("doctor-profile");
  if(doctorProfile){var params=new URLSearchParams(window.location.search);var docId=parseInt(params.get("id"),10)||1;var doc=DOCTORS.find(function(d){return d.id===docId;})||DOCTORS[0];var docReviews=getReviewsFor("doctor",doc.id);doctorProfile.innerHTML='<div class="doctor-profile__header"><img class="doctor-profile__photo" src="'+doc.img+'" alt="'+doc.name+'" /><div><h1 class="doctor-profile__name">'+doc.name+'</h1><p class="doctor-profile__spec">'+doc.spec+'</p><div class="doctor-profile__details"><p class="doctor-profile__detail"><strong>Experience:</strong> '+doc.exp+'</p><p class="doctor-profile__detail"><strong>Location:</strong> '+IC.pin+' '+doc.location+'</p><p class="doctor-profile__detail"><strong>Contact:</strong> '+IC.phone+' '+doc.phone+'</p><p class="doctor-profile__detail"><strong>Rating:</strong> <span style="color:var(--color-amber)">'+stars(doc.rating)+'</span> '+doc.rating+' ('+doc.reviews+' reviews)</p></div></div></div>'+(token?'<div class="book-form"><h2>'+IC.calendar+' Book an Appointment</h2><div class="form-row"><div><label for="appt-date">Date</label><input type="date" id="appt-date" required /></div><div><label for="appt-time">Time</label><input type="time" id="appt-time" required /></div></div><div style="margin-bottom:1rem"><label for="appt-notes">Notes</label><input type="text" id="appt-notes" placeholder="Describe your concern..." /></div><button class="btn btn--gold btn--block" id="book-appt-btn">Book Appointment</button></div>':'<div class="book-form"><h2>'+IC.calendar+' Book an Appointment</h2><p class="note">Please <a href="login.html">log in</a> to book.</p></div>')+'<div class="book-form" style="margin-top:1.5rem"><h2>'+IC.star+' Reviews</h2><div id="reviews-list">'+(docReviews.length?docReviews.map(function(r){return '<div class="review-item"><strong>'+r.user+'</strong> <span style="color:var(--color-amber)">'+stars(r.rating)+'</span><p style="margin:0.25rem 0 0;font-size:0.9rem;color:#4a5c4a">'+r.text+'</p><span style="font-size:0.75rem;color:#888">'+r.date+'</span></div>';}).join(""):'<p class="note">No reviews yet.</p>')+'</div>'+(token?'<div style="margin-top:1rem"><label for="review-text">Your Review</label><input type="text" id="review-text" placeholder="Share your experience..." /><div style="display:flex;gap:0.5rem;margin-top:0.5rem;align-items:center"><label style="margin:0;text-transform:none;font-size:0.9rem">Rating:</label><select id="review-rating"><option value="5">5 Stars</option><option value="4">4 Stars</option><option value="3">3 Stars</option><option value="2">2 Stars</option><option value="1">1 Star</option></select><button class="btn btn--gold btn--sm" id="submit-review-btn">Submit</button></div></div>':'')+'</div>';var bookBtn=document.getElementById("book-appt-btn");if(bookBtn)bookBtn.addEventListener("click",function(){var date=document.getElementById("appt-date").value,time=document.getElementById("appt-time").value;if(!date||!time){alert("Please select date and time.");return;}var appts=JSON.parse(localStorage.getItem("appointments")||"[]");appts.push({doctor:doc.name,doctorId:doc.id,date:date,time:time,notes:document.getElementById("appt-notes").value||"",status:"confirmed"});localStorage.setItem("appointments",JSON.stringify(appts));showToast("Appointment booked with "+doc.name+"!");setTimeout(function(){window.location.href="dashboard.html";},800);});var reviewBtn=document.getElementById("submit-review-btn");if(reviewBtn)reviewBtn.addEventListener("click",function(){var text=document.getElementById("review-text").value;var rating=parseInt(document.getElementById("review-rating").value,10);if(!text.trim()){alert("Please write a review.");return;}addReview("doctor",doc.id,text,rating);showToast("Review submitted!");setTimeout(function(){location.reload();},500);});}

  // PRODUCTS PAGE
  var productsGrid=document.getElementById("products-grid");
  if(productsGrid){
    productsGrid.innerHTML='<p class="note" style="grid-column:1/-1;text-align:center">Loading products...</p>';
    function renderProducts(prods){if(!prods.length){productsGrid.innerHTML='<p class="note" style="grid-column:1/-1">No products found.</p>';return;}productsGrid.innerHTML=prods.map(function(p,idx){var liked=isLiked("product",p.id);return '<article class="product-card"><div class="product-card__image-wrap" style="position:relative"><img class="product-card__image" src="'+p.img+'" alt="'+p.name+'" loading="lazy" /><button class="like-btn'+(liked?' like-btn--active':'')+'" data-type="product" data-id="'+p.id+'" title="Like">'+(liked?IC.heart:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>')+'</button><span class="product-card__cat">'+p.category+'</span></div><div class="product-card__body"><h2 class="product-card__name">'+p.name+'</h2><p class="product-card__desc">'+p.desc+'</p><div class="product-card__row"><p class="product-card__price"><span>₹</span>'+p.price+'</p>'+(token?'<button class="btn btn--gold btn--sm add-to-cart-btn" data-idx="'+idx+'">Add to Cart</button>':'<a href="login.html" class="btn btn--outline-dark btn--sm">Login to Buy</a>')+'</div></div></article>';}).join("");document.querySelectorAll(".product-card .like-btn").forEach(function(b){b.addEventListener("click",function(e){e.stopPropagation();var type=b.getAttribute("data-type"),id=parseInt(b.getAttribute("data-id"),10);var now=toggleLike(type,id);b.innerHTML=now?IC.heart:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>';b.classList.toggle("like-btn--active",now);showToast(now?"Added to favorites!":"Removed from favorites.");});});if(token){document.querySelectorAll(".add-to-cart-btn").forEach(function(btn){btn.addEventListener("click",function(){var i=parseInt(btn.getAttribute("data-idx"),10),p=prods[i];if(p)addToCart({name:p.name,price:p.price,img:p.img});});});}}
    var prodSearch=document.getElementById("product-search");
    var prodSort=document.getElementById("product-sort");
    if(prodSearch)prodSearch.addEventListener("input",function(){filterProducts();});
    if(prodSort)prodSort.addEventListener("change",function(){filterProducts();});
    function filterProducts(){var allProducts=PRODUCTS.slice();var q=(prodSearch?prodSearch.value:"").toLowerCase();var filtered=allProducts.filter(function(p){return !q||p.name.toLowerCase().includes(q)||p.category.toLowerCase().includes(q)||p.desc.toLowerCase().includes(q);});var sv=prodSort?prodSort.value:"";if(sv==="price-low")filtered.sort(function(a,b){return parseFloat(a.price)-parseFloat(b.price);});else if(sv==="price-high")filtered.sort(function(a,b){return parseFloat(b.price)-parseFloat(a.price);});else if(sv==="name")filtered.sort(function(a,b){return a.name.localeCompare(b.name);});renderProducts(filtered);}
    window.loadPlatformData().then(function(){filterProducts();});
  }

  // WELLNESS CENTRES
  var wellnessGrid=document.getElementById("wellness-grid");
  if(wellnessGrid){
    wellnessGrid.innerHTML='<p class="note" style="grid-column:1/-1;text-align:center">Loading wellness centres...</p>';
    var activeFilter="all";
    function renderWellness(centres){if(!centres.length){wellnessGrid.innerHTML='<p class="note" style="grid-column:1/-1">No centres found.</p>';return;}wellnessGrid.innerHTML=centres.map(function(w){var facHTML=w.facilities?'<div class="wellness-card__facilities">'+w.facilities.map(function(f){return '<span class="wellness-card__facility">'+IC.check+' '+f+'</span>';}).join("")+'</div>':"";var typeLabel=w.type==="yoga"?"Yoga Centre":"Wellness Centre";return '<article class="wellness-card"><div style="position:relative"><img class="wellness-card__img" src="'+w.img+'" alt="'+w.name+'" loading="lazy" /><span class="wellness-card__type-badge wellness-card__type-badge--'+(w.type||"wellness")+'">'+typeLabel+'</span></div><div class="wellness-card__body"><h2 class="wellness-card__name">'+w.name+'</h2><p class="wellness-card__meta">'+IC.pin+' '+w.address+'</p><p class="wellness-card__meta">'+IC.spa+' '+w.services+'</p><p class="wellness-card__meta">'+IC.phone+' '+w.phone+'</p>'+(w.exp?'<p class="wellness-card__meta">'+IC.clock+' Experience: '+w.exp+' years</p>':'')+facHTML+'<div class="wellness-card__rating"><span class="wellness-card__stars">'+stars(w.rating)+'</span><span class="wellness-card__score">'+w.rating+'</span></div></div></article>';}).join("");}
    function filterWellness(){var q=(document.getElementById("wellness-search")?document.getElementById("wellness-search").value:"").toLowerCase();var filtered=WELLNESS.filter(function(w){var matchType=activeFilter==="all"||(w.type||"wellness")===activeFilter;var matchQ=!q||w.name.toLowerCase().includes(q)||w.services.toLowerCase().includes(q)||w.address.toLowerCase().includes(q);return matchType&&matchQ;});renderWellness(filtered);}
    document.querySelectorAll(".filter-tab").forEach(function(tab){tab.addEventListener("click",function(){document.querySelectorAll(".filter-tab").forEach(function(t){t.classList.remove("filter-tab--active");});tab.classList.add("filter-tab--active");activeFilter=tab.getAttribute("data-filter");filterWellness();});});
    var wsearch=document.getElementById("wellness-search");
    if(wsearch)wsearch.addEventListener("input",function(){filterWellness();});
    window.loadPlatformData().then(function(){filterWellness();});
  }

  // CART
  var cartItemsEl=document.getElementById("cart-items");var cartSummaryEl=document.getElementById("cart-summary");var cartEmptyEl=document.getElementById("cart-empty");
  if(cartItemsEl&&cartSummaryEl&&cartEmptyEl){function renderCart(){var cart=getCart();if(!cart.length){cartItemsEl.style.display="none";cartSummaryEl.style.display="none";cartEmptyEl.style.display="block";return;}cartEmptyEl.style.display="none";cartItemsEl.style.display="flex";cartSummaryEl.style.display="block";cartItemsEl.innerHTML=cart.map(function(it,idx){var tot=(parseFloat(it.price)*(it.qty||1)).toFixed(0);return '<div class="cart-item"><img class="cart-item__img" src="'+(it.img||'')+'" alt="'+it.name+'" /><div class="cart-item__info"><h3 class="cart-item__name">'+it.name+'</h3><p class="cart-item__price">₹'+tot+'</p><div class="cart-item__qty"><button class="qty-minus" data-idx="'+idx+'">−</button><span>'+(it.qty||1)+'</span><button class="qty-plus" data-idx="'+idx+'">+</button></div></div><button class="cart-item__remove" data-idx="'+idx+'">Remove</button></div>';}).join("");var total=getCartTotal();var se=document.getElementById("cart-subtotal"),te=document.getElementById("cart-total");if(se)se.textContent="₹"+total.toFixed(0);if(te)te.textContent="₹"+total.toFixed(0);document.querySelectorAll(".cart-item__remove").forEach(function(b){b.addEventListener("click",function(){removeFromCart(parseInt(b.getAttribute("data-idx"),10));renderCart();updateCartBadge();});});document.querySelectorAll(".qty-minus").forEach(function(b){b.addEventListener("click",function(){updateQty(parseInt(b.getAttribute("data-idx"),10),-1);renderCart();updateCartBadge();});});document.querySelectorAll(".qty-plus").forEach(function(b){b.addEventListener("click",function(){updateQty(parseInt(b.getAttribute("data-idx"),10),1);renderCart();updateCartBadge();});});}renderCart();var ckBtn=document.getElementById("checkout-btn");if(ckBtn)ckBtn.addEventListener("click",function(){if(!getCart().length){alert("Cart is empty!");return;}if(!token){alert("Please log in.");window.location.href="login.html";return;}var total=getCartTotal();fetch(API_BASE+"/auth/me",{headers:{Authorization:"Bearer "+token}}).then(function(r){if(!r.ok)throw new Error("Session expired.");return r.json()}).then(function(u){return fetch(API_BASE+"/orders",{method:"POST",headers:{"Content-Type":"application/json",Authorization:"Bearer "+token},body:JSON.stringify({user_id:u.user_id,total_amount:total,status:"pending"})})}).then(function(r){if(!r.ok)return r.json().then(function(e){throw new Error(e.detail||"Order failed.");});return r.json()}).then(function(o){localStorage.removeItem("cart");showToast("Order #"+o.order_id+" placed! Total: ₹"+o.total_amount);renderCart();updateCartBadge();}).catch(function(e){alert("Checkout error: "+e.message);});});var clrBtn=document.getElementById("clear-cart-btn");if(clrBtn)clrBtn.addEventListener("click",function(){if(confirm("Clear cart?")){localStorage.removeItem("cart");renderCart();updateCartBadge();}});}

  // ORDER TRACKING TIMELINE
  function renderOrderTracking(orders){var container=document.getElementById("order-tracking");if(!container)return;if(!orders||!orders.length){container.innerHTML='<div class="card"><p class="note">No orders to track. <a href="products.html">Shop products</a></p></div>';return;}var STEPS=["placed","processing","shipped","delivered"];var STEP_LABELS={"placed":"Order Placed","processing":"Processing","shipped":"Shipped","delivered":"Delivered"};var STEP_ICONS={"placed":IC.order,"processing":IC.clock,"shipped":'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"/><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"/><circle cx="5.5" cy="18.5" r="2.5"/><circle cx="18.5" cy="18.5" r="2.5"/></svg>',"delivered":IC.check};container.innerHTML=orders.map(function(o){var currentStep=o.tracking_status||"placed";var currentIdx=STEPS.indexOf(currentStep);if(currentIdx<0)currentIdx=0;var dateStr=o.created_at?new Date(o.created_at).toLocaleDateString("en-IN",{day:"numeric",month:"short",year:"numeric"}):"—";return '<div class="order-track-card"><div class="order-track-card__header"><div><h3 class="order-track-card__title">Order #'+o.order_id+'</h3><span class="order-track-card__date">Placed: '+dateStr+'</span></div><span class="order-track-card__amount">₹'+o.total_amount+'</span></div><div class="order-timeline">'+STEPS.map(function(step,i){var cls="order-timeline__step";if(i<currentIdx)cls+=" order-timeline__step--done";else if(i===currentIdx)cls+=" order-timeline__step--active";return '<div class="'+cls+'"><div class="order-timeline__dot">'+STEP_ICONS[step]+'</div><span class="order-timeline__label">'+STEP_LABELS[step]+'</span></div>';}).join('<div class="order-timeline__line"></div>')+'</div>'+(o.estimated_delivery?'<p class="order-track-card__delivery">'+IC.clock+' Est. delivery: '+o.estimated_delivery+'</p>':'')+'</div>';}).join("");}

  // PATIENT DASHBOARD
  var dashWelcome=document.getElementById("dash-welcome");
  if(dashWelcome&&path==="dashboard.html"){if(!token){alert("Please log in.");window.location.href="login.html";return;}fetch(API_BASE+"/auth/me",{headers:{Authorization:"Bearer "+token}}).then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(u){localStorage.setItem("userName",u.name);dashWelcome.textContent="Welcome back, "+u.name+"!";var av=document.querySelector(".user-info-card__avatar");if(av)av.textContent=u.name.charAt(0).toUpperCase();var ph=document.getElementById("profile-heading");if(ph)ph.textContent=u.name;var dp=document.querySelector(".user-info-card__details p");if(dp)dp.textContent=u.email+(u.phone?" · "+u.phone:"")+(u.user_type?" · "+u.user_type.charAt(0).toUpperCase()+u.user_type.slice(1):"");fetch(API_BASE+"/orders/user",{headers:{Authorization:"Bearer "+token}}).then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(orders){var so=document.getElementById("stat-orders");if(so)so.textContent=orders.length;renderOrderTracking(orders);var oe=document.getElementById("dash-orders");if(oe&&orders.length>0)oe.innerHTML=orders.map(function(o){var dateStr=o.created_at?new Date(o.created_at).toLocaleDateString("en-IN",{day:"numeric",month:"short"}):"";return '<div class="order-card"><div class="order-card__info"><h3>Order #'+o.order_id+'</h3><p><span class="order-card__status order-card__status--'+(o.status==="completed"?"completed":"pending")+'">'+o.status+'</span>'+(dateStr?" · "+dateStr:"")+'</p></div><span class="order-card__amount">₹'+o.total_amount+'</span></div>';}).join("");}).catch(function(){});}).catch(function(){dashWelcome.textContent="Welcome back!";});var appts=JSON.parse(localStorage.getItem("appointments")||"[]");var sa=document.getElementById("stat-appointments");if(sa)sa.textContent=appts.length;var ae=document.getElementById("dash-appointments");if(ae&&appts.length>0)ae.innerHTML=appts.map(function(a){return '<div class="order-card"><div class="order-card__info"><h3>'+a.doctor+'</h3><p>'+a.date+' at '+a.time+'</p></div><span class="tag tag--green">'+a.status+'</span></div>';}).join("");var ss=document.getElementById("stat-streak");if(ss)ss.textContent=localStorage.getItem("yogaStreak")||"3";
  
  // Render patient metrics
  createCircularProgress("wellness-progress", 75, "Wellness Score");
  createCircularProgress("health-progress", 60, "Health Goals");
  createCircularProgress("activity-progress", 85, "Activity Level");
  createActivityTimeline();
  createHealthMetrics();
  createMiniCalendar();
  }

  // ADMIN DASHBOARD
  var adminPanel=document.getElementById("admin-panel");
  if(adminPanel){if(!token||userRole!=="admin"){alert("Admin access required.");window.location.href="login.html";return;}var pending=JSON.parse(localStorage.getItem("pendingListings")||"[]");var approved=JSON.parse(localStorage.getItem("approvedListings")||"[]");var activity=JSON.parse(localStorage.getItem("activityLog")||"[]");document.getElementById("admin-stat-users").textContent=Math.floor(Math.random()*50)+20;document.getElementById("admin-stat-pending").textContent=pending.length;document.getElementById("admin-stat-approved").textContent=approved.length;document.getElementById("admin-stat-orders").textContent=Math.floor(Math.random()*30)+5;var plEl=document.getElementById("admin-pending");if(plEl){if(!pending.length)plEl.innerHTML='<p class="note">No pending listings.</p>';else plEl.innerHTML=pending.map(function(p,i){return '<div class="order-card"><div class="order-card__info"><h3>'+p.name+'</h3><p>Type: '+p.type+' · by '+p.submittedBy+'</p></div><div style="display:flex;gap:0.5rem"><button class="btn btn--gold btn--sm approve-btn" data-idx="'+i+'">Approve</button><button class="btn btn--outline-dark btn--sm reject-btn" data-idx="'+i+'">Reject</button></div></div>';}).join("");document.querySelectorAll(".approve-btn").forEach(function(b){b.addEventListener("click",function(){var i=parseInt(b.getAttribute("data-idx"),10);var item=pending.splice(i,1)[0];item.status="approved";approved.push(item);activity.push({action:"Approved "+item.type+": "+item.name,time:new Date().toLocaleString()});localStorage.setItem("pendingListings",JSON.stringify(pending));localStorage.setItem("approvedListings",JSON.stringify(approved));localStorage.setItem("activityLog",JSON.stringify(activity));showToast("Approved!");location.reload();});});document.querySelectorAll(".reject-btn").forEach(function(b){b.addEventListener("click",function(){var i=parseInt(b.getAttribute("data-idx"),10);var item=pending.splice(i,1)[0];activity.push({action:"Rejected "+item.type+": "+item.name,time:new Date().toLocaleString()});localStorage.setItem("pendingListings",JSON.stringify(pending));localStorage.setItem("activityLog",JSON.stringify(activity));showToast("Rejected.");location.reload();});});}var alEl=document.getElementById("admin-activity");if(alEl){if(!activity.length)alEl.innerHTML='<p class="note">No activity yet.</p>';else alEl.innerHTML=activity.slice(-10).reverse().map(function(a){return '<div class="order-card"><div class="order-card__info"><h3>'+a.action+'</h3><p>'+a.time+'</p></div></div>';}).join("");}
  
  // Enhanced Admin Dashboard Features
  createAdminCharts();
  createUserTypeDistribution();
  createRevenueChart();
  }

  // SELLER DASHBOARD
  var sellerPanel=document.getElementById("seller-panel");
  if(sellerPanel){if(!token||userRole!=="seller"){alert("Seller access required.");window.location.href="login.html";return;}

  var sellerProducts=[]; // Will be populated from API

  function renderSellerProducts(products){var el=document.getElementById("seller-products");if(!el)return;if(!products.length){el.innerHTML='<p class="note">No products added yet.</p>';return;}el.innerHTML=products.map(function(p,i){return '<div class="order-card"><div class="order-card__info"><h3>'+p.name+'</h3><p>₹'+p.price+' · '+(p.status||p.category||"General")+'</p></div></div>';}).join("");}

  // Load seller's products from API
  function loadSellerProducts(){
    fetch(API_BASE+"/products",{headers:{Authorization:"Bearer "+token}})
      .then(function(r){return r.ok?r.json():[];}).catch(function(){return[];})
      .then(function(prods){sellerProducts=prods;renderSellerProducts(sellerProducts);});
  }
  loadSellerProducts();

  var addProdForm=document.getElementById("add-product-form");
  if(addProdForm)addProdForm.addEventListener("submit",function(e){
    e.preventDefault();
    var n=document.getElementById("prod-name").value;
    var pr=document.getElementById("prod-price").value;
    var d=document.getElementById("prod-desc").value;
    var btn=addProdForm.querySelector("button[type=submit]");
    if(btn){btn.disabled=true;btn.textContent="Submitting...";}
    var imgUrl="https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?auto=format&fit=crop&w=400&q=80";
    fetch(API_BASE+"/products",{
      method:"POST",
      headers:{"Content-Type":"application/json",Authorization:"Bearer "+token},
      body:JSON.stringify({name:n,price:parseFloat(pr),desc:d,img:imgUrl,category:"General"})
    }).then(function(r){
      if(!r.ok)return r.json().then(function(e){throw new Error(e.detail||"Failed to add product");});
      return r.json();
    }).then(function(newProd){
      showToast("Product '"+newProd.name+"' added successfully!");
      addProdForm.reset();
      loadSellerProducts(); // Refresh from API
    }).catch(function(err){
      // Fallback: save locally
      var ls=JSON.parse(localStorage.getItem("sellerProducts")||"[]");
      ls.push({name:n,price:pr,desc:d,status:"pending approval (offline)"});
      localStorage.setItem("sellerProducts",JSON.stringify(ls));
      showToast("Saved locally ("+err.message+"). Will sync when online.");
      addProdForm.reset();
      renderSellerProducts(ls);
    }).finally(function(){if(btn){btn.disabled=false;btn.textContent="Submit for Approval";}});
  });

  // DOCTOR DASHBOARD
  var doctorPanel=document.getElementById("doctor-panel");
  if(doctorPanel){if(!token||userRole!=="doctor"){alert("Doctor access required.");window.location.href="login.html";return;}var savedProfile=JSON.parse(localStorage.getItem("doctorProfile")||"null");var profForm=document.getElementById("doctor-profile-form");if(profForm){if(savedProfile){document.getElementById("doc-name").value=savedProfile.name||"";document.getElementById("doc-spec").value=savedProfile.specialization||"";document.getElementById("doc-exp").value=savedProfile.experience||"6-10";document.getElementById("doc-phone").value=savedProfile.phone||"";document.getElementById("doc-location").value=savedProfile.location||"";document.getElementById("doc-image").value=savedProfile.image_url||"";document.getElementById("doc-bio").value=savedProfile.bio||"";}profForm.addEventListener("submit",function(e){e.preventDefault();var profile={name:document.getElementById("doc-name").value,specialization:document.getElementById("doc-spec").value,experience:document.getElementById("doc-exp").value,phone:document.getElementById("doc-phone").value,location:document.getElementById("doc-location").value,image_url:document.getElementById("doc-image").value,bio:document.getElementById("doc-bio").value};localStorage.setItem("doctorProfile",JSON.stringify(profile));fetch(API_BASE+"/doctors",{method:"POST",headers:{"Content-Type":"application/json",Authorization:"Bearer "+token},body:JSON.stringify(profile)}).then(function(r){return r.json()}).then(function(){showToast("Profile saved! You now appear on the Doctors page.");}).catch(function(){showToast("Profile saved locally!");});var customDocs=JSON.parse(localStorage.getItem("customDoctors")||"[]");var existing=customDocs.findIndex(function(d){return d.name===profile.name;});if(existing>=0)customDocs[existing]=profile;else customDocs.push(profile);localStorage.setItem("customDoctors",JSON.stringify(customDocs));});}var myAppts=JSON.parse(localStorage.getItem("appointments")||"[]");var apptList=document.getElementById("doctor-appointments");if(apptList){if(!myAppts.length)apptList.innerHTML='<p class="note">No appointments booked yet.</p>';else apptList.innerHTML=myAppts.map(function(a){return '<div class="order-card"><div class="order-card__info"><h3>Patient Booking</h3><p>'+a.date+' at '+a.time+(a.notes?' — '+a.notes:'')+'</p></div><span class="tag tag--green">'+a.status+'</span></div>';}).join("");}
  
  // Enhanced Doctor Dashboard Features
  createDoctorMetrics();
  createPatientInsights();
  createAppointmentCalendar();
  }

  // WELLNESS DASHBOARD
  var wellnessPanel=document.getElementById("wellness-panel");
  if(wellnessPanel){if(!token||userRole!=="wellness"){alert("Wellness centre access required.");window.location.href="login.html";return;}var wServices=JSON.parse(localStorage.getItem("wellnessServices")||"[]");function renderWServices(){var el=document.getElementById("wellness-services-list");if(!el)return;if(!wServices.length){el.innerHTML='<p class="note">No services added yet.</p>';return;}el.innerHTML=wServices.map(function(s,i){return '<div class="order-card"><div class="order-card__info"><h3>'+s.name+'</h3><p>₹'+s.price+' · '+s.duration+'</p></div><button class="btn btn--outline-dark btn--sm del-svc" data-idx="'+i+'">Delete</button></div>';}).join("");document.querySelectorAll(".del-svc").forEach(function(b){b.addEventListener("click",function(){var i=parseInt(b.getAttribute("data-idx"),10);wServices.splice(i,1);localStorage.setItem("wellnessServices",JSON.stringify(wServices));showToast("Service removed.");renderWServices();});});}renderWServices();var addSvcForm=document.getElementById("add-service-form");if(addSvcForm)addSvcForm.addEventListener("submit",function(e){e.preventDefault();var n=document.getElementById("svc-name").value,pr=document.getElementById("svc-price").value,dur=document.getElementById("svc-duration").value;wServices.push({name:n,price:pr,duration:dur});localStorage.setItem("wellnessServices",JSON.stringify(wServices));var pend=JSON.parse(localStorage.getItem("pendingListings")||"[]");pend.push({name:n,type:"Service",submittedBy:userName||"Centre"});localStorage.setItem("pendingListings",JSON.stringify(pend));showToast("Service submitted for approval!");addSvcForm.reset();renderWServices();});
  
  // Enhanced Wellness Dashboard Features
  if (typeof window.createWellnessMetrics === 'function') {
    window.createWellnessMetrics();
    window.createServiceAnalytics();
    window.createClientProgress();
  }
  }

  }})();

// Make wellness functions available globally
window.createWellnessMetrics = function() {
  var container = document.getElementById("wellness-metrics");
  if (!container) return;
  
  var IC = {
    users:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>',
    spa:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    heart:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>',
    zap:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
  };
  
  var metrics = [
    { icon: IC.users, value: "156", label: "Active Members", trend: "+12", trendDir: "up" },
    { icon: IC.spa, value: "89", label: "Sessions Today", trend: "+7", trendDir: "up" },
    { icon: IC.heart, value: "4.9", label: "Satisfaction", trend: "+0.2", trendDir: "up" },
    { icon: IC.zap, value: "92%", label: "Capacity", trend: "+5%", trendDir: "up" }
  ];
  
  container.innerHTML = '<div class="health-metrics">' +
    metrics.map(function(metric) {
      return '<div class="health-metric">' +
        '<div class="health-metric__icon">' + metric.icon + '</div>' +
        '<div class="health-metric__value">' + metric.value + '</div>' +
        '<div class="health-metric__label">' + metric.label + '</div>' +
        '<div class="health-metric__trend ' + metric.trendDir + '">' + metric.trend + '</div>' +
        '</div>';
    }).join('') +
    '</div>';
};

window.createServiceAnalytics = function() {
  var container = document.getElementById("service-analytics");
  if (!container) return;
  
  var services = [
    { name: "Yoga Classes", bookings: 45, revenue: 22500 },
    { name: "Meditation", bookings: 32, revenue: 16000 },
    { name: "Ayurvedic Massage", bookings: 28, revenue: 42000 },
    { name: "Pranayama", bookings: 21, revenue: 10500 }
  ];
  
  var maxBookings = Math.max.apply(Math, services.map(function(s) { return s.bookings; }));
  
  container.innerHTML = '<div class="chart-container">' +
    '<div class="chart-header">' +
    '<h3 class="chart-title">Service Performance</h3>' +
    '<span class="chart-period">This Month</span>' +
    '</div>' +
    services.map(function(service) {
      var percentage = (service.bookings / maxBookings) * 100;
      return '<div style="margin-bottom: 1rem;">' +
        '<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">' +
        '<span style="font-weight: 600; color: var(--color-dark-green);">' + service.name + '</span>' +
        '<span style="font-size: 0.9rem; color: var(--color-text-muted);">' + service.bookings + ' bookings</span>' +
        '</div>' +
        '<div style="background: rgba(46,125,50,0.1); height: 8px; border-radius: 4px; overflow: hidden;">' +
        '<div style="background: var(--color-forest); height: 100%; width: ' + percentage + '%; border-radius: 4px; transition: width 1s ease;"></div>' +
        '</div>' +
        '<div style="text-align: right; margin-top: 0.25rem;">' +
        '<span style="font-size: 0.8rem; color: var(--color-forest); font-weight: 600;">₹' + service.revenue.toLocaleString() + '</span>' +
        '</div>' +
        '</div>';
    }).join('') +
    '</div>';
};

window.createClientProgress = function() {
  var container = document.getElementById("client-progress");
  if (!container) return;
  
  if (typeof window.createCircularProgress === 'function') {
    window.createCircularProgress("member-retention", 88, "Member Retention");
    window.createCircularProgress("class-attendance", 76, "Class Attendance");
    window.createCircularProgress("wellness-goals", 82, "Wellness Goals Met");
  }
};
