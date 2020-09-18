def simpl(n):
    for i in range(2,n):
        if n%i == 0: return 0
    return 1

def list_div(n):
    list_d = [1]
    for i in range(2,n+1):
        if n%i == 0: list_d.append(i)
    return list_d

def max_div(n):
    list_d=list_div(n)
    list_d.reverse()
    for i in list_d:
        if simpl(i): return i
