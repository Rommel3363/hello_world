class MyClass:
    def __init__(self,value):
        self.value = value
        print(f"Instance created with value:{self.value}")
    def other_method(self):
        print(f"Other method called with value:{self.value}")

MyClass.other_method()