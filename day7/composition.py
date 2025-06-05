# Aggregation = A relationship where one object contains references to other INDEPENDANT obkects
#               "has-a" relationship

# Composition = The composed object directly owns its components, which DEPENDS on it
#               "owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size =size

class Car:
    def __init__(self, make, model, engine_horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(engine_horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def car_spec(self):
        return f"{self.make} {self.model} {self.engine.horse_power} (hp) {self.wheels[0].size} inch wheels"

mustang = Car(make="Ford", model="Mustang", engine_horse_power=326, wheel_size=19)
corvette = Car("Chevrolet", "Corvette", 450, 21)

print(mustang.car_spec())
print(corvette.car_spec())
