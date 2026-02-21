from flask import Flask, jsonify, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/on')
def turn_on():
    return jsonify({"2":"1"})

@app.route('/off')
def turn_off():
    return jsonify({"2":"0"})

if __name__ == "__main__" :
    app.run(host='0.0.0.0', port=8000) 
