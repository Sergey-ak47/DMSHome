from flask import Flask, render_template_string, send_file
import os

app_web = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>DMSHome</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="manifest" href="/manifest.json">
    <style>
        body { background-color: #1a1a1a; color: white; font-family: Arial; text-align: center; padding: 20px; }
        h1 { color: #3B8ED0; }
        button { width: 250px; height: 60px; margin: 10px; font-size: 18px; border-radius: 20px; border: none; cursor: pointer; }
        .on { background-color: #FFD700; color: black; }
        .off { background-color: #3B8ED0; color: white; }
    </style>
</head>
<body>
    <h1>DMSHome</h1>
    <button id="btn_living" class="off" onclick="toggle('living')">Гостиная</button><br>
    <button id="btn_bedroom" class="off" onclick="toggle('bedroom')">Спальня</button><br>
    <button id="btn_kitchen" class="off" onclick="toggle('kitchen')">Кухня</button><br>
    <button id="btn_toilet" class="off" onclick="toggle('toilet')">Туалет</button><br>
    <script>
        function toggle(room) {
            fetch('/toggle/' + room).then(r => r.text()).then(state => {
                let btn = document.getElementById('btn_' + room);
                if (state === 'ON') { btn.className = 'on'; }
                else { btn.className = 'off'; }
            });
        }
    </script>
</body>
</html>
"""

states = {"living": "OFF", "bedroom": "OFF", "kitchen": "OFF", "toilet": "OFF"}

@app_web.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app_web.route('/toggle/<room>')
def toggle_room(room):
    if room in states:
        states[room] = "ON" if states[room] == "OFF" else "OFF"
        return states[room]
    return "ERROR"

@app_web.route('/manifest.json')
def manifest():
    return send_file('manifest.json', mimetype='application/json')

if __name__ == '__main__':
    app_web.run(host='0.0.0.0', port=5000)
