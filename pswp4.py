import time
start1 = time.time()

n=25
p=0.5

probs = [p,1-p]
total = 0
for i in range(2**(n-1)):
    success = False
    step = 1
    weight = 1
    for j in range(n-1):
        flip = i // 2**(n-j-2) % 2
        step+= flip + 1
        weight *= probs[flip]
        if step == n:
            success = True
    if success:
        total += weight
            

print(f"n={n}, p={p}\n")
print("Brute force O(2^n):")
print(f"Time elapsed= {time.time()-start1}")
print(f"Total runs= {2**(n-1)}")
print(f"l({n})= {total}\n")


start2 = time.time()
n=25
sequence = [1,p]
for i in range(2,n):
    term = p*sequence[i-1] + (1-p)*sequence[i-2]
    sequence.append(term)

print("Recurrence Relation Calculation O(n):")
print(f"Time elapsed= {time.time()-start2}")
print(f"Sequence length = {n}")
print(f"l({n})= {sequence[-1]}")
