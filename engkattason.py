fin  = open("input.txt")
fout = open("output.txt","w")

a, b, c = map(int, fin.readline().split())
if a > b:
    if a > c:
        fout.write(str(a))
    else:
        fout.write(str(c))
elif b > c:
    fout.write(str(b))
else:
    fout.write(str(c))

fin.close()
fout.close()