from abc import ABC


class Clothes(ABC):
    def get_tissue_consumption(self):
        pass

    @property
    def tissue_consumption(self):
        pass


class Suit(Clothes):
    def __init__(self, height):
        self.__height = height

    @property
    def height(self):
        return self.__height

    def get_tissue_consumption(self):
        return 2 * self.__height + 0.3

    @property
    def tissue_consumption(self):
        return self.get_tissue_consumption()


class Coat(Clothes):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def get_tissue_consumption(self):
        return self.__size/6.5 + 0.5

    @property
    def tissue_consumption(self):
        return self.get_tissue_consumption()


size = int(input("Input int size for a coat: "))
coat = Coat(size)
print(f'Tissue consumption for the coat in size {coat.size}: {coat.tissue_consumption}')

height = float(input("Input height for a suit: "))
suit = Suit(height)
print(f'Tissue consumption for the suit with height {suit.height}: {suit.tissue_consumption}')