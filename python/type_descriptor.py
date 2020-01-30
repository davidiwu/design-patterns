
MyNewClass = type('MyNewClass', (object,), {})
my_class = MyNewClass()
print(type(my_class))

def init_func(self, color):
    self._color = color

def drive(self):
    print(f"you are driving the {self._color} car")

# use type to define a class
Car = type(
    'Car',
    (object,),
    {
        '__init__': init_func,
        'drive': drive,
    }
)

my_car = Car('red')
my_car.drive()

import itertools

class A:
    def a(self):
        print('you called a')

class B:
    def b(self):
        print('you called b')

class C:
    def c(self):
        print('you called c')

# create classes in a loop using type
for parents in itertools.combinations([A,B,C], 2):
    classname = ''.join([c.__name__ for c in parents])
    globals()[classname] = type(classname, parents, {})

print(AB.__bases__)
my_ab = AB()
my_ab.a()
my_ab.b()


# a data Descriptor
class SimpleDescriptor:
    def __get__(self, instance, owner):
        return f'you called __get__ with: {self!r}, {instance!r}, {owner!r}'

    def __set__(self, instance, value):
        self._value = value

class OrdinaryClass:
    get_me = SimpleDescriptor()


an_instance = OrdinaryClass()
print(an_instance.get_me)

print(type(an_instance))