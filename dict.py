"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

#def ask_user():
  #  """
  #  Замените pass на ваш код
  #  """
  #  pass
    
#if __name__ == "__main__":
#    ask_user()
# Работа со словарем
dic = {"Как дела?":"Хорошо!", 
       "Что делаешь?":"Программирую",
       "Когда перерыв?":"Скоро",
       "Пойдешь в кафе?":"С удовольствием!"}
def check(dic):
    while True:      
        a = input("Введите Ваш вопрос :")
        if a in dic and a != "Стоп":
            print(dic[a])
        else:    
            if a == "Стоп":
                print("Спасибо за работу со словарем")
                break
check(dic)            