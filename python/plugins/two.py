'''
# plugin #2
'''

class Plugin(object):
    def __init__(self, *args, **kwargs):
        print('Plugin Two inited: ', args, kwargs)

    def execute(self, a, b):
        return a - b