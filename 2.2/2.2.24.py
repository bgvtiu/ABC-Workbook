import math

n, x, y = [int(x) for x in input().split()]
coords = []
radii = []

for _ in range(n):
  point = input().split()
  h = int(point[0])
  k = int(point[1])
  coords.append((h, k))

for h, k in coords:
  test_r = math.dist((x,y),(h,k))
  radii.append(test_r)

print(f"{max(radii)*2:.4f}")