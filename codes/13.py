arr = list(map(int, input("Enter elements: ").split()))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

print("Elements in range:")
for x in arr:
    if low <= x <= high:
        print(x, end=" ")






points = []

n = int(input("Enter number of points: "))
for i in range(n):
    x, y = map(int, input("Enter x y: ").split())
    points.append((x, y))

x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))

print("Points in range:")
for (x, y) in points:
    if x1 <= x <= x2 and y1 <= y <= y2:
        print("(", x, ",", y, ")")
