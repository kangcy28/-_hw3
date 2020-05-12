import matplotlib.pyplot as plt

x = []
y = []
L = []

def polynomial(x):
    return pow(x,3)+2*pow(x,2)+11*x+7

def make_point():
    k = 0
    i = 0
    while i <= 25:
        x.append(round(2.50 + 0.20 * i, 1))
        y.append(round(polynomial(x[k]),3))
        i += 1
        k += 1
    
def lagrange(num):  
    ans = 0
    for i in range(0,len(x)-1):
        s = 1
        s *= y[i]
        for j in range(0,len(y)-1):
            if i==j:
                continue
            s *= (num-x[j]) / (x[i] - x[j])
        ans += s
    return round(ans,6)
f = []

def lagrange_drawgraph():
    k = 0
    i = 2.5
    #print(lagrange(2.5))
    #print(lagrange(7.5))

    while i <= 7.5:
        f.append(i) 
        L.append(lagrange(i))
        k += 1
        i += 0.001
        #print(f[-1])
        #print(L[-1])
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Lagrange')
    plt.plot(f,L)
    plt.show()

def main():
    make_point()
    lagrange_drawgraph()


if __name__ == "__main__":
    main()