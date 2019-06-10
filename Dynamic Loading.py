import os
mods = []

print("-----Files-----")
for x in os.listdir("Modules"):
    print(x)
    if x[-3:] == ".py":
        mods.append(x)

print("\n-----Modules-----")
print(mods)

print("\n-----Loading-----")
__import__("Modules", fromlist=mods)

        
