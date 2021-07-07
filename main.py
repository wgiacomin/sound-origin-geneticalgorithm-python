from flask import Flask, render_template, request

import ga

server = Flask(__name__)


@server.route("/", methods=['POST', 'GET'])
def home():
    aux0 = "t1"
    aux1 = "t2"
    aux2 = "t3"
    if request.method == 'POST':
        if request.form.get('teste'):
            solve.generate_graph(solve.random_try())
            aux0 = solve.get_t0
            aux1 = solve.get_t1
            aux2 = solve.get_t2
        else:
            t0 = request.form.get('t1')
            t1 = request.form.get('t2')
            t2 = request.form.get('t3')
            if t0 and t1 and t2:
                t0 = int(t0)
                t1 = int(t1)
                t2 = int(t2)
                solve.calc(t0, t1, t2)
    return render_template('index.html', aT1=solve.get_T0, aT2=solve.get_T1, aT3=solve.get_T2,
                           at0=aux0, at1=aux1, at2=aux2)


@server.route("/change", methods=['POST'])
def change():
    if request.form.get('c1') and request.form.get('c2') and request.form.get('c3'):
        TO = [int(x) for x in request.form.get('c1').split(',')]
        T1 = [int(x) for x in request.form.get('c2').split(',')]
        T2 = [int(x) for x in request.form.get('c3').split(',')]
        solve.set_coord(T0, T1, T2)
        solve.generate_graph_clean()
    return render_template('index.html', aT1=solve.get_T0, aT2=solve.get_T1, aT3=solve.get_T2,
                           at0="t1", at1="t2", at2="t3")


if __name__ == '__main__':
    T0 = [0, 0, 0]
    T1 = [2300, 1100, 20]
    T2 = [-170, 915, 10]
    t0 = 0
    t1 = 0
    t2 = 0
    solve = ga.Solve(T0, T1, T2, t0, t1, t2)
    solve.generate_graph_clean()
    server.run(debug=True)
