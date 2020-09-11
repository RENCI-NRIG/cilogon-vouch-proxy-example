from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def show_headers():
    req = request.headers

    response = """
<!DOCTYPE html>
<body>
<p><b>USAGE:</b><br><br>
HTTP: <a href="http://127.0.0.1:8080/" target="_blank" rel="noopener noreferrer">http://127.0.0.1:8080/</a><br>
HTTPS: <a href="https://127.0.0.1:8443/" target="_blank" rel="noopener noreferrer">https://127.0.0.1:8443/</a><br>
CURL: curl --insecure --cookie $COOKIE https://127.0.0.1:8443 
(where $COOKIE is a local variable created from the "Cookie" attribute)<br>
</p>
<table style="width:100%" border=1 bordercolor=black>
<tr>
<th>Index</th>
<th>Attribute/Claim</th>
<th>Value</th>
</tr>
"""
    i = 1
    for line in req:
        response = response + """
<tr>
<td>{0}</td>
<td>{1}</td>
<td>{2}</td>
</tr>
""".format(str(i), str(line[0]), str(line[1]))
        i = i + 1
    response = response + """
</table>
</body>
"""

    if "curl" in str(req['User-Agent']):
        response = {}
        for line in req:
            response[str(line[0])] = str(line[1])

    return response
