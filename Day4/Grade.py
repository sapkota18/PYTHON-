sub1 = float(input("Mark of sub 1:"))
sub2 = float(input("Mark of sub 2:"))
sub3 = float(input("Mark of sub 3:"))
sub4 = float(input("Mark of sub 4:"))

if sub1 > 100 or sub2 > 100 or sub3 > 100 or sub4 > 100:
    print("Marks cannot exceed 100")
else:
    total = sub1 + sub2 + sub3 + sub4
    gpa = (total * 4) / 400
    if 4.0 >= gpa >= 3.6:
        print("A")
    elif 3.59 >= gpa >= 3.2:
        print("B")
    elif 3.19 >= gpa >= 2.8:
        print("C")
    elif 2.79 >= gpa >= 2.4:
        print("D")
    elif 2.39 >= gpa >= 2.0:
        print("E")
    else:
        print("F")
