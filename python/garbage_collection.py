'''

	• In Python, Everything is a object, even for primitive types: x = 10
		○ A PyObject contains 3 things: type (int), refcount (1), value (10) in heap

	• The algorithm used for garbage collection(GC) is called reference counting.
		○ Reference counting is not thread safe
		○ GIL(Global interpreter lock) can prevent reference counts from being changes concurrently.
		○ So multi-threads are actully only one thread run at a time because of GIL
		○ use multi-processing, each process will have it's own GIL. But need a way to share information between processes.
		○ It cannot detect cyclical reference
		○ Reference counting alone will not GC objects with cyclical references
		
	• Another technical used for GC is Tracing: mark and sweep.
		○ Tracing is run when the number of objects in memory is greater than a threshhold
		○ Start from the GC root, mark any objects that are reachable from the GC root
		○ Sweep all other unreachable objects
		○ Cyclical references can be solved by Tracing

	• Python uses generational GC, it is a type of Tracing technical. It has 3: Gen0, Gen1, Gen3
		○ Newly created objects are stored in Gen0
		○ If a object survived a GC, then it promotes to a higer generation, Gen1/Gen2
		○ Only container objects with a refcount greater than 0 will be stored in a generation list
		○ When the number of objects in generation reaches a threshhold, python runs GC on that generation, and any younger generations.
		○ During a generational GC cycle:
			§ Python makes a list for objects to discard
			§ It runs an algorithm to detect reference cycles
			§ If an object has no outside references, add it to the discard list
			§ When the cycle is done, free up the objects in the discard list
			§ After this, if a object survived, it will be promoted to the next generation
			§ Generation 2 objects stay there as the program executes
		
	• If the reference counting is 0 for an object, GC is invoked immediately, and memory reclaimed. But when cyclical references are GCed unknown
	
	• 而对于较小的整数和短字符python会缓存这些对象，而不是频繁的创建和销毁
	
	• the methods and variables are created on stack memory
	
	• the objects and instance variables are created on heap memory
	
	• a new stack frame is created on invocation of a function/method
	
    • stack frames are destroyed as soon as the function/method returns

'''
import weakref

def immutable_object():
    x = 10
    y = x
    print(type(x))
    assert id(x) == id(y)
    x = x+1
    assert id(x) != id(y)
    z = 10
    assert id(z) == id(y)  ## why? memory reuse
    assert z is y


class Car:
    def __init__(self, w):
        self.wheels = w

def referece_counting():

    car = Car(4)
    print(f'car object memory location: {hex(id(car))}')

    # weak reference do not increace reference counting
    r = weakref.ref(car)

    print('before: ', r)
    car = None
    print('after: ', r)

    print('Garbage collected immediately!')

if __name__=='__main__':
    immutable_object()
    referece_counting()
