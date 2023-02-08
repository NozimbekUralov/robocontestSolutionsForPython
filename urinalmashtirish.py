fin  = open("input.txt")
fout = open("output.txt","w")

a, b = map(int, fin.readline().split())
fout.write(str(b))
fout.write(" ")
fout.write(str(a))

fin.close()
fout.close()