import json

from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

# HTML template for the search page
HTML_PAGE = """
<!doctype html>
<html>
  <head>
    <title>IP Extractor</title>
  </head>
  <body style="font-family: sans-serif; margin: 40px;">
    <h2>Enter any text (with IP addresses):</h2>
    <form method="post">
      <textarea name="user_text" rows="6" cols="60" placeholder="Type or paste text here..."></textarea><br><br>
      <input type="submit" value="Submit">
    </form>
    {% if ips %}
      <h3>Extracted IP Addresses:</h3>
      <ul>
      {% for ip in ips %}
        <li>{{ ip }}</li>
      {% endfor %}
      </ul>
    {% endif %}
  </body>
</html>
"""

# Regex to match IPv4 addresses
IP_REGEX = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'


@app.route('/', methods=['GET', 'POST'])
def index():
    ips = []


    if request.method == 'POST':
        with open('ServiceTags_Public_20251028.json', 'r') as file:
            data = json.load(file)
            # print(data)

        user_text = request.form.get('user_text', '')
        ips = re.findall(IP_REGEX, data)
        file_ips = re.findall(IP_REGEX, user_text)
        print(list(set(ips) & set(file_ips)))

        # Print in console
        # if ips:
        #     # print("Extracted IPs:", ips)
        #     print(data)
        # else:
        #     print("No IP addresses found.")

    # return render_template_string(HTML_PAGE, ips=ips)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)