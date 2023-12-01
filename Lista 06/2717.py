def decidir():
    n = int(input())
    a, b= map(int, input().split())
    if (a+b) <= n:
     return("Farei hoje!")
    else:
     return("Deixa para amanha!")
print(decidir())