"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

#def ask_user():
  
#    pass
    
#if __name__ == "__main__":
#    ask_user()
# Работа со словарем
dic = {"Как дела?":"Хорошо!", 
       "Что делаешь?":"Программирую",
       "Когда перерыв?":"Скоро",
       "Пойдешь в кафе?":"С удовольствием!"}
def check(dic):
    while True:      
        try:
           a = input("Введите Ваш вопрос :") 
            if a in dic and a != "Стоп":
                print(dic[a])
            else:     
                if a == "Стоп":
                    print("Спасибо за работу со словарем")
                    break 
        except KeyboardInterrupt:
            print("Исключение KeyboardInterrupt") 
            break   
        else:
            print("Исключений не произошло") 
            
check(dic)          