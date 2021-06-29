import random

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from geneticalgorithm import geneticalgorithm as ga

T0 = [0, 0, 0]
T1 = [2300, 1100, 20]
T2 = [-170, 915, 10]

t0 = 0
t1 = 0
t2 = 0


def calc_dist(p1, p2):
    return np.sqrt(np.power(p1[0] - p2[0], 2) + np.power(p1[1] - p2[1], 2) + np.power(p1[2] - p2[2], 2))


def f(t3):
    t3_t1 = calc_dist(t3, T1) / .34
    t3_t2 = calc_dist(t3, T2) / .34
    t3_t0 = calc_dist(t3, T0) / .34

    delta = np.power(t3_t1 - t3_t0 - t1 + t0, 2) + np.power(t3_t2 - t3_t0 - t2 + t0, 2)
    return delta


def get_coord(x, y, z, opts=None):
    algorithm_param = {'max_num_iteration': None,
                       'population_size': 300,
                       'mutation_probability': 0.15,
                       'elit_ratio': 0.01,
                       'crossover_probability': 0.5,
                       'parents_portion': 0.1,
                       'crossover_type': 'uniform',
                       'max_iteration_without_improv': 120}

    if opts:
        algorithm_param.update(opts)

    model = ga(function=f,
               dimension=3,
               variable_type='int',
               variable_boundaries=np.array([x, y, z]),
               algorithm_parameters=algorithm_param)

    model.run()

    aux = model.best_variable
    if f(model.best_variable) > 0:
        model.run()
        if f(model.best_variable) == 0:
            return model.best_variable
        aux = (aux + model.best_variable) / 2
    return aux


def random_try():
    global t0, t1, t2
    d3 = [random.randint(0, 1000) for _ in range(2)]
    d3.append(random.randint(0, 100))

    random_time = random.randint(0, 110)
    t0 = calc_dist(d3, T0) / .34 + random_time
    t1 = calc_dist(d3, T1) / .34 + random_time
    t2 = calc_dist(d3, T2) / .34 + random_time

    coord = get_coord([0, 1000], [0, 1000], [0, 100])
    return d3


def generate_graph(T3):
    df = pd.DataFrame(np.array([T0, T1, T2, T3]), columns=['x', 'y', 'z'])
    colors = ['blue', 'blue', 'blue', 'red']
    df_lines = pd.DataFrame(np.array([T0, T3, T1, T3, T2, T3]), columns=['x', 'y', 'z'])

    fig = go.Figure(data=[
        go.Scatter3d(
            x=df['x'],
            y=df['y'],
            z=df['z'],
            text=['T0', 'T1', 'T2', 'Ponto Calculado'],
            mode='markers',
            name='Torres',
            marker=dict(
                sizemode='diameter',
                size=[20, 20, 20, 20],
                color=colors,
            )),
        go.Scatter3d(
            x=df_lines['x'],
            y=df_lines['y'],
            z=df_lines['z'],
            mode='lines',
            name='Linhas de ligação',
            marker=dict(
                color='#b6ff63'
            )),
    ])

    fig.update_layout(width=800, height=800,
                      scene=dict(xaxis=dict(title='Coordenada X', titlefont_color='white'),
                                 yaxis=dict(title='Coordenada Y', titlefont_color='white'),
                                 zaxis=dict(title='Coordenada Z', titlefont_color='white'),
                                 bgcolor='black')
                      )
    fig.show()
    fig.write_html('graph.html')


generate_graph(random_try())
