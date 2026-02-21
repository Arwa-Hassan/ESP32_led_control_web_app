from flask import Flask, jsonify, render_template

app=Flask(__name__)

led_state= {"2":"0"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/on')
def turn_on():
    led_state["2"] = "1"
    return "ON"

@app.route('/off')
def turn_off():
    led_state["2"] = "0"
    return "OFF"

@app.route('/state')
def state():
    return jsonify(led_state)

if __name__ == "__main__" :
    app.run() 
