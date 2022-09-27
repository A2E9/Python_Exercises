import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host = 'localhost',
                                         database = 'test',
                                         user = 'root',
                                         password = 'admin123$')

    if connection.is_connected():
        
        cursor = connection.cursor()
        cursor.execute("SELECT person_id, Anrede, Titel, Vorname, Nachname, Geburtsdatum, Straße, Hausnummer, Postleitzahl, Stadt, Telefon, Mobil, Telefax, EMail, Newsletter, Eintragsdatum FROM person")
        array = cursor.fetchall()

        # for (person_id,Anrede,Titel,Vorname, Nachname, Geburtsdatum, Straße, Hausnummer, Postleitzahl, Stadt, Telefon, Mobil, Telefax, EMail, Newsletter, Eintragsdatum) in array:
        #     print(person_id,Anrede,Titel,Vorname, Nachname, Geburtsdatum, Straße, Hausnummer, Postleitzahl, Stadt, Telefon, Mobil, Telefax, EMail, Newsletter, Eintragsdatum)
        for row in array:
            print("")
            for value in row:
                if(value == None):
                    value = 'leer'
                print(value, end = " | ")
        
        
        
        
        
        
        
        
        
except Error as e:
    print("ERROR")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Closed")