import datetime
from datetime import date

dateOfYear = {}
d = {}
dateOfYear[0] = 31
dateOfYear[1] = 29
dateOfYear[2] = 31
dateOfYear[3] = 30
dateOfYear[4] = 31
dateOfYear[5] = 30
dateOfYear[6] = 31
dateOfYear[7] = 31
dateOfYear[8] = 30
dateOfYear[9] = 31
dateOfYear[10] = 30
dateOfYear[11] = 31
file = open("Data.txt", 'r')
for str in file:
    line = str[:len(str)-1]
    temp = line.split(":")
    if temp.__len__() < 3:
        key, value = line.split(" : ")
        d[key] = value
#print(d)
s = set()

for key, value in d.items():
    today = date.today()
    temp = value.split(".")
    tempYear = today.year
    if int(temp[2]) in range(0, tempYear+1):
        if int(temp[1]) in range(1, 13):
            if int(temp[0]) > int(dateOfYear.get(int(temp[1]) - 1)):
                s.add(key)
        else:
            s.add(key)
    else:
        s.add(key)

for val in s:
    d.pop(val, -1)

file.close()

action = input("Enter the command: ").lower()
while action != 'exit':
    if "delete" in action:
        userName = input("Name: ")
        if userName in d:
            d.pop(userName)
        else:
            print("There is no %s in database!" %userName)
        action = input("Enter the command: ").lower()

    elif "change" in action:
        userName = input("Name: ")
        if userName in d:
            chance = input("Change Name or Data?: ").lower()
            if chance == "name":
                newName = input("New Name: ")
                dNew = {}
                temp = d.get(userName)
                dNew[newName] = temp
                d.pop(userName, -1)
                d.update(dNew)
                print('Successfully changed ', userName, " : ", temp,  ' to ',  newName, " : ", d.get(newName))
            if chance == "data":
                newData = input("New Data: ")
                tempData = newData.split(".")
                yearD = today.year
                if int(tempData[2]) in range(0, yearD + 1):
                    if int(tempData[1]) in range(1, 13):
                        if int(tempData[0]) <= int(dateOfYear.get(int(tempData[1]) - 1)):
                            newD = {}
                            temp = d.get(userName)
                            newD[userName] = newData
                            d.pop(userName, -1)
                            d.update(newD)
                            print('Successfully changed ', userName, " : ", temp, ' to ', userName, " : ", d.get(userName))
                        else:
                            print("This day is incorrect.")
                    else:
                        print("This month is incorrect.")
                else:
                    print("This year is incorrect.")
        else:
            print("There is no ", userName, " in database")
        action = input("Enter the command: ").lower()

    elif "age" in action:
        userName = input("Name: ")
        if userName in d:
            temp = d.get(userName, -1)
            dataPerson = temp.split(".")
            today = date.today()
            age = today.year - int(dataPerson[2])
            if today.month < int(dataPerson[1]):
                age -= 1
            elif today.month == int(dataPerson[1]) and today.day <= int(dataPerson[0]):
                age -= 1
            print(userName, ' is ', age, " years old")
        else:
            print("There is no ", userName, " in database")
        action = input("Enter the command: ").lower()

    elif "B-day" in action:
        max = 367
        tempName = "Alex"
        today = date.today()
        year = today.year
        while max == 367:
            for key, val in d.items():
                dataPerson = val.split(".")
                ran = datetime.date(year, int(dataPerson[1]), int(dataPerson[0]));
                k = (ran - today).days
                if k < max:
                    if k > 0:
                        max = k
                        tempName = key
            year += 1
        print(tempName, ' has next B-day')
        action = input("Enter the command: ").lower()

    elif "Inf" in action:
        command = input("Choose command(day, month, year): ").lower()
        noone = 0
        if command == "day":
            day = input("Set day: ")
            month = input("Set month: ")
            if int(month) in range(1, 13):
                if int(day) <= int(dateOfYear.get(int(month)-1)):
                    for key, val in d.items():
                        dataPerson = val.split(".")
                        if int(day) == int(dataPerson[0]) and int(month) == int(dataPerson[1]):
                            print(key, ' was born in this day and month')
                            noone += 1
                    if noone == 0:
                        print('Noone was born in this day')
                else:
                    print("This day is incorrect for this month! Try again.")
            else:
                print("This month is incorrect! Try again.")
            action = input("Enter the command: ").lower()

        if command == "month":
            month = input("Set month: ")
            if month in range(1, 13):
                for key, val in d.items():
                    dataPerson = val.split(".")
                    if int(month) == int(dataPerson[1]):
                        print(key, ' was born in this month')
                        noone += 1
                if noone == 0:
                        print('Noone was born in this month')
            else:
                print("This month is incorrect! Try again.")
            action = input("Enter the command: ").lower()

        if command == "year":
            year = input("Set year: ")
            today = date.today();
            if year in range(0, today.year+1):
                for key, val in d.items():
                    dataPerson = val.split(".")
                    if int(year) == int(dataPerson[2]):
                        print(key, ' was born in this year')
                        noone += 1
                if noone == 0:
                        print('Noone was born in this year')
            else:
                print("This year is incorrect! Try again!")
            action = input("Enter the command: ").lower()

    elif "add" in action:
        name = input("Set name: ")
        val = input("Set B-day: ")
        tempVal = val.split(".")
        yearVal = today.year
        if int(tempVal[2]) in range(0, yearVal + 1):
            if int(tempVal[1]) in range(1, 13):
                if int(tempVal[0]) <= int(dateOfYear.get(int(tempVal[1]) - 1)):
                    d[name] = val
                    print("Complete!")
                else:
                    print("This day is incorrect.")

            else:
                print("This month is incorrect.")
        else:
            print("This year is incorrect.")
        action = input("Enter the command: ").lower()

    elif "quit" in action:
        file = open("Data.txt", "w")
        for key, value in d.items():
            file.write("%s : %s \n" % (key, value))
        file.close()
        break

    else:
        print("There is no this command! Try again.")
        action = input("Enter the command: ").lower()
