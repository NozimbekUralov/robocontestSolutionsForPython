fin  = open("input.txt")
fout = open("output.txt","w")

a = int(fin.readline())
if a == 6:
    fout.write(str(1))
elif a == 5:
    fout.write(str(2))
elif a == 4:
    fout.write(str(3))
elif a == 3:
    fout.write(str(4))
elif a == 2:
    fout.write(str(5))
else :
    fout.write(str(6))

fin.close()
fout.close()