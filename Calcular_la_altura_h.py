#input
print("----------------------------------------------------------")
h = float(input("Ingrese la altura inicial de la pelota en (m): "))
print("----------------------------------------------------------")

#processing
q = h / 5
n = 0

while h > q:
    h *= 0.9
    n +=1

#ouput
print(f"La pelota da un total de {n} rebotes antes de llegar a la quinta parte de su altura inicial.")
