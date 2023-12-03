
class Burger: 
    def __init__(self, ingredients): 
        self.ingredients = ingredients

    def print(self): 
        print(self.ingredients)

    
class BurgerFactory: 

    def createCheeseBurger(self): 
        ingredients = ["bun", "cheese", "beef-patty"]
        return Burger(ingredients)

    def createDeluxCheeseBurger(self): 
        ingredients = ["bun", "tomatoe", "lettuce", "cheese", "beef-patty"]
        return Burger(ingredients)

    def createVeganBurger(self): 
        ingredients = ["bun", "cheese", "veggie-patty"]
        return Burger(ingredients)


    