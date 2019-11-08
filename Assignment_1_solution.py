
name = input("give me your name : ")
print("my name is  "  + name)

age = int(input("what is your age ? " ))

import datetime as d
c_year = int(d.datetime.now().year)

birthyear = (c_year - age)
print("okay !! you born in " ,birthyear)

after100y = birthyear + 100
print(name, "you will be 100 years old in" , after100y)
