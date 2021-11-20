user = int(input("Введите время в секундах: "))
hours = user // 3600
minutes = (user - hours * 3600) // 60
seconds = user - (hours * 3600 + minutes * 60)
print(f"Время  {hours:02} : {minutes:02} : {seconds:02}")