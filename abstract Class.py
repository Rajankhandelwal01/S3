from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running")

class Whiteboard:
    def write(self):
        print("its writing")
class Programmer:
    def work(self, com):
        print("Solving Bugs")
        com1.process()
com1 = Laptop()
prog1 = Programmer()
prog1.work(com1)