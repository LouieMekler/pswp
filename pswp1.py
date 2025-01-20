mod = 10
fib = 2
def fun(array):
    return array[0] + array[1]


foundCombos = []
allCombos = []
for i in range(mod**fib):
    combo = []
    for j in range(fib):
        combo.append(i // mod**(fib-j-1) % mod)
    allCombos.append(combo)


total=0
braclets=[]
for combo in allCombos:
    if combo not in foundCombos:
        start = combo[::]
        chain = combo[::]
        
        chain.append(fun(chain)%mod)
        while chain[-fib::] not in foundCombos:
            foundCombos.append(chain[-fib::])
            chain.append(fun(chain[-fib::])%mod)

        total+=1
        braclets.append("{:<5}".format(str(total)+".") + "".join([str(x) for x in chain[:-1:]])+"->")
        

print("total number of unique braclets =",total,end="\n\n")
print("\n".join(braclets))
