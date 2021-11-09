class Road:
    depth = 5   # initial coverage depth (in sm)
    mass_per_sq_m = 25  # initial mass per square meter (in kg)

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_count(self):
        return (self._width * self._length * self.depth * self.mass_per_sq_m)/1000


road_length = int(input("Input road length (in meters): "))
road_width = int(input("Input road width (in meters): "))
road = Road(road_length, road_width)
mass = road.mass_count()
print(f'Mass of asphalt = {mass} t')