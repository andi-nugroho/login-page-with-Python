from re import I


hitung = []


def fibonaci(n):
    if n == 0 or n == 1:
        n = 1
        hitung.append(n)

    else:
        fibonaci(n - 1)
        fibonaci(n - 2)
        n = 0
        hitung.append(n)


fibonaci(3)
print(hitung)

