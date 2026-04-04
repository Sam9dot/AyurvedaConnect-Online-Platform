import glob, re
import os

for f in glob.glob('frontend/*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        c = file.read()
    c = re.sub(r'width="56" height="56"', 'width="72" height="72"', c)
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)

app_js = 'frontend/js/app.js'
with open(app_js, 'r', encoding='utf-8') as file:
    c = file.read()

# Make User Name dynamic for dashboards
dashboard_logic = """
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
"""
c = c.replace('// === PAGE HANDLERS', dashboard_logic + '\n  // === PAGE HANDLERS')

with open(app_js, 'w', encoding='utf-8') as file:
    file.write(c)
print("Finished updates.")
