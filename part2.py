class Tissue:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_s(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Total fabric area: {(coat.width / 6.5 + 0.5) + (suit.height * 2 + 0.3)}')


class Coat(Tissue):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Area on coat {self.square_c}'


class Suit(Tissue):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Area on suit {self.square_j}'


coat = Coat(2, 4)
suit = Suit(1, 2)
print(f"{coat} ({suit.get_square_c()})")
print(f"{suit} ({suit.get_square_s()})")
print(coat.get_sq_full)
