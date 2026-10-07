# Lab 1 — Linear Transformations

Applied Linear Algebra, KSE, Autumn 2026/2027.

## Structure
- `lab1_part1.py` — Part 1 (2D): stretch, shear, reflection, rotation + compositions (Tasks 1–2)
- `lab1_part2.py` — Part 2 (3D): rotations of a ModelNet40 model (Tasks 3–4)
- `data/` — ModelNet40 `.off` files (not committed, download from Kaggle; part 2 uses `data/airplane_0001.off`)

## Setup
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python lab1_part1.py
```
The `# %%` markers let VS Code / PyCharm run the file cell by cell, like a notebook.
