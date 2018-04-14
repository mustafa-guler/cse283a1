import matplotlib.pyplot as plt
import numpy as np

with open("./q2.dat") as f:
    data = [int(x.strip()) for x in f]

#data.sort()
#data, counts = np.unique(data, return_counts=True)

plt.hist(data, normed=True)
plt.title("Haplotype Counts for Different Variants Covered")
plt.xlabel("Number of Variants Covered")
plt.ylabel("Number of Haplotypes")
plt.show()
