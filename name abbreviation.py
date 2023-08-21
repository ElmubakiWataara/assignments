"""Write a program that takes your full name as input and displays the abbreviations of the first
and middle names except the last name which is displayed as it is. For example, if your name
is Robert Brett Roser, then the output should be R.B.Roser"""


name = {"first_name":"Abdul","second_name":"Barki","last_name":"Suleman"}
Name = name["first_name"][0],name["second_name"][0],name["last_name"]
Name = '.'.join(Name)
print(Name)