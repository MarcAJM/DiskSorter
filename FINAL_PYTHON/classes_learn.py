#imports

class MainClass:
    def __init__(self):
        pass

    def run(self):
        # Instantiate the subclasses
        subclass1 = SubClass1()
        subclass2 = SubClass2()

        # Call methods of the subclasses
        subclass1.method1()
        subclass2.method2()
    
class SubClass1:
    def __init__(self):
        pass

    def method1(self):
        print("This is method 1 of SubClass1")


class SubClass2:
    def __init__(self):
        pass

    def method2(self):
        print("This is method 2 of SubClass2")

if __name__ == "__main__":
    main = MainClass()
    main.run()