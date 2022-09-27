
# Aufgabe 4:
# 	input number: 4
# 	{1: 1, 2: 4, 3: 9, 4: 16}


inputN = input("Input Number: ")
dict={}
for x in range( 1, int(inputN)+1):
    dict.update({f"{x}": f"{x*x}"})
print(dict)