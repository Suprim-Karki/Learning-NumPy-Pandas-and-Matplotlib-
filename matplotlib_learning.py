import matplotlib.pyplot as plt

# x=[1,2,3,4]
# y=[10,20,15,30]

# plt.plot(x,y)
# plt.show()

'''Title, xlabel, ylabel'''
# x=["Mon","Tue","Wed","Thu","Fri"]
# y=[18,7,10,25,4]

# plt.plot(x,y)
# plt.title("Sales of the week")
# plt.xlabel("Days")
# plt.ylabel("Sales")
# plt.show()

'''Customizing graph
Syntax: plt.plot(x,y,color="color_name",linestyle="linestyle,linewidth=value, marker=marker_symbol,label="label_name")
'''
# x=[1,2,3,4]
# y=[10,20,15,30]

# plt.plot(x,y,color="red",linestyle="--",linewidth=2,marker="o",label="2025 Sales")
# plt.legend(loc="upper left",fontsize=12)
# plt.grid(color="gray",linestyle=":",linewidth=1)
# plt.xlim(1,4)
# plt.ylim(1,40)
# plt.show()

'''Bar Chart'''
# product=["A","B","C","D"]
# sales=[1000,5000,1500,3000]

# plt.barh(product,sales,color="cyan",label="Sales 2025")
# plt.xlabel(product)
# plt.ylabel(sales)
# plt.legend("2025")
# plt.show()

'''Pie chart'''
# regions=["N","S","E","W"]
# revenue=[1000,1500,5000,3000]

# plt.pie(revenue,labels=regions, autopct="%1.1f%%",colors=["red","blue","yellow","green"],)
# plt.title("Revenue of each region")
# plt.show()


'''Histogram'''
# scores=[10,20,11,14,18,8,15,15,11,8,10,20,11,18]
# plt.hist(scores,color="purple",edgecolor="black")
# plt.xlabel("Score Range")
# plt.ylabel("Number of Students")
# plt.title("Score distribution of students")
# plt.show()

# scores=[1000,2000,1000,2000,3000,4000,5000,6000]
# plt.hist(scores,color="black",edgecolor="white")
# plt.xlabel("Price")
# plt.ylabel("Frequency")
# plt.title("Frequency of price")
# plt.show()

'''Scatterplot'''
# a=[10,20,40,20,12,34,53]
# b=[23,43,45,54,32,32,32]

# plt.scatter(a,b,marker="o",color="green",label="class A")

# hours_studies=[1,2,3,4,5]
# exam_scores=[10,33,93,12,43]
# plt.xlabel("Hours studies")
# plt.ylabel("Exam scores")
# plt.scatter(hours_studies,exam_scores,marker="o",color="red",label="class B")
# plt.legend()
# plt.grid(True)
# plt.show()

# plt.scatter([1,2,3],[50,55,60],color="blue",label="class 1")
# plt.scatter([1,2,3],[55,40,65],color="red",label="class 2")

# plt.title("Comparision of two classes")
# plt.legend()
# plt.show()


'''Subplot: Plotting 2 or more graphs together'''

x=[1,2,3,4]
y=[10,20,15,25]

plt.subplot(1,2,1)  #1 row 2 column 1st row
plt.plot(x,y)
plt.title("Line chart")
plt.show()





