# import json
#
# from flask import Flask, request, render_template_string
# import re
#
# IP_REGEX = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
#
#
#
#
# with open('ServiceTags_Public_20251028.json', 'r') as file:
#     # data = json.load(file)
#     data = file.read()
#     # print(data)
#
# user_text = "4.198.222.96, 4.251.0.64/29"
# ips = re.findall(IP_REGEX, data)
# file_ips = re.findall(IP_REGEX, user_text)
# print(list(set(ips) & set(file_ips)))
import re

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



from flask import Flask, request, render_template_string
import ipaddress

IP_REGEX = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        with open('ServiceTags_Public_20251028.json', 'r') as file:
            data = file.read()

    ips_from_json = re.findall(IP_REGEX, data)

        # query = request.form['query']
        # try:
        #     ipaddress.ip_address(query) # check if the input is a valid IP address
        #     print("Searching for", query)
        #     return "Found IP Address"
        # except ValueError as e:
        #     return str(e)
    return render_template_string(HTML_PAGE,  ips=ips_from_json) #, ips=ips
if __name__ == '__main__':
    app.run()