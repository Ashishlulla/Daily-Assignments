
class Greeter:
    visitor1 = ""
    def __init__(self, boss):
        self.boss = boss
    
    def enters(self,visitor):
        Greeter.visitor1 = visitor 
    
    def greet(self):
        return f"Welcome,{Greeter.visitor1}"


if __name__ == "__main__":
    g = Greeter('Chuck')
    g.enters("John")
    print(g.greet())
