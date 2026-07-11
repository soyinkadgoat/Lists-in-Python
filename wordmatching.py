words = ["ball", "net", "dad", "pop", "tent"]
count = 0

for i in words:
    firstletter = i[0]
    lastletter = i[-1]

    if firstletter == lastletter:
        count = count + 1
    
print(count)