summe = 0
for feld in range(64):
    reiskorn = 2**feld
    summe = summe + reiskorn
    print("feld {}. = {:>30,} reiskörner und damit insgesamt {:>30,} reiskörner".format(feld+1,reiskorn,summe))
gewicht = summe *0.02 / 1000 / 1000
print()
print("Wenn ein reiskorn 0,02g wiegt, wiegen die gesamten")
print("reiskörner {:18,.0f} in tonnen".format(gewicht))
print("YA!")
