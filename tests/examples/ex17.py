n = 5000
m = 7000
p = 5000
a = zeros(shape=(n,m), dtype=float)
b = zeros(shape=(m,p), dtype=float)
c = zeros(shape=(n,p), dtype=float)
for i in range(0, n):
    for j in range(0, m):
        a[i,j] = i-j

for i in range(0, m):
    for j in range(0, p):
        b[i,j] = i+j
for i in range(0, n):
    for j in range(0, p):
        for k in range(0, p):
            c[i,j] = c[i,j] + a[i,k]*b[k,j]