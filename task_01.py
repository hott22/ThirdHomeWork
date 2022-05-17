# Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_str = 'Напишите прогабврамму, удаляабвющую из текабвста все слова, содержащие'
my_str = my_str.split(" ")
print(my_str)
fragment = 'абв'
new_my_str = []
result = [new_my_str.append(i) for i in my_str if fragment not in i]
print(new_my_str)