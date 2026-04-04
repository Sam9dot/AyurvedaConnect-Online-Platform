import re
import os

with open(r'c:\Users\shriy\epl\frontend\js\app.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

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
      
      // Update variables if database is NOT empty.
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

js_content = js_content.replace('var DOCTORS = [', 'window.__FALLBACK_DOCTORS__ = [')
js_content = js_content.replace('var PRODUCTS = [', 'window.__FALLBACK_PRODUCTS__ = [')
js_content = js_content.replace('var WELLNESS = [', 'window.__FALLBACK_WELLNESS__ = [')

# Inject integration code before PAGE HANDLERS
js_content = js_content.replace('// === PAGE HANDLERS', integration_code + '\n  // === PAGE HANDLERS')

# Wrap DOMContentLoaded logic in promise:
# `document.addEventListener('DOMContentLoaded',function(){` -> `document.addEventListener('DOMContentLoaded',function(){ window.loadPlatformData().then(() => {`
# And add closing `});` at the end of the script block.

# Rather than regexing DOMContentLoaded, we can just replace the calls directly or override the handlers.
# Wait, let's just make `renderDoctors()`, `renderProducts()` asynchronous manually.
# In app.js: `if(dl&&path==="doctors.html"){renderDoctors();}` -> `if(dl&&path==="doctors.html"){ window.loadPlatformData().then(() => renderDoctors()); } else if(dl)`

handler_fixes = [
    ('if(dl&&path==="doctors.html"){renderDoctors();}', 'if(dl&&path==="doctors.html"){ window.loadPlatformData().then(() => renderDoctors()); }'),
    ('if(pl&&path==="products.html"){renderProducts();}', 'if(pl&&path==="products.html"){ window.loadPlatformData().then(() => renderProducts()); }'),
    ('if(wl&&path==="wellness.html"){renderWServices();}', 'if(wl&&path==="wellness.html"){ window.loadPlatformData().then(() => renderWServices()); }'),
]

for orig, repl in handler_fixes:
    js_content = js_content.replace(orig, repl)


# Wait, on index.html, it shows DOCTORS too:
# `var fdl=document.getElementById("featured-doctors-list");if(fdl&&path==="index.html"){ ... }`
idx_fix = 'var fdl=document.getElementById("featured-doctors-list");if(fdl&&path==="index.html"){'
js_content = js_content.replace(idx_fix, 'var fdl=document.getElementById("featured-doctors-list");if(fdl&&path==="index.html"){ window.loadPlatformData().then(() => {')

# Need to close that block. The block ends with setting up yoga-btn click listener.
js_content = js_content.replace('if(yb){yb.addEventListener("click",', '});\n    if(yb){yb.addEventListener("click",')

with open(r'c:\Users\shriy\epl\frontend\js\app.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Integration complete")
