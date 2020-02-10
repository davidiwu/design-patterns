
#使用装饰器(decorator),  
#这是一种更pythonic,更elegant的方法,  
#单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的
  
def singleton(cls, *args, **kw):  
    instances = {}  
    def _singleton(*args, **kw):  
        if cls not in instances:  
            instances[cls] = cls(*args, **kw)  
        return instances[cls]  
    return _singleton  


@singleton  
class MySingletonClass(object):  
    a = 1  
    def __init__(self, x=3):  
        self.x = x  

a = MySingletonClass(8)
b = MySingletonClass(34)

assert a == b

print(f'type of a is {type(a)}, id of a is {id(a)}')
print(f'type of b is {type(b)}, id of b is {id(b)}')
print(f'x in a in {a.x}, x in b is {b.x}')