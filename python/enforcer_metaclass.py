'''
meta class's functiona are called in below order:

__prepare__(cls, name, bases, **kwargs)
__new__(cls, clsname, bases, clsdict, **kwargs)
__init__(cls, clsname, bases, clsdict, **kwargs)
__call__(cls, *args, **kwargs)

'''
class EnforceMeta(type):
    def __new__(cls, clsname, bases, clsdict, private):
        print(f'is private? {private}')
        for name in clsdict:
            if name.lower() != name:
                raise TypeError("Inappropriate method name: " + name)

        return super().__new__(cls, clsname, bases, clsdict)

class Root(metaclass=EnforceMeta, private=True):
    pass

class ChildA(Root, private=True):
    def method_name(self):
        pass


class ChildB(Root, private=True):
    # TypeError: Inappropriate method name: methodName
    def method_name(self):
        pass

a = ChildA()
b = ChildB()  