import random
import sys
import time


# FUNCTIONS
    # --> twisting
    
def shuffleList(l):
    """ Sortiert eine Liste zufällig neu um """
    for x in range(len(l)*50):        #  genug Durchläufe um gut zu mischen
        i = random.randint(0, len(l)-1)    # zufälliger index eines Listenelements
        buf = l[i]                        # Element speichern
        del l[i]                            # Element löschen
        l.append(buf)                        # gespeichertes Element hinten an die Liste anhängen
        
    return l

def twistWord(word2twist):
    """ twistet einzelnes Wort """
    if len(word2twist) > 3:									# Wenn man das Wort twisten kann
        firstLetter = word2twist[0]	
        lastLetter = word2twist[-1]						# ersten und letzten Buchstaben speichern
        midLettersList = list(word2twist[1:-1])	# mittlere Buchstaben in Liste speichern
        
        # PROCESS/SHUFFLE MIDLETTERS LIST
        midlettersList = shuffleList(midLettersList)			# Liste zufällig neu sortieren
        
        midLetters = "".join(midLettersList)                    # Liste in String
        
        twistedWord = firstLetter + midLetters + lastLetter
        return twistedWord
    else:													# Wort zu kurz zum twisten (nur ein mittlerer Buchstabe)
        return word2twist

def twist():
    """ twistet satz den user eingibt """
    userIn = input("zu twistender Satz:\n >>> ")            # Satz der getwistet werden soll

    print("Twisting...")

    outputList = list(userIn)                        # Satz in Liste mit einzelnen Buchstaben trennen

    wordStart = 0
    wordEnd = 0

    inWord = False

    for x in range(len(userIn)):                    # über Buchstaben des Satzes iterieren
        l = userIn[x]                                # l = aktuelles Zeichen
        if not inWord and l.isalpha():            # neues Wort fängt an (nicht in Wort und l = buchstabe)
            inWord = True                            # flag setzen
            wordStart = x                            # index des Wortstarts speichern
        if inWord:
            if not l.isalpha() or x == len(userIn) - 1:    # wortende (nicht-buchstabe oder end of string)
                inWord = False                        # flag resetten
                wordEnd = x                            # index des Wortendes speichern
                if l.isalpha():                        # falls Wortende wegen EOS:
                    wordEnd += 1                        # letzten Buchstabe hinzufügen

                word = userIn[wordStart:wordEnd]        # word = aktuelles Wort
            
                word = twistWord(word)                    # word twisten
            
                for y in range(wordStart, wordEnd):        # wort durch getwistetes wort ersetzen
                    outputList[y] = word[y - wordStart]
    

    output = "".join(outputList)                        # Liste zu String konvertieren

    print("Getwisteter Satz: " + output)


    # --> unTwisting

def untwistWord(word2untwist):
    """ untwistet einzelnes Wort """
    if len(word2untwist) > 3:
        subWord = word2untwist.lower()                # Groß/Kleinschreibung ignorieren
        firstLetter = subWord[0]                        # ersten und letzten Buchstaben speichern
        lastLetter = subWord[-1]
        midLettersList = list(subWord[1:-1])        # Buchstaben dazwischen zum abgleichen sortieren
        midLettersList.sort()
    
        for x in range(len(dict)):                    # jedes Wort im Dict checken
            word = dict[x].lower()                    # Groß/Kleinschreibung ignorieren
            wordFirstLetter = word[0]
            if wordFirstLetter == firstLetter:        # Wenn erster Buchstabe stimmt
                wordLastLetter = word[-1]
                if wordLastLetter == lastLetter:        # Wenn letzter Buchstabe stimmt
                    if(len(word) == len(subWord)):        # Wenn Wortlänge stimmt
                        wordMidLettersList = list(word[1:-1])
                        wordMidLettersList.sort()
                        if midLettersList == wordMidLettersList:     # Wenn mittlere B. stimmen, gefunden
                            return(dict[x])
        return None                # kein Wort gefunden
    else:
        return word2untwist


def untwist():
    """ untwistet einen text """
    userIn = input("zu unTwistender Satz:\n >>> ")                # Satz der geuntwistet werden soll
    
    print()
    print()
    print("============================================")
    print("Untwisting...")
    print("============================================")
    print()
    
    startTime = time.time()
    
    outputList = list(userIn)                    # Satz in Liste mit einzelnen Buchstaben trennen
    
    wordStart = 0
    wordEnd = 0
    
    inWord = False
    
    match = False
    noMatch = False
    
    markFailure = True
    
    for x in range(len(userIn)):                    # über Buchstaben des Satzes iterieren
        l = userIn[x]                                # l = aktueller Buchstabe
        if not inWord and l.isalpha():        # neues Wort fängt an (nicht in Wort und l = buchstabe)
            # word begins
            inWord = True                        # flag setzen
            wordStart = x                        # Index des Wortstarts speichern
        if inWord:
            if not l.isalpha() or x == len(userIn) - 1:    # wortende (nicht-buchstabe oder end of string)
                # word ends
                inWord = False                    # flag resetten
                wordEnd = x                        # Index des Wortendes speichern
                if l.isalpha():                    # falls Wortende wegen EOS:
                    wordEnd += 1                    # letzen Buchstaben hinzufügen
                word = userIn[wordStart : wordEnd]    # word = aktuelles Wort
                
                word = untwistWord(word)                # Wort untwisten
                
                for y in range(wordStart, wordEnd):
                    if word:
                        outputList[y] = word[y - wordStart]
                        match = True                    # wort geuntwistet
                    else:
                        noMatch = True                # wort untwisten fehlgeschlagen
                        if markFailure:
                            outputList[y] = "x"        # fehler mit "x" markieren
    
    output = "".join(outputList)
    
    
    if not match:                                # kein einziges Wort geuntwistet
        print("Untwisting Unsuccessfull")
    elif match and noMatch:                        # je mindestens ein wort geuntwistet und fehlgeschlagen
        print("Untwisting partially Successfull")
    else:                                        # kein einziges Wort fehlgeschlagen
        print("Untwisting Successfull")
        
    print("operation took " + str(round(time.time() - startTime, 2)) + " Seconds")
    print()
    print("Geuntwisteter Satz: " + output)


# CODE

print("###############################################")
print("BwInf 2018 - A2: Twist")
print("Teilnehmer: Jakob Staudt & Jordan Körte")
print("###############################################\n")

print("Lade Wörterbuch...")
with open('woerterliste.txt', 'r', encoding="utf-8") as inputFile:
                dict = [x.strip() for x in inputFile]						# Wörterbuch in Liste laden
print("Wörterbuch geladen!")

while True:
    print("### HAUPTMENÜ ###")
    print("  1 > Satz twisten:          't' oder '1'")
    print("  2 > Satz untwisten:        'u' oder '2'")
    print("  3 > Beenden:               'e' oder '3'")
    cmd = input(">>>")
    if cmd == "t" or cmd == "1":
        print("Twister aufgerufen!\n\n")
        twist()
        print("Twister beendet!\n\n\n")
    elif cmd == "u" or cmd == "2":
        print("UnTwister aufgerufen!\n\n")
        untwist()
        print("UnTwister beendet!\n\n\n")
    elif cmd == "e" or cmd == "3":
        print("bye")
        sys.exit()
    else:
        print("Befehl nicht erkannt!")


