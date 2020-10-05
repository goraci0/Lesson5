#tests


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

def test_1_simpl():
    assert simpl(10) == 1

def test_2_simpl():
    assert simpl(7)==1

def test_3_list():
    assert list_div(10) == [1,2,5,10]

def test_4_max_div():
    assert max_div(10) == 5

def test_5_max_div():
    assert max_div(12) == 4

