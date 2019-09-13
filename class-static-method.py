#In class method we need to pass cls as 1st argument.
#compulsory we need to we @classmethod decorator

class Animal:
    legs=4


    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))

Animal.walk('Lion')

