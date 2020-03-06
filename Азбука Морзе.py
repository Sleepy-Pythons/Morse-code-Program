MorseCode = {'A': '.-',  # Кодирование латиницы
             'B': '-...',
             'C': '-.-.',
             'D': '-..',
             'E': '.',
             'F': '..-.',
             'G': '--.',
             'H': '....',
             'I': '..',
             'J': '.---',
             'K': '-.-',
             'L': '.-..',
             'M': '--',
             'N': '-.',
             'O': '---',
             'P': '.--.',
             'Q': '--.-',
             'R': '.-.',
             'S': '...',
             'T': '-',
             'U': '..-',
             'V': '...-',
             'W': '.--',
             'X': '-..-',
             'Y': '-.--',
             'Z': '--..',
             'Ö': '---.',
             'CH': '----',
             'Ñ': '--.--',
             'É': '..-..',
             'Ü': '..--',
             'Ä': '.-.-'
             }

KirCoding = {'А': '.-',  # Кодирование кириллицы
             'Б': '-...',
             'В': '.--',
             'Г': '--.',
             'Д': '-..',
             'Е': '.',
             'Ж': '...-',
             'З': '--..',
             'И': '..',
             'Й': '.---',
             'К': '-.-',
             'Л': '.-..',
             'М': '--',
             'Н': '-.',
             'О': '---',
             'П': '.--.',
             'Р': '.-.',
             'С': '...',
             'Т': '-',
             'У': '..-',
             'Ф': '..-.',
             'Х': '....',
             'Ц': '-.-.',
             'Ч': '---.',
             'Ш': '----',
             'Щ': '--.-',
             'Ъ': '--.--',
             'Ь': '-..-',
             'Ы': '-.--',
             'Э': '..-..',
             'Ю': '..--',
             'Я': '.-.-'
             }

KirDecoding = {'.-': 'А',
               '-...': 'Б',
               '.--': 'В',
               '--.': 'Г',
               '-..': 'Д',
               '.': 'Е',
               '...-': 'Ж',
               '--..': 'З',
               '..': 'И',
               '.---': 'Й',
               '-.-': 'К',
               '.-..': 'Л',
               '--': 'М',
               '-.': 'Н',
               '---': 'О',
               '.--.': 'П',
               '.-.': 'Р',
               '...': 'С',
               '-': 'Т',
               '..-': 'У',
               '..-.': 'Ф',
               '....': 'Х',
               '-.-.': 'Ц',
               '---.': 'Ч',
               '----': 'Ш',
               '--.-': 'Щ',
               '--.--': 'Ъ',
               '-..-': 'Ь',
               '-.--': 'Ы',
               '..-..': 'Э',
               '..--': 'Ю',
               '.-.-': 'Я'
               }

MorseCodeDecoding = {'.-': 'A',
                     '-...': 'B',
                     '-.-.': 'C',
                     '-..': 'D',
                     '.': 'E',
                     '..-.': 'F',
                     '--.': 'G',
                     '....': 'H',
                     '..': 'I',
                     '.---': 'J',
                     '-.-': 'K',
                     '.-..': 'L',
                     '--': 'M',
                     '-.': 'N',
                     '---': 'O',
                     '.--.': 'P',
                     '--.-': 'Q',
                     '.-.': 'R',
                     '...': 'S',
                     '-': 'T',
                     '..-': 'U',
                     '...-': 'V',
                     '.--': 'W',
                     '-..-': 'X',
                     '-.--': 'Y',
                     '--..': 'Z',
                     '---.': 'Ö',
                     '----': 'CH',
                     '--.--': 'Ñ',
                     '..-..': 'É',
                     '..--': 'Ü',
                     '.-.-': 'Ä'
                     }


def encode_to_morse(text):
    # функция кодирования входного текста в Азбуку Морзе
    global MorseCode  # объявление глобальной переменной - словаря,
    # где ключ - буква, а значение эта буква в Азбуке Морзе
    text = text.upper().split()  # разбиение текста в список слов
    output = ''
    for i in text:
        for k in i:
            if k in MorseCode:
                output += MorseCode[k] + ' '
                # Добавление кода в переменную вывода
            else:
                output += k
    return output.rstrip()


def decode_from_morse(code):
    # функция декодирования входного текста на латиницу
    global MorseCodeDecoding  # объявление глобальной переменной - словаря,
    # где ключ - код Морзе, а значение буква, соответствующая этому коду
    text = code.split()  # разбиение кода в список
    output = ''
    for i in text:
        if i in MorseCodeDecoding:
            output += MorseCodeDecoding[i] + ' '
            # Добавление букв в переменную вывода
        else:
            output += i
    return output.rstrip()


def encode_kir_to_morse(text):
    # функция кодирования входного текста в Азбуку Морзе
    global KirCoding  # объявление глобальной переменной - словаря,
    # где ключ - буква, а значение эта буква в Азбуке Морзе
    text = text.upper().split()  # разбиение текста в список слов
    output = ''
    for i in text:
        for k in i:
            if k in KirCoding:
                output += KirCoding[k] + ' '
                # Добавление кода в переменную вывода
            else:
                output += k
    return output.rstrip()


def decode_kir_from_morse(code):
    # функция декодирования входного текста на кириллицу
    global KirDecoding  # объявление глобальной переменной - словаря,
    # где ключ - код Морзе, а значение буква, соответствующая этому коду
    text = code.split()  # разбиение кода в список
    output = ''
    for i in text:
        if i in KirDecoding:
            output += KirDecoding[i] + ' '
            # Добавление букв в переменную вывода
        else:
            output += i
    return output.rstrip()


def main():
    # функция, обеспечивающая взаимодействие с пользователем
    print("Привет! Эта программа поможет кодировать и "
          "декодировать сообщения на Азбуке Морзе!")
    while True:
        print("Нажмите 1, чтобы закодировать сообщение, "
              "напечатанное на латинице.\n"
              "Нажмите 2, чтобы декодировать сообщение, "
              "напечатанное на латинице.\n"
              "Нажмите 3, чтобы закодировать сообщение, "
              "напечатанное на кирилице.\n"
              "Нажмите 4, чтобы декодировать сообщение, "
              "напечатанное на кирилице.")
        command = input()
        message = input("Введите Ваше сообщение: ")
        if len(message) != 0:
            if command == "1":
                print(f"Ваше сообщение на Азбуке Морзе: "
                      f"{encode_to_morse(message)}")
            elif command == "2":
                print(f"Ваше сообщение на латинице: "
                      f"{decode_from_morse(message)}")
            elif command == "3":
                print(f"Ваше сообщение на Азбуке Морзе: "
                      f"{encode_kir_to_morse(message)}")
            elif command == "4":
                print(f"Ваше сообщение на кириллице: "
                      f"{decode_kir_from_morse(message)}")
            else:
                print("Ой! Вы ввели что-то не то! Давайте попробуем ещё раз!")
        else:
            print("Ой! Кажется, Вы ничего мне не дали на перевод!")
