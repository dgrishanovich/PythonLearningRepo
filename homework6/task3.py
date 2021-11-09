class Worker:
    def __init__(self, name, surname, position, income):
        self._name = name
        self._surname = surname
        self.__position = position
        self._income = income   # {"wage": wage, "bonus": bonus}

    def get_position(self):
        return self.__position


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return " ".join([self._name, self._surname])

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker_name = input("Input name: ")
worker_surname = input("Input surname: ")
worker_position = input("Input position: ")
worker_wage = int(input("Input wage: "))
worker_bonus = int(input("Input bonus: "))
pos = Position(worker_name, worker_surname, worker_position, {"wage": worker_wage, "bonus": worker_bonus})
print(f'Full name is: {pos.get_full_name()}')
print(f'Position of the worker is: {pos.get_position()}')
print(f'Total income is: {pos.get_total_income()}')