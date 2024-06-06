week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
day = input("Enter a day: ").lower()

if day == 'sunday':
    del week[:1]
    print("Remaining days in holidays:", week)
elif day == 'monday':
    del week[:2]
    print("Remaining days in holidays:", week)
elif day == 'tuesday':
    del week[:3]
    print("Remaining days in holidays:", week)
elif day == 'wednesday':
    del week[:4]
    print("Remaining days in holidays:", week)
elif day == 'thursday':
    del week[:5]
    print("Remaining days in holidays:", week)
elif day == 'friday':
    del week[:6]
    print("Remaining days in holidays:", week)
elif day == 'saturday':
    del week[:7]
    print("It is a holiday", week)
else:
    print("Invalid input or not a holiday.")
