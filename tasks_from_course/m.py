class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hello, my name is {self.name}")
human = Person("Jessica")
human.talk()
human = Person("Bob Smith")
human.talk()