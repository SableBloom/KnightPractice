gb_count = 0
y = "GOODBYE!"

print("HEY KID!")

while gb_count < 2:
    x = input()
    if (x == ('')):
        print("WHAT?!")
    elif (x.isupper() == False):
        print("SPEAK UP, KID!")
    elif (x.isupper() and x != y):
        print("NO, NOT SINCE 1946!")
    elif (x == y and gb_count == 0):
        gb_count += 1
        print("LEAVING SO SOON?")
    else:
        gb_count += 1

print("LATER SKATER!")
