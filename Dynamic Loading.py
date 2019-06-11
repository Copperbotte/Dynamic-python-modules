import os
directory = "Modules"

#filter python files from a folder
mods = [x[:-3] for x in os.listdir(directory) if x[-3:] == '.py']
funcs = dict()

#import filtered files
#filtered files self-register with the __register_plugin__ function
modules = __import__(directory, globals(), locals(), mods, 0)
for m in mods:
    name, func = getattr(modules, m).register()
    funcs[name] = func
    globals()[name] = func


