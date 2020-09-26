"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


#def ask_user():
#  
#    Замените pass на ваш код
#    """
#    pass
#
#    
#if __name__ == "__main__":
 #   ask_user()
# Цикл  While

def ask_user():
    while True:
        try:
            usay = input("Как дела?")
            if usay == "Хорошо":
                break
        except KeyboardInterrupt:
            print("Пока!")    
            break
ask_user()        