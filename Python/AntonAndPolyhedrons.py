n=int(input())
Total=0
Tetrahedron=4
Cube=6
Octahedron=8
Dodecahedron=12
Icosahedron=20
for i in range(n):
    string=input()
    if string=="Tetrahedron":
        Total+=Tetrahedron
    elif string=="Cube":
        Total+=Cube
    elif string=="Octahedron":
        Total+=Octahedron
    elif string=="Dodecahedron":
        Total+=Dodecahedron
    else:
        Total+=Icosahedron
print(Total)
