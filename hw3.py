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
        x.append(2.5 + 0.2 * i)
        print(2.5+0.2*i)
        y.append(polynomial(x[k]))
        i += 1
        k += 1

    #print(y[0:len(y)])
    


def lagrange(num):
	ans = 0
	for i in range(0,25):
		s = 0
		for j in range(0,25):
			if i==j:
				continue
			s = s * (num-x[j]) / (x[i] - x[j])
		ans += s
	return ans

f = []

def lagrange_drawgraph():
    k = 0
    i = 2.5
    while i <= 7.5:
        f.append(i) 
        L.append(lagrange(i))
        k += 1
        i += 0.001

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Lagrange')
    plt.plot(f,L)
    plt.show()

def main():
    make_point()
    #lagrange_drawgraph()

if __name__ == "__main__":
    main()