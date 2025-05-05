import matplotlib.pyplot as plt

# x=[1,2,3,4]
# y=[10,20,15,30]

# plt.plot(x,y)
# plt.show()

'''Title, xlabel, ylabel'''
x=["Mon","Tue","Wed","Thu","Fri"]
y=[18,7,10,25,4]

plt.plot(x,y)
plt.title("Sales of the week")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()