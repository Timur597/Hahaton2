

# Задание 1:
# Напишите Программу - которая работает по принципу алгоритма Шифр Цезаря.
# Нужно создать класс состоящий из 2 методов:
# 1. Метод который ШИФРУЕТ данные.
# 2. Метода который ДЕШИФРУЕТ эти же данные.
# Представим что ваш метод получает слово состоящее из ЛЮБЫХ символов.
# Ваш 1-й метод должен вернуть зашифрованную строку.
# Алгоритм Шифрования: ASCII позиция + 7.
# Алгоритм Дешифровки: Обратная операция Алгоритма Шифрования.



# Вариант№1
# Решение:

# class CaesarCipher(object):
#     def __init__(self, offset: int):
#         self.offset = offset

#     def encode(self, message: str, shifting_mode: int = 1):
#         return_value = ""

#         for i in range(len(message)):
#             c = message[i]

#             if c.isupper():
#                 return_value += chr((ord(c) + (shifting_mode * self.offset) - 65) % 26 + 65)
#             else:
#                 return_value += chr((ord(c) + (shifting_mode * self.offset) - 97) % 26 + 97)

#         return return_value

#     def decode(self, message: str):
#         return self.encode(message, shifting_mode=-1)

# offset = int(input("Enter offset: "))  # Little test program for CaesarCipher class
# message = input("Enter message to encrypt: ")

# encryptor = CaesarCipher(offset)
# encoded_message = encryptor.encode(message)

# print("Encrypted text: {0}".format(encoded_message))
# print("Decrypted text: {0}".format(encryptor.decode(encoded_message)))

# Вариант№2

# class  CaescaeCipher(object):
#     def __init__(self,object):
#         self.object = object
# ALPHABET = ('абвгдеёжзиклмнопрстуфхчшщъыьэюя'
#             'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')


# def encryption_caesar(msg, offset):
#     """
#     Возвращает сообщение зашифрованное шифром Цезаря.
#     :param msg Сообщение
#     :param offset Смещение в алфавите

#     :return Зашифрованное сообщение
#     """

#     encrypted_alphabet = ALPHABET[offset:] + ALPHABET[:offset]
#     encrypted = []

#     for char in msg:
#         index = get_char_index(char, ALPHABET)
#         encrypted_char = encrypted_alphabet[index] if index >= 0 else char
#         encrypted.append(encrypted_char)

#     return ''.join(encrypted)


# def get_char_index(char, alphabet):
#     """
#     Возвращает индекс первого вхождения символа с сторку алфавита.
#     :param char: Символ
#     :return: Индекс
#     """
#     char_index = alphabet.find(char)

#     return char_index


# def decryption_caesar(msg, offset=None):
#     """
#     Возвращает расшифрованное сообщение, зашифрованное шифром Цезаря.
#     Если shift = None, будет пробовать расшифровывать без смещения
#     :param msg Сообщение
#     :param offset Смещение в алфавите

#     :return Расшифрованное сообщение
#     """

#     encrypted_alphabet = ALPHABET[offset:] + ALPHABET[:offset]
#     decrypted = []

#     if offset:
#         # Если известно смещение, просто дешифруем сообщение по обратно
#         for char in msg:
#             index = get_char_index(char, encrypted_alphabet)
#             encrypted_char = encrypted_alphabet[index - offset] \
#                 if index >= 0 else char
#             decrypted.append(encrypted_char)

#         return ''.join(decrypted)
#     else:
#         # Если нет, то будем дешифровать и искать вхождение слов из словаря
#         # Так как это просто пример, словарь маленький
#         dictionary = ['Привет', 'пока', 'что']

#         for offset in range(len(ALPHABET)):
#             # Каждого смещения, начиная с 0 создаем смещенный алфавит
#             encrypted_alphabet = ALPHABET[offset:] + ALPHABET[:offset]
#             for char in msg:
#                 index = get_char_index(char, encrypted_alphabet)
#                 encrypted_char = ALPHABET[index] if index >= 0 else char
#                 decrypted.append(encrypted_char)

#             decrypted = ''.join(decrypted)

#             for word in dictionary:
#                 # Если слово из словаря входит в дешифрованную строку,
#                 # возвращаем её
#                 if word in decrypted:
#                     return decrypted

#             decrypted = []  # Обнуляем расшифрованное сообщение

#     return 'Не удалось расшифровать сообщение %s' % msg


# if __name__ == '__main__':
#     message = 'Привет! Мир'
#     shift = 7 # Смещение алфавита

#     encrypted_message = encryption_caesar(message, shift)

#     print('Сообщение: %s' % message)
#     print('Зашифрованное сообщение: %s' % encrypted_message)
#     print('Расшифрованное сообщение: %s' % decryption_caesar(encrypted_message))

# # Задание 2:
# Напишите программу Logger.
# Это может быть либо функцией либо методом класса.
# Функция должна делать следующее:
# 1. Принимать Логин, Пароль1 и Пароль2.
# 2. Проверять если Логин меньше 5 символов возвращать пользователю что Логин слишком короткий.
# 3. Если Логин указан верно запустить бесконечный цикл для запроса пароля. Пока пользователь не введёт верный пароль спрашивать снова и снова.
# 4. Проверять если Пароль меньше 8 символов выводить на экран пользователю что Пароль слишком короткий.
# 5. Проверять если Пароль1 НЕ равен Пароль2 выводить на экран пользователю что пароли не совпадают.
# 6. Если все данные верны создайте файл users.txt и запишите туда Логин и Пароль пользователя в формате: Логин: <Логин Пользователя> - Пароль: <Пароль Пользователя>
# 7. Информацию о Всех Успешно Зарегистрированных Пользователей вносите в другой файл log.txt в формате: "Пользователь успешно зарегистрирован <ВРЕМЯ>"
# Время должно быть в формате: <ЧАС>:<МИНУТЫ>:<СЕКУНДЫ>.<ТЫСЯЧНЫЕ СЕКУНДЫ>

# Решение:
# import datetime
# import sys
# class Logger():
#     '''Создание класса Logger'''
#     def __init__(self,passлог,passворд,passворд2):
#         '''инициализация атрибутов логера'''
#         self.login = "Хаджимураткановскидебчик"
#         self.password = "Кутлекутянчик"
#         self.passлог = passлог
#         self.passворд = passворд
#         self.passворд2 = passворд2
#     def Проверка(self):
#         '''Проверка логина на количество символов'''
#         if len(self.login) < 5:
#             print('Логин слишком короткий')
#         else:
#             pass
#     def Проверка_Лг(self):
#         '''Проверка правильности написания логина'''
#         if self.passлог != self.login:
#             print('Логин неверный!')
#             sys.exit()
#         while True:
#             if self.passлог == self.login:
#                 print('Логин верный.')
#                 break
#     def Проверка_Пр(self):
#         while True:
#             if len(self.passворд) < 8 or self.passворд != self.password:
#                 print('Пароль не верный!')
#                 a = input('Введите пароль: ')
#                 if a == self.password:
#                     break
#             if  self.passворд == self.password:
#                 print('Пароль верный.')
#                 break
        
#     def Сверка_Паролей(self):
#         if self.passворд != self.passворд2:
#             print('Пароли не совпадают!')
#         elif self.passлог != self.login:
#             pass
#         else:
#             t = open ("haha.txt", "w")
#             t.write(f"login : {self.passлог} , password1: {self.passворд} ,password2 : {self.passворд2}")
#             t.close()
#     def Время(self):
#         current_date_time = datetime.datetime.now()
#         current_time = current_date_time.time()
#         d = open ("log.txt", "w")
#         d.write(f'Пользователь успешно зарегистрирован {current_time}')
#         d.close()
    
# Hakaton = Logger(input('Введите логин: '),input('Введите пароль: '),input('Введите пароль повторно: '))
# Hakaton.Проверка()
# Hakaton.Проверка_Лг()
# Hakaton.Проверка_Пр()
# Hakaton.Сверка_Паролей()
# Hakaton.Время()





# # Задание 3:
# Перейдите по ссылке в Google Colab и используйте набор данных под кодовым названием - user_data.
# Создайте класс который будет принимать эти данные как аргумент.
# 1.Создайте метод genders() который вернёт всё разнообразие полов в типе данных Tuple.
# Example: ("Male", "Female",...)
# 2. Создайте метод get_domain() который возвращает Tuple ДОМЕННЫХ имён электронной почты ВСЕХ пользователей.
# Что такое доменное имя:
# python.itc@gmail.com
# 1. ИМЯ ПОЧТЫ - python.itc
# 2. РАЗДЕЛИТЕЛЬНЫЙ СИМВОЛ - @
# 3. ДОМЕННОЕ ИМЯ - gmail.com

# Решение:

# class User_data():
#     def __init__(self,listik):
#         self.listik = listik
#     def Genders(self):
#         for i in self.listik:
#             if i == 'Male' or i == 'Female' or i == "Hidden" or i == "Transgender":
#                 print(tuple(i))
# CC = User_data([{
#   "id": 1,
#   "first_name": "Humphrey",
#   "last_name": "Wilcox",
#   "email": "hwilcox0@odnoklassniki.ru",
#   "gender": "Male",
#   "ip_address": "80.232.175.95"
# }, {
#   "id": 2,
#   "first_name": "Erhard",
#   "last_name": "Byart",
#   "email": "ebyart1@addthis.com",
#   "gender": "Male",
#   "ip_address": "125.7.237.155"
# }, {
#   "id": 3,
#   "first_name": "Brok",
#   "last_name": "Leiden",
#   "email": "bleiden2@usnews.com",
#   "gender": "Male",
#   "ip_address": "108.201.248.102"
# }, {
#   "id": 4,
#   "first_name": "Gradeigh",
#   "last_name": "Spreckley",
#   "email": "gspreckley3@marriott.com",
#   "gender": "Male",
#   "ip_address": "90.169.195.245"
# }, {
#   "id": 5,
#   "first_name": "Trueman",
#   "last_name": "McArd",
#   "email": "tmcard4@cargocollective.com",
#   "gender": "Male",
#   "ip_address": "249.26.239.198"
# }, {
#   "id": 6,
#   "first_name": "Giacobo",
#   "last_name": "Rishworth",
#   "email": "grishworth5@merriam-webster.com",
#   "gender": "Male",
#   "ip_address": "156.104.68.219"
# }, {
#   "id": 7,
#   "first_name": "Marcia",
#   "last_name": "Burney",
#   "email": "mburney6@gmpg.org",
#   "gender": "Female",
#   "ip_address": "52.104.185.232"
# }, {
#   "id": 8,
#   "first_name": "Court",
#   "last_name": "Haysar",
#   "email": "chaysar7@eepurl.com",
#   "gender": "Hidden",
#   "ip_address": "60.138.180.175"
# }, {
#   "id": 9,
#   "first_name": "Penn",
#   "last_name": "Slatten",
#   "email": "pslatten8@narod.ru",
#   "gender": "Male",
#   "ip_address": "216.91.212.228"
# }, {
#   "id": 10,
#   "first_name": "Rayna",
#   "last_name": "Jacobsson",
#   "email": "rjacobsson9@4shared.com",
#   "gender": "Female",
#   "ip_address": "158.81.126.17"
# }, {
#   "id": 11,
#   "first_name": "Elissa",
#   "last_name": "Milch",
#   "email": "emilcha@ucoz.ru",
#   "gender": "Female",
#   "ip_address": "160.46.17.104"
# }, {
#   "id": 12,
#   "first_name": "Cissiee",
#   "last_name": "Dever",
#   "email": "cdeverb@dailymail.co.uk",
#   "gender": "Hidden",
#   "ip_address": "198.12.171.92"
# }, {
#   "id": 13,
#   "first_name": "Lorie",
#   "last_name": "Cavozzi",
#   "email": "lcavozzic@apache.org",
#   "gender": "Female",
#   "ip_address": "252.228.114.151"
# }, {
#   "id": 14,
#   "first_name": "Shelton",
#   "last_name": "Pipe",
#   "email": "spiped@opera.com",
#   "gender": "Male",
#   "ip_address": "217.193.203.141"
# }, {
#   "id": 15,
#   "first_name": "Cordell",
#   "last_name": "Hrinchenko",
#   "email": "chrinchenkoe@ovh.net",
#   "gender": "Transgender",
#   "ip_address": "147.76.167.191"
# }, {
#   "id": 16,
#   "first_name": "Dyanna",
#   "last_name": "Sizzey",
#   "email": "dsizzeyf@xing.com",
#   "gender": "Female",
#   "ip_address": "8.177.20.12"
# }, {
#   "id": 17,
#   "first_name": "Felice",
#   "last_name": "Floyed",
#   "email": "ffloyedg@instagram.com",
#   "gender": "Male",
#   "ip_address": "4.150.254.58"
# }, {
#   "id": 18,
#   "first_name": "Arel",
#   "last_name": "Donoher",
#   "email": "adonoherh@youtu.be",
#   "gender": "Male",
#   "ip_address": "186.214.243.230"
# }, {
#   "id": 19,
#   "first_name": "Kristoffer",
#   "last_name": "Carvill",
#   "email": "kcarvilli@xinhuanet.com",
#   "gender": "Male",
#   "ip_address": "58.204.72.103"
# }, {
#   "id": 20,
#   "first_name": "Norbie",
#   "last_name": "Oleksinski",
#   "email": "noleksinskij@free.fr",
#   "gender": "Male",
#   "ip_address": "242.192.49.216"
# }])   
# CC.Genders()




# # Задание 4:
# Создайте функцию которая принимает SET.
# Пример SET можете посмотреть в Google Colab под кодовым именем - data_set или создать свой минимум 7 элементов в SET.
# Сделайте так чтобы из набора данных который пришёл вам в SET можно было вытаскивать элементы по индексу.
# Выведите все элементы из набора данных в обратной последовательности. Обязательно сделать это РЕКУРСИВНО!



# # Задание 5:
# Создайте функцию world() которая возвращает вам "Hello World"
# Создайте функцию kyrgyzstan() которая возвращает вам "Hello Kyrgyzstan"
# Создайте функцию bishkek() которая возвращает вам "Hello Bishkek"
# ОБЯЗАТЕЛЬНО НЕ ИСПОЛЬЗОВАТЬ IF!
# Спросите у пользователя какую из функций запустить и пусть пользователь c Терминала напишет код который запустит одну из трёх функций.
# Подсказка: Встроенные Функции.

# Решение:

# def world(a="Hello ",b="World"):
#         return a+b

# def kyrgyzstan(e="Hello ",r="Kyrgyzstan"):
#         return e+r

# def bishkek(q="Hello ",w="Bishkek"):
#         return q+w

# i = input("Спросите у пользователя какую из функций запустить и пусть пользователь: ")
# print(bishkek())


# # Задание 6:
# Представьте вы работаете в Банке, но Банк не работает по выходным.
# Если клиент захочет взять кредит в пятницу Вы должны сказать что сейчас это не возможно и вернуть ему время когда эта операция будет доступна.
# Пятницы выпали на 5, 12, 19, 26 числа.
# Если в дате которую введёт пользователь будет 5, 12, 19 или 26 число любого месяца вы должны вернуть ему дату в таком же формате как он и отправил.
# Напишите функцию которая спрашивает у пользователя дату в формате: ГГГГ-ММ-ДД ЧЧ:ММ
# 1. Если пользователь ввёл не верный формат Вы должны вернуть ему - "Неверный формат!"
# 2. Если пользователь всё ввёл верно верните ему дату которую он ввёл + 60 часов.
# 3. Можете использовать datetime module, можете использовать другие модули.



# # Задание 7:
# Создайте функцию которая возвращает список 10 любых Linux команд.
# Вызовите вашу функцию и сохраните её в переменную.
# Затем удалите ТОЛЬКО функцию так ЧТОБЫ при втором запуске вашего файла не было ошибок NameError.
# Переменную не удаляйте!
# Решение:

# def list():
#     command_list = ["ls","cd","mv","cp","sudo","touch","cat","nano","mkdir","find"]
#     return command_list
# a=list()
# print(a)