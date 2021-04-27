
def generate_opportunity():
    return {
        "ClientId":  6865358,
        "OpportunityName": "After 5"
    }

opportunity_post_data = []
opportunity_post_data.append(generate_opportunity())
print(opportunity_post_data)

# ACCESSABILITY
# Everything is public in python. The foll are just conventions.
# Method or field starting _  means avoid using it, can change
# __ do not use, use at risk
# --------------------------------CLASS---------------------------------------------------------------#

class Cat:
    name = ''
    __trial = 'AMIT'

    def __init__(self, name, age=5):  # init is constructor. set default args.
        self.name = name
        self.age = age

    @property
    def name(self):
        print('Getter')
        return self.__name

    # __ is calling field behind scenes, note method names same as prop

    @name.setter
    def name(self, value):
        print('Setter')
        # validation for value
        self.__name = value

    def info(self):  # all functions in call should have self as first param which rep calling object
        # also constructor props are available to methods
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self, sound): # class function will have 1 arg more than caller object methods
        print(sound)


class Ragdoll(Cat):
    def __init__(self, name, age, country):
        super().__init__(name, age)
        self.country = country

    def make_sound(self, sound):     # Override
        print("I'm furry")


cat1 = Cat('Andy', 2)  # cat1 = Cat() throws error since no args
cat2 = Cat('Phoebe')
print(cat1.info())  # cat1.info is Cat.info(cat1); need self since receiver class shd b explicit
cat2.make_sound("Meow")
print(cat2.age)
del cat2.age    # references can be deleted
print(cat2.name)
# cat2.__trial can't be accessed ENCAPSULATION
print('------------------------------------INHERITANCE------------------------------------------')
ragdoll = Ragdoll('Jackson', 10, 'Persia')
print(ragdoll.info())
print(ragdoll.make_sound('Purr'))
print(isinstance(ragdoll,Cat))  # ragdoll is instance of Ragdoll hence Cat (IS-A)
