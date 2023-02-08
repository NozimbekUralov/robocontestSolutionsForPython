fin  = open("input.txt")
fout = open("output.txt","w")

a = int(fin.readline())
fout.write(str(a*a))

fin.close()
fout.close()