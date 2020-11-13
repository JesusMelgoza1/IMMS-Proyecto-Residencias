from flask import Flask, render_template

app = Flask(__name__)

@app.route('/politica')
def politica():
    return render_template("politica.html")

@app.route('/encuesta1_P1')
def encuesta():
    return render_template("encuesta1_P1.html")

@app.route('/encuesta1_P2')
def encuesta2():
    return render_template("encuesta1_P2.html")

@app.route('/encuesta1_P3')
def encuesta3():
    return render_template("encuesta1_P3.html")

@app.route('/registrodeusuario')
def formulario():
    return render_template("registrodeusuario.html")

@app.route('/passena')
def pascon():
    return render_template("passena.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)