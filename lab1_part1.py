# %% [markdown]
# # Lab 1. Linear Transformations — Part 1 (2D)
# Applied Linear Algebra, KSE, Autumn 2026/2027
#
# Rules: only NumPy (matrices) and Matplotlib (plots).
# No ready-made transformation functions from libraries.

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ## Data: KSE Lynx silhouette (from the lab PDF)
# Each row here is a point (x, y). We transpose it so that the matrix has
# 2 rows (x and y) and each column is one point — as in the theory: A @ L = L'.

# %%
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


# %% [markdown]
# ## Helper: draw original vs transformed shape + print the matrix

# %%
def show(original, transformed, matrix, title="Transformation"):
    """Draw the original (grey) and transformed (colored) shapes side by side
    and print the transformation matrix."""
    print(f"{title}\nMatrix:\n{np.round(matrix, 3)}\n")

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    for ax, pts, color, name in [
        (axes[0], original, "grey", "Original"),
        (axes[1], transformed, "tab:blue", title),
    ]:
        ax.fill(pts[0], pts[1], color=color, alpha=0.5, edgecolor="black")
        ax.axhline(0, color="black", linewidth=0.5)
        ax.axvline(0, color="black", linewidth=0.5)
        ax.set_aspect("equal")
        ax.set_xlim(-700, 700)
        ax.set_ylim(-700, 700)
        ax.grid(alpha=0.3)
        ax.set_title(name)
    plt.tight_layout()
    plt.show()


# %% [markdown]
# ## Task 1. Functions for each linear transformation
# Each function:
#   1. copies X (X.copy()),
#   2. builds the 2x2 matrix,
#   3. multiplies matrix @ X,
#   4. returns (result, matrix) — the matrix is needed to print it.

# %%
def stretch(X, a, b):
    """Stretch by a along x and by b along y.  Matrix: [[a, 0], [0, b]]"""
    X = X.copy()
    # TODO: build matrix A
    # TODO: compute result = A @ X
    raise NotImplementedError


def shear(X, a, b):
    """Shear. Matrix: [[1, a], [b, 1]]"""
    X = X.copy()
    # TODO
    raise NotImplementedError


def reflection(X, a, b):
    """Reflection about the line spanned by vector (a, b).
    Matrix: 1/(a^2+b^2) * [[a^2-b^2, 2ab], [2ab, b^2-a^2]]"""
    X = X.copy()
    # TODO
    raise NotImplementedError


def rotation(X, theta):
    """Counterclockwise rotation by theta radians.
    Matrix: [[cos, -sin], [sin, cos]]"""
    X = X.copy()
    # TODO
    raise NotImplementedError


# %% [markdown]
# ## Task 1. Demonstration
# Uncomment after implementing the functions.

# %%
# result, A = stretch(lynx, 1.5, 0.7)
# show(lynx, result, A, "Stretch (1.5, 0.7)")

# result, A = shear(lynx, 0.5, 0)
# show(lynx, result, A, "Shear (0.5, 0)")

# result, A = reflection(lynx, 1, 1)
# show(lynx, result, A, "Reflection (line y = x)")

# result, A = rotation(lynx, np.pi / 4)
# show(lynx, result, A, "Rotation 45°")

# %% [markdown]
# ### Experiments: how matrix elements affect the result
# Try e.g. stretch with a negative value, shear (0, 0.5), rotation -pi/2 ...
# and write a short conclusion for each.

# %%
