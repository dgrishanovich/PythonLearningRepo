import time


class TrafficLight:
    color_rules = {"Red": 3, "Yellow": 2, "Green": 7}
    next_color_map = {"Red": "Yellow", "Yellow": "Green", "Green": "Red"}

    def __init__(self, color):
        self.__color = color

    def running(self, next_color=None):
        sleep_time = self.color_rules[self.__color]
        print(f'Color: {self.__color}, waiting for {sleep_time} seconds...')
        time.sleep(sleep_time)
        if next_color is not None:
            if next_color != self.next_color_map[self.__color]:
                print("Next color is not correct!")
                return
        self.__color = self.next_color_map[self.__color]
        print(f'Next color is: {self.__color}')


t = TrafficLight("Red")
for i in range(10):
    t.running()
t.running("Red")