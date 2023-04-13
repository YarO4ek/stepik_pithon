

a = []
b = {}
c = []
d = []
def keydd(k):
    kk = k.replace("dict_keys(['", '')
    kk = kk.replace("'])", '')
    return kk
def valuesdd(op):
    opp = op.replace("dict_values(['", '')
    opp = opp.replace("'])", '')
    return opp

with open("dataset.txt", 'r') as s:
    ss = s.readline()
    a+=(ss)
    for i in range(0, len(ss)):
        if i != len(ss):
            if a[i] == '0' or a[i] == '1' or a[i] == '2' or a[i] == '3' or a[i] == '4' or a[i] == '5' or a[i] == '6' or a[i] == '7' or a[i] == '8' or a[i] == '9':
                if a[i+1] == '0' or a[i+1] == '1' or a[i+1] == '2' or a[i+1] == '3' or a[i+1] == '4' or a[i+1] == '5' or a[i+1] == '6' or a[i+1] == '7' or a[i+1] == '8' or a[i+1] == '9':
                    a[i] = str(a[i])+str(a[i+1])
                    del a[i+1]
                    a.insert(i+1, ' ') 
                    b[a[i-1]] = a[i]
                    l = b.keys()
                    k = b.values()
                    kk = str(k)
                    j = str(l)
                    hoh = keydd(j)
                    print(hoh)
                    hd = valuesdd(kk)
                    print(hd)
                    b.clear()
                    d.append(hoh*int(hd))
                else:
                    b[a[i-1]] = a[i]
                    l = b.keys()
                    k = b.values()
                    kk = str(k)
                    j = str(l)
                    hoh = keydd(j)
                    print(hoh)
                    hd = valuesdd(kk)
                    print(hd)
                    b.clear()
                    d.append(hoh*int(hd))
print('Ответ: \n')
for hghg in range(0, len(d)):
    print(d[hghg], end='')