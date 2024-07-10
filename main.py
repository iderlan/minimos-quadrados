import numpy as np
import matplotlib.pyplot as plt

def plot_interpolated_line(x, y):
    # Cálculo dos coeficientes da reta de mínimos quadrados
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]

    # Plotagem dos pontos originais
    plt.scatter(x, y, color='red', label='Pontos Originais')

    # Plotagem da reta interpolada
    plt.plot(x, m * x + c, color='blue', label='Reta de Mínimos Quadrados')

    # Configuração do gráfico
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    # Exibição do gráfico
    plt.show()

# Exemplo de pontos para interpolação
x = np.array([1, 2, 3, 4, 5])
y = np.array([3.5, 3.5, 4, 4, 3.5])

# Chamar a função para traçar a reta interpolada
plot_interpolated_line(x, y)