import base64
import os
import re

def get_base64(file_path):
    with open(file_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

html_path = '/home/ubuntu/replicated_page.html'
with open(html_path, 'r') as f:
    html = f.read()

# Replace images and video
replacements = {
    '/static/images/d-ticket-icon.png': f"data:image/png;base64,{get_base64('/home/ubuntu/assets/d-ticket-icon.png')}",
    '/static/images/mopla-logo.png': f"data:image/png;base64,{get_base64('/home/ubuntu/assets/mopla-logo.png')}",
    '/static/images/mopla-logo.mp4': f"data:video/mp4;base64,{get_base64('/home/ubuntu/assets/mopla-logo.mp4')}",
    '/qrcode/bbd6f9bd27324109aa33a22b9d3f36a8.png': f"data:image/png;base64,{get_base64('/home/ubuntu/assets/qrcode.png')}"
}

for old, new in replacements.items():
    html = html.replace(old, new)

# Replace Google Fonts links with inline @font-face
font_style = f"""
    <style>
        @font-face {{
            font-family: 'Poppins';
            font-style: normal;
            font-weight: 400;
            src: url(data:font/woff2;base64,{get_base64('/home/ubuntu/assets/poppins-400.woff2')}) format('woff2');
        }}
        @font-face {{
            font-family: 'Poppins';
            font-style: normal;
            font-weight: 600;
            src: url(data:font/woff2;base64,{get_base64('/home/ubuntu/assets/poppins-600.woff2')}) format('woff2');
        }}
        @font-face {{
            font-family: 'Poppins';
            font-style: normal;
            font-weight: 700;
            src: url(data:font/woff2;base64,{get_base64('/home/ubuntu/assets/poppins-700.woff2')}) format('woff2');
        }}
        @font-face {{
            font-family: 'Public Sans';
            font-style: normal;
            font-weight: 400;
            src: url(data:font/woff2;base64,{get_base64('/home/ubuntu/assets/publicsans-400.woff2')}) format('woff2');
        }}
        @font-face {{
            font-family: 'Public Sans';
            font-style: normal;
            font-weight: 600;
            src: url(data:font/woff2;base64,{get_base64('/home/ubuntu/assets/publicsans-600.woff2')}) format('woff2');
        }}
        @font-face {{
            font-family: 'Public Sans';
            font-style: normal;
            font-weight: 700;
            src: url(data:font/woff2;base64,{get_base64('/home/ubuntu/assets/publicsans-700.woff2')}) format('woff2');
        }}
    </style>
"""

# Remove Google Fonts links
html = re.sub(r'<link [^>]*fonts\.googleapis\.com[^>]*>', '', html)
html = re.sub(r'<link [^>]*fonts\.gstatic\.com[^>]*>', '', html)

# Insert font_style before </head>
html = html.replace('</head>', font_style + '</head>')

# Remove manus-helper attributes
html = re.sub(r' manus-helper-ready="true"', '', html)
html = re.sub(r' data-manus_clickable="true"', '', html)
html = re.sub(r' data-manus_click_id="\d+"', '', html)

with open('/home/ubuntu/Deutschlandticket_Po_Yi_Offline.html', 'w') as f:
    f.write(html)

print("Offline HTML generated at /home/ubuntu/Deutschlandticket_Po_Yi_Offline.html")
