import numpy as np

w = np.linspace(0.1, 10, 495)

with open("test.txt", "w") as f:
    for k in range(len(w)):
        f.write(f"{w[k]}\n")
