# Problem Statement : Create a tuple containing six temperature readings: three for Saturday and three for Sunday. Use a for loop to display each reading and calculate the highest and lowest temperatures.


# 6 Temperature Readings in a Tuple

SatTemperatures = (25, 30, 28)

SunTemperatures = (35, 22, 55)

for i in range(len(SatTemperatures)):
    print(f"Saturday Temperature {i+1}: {SatTemperatures[i]}°C")

for i in range(len(SunTemperatures)):
    print(f"Sunday Temperature {i+1}: {SunTemperatures[i]}°C")

highest_temperature = max(max(SatTemperatures), max(SunTemperatures))
print(f"Highest Temperature: {highest_temperature}°C")

lowest_temperature = min(min(SatTemperatures), min(SunTemperatures))
print(f"Lowest Temperature: {lowest_temperature}°C")