import os
from app import create_app
from flask import render_template

#settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app()

@app.route('/')
def home():
    return render_template("index.html")

port = int(os.environ.get('PORT', 5000))
app.run(debug=True, host='0.0.0.0', port=port)
