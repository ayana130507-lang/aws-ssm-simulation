
from flask import Flask, request
from html import escape

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    command = request.form.get("command", "").strip()

    results = {
        "hostname": "ec2-simulator",
        "date": "2026-10-28 12:00:00",
        "whoami": "ec2-user (simulation)",
        "os": "Linux (simulation)",
        "pwd": "/home/ec2-user (simulation)"
    }

    output = results.get(command, "Unknown command") if command else ""

    result_html = ""
    if command:
        status = "Success" if command in results else "Failed"
        result_html = (
            "<pre>Command: " + escape(command)
            + "\nStatus: " + status
            + "\nOutput: " + escape(output) + "</pre>"
        )

    return """
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="UTF-8">
      <title>AWS Systems Manager</title>
      <style>
        body {font-family:Arial;max-width:700px;margin:50px auto;padding:20px}
        input,button {padding:12px}
        button {background:#e68a00;color:white;border:0}
        pre {background:#17202a;color:#7CFC98;padding:20px;white-space:pre-wrap}
      </style>
    </head>
    <body>
      <h1>AWS Systems Manager</h1>
      <h3>EC2 Remote Command Simulator</h3>
      <p>Instance ID: i-1234567890abcdef0</p>
      <p>Status: Running (simulation)</p>
      <form method="post">
        <input name="command" placeholder="hostname, date, whoami, os, pwd" required>
        <button type="submit">Run Command</button>
      </form>
    """ + result_html + """
    </body>
    </html>
    """

