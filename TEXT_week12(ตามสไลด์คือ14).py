# Line chart
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 4, 10]
plt.plot(x, y, linestyle='--', marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
#กราฟเส้นประมีจุดวงกลม 5 จุด พุ่งขึ้นที่ x=5

# Bar chart
products = ['Product A', 'Product B', 'Product C']
revenue = [45000, 78000, 32000]
plt.bar(products, revenue, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.ylabel('Revenue ($)')
plt.title('Product Performance')
plt.show()
#แท่ง 3 สี Product B สูงสุด (78000)

# Pie chart
hobbies = ['Gaming', 'Reading', 'Exercise', 'Gardening']
hours = [10, 6, 5, 3]
plt.pie(hours, labels=hobbies)
plt.title('Weekly Time Spent on Hobbies')
plt.show()
#วงกลมแบ่ง 4 ส่วน Gaming ใหญ่สุด