import numpy as np
import matplotlib.pyplot as plt

N = 10

# construct gray codes
a = np.arange(2<<(N-1), dtype=np.uint64)
gray = a ^ (a>>1)
gray = np.append(np.repeat(gray, 5), 0).astype(np.uint64)

t = np.linspace(0, 2*np.pi, gray.size)

plt.figure(figsize=(12,12))

for n in range(N):
    # pick n-th bits from gray codes
    g = (gray>>n) & 1
    r = N + (g-0.5) * n

    plt.plot(r*np.cos(t), r*np.sin(t))

plt.legend(range(N))
plt.title("N=%d"%N)

# plt.show()
plt.savefig("./N-%d.png"%N)

