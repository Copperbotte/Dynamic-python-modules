import os
mods = []

#filter python files from a folder
for x in os.listdir("Modules"):
    if x[-3:] == ".py":
        mods.append(x[:-3])

#import filtered files
#filtered files self-register with the __register_plugin__ function
modules = __import__("Modules", globals(), locals(), mods, 0)
for m in mods:
    getattr(modules, m).register()
