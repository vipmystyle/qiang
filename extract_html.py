import json
import os

file_path = '/home/ubuntu/console_outputs/exec_result_2026-03-18_17-09-12_266.txt'
with open(file_path, 'r') as f:
    content = f.read().strip()

# The content is a JSON-encoded string (with quotes and escapes)
try:
    # Use json.loads to handle escapes correctly
    html_content = json.loads(content)
except Exception as e:
    print(f"Error parsing: {e}")
    # Fallback: remove leading/trailing quotes and unescape manually if needed
    if content.startswith('"') and content.endswith('"'):
        html_content = content[1:-1].replace('\\"', '"').replace('\\n', '\n').replace('\\/', '/')
    else:
        html_content = content

with open('/home/ubuntu/replicated_page.html', 'w') as f:
    f.write(html_content)

print("HTML extracted to /home/ubuntu/replicated_page.html")
