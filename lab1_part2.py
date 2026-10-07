import os
import numpy as np
import matplotlib.pyplot as plt


def multiply(A, B):
    rows = A.shape[0]
    cols = B.shape[1]
    inner = A.shape[1]

    result = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            total = 0
            for k in range(inner):
                total = total + A[i][k] * B[k][j]
            result[i][j] = total
    return result


def read_points(path):
    file = open(path)
    lines = file.readlines()
    file.close()

    n = int(lines[1].split()[0])

    points = []
    for i in range(2, 2 + n):
        x, y, z = lines[i].split()
        points.append([float(x), float(y), float(z)])

    return np.array(points).T


PATH = os.path.join(os.path.dirname(__file__), "plane", "airplane_0001.off")
model = read_points(PATH)
print("Model shape:", model.shape)


def draw(ax, points, title, lim):
    ax.scatter(points[0], points[1], points[2], s=0.1)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(title)


def show3d(original, transformed, matrix, title):
    print(title)
    print(np.round(matrix, 3))
    print()

    lim = max(np.abs(original).max(), np.abs(transformed).max())

    fig = plt.figure(figsize=(12, 6))
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    draw(ax1, original, "Original", lim)
    draw(ax2, transformed, title, lim)
    plt.show()


def rotate_xy(X, theta):
    X = X.copy()

    c = np.cos(theta)
    s = np.sin(theta)

    A = np.array([[c, -s, 0],
                  [s, c, 0],
                  [0, 0, 1]])

    result = multiply(A, X)
    return result, A


def rotate_yz(X, theta):
    X = X.copy()

    c = np.cos(theta)
    s = np.sin(theta)

    A = np.array([[1, 0, 0],
                  [0, c, -s],
                  [0, s, c]])

    result = multiply(A, X)
    return result, A


def rotate_xz(X, theta):
    X = X.copy()

    c = np.cos(theta)
    s = np.sin(theta)

    A = np.array([[c, 0, s],
                  [0, 1, 0],
                  [-s, 0, c]])

    result = multiply(A, X)
    return result, A


result, A = rotate_xy(model, np.pi / 2)
show3d(model, result, A, "Rotation in xy plane, 90°")

result, A = rotate_yz(model, np.pi / 2)
show3d(model, result, A, "Rotation in yz plane, 90°")

result, A = rotate_xz(model, np.pi / 2)
show3d(model, result, A, "Rotation in xz plane, 90°")


# Висновок до Task 3:
# У 3D можна крутити в трьох площинах: xy, yz і xz.
# При кожному повороті одна координата не змінюється (z, x або y).
# Модель тільки крутиться, форма і розмір ті самі.


step1, A1 = rotate_xy(model, np.pi / 4)
step2, A2 = rotate_yz(step1, np.pi / 3)
step3, A3 = rotate_xz(step2, np.pi / 6)

total = multiply(A3, multiply(A2, A1))
show3d(model, step3, total, "xy 45° -> yz 60° -> xz 30°")


# Висновок до Task 4:
# Три повороти можна склеїти в одну матрицю, якщо їх перемножити.
# Літак став в нове положення, але сам не змінився.
# Якщо змінити порядок поворотів, літак стане в інше положення.
