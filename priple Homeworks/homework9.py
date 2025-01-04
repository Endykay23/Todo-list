class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needs_maintenance = False
        self.trips_since_maintenance = 0

    def repair(self):
        self.trips_since_maintenance = 0
        self.needs_maintenance = False
        print(f"{self.make} {self.model} has been repaired.")

class Cars(Vehicle):
    def __init__(self, make, model, year, weight):
        super().__init__(make, model, year, weight)
        self.is_driving = False

    def drive(self):
        self.is_driving = True

    def stop(self):
        if self.is_driving:
            self.is_driving = False
            self.trips_since_maintenance += 1
            print(f"{self.make} {self.model} trip count: {self.trips_since_maintenance}")
            if self.trips_since_maintenance > 100:
                self.needs_maintenance = True
                print(f"{self.make} {self.model} needs maintenance.")

class Planes(Vehicle):
    def __init__(self, make, model, year, weight):
        super().__init__(make, model, year, weight)
        self.is_flying = False

    def fly(self):
        if self.needs_maintenance:
            print(f"{self.make} {self.model} can't fly until it's repaired.")
            return False
        else:
            self.is_flying = True
            return True

    def land(self):
        if self.is_flying:
            self.is_flying = False
            self.trips_since_maintenance += 1
            print(f"{self.make} {self.model} trip count: {self.trips_since_maintenance}")
            if self.trips_since_maintenance > 100:
                self.needs_maintenance = True
                print(f"{self.make} {self.model} needs maintenance.")
# Creating 3 different cars
car1 = Cars("Toyota", "Corolla", 2015, 2800)
car2 = Cars("Honda", "Civic", 2018, 2900)
car3 = Cars("Ford", "Mustang", 2020, 3500)

# Driving the cars different numbers of times
for _ in range(50):
    car1.drive()
    car1.stop()

for _ in range(120):
    car2.drive()
    car2.stop()

for _ in range(101):
    car3.drive()
    car3.stop()

# Printing the car details
cars = [car1, car2, car3]
for car in cars:
    print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}, Weight: {car.weight} lbs")
    print(f"Needs Maintenance: {car.needs_maintenance}")
    print(f"Trips Since Maintenance: {car.trips_since_maintenance}\n")

# Creating a Plane
plane = Planes("Boeing", "747", 2010, 80000)

# Flying the plane
for _ in range(101):
    if plane.fly():
        plane.land()

# Attempting another flight after the maintenance threshold
plane.fly()

# Repairing the plane
plane.repair()

# Flying the plane again after repair
plane.fly()
plane.land()
