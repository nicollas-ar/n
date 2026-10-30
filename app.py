from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # host 0.0.0.0 permite abrir pelo celular na mesma rede Wi-Fi:
    # http://IP_DO_SEU_COMPUTADOR:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
