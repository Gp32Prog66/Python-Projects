#multiple choice program

def ReverseList(lists):
    return [ele for ele in reversed(lists)]

print("What program do you want to choose?")
print("Reverse List \n Find Length of List \n Linear Search \n Cocktail Sort")

a = 1;
b = 2;
c = 3;
d = 4;
e = 5;
f = 6;


userMenuChoice = input("Selection:")




if userMenuChoice == a:
    print("Reverse List \n")
    lists = [46, 47, 49, 50]
    print(ReverseList(lists))
