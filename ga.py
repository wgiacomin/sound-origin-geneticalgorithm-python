import random

import numpy as np
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
                       'population_size': 200,
                       'mutation_probability': 0.15,
                       'elit_ratio': 0.01,
                       'crossover_probability': 0.5,
                       'parents_portion': 0.1,
                       'crossover_type': 'uniform',
                       'max_iteration_without_improv': 200}

    if opts:
        algorithm_param.update(opts)

    model = ga(function=f,
               dimension=3,
               variable_type='int',
               variable_boundaries=np.array([x, y, z]),
               algorithm_parameters=algorithm_param)

    model.run()
    return model.best_variable


def random_try():
    global t0, t1, t2
    d3 = [random.randint(0, 1000) for _ in range(2)]
    d3.append(random.randint(0, 100))

    random_time = random.randint(0, 110)
    t0 = calc_dist(d3, T0) / .34 + random_time
    t1 = calc_dist(d3, T1) / .34 + random_time
    t2 = calc_dist(d3, T2) / .34 + random_time

    coord = get_coord([0, 1000], [0, 1000], [0, 100])
    print('\n')
    print(coord)
    print(d3)
    print(f(coord))
    return calc_dist(d3, coord)


random_try()
