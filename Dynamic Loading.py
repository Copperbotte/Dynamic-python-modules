import os

funcs = dict()

#filter python files from a folder
mods = [x for x in os.listdir() if x[-3:] == '.py']

#import filtered files
#filtered files self-register with the __register_plugin__ function
modules = __import__("Modules", globals(), locals(), mods, 0)
for m in mods:
    name, func = getattr(modules, m).register()
    funcs[name] = func
    globals()[name] = func


