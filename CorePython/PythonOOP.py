
def generate_opportunity():
    return {
        "ClientId":  6865358,
        "OpportunityName": "After 5"
    }

opportunity_post_data = []
opportunity_post_data.append(generate_opportunity())
print(opportunity_post_data)


# --------------------------------CLASS---------------------------------------------------------------#

class Cat:
    name = 'Brittany'

    def __init__(self, name, age=5):  # init is called when objects created. set default args.
        self.name = name
        self.age = age

    def info(self):  # all functions in call should have self as first param which rep calling object
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self, sound): # class function will have 1 arg more than caller object methods
        print(sound)


cat1 = Cat('Andy', 2)  # cat1 = Cat() throws error since no args
cat2 = Cat('Phoebe')
print(cat1.info())  # cat1.info is Cat.info(cat1); need self since receiver class shd b explicit
cat2.make_sound("Meow")
del cat2.age    # references can be deleted
print(cat2.name)



