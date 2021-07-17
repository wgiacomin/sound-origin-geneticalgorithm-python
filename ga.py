import random

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from geneticalgorithm import geneticalgorithm as ga


class Solve:
    def __init__(self, T0, T1, T2, t0, t1, t2):
        self.T0 = T0
        self.T1 = T1
        self.T2 = T2
        self.t0 = t0
        self.t1 = t1
        self.t2 = t2
        self.T3 = None
        self.random = None

    @staticmethod
    def calc_dist(p1, p2):
        return np.sqrt(np.power(p1[0] - p2[0], 2) + np.power(p1[1] - p2[1], 2) + np.power(p1[2] - p2[2], 2))

    def f(self, t3):
        t3_t1 = self.calc_dist(t3, self.T1) / .34
        t3_t2 = self.calc_dist(t3, self.T2) / .34
        t3_t0 = self.calc_dist(t3, self.T0) / .34

        delta = np.power(t3_t1 - t3_t0 - self.t1 + self.t0, 2) + np.power(t3_t2 - t3_t0 - self.t2 + self.t0, 2)
        return delta

    def get_coord(self, x, y, z, opts=None):
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

        model = ga(function=self.f,
                   dimension=3,
                   variable_type='int',
                   variable_boundaries=np.array([x, y, z]),
                   algorithm_parameters=algorithm_param)

        model.run()

        aux = model.best_variable
        if self.f(model.best_variable) > 0:
            model.run()
            if self.f(model.best_variable) == 0:
                self.T3 = aux
                return model.best_variable
            aux = (aux + model.best_variable) / 2
        self.T3 = aux
        return aux

    def random_try(self):
        d3 = [random.randint(0, 1000) for _ in range(2)]
        d3.append(random.randint(0, 100))
        self.random = d3
        random_time = random.randint(0, 110)
        self.t0 = self.calc_dist(d3, self.T0) / .34 + random_time
        self.t1 = self.calc_dist(d3, self.T1) / .34 + random_time
        self.t2 = self.calc_dist(d3, self.T2) / .34 + random_time

        coord = self.get_coord([0, 1000], [0, 1000], [0, 100])
        return coord

    def generate_graph(self, T3):
        df = pd.DataFrame(np.array([self.T0, self.T1, self.T2, T3]), columns=['x', 'y', 'z'])
        colors = ['blue', 'blue', 'blue', 'red']
        df_lines = pd.DataFrame(np.array([self.T0, T3, self.T1, T3, self.T2, T3]), columns=['x', 'y', 'z'])

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

        fig.update_layout(width=600, height=600,
                          scene=dict(xaxis=dict(title='Coordenada X', titlefont_color='black'),
                                     yaxis=dict(title='Coordenada Y', titlefont_color='black'),
                                     zaxis=dict(title='Coordenada Z', titlefont_color='black'),
                                     bgcolor='#f4f4f4')
                          )
        # fig.show()
        fig.write_html(r'.\templates\graph.html', include_plotlyjs='cdn')

    def generate_graph_clean(self):
        df = pd.DataFrame(np.array([self.T0, self.T1, self.T2]), columns=['x', 'y', 'z'])

        colors = ['blue', 'blue', 'blue', 'red']

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
                ))
        ])

        fig.update_layout(width=600, height=600,
                          scene=dict(xaxis=dict(title='Coordenada X', titlefont_color='black'),
                                     yaxis=dict(title='Coordenada Y', titlefont_color='black'),
                                     zaxis=dict(title='Coordenada Z', titlefont_color='black'),
                                     bgcolor='#f4f4f4')
                          )
        # fig.show()
        fig.write_html(r'.\templates\graph.html', include_plotlyjs='cdn')

    def set_coord(self, T0, T1, T2):
        self.T0 = T0
        self.T1 = T1
        self.T2 = T2

    def calc(self, z, x, y):
        self.t0 = z
        self.t1 = x
        self.t2 = y
        m = 10000
        self.generate_graph(self.get_coord([-m, m], [-m, m], [-m, m]))

    @property
    def get_T0(self):
        return f"{self.T0[0]},{self.T0[1]},{self.T0[2]}"

    @property
    def get_T1(self):
        return f"{self.T1[0]},{self.T1[1]},{self.T1[2]}"

    @property
    def get_T2(self):
        return f"{self.T2[0]},{self.T2[1]},{self.T2[2]}"

    @property
    def get_t0(self):
        return f"{self.t0:.2f}"

    @property
    def get_t1(self):
        return f"{self.t1:.2f}"

    @property
    def get_t2(self):
        return f"{self.t2:.2f}"

    @property
    def get_random(self):
        if self.random is not None:
            return f"{self.random[0]},{self.random[1]},{self.random[2]}"
        return ""

    @property
    def get_delta(self):
        if self.T3 is not None:
            return self.f(self.T3)
        return ""
