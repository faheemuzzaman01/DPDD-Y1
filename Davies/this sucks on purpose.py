import time

saltandjuice = False
print("i'm very hungry.")
time.sleep(1)
while not saltandjuice:
    print("give me the salt.")
    salt = input("> ")
    if salt != "salt":
        print("no!")
        time.sleep(1)
        print("i don't want that.")
        time.sleep(1)
    print("give me the juice.")
    juice = input("> ")
    if juice != "juice":
        print("no!")
        time.sleep(1)
        print("i don't want that.")
        time.sleep(1)
    if (salt, juice) == ("salt", "juice"):
        saltandjuice = True