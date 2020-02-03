import matplotlib.pyplot as plt
import numpy as np

Q1 = 1000
mu, sigma = Q1/4, 100.5 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
print("s == " + str(s))
print("s[1] == " + str(s[1]))
print("s[2] == " + str(s[2]))
print("s[3] == " + str(s[3]))

count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
         np.exp(- (bins - mu)**2 / (2 * sigma**2)),
         linewidth=2, color='r')
plt.show()
