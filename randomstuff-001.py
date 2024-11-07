def rec(num):
    if num == 10:
        return num
    else:
        print("hello.")
        return rec(num + 1)
    
print(rec(0))