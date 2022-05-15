import matplotlib.pyplot as plt

X1, Y1 = [0,1], [1,2]
X2, Y2 = [1,1], [2,0]

plt.plot(X1,Y1,'ro-',X2,Y2,'ro-')
plt.plot([2,2],[2,1],[2,3],[1,1],[3,3],[2,0])

x=[i for i in range(4,6)]
y=[2 for i in x]
u=[5,5,5]
w=list(range(0,3))

plt.plot(x,y,'gs-',u,w,'bD--')
plt.show()
