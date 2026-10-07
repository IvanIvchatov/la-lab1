import numpy as np
import matplotlib.pyplot as plt


lynx = np.array([
    [209.70, 368.42], [157.63, 332.16], [118.82, 284.21], [80.95, 224.56], [43.08, 244.44],
    [20.36, 266.67], [-4.26, 293.57], [2.37, 263.16], [-20.36, 292.40], [-39.29, 299.42],
    [-21.30, 259.65], [-50.65, 267.84], [-39.29, 242.11], [-55.38, 240.94], [-100.83, 300.58],
    [-149.11, 345.03], [-172.78, 361.40], [-189.82, 300.58], [-192.66, 225.73], [-181.30, 145.03],
    [-168.05, 104.09], [-184.14, 66.67], [-186.98, 31.58], [-183.20, 3.51], [-208.76, -4.68],
    [-197.40, -29.24], [-182.25, -44.44], [-203.08, -43.27], [-172.78, -92.40], [-131.12, -126.32],
    [-101.78, -147.37], [-74.32, -163.74], [-110.30, -224.56], [-143.43, -287.72], [-161.42, -240.94],
    [-282.60, -221.05], [-388.64, -205.85], [-370.65, -301.75], [-339.41, -397.66], [18.46, -397.66],
    [345.09, -400.00], [359.29, -378.95], [367.81, -342.69], [346.98, -362.57], [363.08, -302.92],
    [357.40, -243.27], [348.88, -266.67], [336.57, -201.17], [290.18, -135.67], [240.00, -118.13],
    [258.93, -164.91], [257.99, -228.07], [252.31, -271.35], [256.09, -333.33], [247.57, -359.06],
    [230.53, -307.60], [194.56, -238.60], [160.47, -181.29], [120.71, -149.71], [165.21, -132.16],
    [201.18, -100.58], [183.20, -99.42], [221.07, -73.68], [253.25, -24.56], [222.01, -23.39],
    [251.36, -1.17], [262.72, 24.56], [234.32, 25.73], [214.44, 42.11], [202.13, 60.82],
    [220.12, 101.75], [234.32, 160.23], [240.00, 230.41], [232.43, 316.96],
]).T

print("Lynx shape:", lynx.shape)


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


def draw(ax, points, title, lim):
    ax.fill(points[0], points[1], alpha=0.5, edgecolor="black")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    ax.set_title(title)


def show(original, transformed, matrix, title):
    print(title)
    print(np.round(matrix, 3))
    print()

    lim = max(np.abs(original).max(), np.abs(transformed).max()) * 1.1

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    draw(ax1, original, "Original", lim)
    draw(ax2, transformed, title, lim)
    plt.show()


def stretch(X, a, b):
    X = X.copy()

    A = np.array([[a, 0],
                  [0, b]])

    result = multiply(A, X)
    return result, A


def shear(X, a, b):
    X = X.copy()

    A = np.array([[1, a],
                  [b, 1]])

    result = multiply(A, X)
    return result, A


def reflection(X, a, b):
    X = X.copy()

    length_squared = a**2 + b**2
    m11 = (a**2 - b**2) / length_squared
    m12 = (2 * a * b) / length_squared
    m22 = (b**2 - a**2) / length_squared

    A = np.array([[m11, m12],
                  [m12, m22]])

    result = multiply(A, X)
    return result, A


def rotation(X, theta):
    X = X.copy()

    c = np.cos(theta)
    s = np.sin(theta)

    A = np.array([[c, -s],
                  [s, c]])

    result = multiply(A, X)
    return result, A


result, A = stretch(lynx, 1.5, 0.7)
show(lynx, result, A, "Stretch (1.5, 0.7)")

result, A = shear(lynx, 0.5, 0)
show(lynx, result, A, "Shear (0.5, 0)")

result, A = reflection(lynx, 1, 1)
show(lynx, result, A, "Reflection (line y = x)")

result, A = rotation(lynx, np.pi / 4)
show(lynx, result, A, "Rotation 45°")

result, A = stretch(lynx, -1, 1)
show(lynx, result, A, "Stretch (-1, 1): flip left-right")

result, A = stretch(lynx, 0.5, 1.5)
show(lynx, result, A, "Stretch (0.5, 1.5)")

result, A = stretch(lynx, 1, 0)
show(lynx, result, A, "Stretch (1, 0): collapse onto x-axis")


result, A = shear(lynx, 0, 0.5)
show(lynx, result, A, "Shear (0, 0.5): vertical")

result, A = shear(lynx, -0.5, 0)
show(lynx, result, A, "Shear (-0.5, 0): horizontal, other way")

result, A = shear(lynx, 0.5, 0.5)
show(lynx, result, A, "Shear (0.5, 0.5): both directions")

result, A = reflection(lynx, 1, 0)
show(lynx, result, A, "Reflection (x-axis)")

result, A = reflection(lynx, 0, 1)
show(lynx, result, A, "Reflection (y-axis)")

result, A = reflection(lynx, 1, -1)
show(lynx, result, A, "Reflection (line y = -x)")

result, A = rotation(lynx, -np.pi / 2)
show(lynx, result, A, "Rotation -90°")

result, A = rotation(lynx, np.pi)
show(lynx, result, A, "Rotation 180°")

result, A = rotation(lynx, np.pi / 6)
show(lynx, result, A, "Rotation 30°")


# Висновок до Task 1:
# Stretch: числа на діагоналі розтягують або стискають фігуру вздовж осей.
# Більше 1 - розтягує, менше 1 - стискає, мінус - віддзеркалює, нуль - сплющує в лінію.
# Shear: числа поза діагоналлю перекошують фігуру, як колоду карт.
# Чим більше число, тим сильніший нахил, мінус - нахил в інший бік.
# Reflection: фігура віддзеркалюється відносно прямої, розмір не змінюється.
# Rotation: фігура повертається навколо центру, форма і розмір ті самі.
# Додатний кут - проти годинникової стрілки, від'ємний - за нею.


step1, A1 = stretch(lynx, 1.5, 0.7)
show(lynx, step1, A1, "Step 1: stretch")
step2, A2 = shear(step1, 0.5, 0)
show(step1, step2, A2, "Step 2: shear")
step3, A3 = rotation(step2, np.pi / 4)
show(step2, step3, A3, "Step 3: rotation")
total = multiply(A3, multiply(A2, A1))
show(lynx, step3, total, "Combined: stretch -> shear -> rotation")


step1, A1 = rotation(lynx, np.pi / 4)
show(lynx, step1, A1, "Step 1: rotation")
step2, A2 = shear(step1, 0.5, 0)
show(step1, step2, A2, "Step 2: shear")
step3, A3 = stretch(step2, 1.5, 0.7)
show(step2, step3, A3, "Step 3: stretch")
total = multiply(A3, multiply(A2, A1))
show(lynx, step3, total, "Combined: rotation -> shear -> stretch")


step1, A1 = shear(lynx, 0.5, 0)
show(lynx, step1, A1, "Step 1: shear")
step2, A2 = rotation(step1, np.pi / 4)
show(step1, step2, A2, "Step 2: rotation")
step3, A3 = stretch(step2, 1.5, 0.7)
show(step2, step3, A3, "Step 3: stretch")
total = multiply(A3, multiply(A2, A1))
show(lynx, step3, total, "Combined: shear -> rotation -> stretch")


step1, A1 = stretch(lynx, 1.5, 0.7)
show(lynx, step1, A1, "Step 1: stretch")
step2, A2 = rotation(step1, np.pi / 4)
show(step1, step2, A2, "Step 2: rotation")
step3, A3 = shear(step2, 0.5, 0)
show(step2, step3, A3, "Step 3: shear")
total = multiply(A3, multiply(A2, A1))
show(lynx, step3, total, "Combined: stretch -> rotation -> shear")


# Висновок до Task 2:
# Так, результат залежить від порядку. Перетворення ті самі, а рисі вийшли різні,
# бо при множенні матриць порядок важливий: A * B != B * A.
# Площа рисі змінилась однаково в усіх варіантах, бо визначник завжди 1.05.
