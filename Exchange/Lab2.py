have = {}
want = {}
flag = 0

file = open("Have.txt", 'r')

for str in file:
    st = str.split(" : ")
    have[st[0]] = st[1][:len(st[1]) - 1]
file.close()

file2 = open("Want.txt", 'r')

for str in file2:
    st = str.split(" : ")
    want[st[0]] = st[1][:len(st[1]) - 1]
file2.close()

print("Enter the participants: ")
elem = input()
while elem != "exit":
    temp = set()
    temp1 = elem.split(" ")
    for values in temp1:
        temp.add(values)

    if temp.__len__() < 2:
        print("The exchange is impossible! Not enough people.")

    if temp.__len__() >= 2:
        haveMoney = set()
        wantMoney = set()
        for name in temp1:
            if have.get(name, -1) != -1 and want.get(name, -1) != -1:
                t = have.get(name, -1)
                tempT = t.split(", ")
                haveMoney = haveMoney.union(tempT)
                v = want.get(name, -1)
                tempV = v.split(", ")
                wantMoney = wantMoney.union(tempV)
            else:
                print("There is no ", name, "!")
                flag = 1
        if flag == 0:
            can = haveMoney.intersection(wantMoney)
            if len(can) == len(temp):
                peopleForJob = set()
                for people in temp:
                    z = 0
                    for element in wantMoney:
                        tempPeopleHave = have.get(people)
                        peopleHave = tempPeopleHave.split(", ")
                        if {element}.issubset(peopleHave):
                            peopleForJob.add(people)
                            z = element
                            break
                    if z != 0:
                        wantMoney.discard(z)
                if len(peopleForJob) == len(temp):
                    print("The exchange is possible!")
                else:
                    print("The exchange is impossible!")
            else:
                print("The exchange is impossible!")













    elem = input()
