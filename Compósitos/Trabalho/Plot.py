import matplotlib.pyplot as plt

def plot(Pmax):
    x = []
    y = []
    for i in Pmax:
        x.append(Pmax[i])
        y.append(i)
    plt.plot(x, y)
    plt.show()
