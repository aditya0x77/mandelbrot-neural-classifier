# 🌀 MandelNet — Neural Network Learns the Mandelbrot Set

A TensorFlow-based neural network that learns to classify whether a given complex coordinate lies **inside** the Mandelbrot set or not and visualizes its learning process epoch by epoch.

---

## 🎥 Demo

Watch the model *learn* the Mandelbrot fractal over time:

> *(insert your training video or GIF below)*  
> ![Mandelbrot Learning Animation](images/demo.gif)

---

## 🧠 Concept

The Mandelbrot set is defined by all complex numbers `c` for which the iteration:

\[
z_{n+1} = z_n^2 + c
\]

does **not** diverge after a large number of steps.

This project teaches a **deep neural network** to approximate that boundary directly from data — no iterative escape-time algorithm used at inference!

---

## 🧩 How It Works

1. A dataset of 2D coordinates (`x`, `y`) is generated with escape counts.
2. Points that never escape (e.g. `esc == 1000`) are labeled `1`, others `0`.
3. A deep fully-connected neural network learns to classify them.
4. After every training epoch, the model predicts across a grid of coordinates.
5. The visualization callback saves the model’s evolving “understanding” of the fractal.

---

## 🧱 Architecture

| Layer | Type | Units | Activation |
|-------|------|--------|-------------|
| 1 | Input | 2 | — |
| 2–21 | Dense | 200 | ReLU |
| 22 | Dense | 1 | Sigmoid |

> You can easily adjust the depth and width — even a 3–4 layer network can capture the structure surprisingly well.

---

## 🖼️ Visualization Example

Each image below is generated automatically during training via a custom Keras callback:

| Epoch 1 | Epoch 10 | Epoch 50 | Epoch 200 |
|----------|-----------|-----------|------------|
| ![E1](images2/1.png) | ![E10](images2/10.png) | ![E50](images2/50.png) | ![E200](images2/200.png) |

---

## 🧰 Requirements

- Python 3.9+
- TensorFlow
- NumPy
- Matplotlib
- Pandas

Install dependencies:

```bash
pip install tensorflow numpy matplotlib pandas
