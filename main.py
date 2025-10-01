import numpy as np
temps = np.array([
    [30, 32, 31, 29, 28, 27, 26],   # City A
    [22, 21, 23, 24, 25, 26, 24],   # City B
    [15, 17, 16, 18, 19, 20, 21]    # City C
])
city_A = np.array(temps[0])
city_B = np.array(temps[1])
city_C = np.array(temps[2])
max_A = np.max(city_A)
print(f"Maximum temprature recorded in City A is {max_A}")
day = temps.max(axis=0).argmax()
print(f"Highest temprature was on day, {day + 1}")
if np.average(city_A) > np.average(city_B):
  print("City A has higher temprature")
else:
  print("City B has higher temprature")


# ============================================

