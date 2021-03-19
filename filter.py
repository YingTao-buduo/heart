import numpy as np


def median_average(inputs, per):
    if np.shape(inputs)[0] % per != 0:
        length = np.shape(inputs)[0] / per
        for x in range(int(np.shape(inputs)[0]), int(length + 1) * per):
            inputs = np.append(inputs, inputs[np.shape(inputs)[0] - 1])
    inputs = np.array(inputs).reshape(-1, per)
    mean = []
    for tmp in inputs:
        tmp = np.delete(tmp, np.where(tmp == tmp.max())[0], axis=0)
        tmp = np.delete(tmp, np.where(tmp == tmp.min())[0], axis=0)
        mean.append(tmp.mean())
    return np.array(mean)