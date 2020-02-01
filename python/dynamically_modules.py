
# from plugins import one, two

import importlib

# user configable string:
PLUGIN_NAME = 'plugins.one'
# PLUGIN_NAME = 'plugins.two'

plugin_module = importlib.import_module(PLUGIN_NAME, ".")
print(plugin_module)

plugin = plugin_module.Plugin("hello", key=123)
result = plugin.execute(5, 3)
print(result)

# change the module name if needed
_global = globals()
_global['alias'] = plugin_module

my_alias = alias.Plugin("alias", key=321)
print(my_alias.execute(6,5))
