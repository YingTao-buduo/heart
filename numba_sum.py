import numba as nb


@nb.jit()
def nb_sum(a):
    n_sum = 0
    for i in range(len(a)):
        n_sum += a[i]
    return n_sum
