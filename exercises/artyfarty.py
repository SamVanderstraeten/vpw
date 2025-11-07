"""
Schrijf een programma dat een ascii-art figuur laat zien op het scherm. De grootte van de figuur is de invoer voor je programma: 
het is een geheel getal strikt tussen 0 en 100 (dus 0 en 100 niet inbegrepen). 
Hieronder staan wat figuren voor verschillende gegeven groottes. 
Je moet zelf de correcte manier vinden om voor andere groottes de juiste figuur op het scherm te toveren.
https://www.vlaamseprogrammeerwedstrijd.be/2026/#oefenvragen
"""

n = int(input())
max_width = 3 + 4*n
dots = "***"
dots_side = "* *"

lines = []

def center(size, line):
    pad = int((size - len(line)) / 2)
    return pad*" " + line

def store_line(line):
    lines.append(center(max_width, line))

store_line(dots)
store_line(dots_side)

for i in range(1, n+1):
        current_width = 3 + 4*i
        line = dots + (current_width - 2*len(dots))*" " + dots
        store_line(line)

        line = "*" + (current_width - 2)*" " + "*"
        store_line(line)

for line in lines:
    print(line)
for line in lines[-2::-1]:
    print(line)