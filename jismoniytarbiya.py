fin  = open("input.txt")
fout = open("output.txt","w")

a = int(fin.readline())
fout.write(str(a+2))

fin.close()
fout.close()