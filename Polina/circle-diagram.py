import matplotlib.pyplot as plt


vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]
fig = plt.figure(figsize = (10, 5))

plt.bar(labels, vals)
plt.show()