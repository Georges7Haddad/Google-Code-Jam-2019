def index(N):
    index = []
    index2 = 1
    N = str(N)

    for i in range(0, len(N) - 1):
        index2 = index2 * 10

    for i in N:
        if i == '4':
            index.append(index2)
        index2 = index2 / 10
    return index


N = []
T = int(input("Enter number of Tests: "))
for i in range(0, T):
    N.append(int(input("Enter N: ")))
for i in range(0, T):
    A = sum(index(N[i])) * 2
    B = N[i] - A
    print("Case #", i + 1, ":", " A= ", A, " B= ", B)
    assert A + B, N
