from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

# DUMMY DATA: Simulasi data dari database
dummy_tasks = [
    {"id": 1, "title": "Desain Mockup UI", "status": "done", "tupoksi": "desainer"},
    {"id": 2, "title": "Setup Database Supabase", "status": "doing", "tupoksi": "backend"},
    {"id": 3, "title": "Integrasi API Login", "status": "todo", "tupoksi": "backend"},
    {"id": 4, "title": "Slicing HTML/CSS", "status": "todo", "tupoksi": "frontend"}
]

@app.route('/')
def dashboard():
    return render_template('dashboard.html', tasks=dummy_tasks)
