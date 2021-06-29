from flask import Flask, render_template, request

import ga

server = Flask(__name__)


@server.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.form.get('teste'):
            ga.generate_graph(ga.random_try())
        else:
            t0 = request.form.get('t1')
            t1 = request.form.get('t2')
            t2 = request.form.get('t3')
            if t0 and t1 and t2:
                t0 = int(t0)
                t1 = int(t1)
                t2 = int(t2)
                ga.calc(t0, t1, t2)

    return render_template('index.html')


if __name__ == '__main__':
    server.run()
