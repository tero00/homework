# pop = open("C:\\Users\\tero0\\Desktop\\Code\\Python\\memory\\populationdata.txt", "w")
# data = open("C:\\Users\\tero0\\Desktop\\Code\\Python\\memory\\worlddata.txt", "r")
# data_copy = data
# data.readline()
# for _ in range(len(data_copy.readlines())):
#     pop.write(data.readline())

with open("C:\\Users\\tero0\\Desktop\\Code\\Python\\memory\\worlddata.txt", "r") as data:
    full_lines = data.readlines()


cpop = []
for l in full_lines:
    a = l.split(",")
    cpop.append((a[7].strip('"'), a[-1].strip('\n')))
cpop = sorted(cpop)


with open("C:\\Users\\tero0\\Desktop\\Code\\Python\\memory\\populationdata.txt", "w") as output:
    for t in cpop:
        output.write(f"{t[0]}\t\t{t[1]}\n")
print("done")