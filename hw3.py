import matplotlib.pyplot as plt

x = []
y = []
L = []

def polynomial(x):
    return pow(x,3)+2*pow(x,2)+11*x+7
    #return pow(x,3)-x-1

def make_point():
    k = 0
    i = 0
    while i <= 20:
        x.append(round(2.5 + 0.25 * i, 3))
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
l1 = []
l2 = []

def drawgraph(type):

    i = 2.5
    while i <= 7.5:
        f.append(i)
        if type == 1:
            L.append(lagrange(i))
        elif type == 2:
            L.append(Gregory_Newton_Forward_Difference(i,0.25))
        elif type == 3:
            L.append(Gregory_Newton_backward_Difference(i,0.25))
        i += 0.001
    
    i=2.5
    while i <= 7.5:
        l1.append(i)
        l2.append(polynomial(i))
        i += 0.001
        
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    
    if type == 1:
        plt.title('Lagrange')
        plt.plot(f, L, color = 'red', label = 'Lagrange',linestyle='-')
    elif type == 2:
        plt.title('Gregory Newton Forward Difference')
        plt.plot(f, L, color = 'red', label = 'Gregory Newton Forward Difference',linestyle='-')
    elif type == 3:
        plt.title('Gregory Newton Backward Difference')
        plt.plot(f, L, color = 'red', label = 'Gregory Newton Backward Difference',linestyle='-')
    
    plt.plot(l1, l2, color = 'blue', label = 'nature',linestyle=':')
    plt.legend()
    plt.show()
    
    L.clear()
    l1.clear()
    l2.clear()
    f.clear()


w, h = 50, 50;
gnfd = [[0 for x in range(w)] for y in range(h)]

def make_table():
    i=0
    while i < len(x):
        gnfd[i][0] = y[i]
        i+=1
    for i in range(1,len(x)-1):
        for j in range(0,len(x)-i-1):
            gnfd[j][i] = round((gnfd[j+1][i-1] - gnfd[j][i-1]),3)

def mo(k,h):
    sum = 1
    for i in range(1,k+1):
        sum = sum * i * h
    return sum

def Gregory_Newton_Forward_Difference(num,h):
    ans = gnfd[0][0]
    prefixproduct = 1
    
    for i in range(1,len(x)-1):
        prefixproduct *= (num - x[i-1])
        tmp = prefixproduct * gnfd[0][i] / mo(i,h)
        ans += tmp
    return ans

def Gregory_Newton_backward_Difference(num,h):
    ans = gnfd[len(x)-1][0]
    prefixproduct = 1
    
    for i in range(1,len(x)-1):
        prefixproduct *= (num - x[len(x)-1-(i-1)])
        tmp = prefixproduct * gnfd[len(x)-i][i] / mo(i,h)
        ans += tmp
    return ans
    
def main():
    make_point()
    make_table()
    #drawgraph(1)
    #drawgraph(2)
    drawgraph(3)

if __name__ == "__main__":
    main()