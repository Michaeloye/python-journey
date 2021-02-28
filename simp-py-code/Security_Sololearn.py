layout = input("Please Enter the layout of: ")
list1 = []
for char in layout:
    list1.append(char)


money1 = list1.index("$")
after_money = list1[money1+1:]

list2 = list1[::-1]

money2 = list2.index('$')
before_money = list2[money2+1:]

thief1 = int()
thief2 = int()

guard1 = int()
guard2 = int()

if "T" in after_money:
    thief1 = after_money.index("T")
if "T" in before_money:
    thief2 = before_money.index("T")

if "G" in after_money:
    guard1 = after_money.index("G")
if "G" in before_money:
    guard2 = before_money.index("G")

if thief1<=thief2 and guard1<=guard2:
    if thief1<=guard1:
        print("Alert")
    else:
        print("Safe")
elif thief1<thief2 and guard2<guard1:
    if thief1<=guard1:
        print("Alert")
    else: 
        print("Safe")
elif thief2<=thief1 and guard1<=guard2:
    if thief2<=guard1:
        print("Alert")
    else: 
        print("Safe")
elif thief2<=thief1 and guard2<=guard1:
    if thief2<=guard2:
        print("Alert")
    else: 
        print("Safe")



    