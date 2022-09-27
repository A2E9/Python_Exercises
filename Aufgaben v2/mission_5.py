# Aufgabe 5:
# 	(1, 2, 3, 4, 5, 6, 7, 8, 9)
# 	Ausgabe:
# 		Gerade Zahlen: 4
# 		Ungerade Zahlen: 5

listt = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = 0
odd = 0
for x in listt:
    if x % 2 == 0:
        even+=1
    else:
       odd+=1
print(f"Gerade Zahen: {even}\nUngerade Zahen: {odd}") 