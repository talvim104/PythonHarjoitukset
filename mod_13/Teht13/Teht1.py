from flask import Flask, request

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def tarkista_alkuluku(luku):
    if luku < 2:
        alkuluku = False
    else:
        alkuluku = True
        for i in range(2, luku):
            if luku % i == 0:
                alkuluku = False
                break

    if alkuluku:
        return f"Luku {luku} on alkuluku."
    else:
        return f"Luku {luku} ei ole alkuluku."

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
