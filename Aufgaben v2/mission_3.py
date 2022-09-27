# Aufgabe 3: String umkehren
# 	input string - "thgu54asd"
# 	Ausgabe: 	   "dsa45ught"

string = input("Input String: ")
list = []
length = len(string)
for x in string:
    list.append(string[length-1]) 
    length -=1
print("".join(list))


print(string[::-1])
