import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def derive(my_list, d_x=0.2):
    d_y = []
    
    for i in range(len(my_list) - 1):
        d_y.append((my_list[i + 1] - my_list[i]) / d_x)
    
    return d_y


def gen_x_vals(my_list):
    X = [-5 + 0.2 * x for x in range(len(my_list))]
    return X


def draw_plot(x_cord_1, y_cord_1, x_cord_2, y_cord_2):
    plt.plot(x_cord_1, y_cord_1)
    plt.plot(x_cord_2, y_cord_2)
    plt.legend(['f\'(x)', 'f\'\'(x)'])
    plt.show()


if __name__ == '__main__':
    X = np.arange(-5, 5, 0.2)
    y = [sigmoid(x) for x in X]
    y_1 = derive(y)
    y_2 = derive(y_1)
    x_1 = gen_x_vals(y_1)
    x_2 = gen_x_vals(y_2)
    draw_plot(x_1, y_1, x_2, y_2)

