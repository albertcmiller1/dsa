from datetime import datetime
from functools import wraps
import pprint

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
            
            print("the transition wrapper is getting called now.")
            # print(publisher.msg)
            # print(args)             # (<__main__.Publisher object at 0x1045b3970>, 'fee', 'fi')
            # print(kwargs)           # {'fo': 'fo', 'fum': 'fum'}
            # print(self.name)        # Initial, a string

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


p = Publisher() # the decorators will get initialized first, the the publisher __init__ will then get initialized 
# print(f"\nglobals: ")
# pprint.pprint(globals())
# print("\n")

p.start("fee", "fi", fo="fo", fum="fum")


# p.write("one", "two", fo="three", fum="four")
# print(p.current_state.args)

print("\n")
if isinstance(p.current_state, Initial):
    print("p.current_state object is of type Initial")
    print(p.current_state)
    print(f"p.current_state class attributes: {p.current_state.args} + {p.current_state.kwargs}")
    print(isinstance(p.current_state, Initial))
    print(isinstance(p, Publisher))
    print(globals()['Initial'])
    print(p.current_state.args)
    print(p.current_state.kwargs)
else: 
    print(f"p object is NOT in current state mode. Current state: {p.current_state}")


# print(f"\nglobals: ")
# pprint.pprint(globals())
# print("\n")