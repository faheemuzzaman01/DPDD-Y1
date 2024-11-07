def perimeter():
    length = float(input("enter length"))
    width = float(input("enter width"))
    result=str(2*(length+width))
    l = len(result)-2
    if result[l:] == ".0":
        result = result[:l] 
    print(result + "cm")
perimeter()