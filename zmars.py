import ephem

print("Начало")
mars = ephem.Mars('2001/01/01')
print("Обращение")
constellation = ephem.constellation(mars)
print("Результат")
print(constellation)