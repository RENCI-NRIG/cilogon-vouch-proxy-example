from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def show_headers():
    req = request.headers
    buttons = """"""
    try:
        if req['X-Vouch-User']:
            # User is logged in
            buttons = """
<h3>Logout to view less header information</h3>
<div>
<button type="button" class="btn btn-default" onclick="window.location.href='/login/flask'" disabled="disabled">
Login
</button>
<button type="button" class="btn btn-danger" onclick="window.location.href='/logout/flask'">
Logout
</button>
</div>
<h3>Header Information (authenticated)</h3>
"""
    except KeyError:
        # User is logged out
        buttons = """
<h3>Login to view additional header information</h3>
<div>
<button type="button" class="btn btn-success" onclick="window.location.href='/login/flask'">
Login
</button>
<button type="button" class="btn btn-default" onclick="window.location.href='/logout/flask'" disabled="disabled">
Logout
</button>
</div>
<h3>Header Information (non-authenticated)</h3>
"""

    response = """
<!DOCTYPE html>
<head>
<title>CILogon / Vouch-Proxy</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<style>
body {
width: 90%;
margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif;
}

table, th, td {
border: 1px solid black;
border-collapse: collapse;
}

th, td {
padding: 5px;
}

th {
text-align: center;
}
</style>
</head>
<body>
<div class="container">
"""
    response = response + buttons + """
</div>
<div class="container">
<table style="width:100%">
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
</div>
</br>
Back to <a href="/">Homepage</a>
</body>
"""

    if "curl" in str(req['User-Agent']):
        response = {}
        for line in req:
            response[str(line[0])] = str(line[1])

    return response
