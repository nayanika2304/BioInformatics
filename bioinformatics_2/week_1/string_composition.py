def string_composition(k,text):
    result = []
    for i in range(0,len(text)-k):
        result.append(text[i:i+k])
    #result.sort()
    return result

with open('dataset_197_3.txt','r') as f:
    data = []
    for i in f.readlines():
        data.append(i)
    k = int(data[0])
    text = data[1]
r = string_composition(k,text)
for a in r:
    print(a)
