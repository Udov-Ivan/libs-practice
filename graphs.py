import matplotlib.pyplot as plt

days = ['Пн', 'Вв', 'Ср', 'Чт', 'Пт']
coffee_sales = [45, 50, 42, 60, 85]
#

# plt.title("Тренд продажів кави")
# plt.xlabel("Дні тижня")
# plt.ylabel("Кількість чашок")
# plt.grid(True) # Вмикаємо сітку
# plt.show() # Відображаємо результат

hours_studied = [1, 2, 3, 4, 5, 6]
exam_scores = [40, 50, 65, 70, 85, 90]

plt.figure(figsize=(8, 4))
plt.scatter(hours_studied, exam_scores, color='red', s=150, alpha=0.7) #

plt.plot(days, coffee_sales, color='green', marker='o', linestyle='--')
plt.title("Залежність балів від часу підготовки")
plt.xlabel("Години підготовки")
plt.ylabel("Бал за іспит")
plt.show()