'''
class that can only have a single instance of it thats instantiated 
'''


class ApplicationState: 
    instance = None 

    def __init__(self): 
        self.isLoggedIn = False

    @staticmethod
    def getAppState(): 
        if not ApplicationState.instance: 
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance


appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn) # False

appState2 = ApplicationState.getAppState() # same instance as appState1

appState1.isLoggedIn = True 


print(appState1.isLoggedIn) # True
print(appState2.isLoggedIn) # True

print("\n\n")
print(appState1 is appState2) # True 