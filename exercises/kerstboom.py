"""
Schrijf een programma dat een getal N inleest en een kerstboom van grootte N op het scherm uitprint. 
N is een geheel getal tussen 1 en 100. 
De kerstboom bestaat uit een kruin en een stam. 
De kruin bestaat uit N lijnen met telkens een aantal spaties gevolgd door een oneven aantal sterretjes (*): 1, 3, 5, ..., 2*N-1. 
De stam bestaat uit 2 lijnen met telkens een sterretje dat gecentreerd is ten opzichte van de kruin.
"""
h = int(input())

max = 2*h-1
for i in range(h):
    breedte = 2*i+1
    padding = (max-breedte) / 2
    ps = " "*int(padding)
    bs = "*"*breedte
    print(f"{ps}{bs}")
for i in range(2):
    breedte = 1
    padding = (max-breedte) / 2
    ps = " "*int(padding)
    bs = "*"*breedte
    print(f"{ps}{bs}")
