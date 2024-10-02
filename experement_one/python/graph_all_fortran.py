import numpy as np
import matplotlib.pyplot as plt

# Чтение данных из файла
data = []
file_path = r"E:\\Programming_Work\\VScode_Work\\Langmuir-waves\\experement_one\\fortran\data\\output\\langmuir_data_1.dat"  # Полный путь к файлу

with open(file_path, "r") as f:
    lines = f.readlines()

# Парсинг данных
time_steps = []
current_time = None
current_data = []
for line in lines:
    if "Time" in line:
        if current_data:
            data.append((current_time, np.array(current_data)))
        current_time = float(line.split("=")[1])
        time_steps.append(current_time)
        current_data = []
    else:
        current_data.append([float(x) for x in line.split()])

# Добавление последнего блока данных
if current_data:
    data.append((current_time, np.array(current_data)))

# Параметры
step_interval = 20  # Интервал временных шагов для отображения
max_steps = 6  # Количество временных шагов для отображения
time_indices = list(range(0, min(len(data), max_steps * step_interval), step_interval))

# Визуализация нескольких временных шагов
plt.figure(figsize=(20, 15))
for idx, time_index in enumerate(time_indices):
    time, u_values = data[time_index]

    plt.subplot(len(time_indices), 1, idx + 1)
    plt.contourf(u_values, cmap="RdBu", levels=20)
    plt.colorbar(label="Горизонтальная скорость (м/с)")
    plt.title(f"Циркуляция Ленгмюра на временном шаге: {time:.2f} с")
    plt.xlabel("Горизонтальное положение (X)")
    plt.ylabel("Глубина (Z)")
    plt.gca().invert_yaxis()  # Инверсия оси Z, чтобы 0 был наверху (поверхность воды)

plt.tight_layout()
plt.show()
