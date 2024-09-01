import numpy as np
from matplotlib import pyplot as plt


def H(ang: float, dx: int, dy: int) -> np.array:
    return np.array([
        [np.cos(ang), -np.sin(ang), dx],
        [np.sin(ang), np.cos(ang), dy],
        [0, 0, 1],
    ])


a1 = np.pi / 6 # First angle rotation
a2 = -np.pi / 3 # Second angle rotation
a3 = -np.pi / 4 # Third angle rotation
l1 = 3 # first link length
l2 = 2 # second link length

plt.figure(figsize=(6, 6))

# x-lim and y-lim
lim = [-2, 6]
plt.xlim(*lim) 
plt.ylim(*lim)
plt.grid() # grid on the plot


def solution(a1, a2, a3, l1, l2):
    O = np.array([0, 0]) # start point

    H1 = H(a1, 0, 0)
    H2 = H(a2, l1, 0)
    H3 = H(a3, l2, 0)

    H12 = np.matmul(H1, H2)
    H123 = np.matmul(H12, H3)


    # Draw solution
    plt.quiver(*O, *H123[:2, 2], color='c', scale_units='xy', angles='xy', scale=1) # FK solution

    # Creating plot 
    plt.quiver(*O, *(l1 * H1[:2,0]), color='r', scale_units='xy', angles='xy', scale=1) # first link
    plt.quiver(*H12[:2, 2], *(l2 * H12[:2,0]), color='g', scale_units='xy', angles='xy', scale=1) # second link


    plt.quiver(*np.array([O, O]).T, *H1[:2, :2], color='k', scale_units='xy', angles='xy', scale=1) # base frame
    plt.quiver(*np.array([H12[:2, 2], H12[:2, 2]]).T, *H12[:2, :2], color='k', scale_units='xy', angles='xy', scale=1) # second frame
    plt.quiver(*np.array([H123[:2, 2], H123[:2, 2]]).T, *H123[:2, :2], color='k', scale_units='xy', scale=1) # third frame

    plt.scatter(*np.array([O, H12[:2, 2], H123[:2, 2]]).T, c=['r', 'g', 'b'])




plt.show()