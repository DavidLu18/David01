import numpy as np
import matplotlib.pyplot as plt

# Hằng số và tham số cho phân phối Maxwell-Boltzmann
k = 1.38e-23  # Hằng số Boltzmann
m = 9.109e-31  # Khối lượng của electron
T = 300  # Nhiệt độ của hơi nhiệt nguyên tử
v_mean = np.sqrt(8*k*T/(np.pi*m))  # Vận tốc trung bình
N = 1000  # Số lượng động học

# Khởi tạo dải giá trị của v
v = np.linspace(0, 5*v_mean, N)

# Tính phân phối Maxwell-Boltzmann
f_MB = 4*np.pi*(m/(2*np.pi*k*T))**(3/2)*v**2*np.exp(-m*v**2/(2*k*T))

# Khởi tạo biểu đồ
fig, ax = plt.subplots()

# Vẽ đường cong biểu diễn phân phối Maxwell-Boltzmann
ax.plot(v, f_MB)

# Tạo chú thích và hiển thị biểu đồ
ax.set_xlabel("v")
ax.set_ylabel("Probability Density")
ax.set_title("Light Transmission in Atomic Vapor (Maxwell-Boltzmann Distribution)")
plt.show()
