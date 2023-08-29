import numpy as np


def mesh_function(f, t):
    ft = np.zeros(len(t))
    for i in range(len(t)):
        ft[i] = f(t[i])
    return ft
    pass

def func(t):
    if t >= 0 and t <= 3:
        return(np.exp(-t))
    elif t <= 4 and t > 3:
        return(np.exp(-3*t))
    pass

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)
