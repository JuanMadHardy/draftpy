
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        return f"{self.make} {self.model} is starting."

    def stop(self):
        return f"{self.make} {self.model} is stopping."
