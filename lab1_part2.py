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


def read_off(path):
    file = open(path)
    lines = file.readlines()
    file.close()

    if lines[0].strip() == "OFF":
        counts = lines[1].split()
        start = 2
    else:
        counts = lines[0][3:].split()
        start = 1

    n_vertices = int(counts[0])
    n_faces = int(counts[1])

    vertices = []
    for i in range(start, start + n_vertices):
        x, y, z = lines[i].split()
        vertices.append([float(x), float(y), float(z)])

    faces = []
    for i in range(start + n_vertices, start + n_vertices + n_faces):
        numbers = lines[i].split()
        faces.append([int(numbers[1]), int(numbers[2]), int(numbers[3])])

    return np.array(vertices).T, np.array(faces)


PATH = "data/airplane_0001.off"

model, faces = read_off(PATH)

center = model.mean(axis=1)
model[0] = model[0] - center[0]
model[1] = model[1] - center[1]
model[2] = model[2] - center[2]

print("Model shape:", model.shape)


def draw(ax, points, color, title, lim):
    ax.plot_trisurf(points[0], points[1], points[2], triangles=faces, color=color)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_title(title)


def show3d(original, transformed, matrix, title):
    print(title)
    print("Matrix:")
    print(np.round(matrix, 3))
    print()

    lim = max(np.abs(original).max(), np.abs(transformed).max())

    fig = plt.figure(figsize=(12, 6))
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    draw(ax1, original, "grey", "Original", lim)
    draw(ax2, transformed, "tab:blue", title, lim)
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


step1, A1 = rotate_xy(model, np.pi / 4)
step2, A2 = rotate_yz(step1, np.pi / 3)
step3, A3 = rotate_xz(step2, np.pi / 6)

total = multiply(A3, multiply(A2, A1))
show3d(model, step3, total, "xy 45° -> yz 60° -> xz 30°")
