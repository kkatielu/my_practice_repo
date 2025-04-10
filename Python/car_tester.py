from car import Car

cars = []
with open("cars.txt") as file:
    for line in file:
        car_attributes = line.strip().split()
        color, engine_type, gas_tank, odometer = car_attributes
        cars.append(Car(color, engine_type, gas_tank, odometer))

print(cars[0])
cars[0].drive()
print(cars[0].get_gas_tank())
print(cars[0].get_odometer())

print(cars[1])
cars[1].drive()
print(cars[1].get_gas_tank())
print(cars[1].get_odometer())