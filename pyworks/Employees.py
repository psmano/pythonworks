fobj = open('employees.csv','w')
fobj.write('First Name, Last Name, Salary \n')

employees = [("Manohar","P S",41), ("Prasad","M",39), ("Viswa","Nathan",36), ("Deepak","Majjiga",32)]
for employee in employees:
    fn = employee[0]
    ln = employee[1]
    age = employee[2]

    fobj.write(fn + "," + ln + "," + str(age) + ",\n")
    print("Done")
fobj.close()
