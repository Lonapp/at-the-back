from app import app

@app.route('/')
def index():
    return "Welcome to Lon'!"

app.run(host='0.0.0.0', port=5000, debug=True)
