def media(a,b):
    c = (a * 3.5 + b * 7.5) / 11.0
    return c
x = float(input())
y = float(input())
z = media(x,y)
print(f"MEDIA = {z:.5f}")