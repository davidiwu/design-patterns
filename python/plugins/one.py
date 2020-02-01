'''
# plugin #1
'''

class Plugin(object):
    def __init__(self, *args, **kwargs):
        print('Plugin One inited: ', args, kwargs)

    def execute(self, a, b):
        return a + b