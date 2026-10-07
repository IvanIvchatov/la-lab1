


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
]).T  # shape (2, 74): row 0 = x, row 1 = y

print("Lynx shape:", lynx.shape)

def show(original, transformed, matrix, title="Transformation"):
    print(f"{title}\nMatrix:\n{np.round(matrix, 3)}\n")

    # axis limits big enough for both shapes
    lim = max(np.abs(original).max(), np.abs(transformed).max()) * 1.1

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    for ax, pts, color, name in [
        (axes[0], original, "grey", "Original"),
        (axes[1], transformed, "tab:blue", title),
    ]:
        ax.fill(pts[0], pts[1], color=color, alpha=0.5, edgecolor="black")
        ax.axhline(0, color="black", linewidth=0.5)
        ax.axvline(0, color="black", linewidth=0.5)
        ax.set_aspect("equal")
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.grid(alpha=0.3)
        ax.set_title(name)
    plt.tight_layout()
    plt.show()


def stretch(X, a, b):
    X = X.copy()
    A = np.array([[a, 0],
                  [0, b]])
    result = A @ X
    return result, A


def shear(X, a, b):
    X = X.copy()
    A = np.array([[1, a],
                  [b, 1]])
    result = A @ X
    return result, A


def reflection(X, a, b):
    X = X.copy()
    A = np.array([[a**2 - b**2, 2 * a * b],
                  [2 * a * b, b**2 - a**2]]) / (a**2 + b**2)
    result = A @ X
    return result, A


def rotation(X, theta):
    X = X.copy()
    A = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    result = A @ X
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


# %% [markdown]
# ## Task 2. Combination of Stretch, Shear and Rotation in different orders

# %%
def apply_in_order(X, order):
    current = X.copy()
    total = np.eye(2)

    for name in order:
        if name == "stretch":
            new, A = stretch(current, 1.5, 0.7)
        elif name == "shear":
            new, A = shear(current, 0.5, 0)
        elif name == "rotation":
            new, A = rotation(current, np.pi / 4)

        show(current, new, A, f"Step: {name}")
        total = A @ total
        current = new

    show(X, current, total, "Combined: " + " -> ".join(order))


# %%
apply_in_order(lynx, ["stretch", "shear", "rotation"])
apply_in_order(lynx, ["rotation", "shear", "stretch"])
apply_in_order(lynx, ["shear", "rotation", "stretch"])
apply_in_order(lynx, ["stretch", "rotation", "shear"])

# %% [markdown]
# ### Conclusion
# Yes, the final result depends on the order: the same three matrices give
# different combined matrices and different pictures, because matrix
# multiplication is not commutative (A @ B != B @ A).
