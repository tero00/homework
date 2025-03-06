import numpy as np

with open(__file__[:-12] + "v.txt", "r") as f:
    lines = f.readlines()
valtiot = [line.strip().split() for line in lines]
countries = {v[0]: v[-4:] for v in valtiot}

with open(__file__[:-12]+"saurus.txt","r") as s:
    lines = s.readlines()
saurus = lines[:]
saurus = [line.strip().split() for line in saurus]

for v,c in countries.items():
    sent = []
    for n in c[-4:]:
        w = float(n)
        if w < 100:
            sent.append(saurus[int(w)][0])
            if w - np.floor(w) != 0:
                # print(str(w)+" "+str(int(w))+" "+str(w-int(w))+str(int((w-int(w))*10))+" "+str(int((w-int(w))*10)))
                sent.append(saurus[0][int(np.round((w-int(w))*10))])
        elif w > 1000:
            sent.append("saur "+saurus[int(np.mod(w,100))][int(str(w)[1])])
        else:
            sent.append(saurus[int(np.mod(w,100))][int(str(w)[:1])])
    print(v+" "+str(sent))

