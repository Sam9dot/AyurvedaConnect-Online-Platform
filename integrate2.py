import re
import os

with open(r'c:\Users\shriy\epl\frontend\js\app.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Make the arrays fallback variables
js_content = js_content.replace('var DOCTORS = [', 'window.__FALLBACK_DOCTORS__ = [')
js_content = js_content.replace('var PRODUCTS = [', 'window.__FALLBACK_PRODUCTS__ = [')
js_content = js_content.replace('var WELLNESS = [', 'window.__FALLBACK_WELLNESS__ = [')

integration_code = """
  // ===== DYNAMIC FALLBACK VARIABLES =====
  let DOCTORS = window.__FALLBACK_DOCTORS__ || [];
  let PRODUCTS = window.__FALLBACK_PRODUCTS__ || [];
  let WELLNESS = window.__FALLBACK_WELLNESS__ || [];

  // Async loader
  window.loadPlatformData = function() {
    return Promise.all([
      fetch(API_BASE + '/doctors').then(res => res.ok ? res.json() : []).catch(() => []),
      fetch(API_BASE + '/products').then(res => res.ok ? res.json() : []).catch(() => []),
      fetch(API_BASE + '/wellness').then(res => res.ok ? res.json() : []).catch(() => [])
    ]).then(([fetchedDoctors, fetchedProducts, fetchedWellness]) => {
      
      if (fetchedDoctors && fetchedDoctors.length > 0) {
        DOCTORS = fetchedDoctors.map(d => ({
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
        }));
      }

      if (fetchedProducts && fetchedProducts.length > 0) {
        PRODUCTS = fetchedProducts.map(p => {
          let fallback = window.__FALLBACK_PRODUCTS__.find(fp => p.name.includes(fp.name)) || window.__FALLBACK_PRODUCTS__[0];
          return {
            id: p.product_id || p.id,
            name: p.name,
            desc: fallback.desc,
            price: p.price,
            img: fallback.img,
            category: "Supplements" 
          };
        });
      }

      if (fetchedWellness && fetchedWellness.length > 0) {
        WELLNESS = fetchedWellness.map(w => ({
          name: w.name,
          type: w.center_type || "wellness",
          address: w.location || "Pune",
          services: w.services || "Wellness, Spa",
          phone: w.phone || "",
          rating: w.rating || 4.5,
          exp: w.experience || "3-5",
          img: w.image_url || window.__FALLBACK_WELLNESS__[0].img,
          facilities: w.amenities ? w.amenities.split(',') : ["Consultation"]
        }));
      }
    });
  }
"""

if "window.__FALLBACK_DOCTORS__" not in js_content:
    js_content = js_content.replace('// === PAGE HANDLERS', integration_code + '\n  // === PAGE HANDLERS')

# We need to find everywhere `renderXYZ();` is called and wrap it in `window.loadPlatformData().then(() => { renderXYZ(); });`
js_content = re.sub(r'(if\(.*?\){\s*)(renderDoctors\(\);\s*})', r'\1window.loadPlatformData().then(() => { renderDoctors(); });}', js_content)
js_content = re.sub(r'(if\(.*?\){\s*)(renderProducts\(\);\s*})', r'\1window.loadPlatformData().then(() => { renderProducts(); });}', js_content)
js_content = re.sub(r'(if\(.*?\){\s*)(renderWServices\(\);\s*})', r'\1window.loadPlatformData().then(() => { renderWServices(); });}', js_content)

with open(r'c:\Users\shriy\epl\frontend\js\app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Integration wrapped!")
