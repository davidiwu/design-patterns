
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