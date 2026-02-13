from flask import Flask, render_template_string, send_file
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Deepanshi | Software Developer</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body{
    margin:0;
    font-family: Arial, sans-serif;
    background: linear-gradient(120deg,#1f1c2c,#928dab);
    color:white;
}
header{
    text-align:center;
    padding:60px 20px;
}
h1{
    font-size:40px;
}
.section{
    padding:40px;
}
.card{
    background:white;
    color:black;
    padding:20px;
    margin:15px 0;
    border-radius:10px;
}
button{
    padding:10px 20px;
    background:#ff9800;
    border:none;
    color:white;
    cursor:pointer;
    border-radius:5px;
}
footer{
    text-align:center;
    padding:20px;
    background:black;
}
</style>
</head>
<body>

<header>
    <h1>Deepanshi</h1>
    <p>Software Developer | Python | Web Developer</p>
    <a href="/resume"><button>Download Resume</button></a>
</header>

<div class="section">
<h2>Skills</h2>
<div class="card">
Python, Flask, Django, HTML, CSS, JavaScript, MySQL, Git, GitHub, REST API, Microservices
</div>
</div>

<div class="section">
<h2>Projects</h2>

<div class="card">
<h3>1. AI Resume Screening System</h3>
<p>AI based resume filtering system using NLP & Machine Learning.</p>
</div>

<div class="card">
<h3>2. Microservices E-Commerce Website</h3>
<p>Advanced scalable ecommerce system built with Flask microservices architecture.</p>
</div>

<div class="card">
<h3>3. Expense Tracker Application</h3>
<p>Desktop based expense tracker with charts and Excel integration.</p>
</div>

<div class="card">
<h3>4. Smart Portfolio Website</h3>
<p>Dynamic personal portfolio with resume download & contact form.</p>
</div>

<div class="card">
<h3>5. Remote Code Execution System</h3>
<p>Secure web-based system to compile and execute code remotely.</p>
</div>

</div>

<div class="section">
<h2>Contact</h2>
<div class="card">
Email: deepanshi.dev@example.com
</div>
</div>

<footer>
© 2026 Deepanshi | All Rights Reserved
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/resume")
def resume():
    return send_file("resume.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
