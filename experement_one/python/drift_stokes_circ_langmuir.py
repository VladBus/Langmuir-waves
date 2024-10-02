import numpy as np
import matplotlib.pyplot as plt

# Параметры модели
L = 1000  # Длина области, м
H = 200  # Глубина области, м
Nx = 100  # Число ячеек по оси x
Nz = 20  # Число ячеек по оси z
dx = L / Nx  # Шаг по x
dz = H / Nz  # Шаг по z
dt = 0.01  # Время шага, с
T = 100  # Время моделирования, с
time_steps = int(T / dt)

# Параметры волн Ленгмюра
a = 1  # Амплитуда волны
k = 2 * np.pi / 200  # Волновое число
omega = 2 * np.pi / 10  # Угловая частота
rho = 1025  # Плотность воды, кг/м³

# Инициализация массивов для скорости
u = np.zeros((Nz, Nx))  # Горизонтальная скорость
w = np.zeros((Nz, Nx))  # Вертикальная скорость


# Основная функция дрифта Стокса для вычисления скорости
def stokes_drift(x, z, t):
    return a * k * np.exp(2 * k * z) * np.cos(k * x - omega * t)


# Моделирование циркуляции Ленгмюра
for t in range(time_steps):
    for i in range(Nx):
        for j in range(Nz):
            x = i * dx
            z = -j * dz
            u[j, i] = stokes_drift(x, z, t * dt)

    # Визуализация результатов
    if t % 100 == 0:
        plt.figure(figsize=(10, 5))
        plt.contourf(u, cmap="RdBu", levels=20)
        plt.colorbar(label="Скорость дрифта (м/с)")
        plt.title(f"Циркуляция Ленгмюра, время: {t*dt:.2f} с")
        plt.xlabel("X (м)")
        plt.ylabel("Глубина (м)")
        plt.gca().invert_yaxis()
        plt.show()
