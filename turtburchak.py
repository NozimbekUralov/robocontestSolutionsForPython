fin  = open("input.txt")
fout = open("output.txt","w")

a, b = map(int, fin.readline().split())
S=a*b
P=(a+b)*2
if S > P:
    fout.write(str(S))
else:
    fout.write(str(P))

fin.close()
fout.close()