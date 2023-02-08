fin  = open("input.txt")
fout = open("output.txt","w")

a, b = map(int, fin.readline().split())
if a == b:
    ans="="
    fout.write(ans)
elif a > b:
    ans=">"
    fout.write(ans)
else:
    ans="<"
    fout.write(ans)

fin.close()
fout.close()