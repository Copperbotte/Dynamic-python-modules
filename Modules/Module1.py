
print("module 1 loaded")

def Mod1func():
    print("module 1 function")

def register():
    print("module 1 registered")
    return Mod1func.__name__, Mod1func
