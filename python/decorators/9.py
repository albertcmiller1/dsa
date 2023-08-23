from datetime import datetime
from functools import wraps

class Initial: 
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print(f"initializing Initial class")

class Write: 
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print(f"initializing Write class")

class Poll: 
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print(f"initializing Poll class")


class Transition: 
    def __init__(self, name):
        self.name = name
        print(f"initializing: {self.name} <- is a string")
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            publisher = args[0]
            
            # print(publisher.msg)
            # print(args)             # (<__main__.Publisher object at 0x1045b3970>, 'fee', 'fi')
            # print(kwargs)           # {'fo': 'fo', 'fum': 'fum'}
            # print(self.name)        # Initial, a string

            # how does self.name get set? 
            publisher.current_state = globals()[self.name](*args[1:], **kwargs)
            return func(*args, **kwargs)

        return wrapper



class Publisher: 
    def __init__(self): 
        print("Initializing Publisher class")
        self.msg = "im a cool publisher class"
        self.start_time = datetime.now()
        self.current_state = None

    @Transition(name="Initial")
    def start(self, fee, fi, fo, fum):
        print(f"im the start function from the publisher class.")

    @Transition(name="Write")
    def write(self, fee, fi, fo, fum):
        print("im the writing function from the publisher class")

    @Transition(name="Polll")
    def poll(self, fee, fi, fo, fum):
        print("im the polling function from the publisher class")


# print(globals())
p = Publisher()
print("\n")
p.start("fee", "fi", fo="fo", fum="fum")
# print(p.current_state)
print(p.current_state.args)
# print(p.current_state.kwargs)
p.write("one", "two", fo="three", fum="four")
print(p.current_state.args)


if isinstance(p.current_state, Initial):
    print("p object is in current state mode")
else: 
    print("p object is NOT in current state mode")