#Aufgabe 1: 
# 	function("Tell me how Are You doing today")
# 	Ausgabe:
# 		Groß geschriebene Wörter: 3
# 		Klein geschriebene Wörter: 4


def function():
    string = input(" :")
    big = 0
    small = 0
    for word in string.split():
        if word[0].isupper():
            big += 1
        else:
            small += 1
    print("Groß geschriebene Wörter: ", big )
    print("Klein geschriebene Wörter: ", small)


    
function()