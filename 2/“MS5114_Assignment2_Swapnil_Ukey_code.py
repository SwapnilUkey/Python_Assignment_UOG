# Name - Swapnil Haripal Ukey
# Module Code : 2223-MS5114 Advanced Programming for Business Analytics
# Student ID - 22220959

# Expected knowledge to resolve the assignment:
#   1. Objected oriented programming in Python
#   2. Classes
#   3. Composition
#   4. Inheritance
#   5. Polymorphism

#####################################################################################################################
#####################################################################################################################

# 1. Implement a class named "MyClass"
# This class should have:
# * During instantiation of this class, the 'some_val' parameter should be set as
#   a variable with the same name in the instance
# * Implement the method called 'plus_n' that takes one parameter (named 'n'), such that
#   it should return the sum of instance's 'some_val' variable and 'n'
class MyClass:
    def __init__(self, some_val):
        self.some_val = some_val

    def plus_n(self, n):
        return self.some_val + n

#####################################################################################################################
#####################################################################################################################

# 2. Given two classes 'Animal' and 'DigestiveSystem, implement, using COMPOSITION the method 'eat_food' in the 'Animal' class.
# * Animal instances should have a 'diggestive_system' attribute, which is the DigestiveSystem instance of that object.
# * The eat_food method should PROCESS any 'food' (any string) that are not allergenic (use the method 'has_allergy' to check for this case)
# * The DigestiveSystem is a class responsible for the PROCESS of any food eaten,
#       so make use of this in the Animal.eat_food method (remember COMPOSITION!)

class DigestiveSystem:
    """This class is already done for you
    don't changea any code on it.
    """
    def process_food(self, food):
        return f'processed-{food}'


class Animal:
    def __init__(self):
        # your code goes here instead of pass
        self.digestive_system = DigestiveSystem()

    def has_allergy(self, food):
        if food.lower() in ['peanut', 'milk']:
            return True
        return False

    def eat_food(self, food):
        """
        The 'food' parameter is just a string, such as 'apple', 'pear' or 'peanut'
        """

        # your code goes here instead of pass
        if not self.has_allergy(food):
            return self.digestive_system.process_food(food)
        else:
            return f"{food} is allergenic, can't eat it!"


#####################################################################################################################
#####################################################################################################################

# 3. Rewrite the Human class bellow (without changing it's name), so that it inherits from the Animal class of the exercice 2.
# * You should override the 'has_allergy' method in the Human class, so that it now only returns True if the food is 'peanut'

class Human(Animal):
    def has_allergy(self, food):
        if food.lower() == 'peanut':
            return True
        return False

#####################################################################################################################
#####################################################################################################################

# 4. Implement the Child class below, which inherets from Human (from exercice 3).
# * Instances of Child need to have a 'toy' attribute (string), which is defined during instantiation
# * This class should also have a 'playing_with_toy' method, which should return the 'toy' (string) that the Child has.
# * Other than that, a Child should behave exactly like a Human instance, so make sure it is inheriting all the logic from its parents '__init__' method


class Child(Human):
    def __init__(self, toy):
        super().__init__()
        self.toy = toy

    def playing_with_toy(self):
        return self.toy


#####################################################################################################################
#####################################################################################################################


# 5. Write code in the following __main__ function to test all classes, their attributes and functions.
# * Currently this function includes some examples tests, so you need to extend this code to include all needed tests.
if __name__ == '__main__':

    # Example code for testing
    
    # Testing MyClass
    my_instance = MyClass(some_val=90)
    assert my_instance.some_val == 90

    another_instance = MyClass(some_val=100)
    assert another_instance.plus_n(7) == 107

    # Testing Animal
    animal = Animal()
    assert isinstance(animal.digestive_system, DigestiveSystem)
    assert animal.eat_food('apple') == 'processed-apple'
    assert animal.eat_food('milk') == "milk is allergenic, can't eat it!"
    assert animal.eat_food('peanut') == "peanut is allergenic, can't eat it!"

    # Testing Humans
    human = Human()
    assert human.eat_food('apple') == 'processed-apple'
    assert human.eat_food('milk') == 'processed-milk'
    assert human.eat_food('peanut') == "peanut is allergenic, can't eat it!"

    assert human.has_allergy('peanut') == True
    assert human.has_allergy('milk') == False
    assert human.has_allergy('almonds') == False

    # Testing Child
    child = Child(toy='car')
    assert child.playing_with_toy() == 'car'

    print('All my tests passed')