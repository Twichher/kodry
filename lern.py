n, m = map(int, input().split())

a = [['*'] * m for i in range(n)]

for i in range(n):
	for t in range(m):
		a[i][t] = i + t + 2

a[n-1], a[0] = a[0], a[n-1]

for i in a:
	print(*i)
print('hello git')
print(*a[n-1])

for i in a[1:n-1]:
	print(*i)

print(*a[0])