class Computer:
    def __init__(self, computer: str, ram: int, diagonal: int):
        self.computer = computer
        self.ram = ram
        self.diagonal = diagonal
    def value_diagonal(self):
        return f"My diagonal:{self.diagonal} and she is the biggest in the class"
class Tablet:
    def __init__(self,model: str):
        self.model = model
class Mobile_phone(Computer,Tablet):
    def __init__(self,computer: str, ram: int, diagonal: int, ssd: int, model):
        self.ssd = ssd
        super().__init__(computer, ram, diagonal)
        Tablet.__init__(self,model=model)
    def value_diagonal(self):
        return f"My diagonal:{self.diagonal} and she is the smallest in the class"
samsung = Mobile_phone("Samsung", 4, 15, 124, "A51")
print("This is computer:",samsung.computer)
print("This is computer has ram of:",samsung.ram)
print("This is computer has diagonal of:",samsung.diagonal)
print("This is computer has ssd of:",samsung.ssd)
print("This is computer has this model:",samsung.model)
print(samsung.value_diagonal())