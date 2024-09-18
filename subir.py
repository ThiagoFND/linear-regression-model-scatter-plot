import matplotlib.pyplot as plt
import numpy as np

X = np.array([1, 2, 3, 4, 5, 6])
Y = np.array([70, 50, 40, 30, 20, 10])

b = -11.43
a = 76.67

x_values = np.linspace(0, 7, 100)
y_values = a + b * x_values

plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='blue', label='Dados Observados')
plt.plot(x_values, y_values, color='red', label='Reta de Regressão')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Diagrama de Dispersão e Reta de Regressão')
plt.legend()
plt.grid(True)
plt.show()
