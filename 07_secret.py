#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть зашифрованное сообщение

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

# ключ к расшифровке:
#   первое слово - 4-я буква
#   второе слово - буквы с 10 по 13, включительно
#   третье слово - буквы с 6 по 15, включительно, через одну
#   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
#   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
#
# Требуется задать конкретные индексы, например secret_message[3][12:23:4]
# Если нужны вычисления и разные пробы - делайте это в консоли пайтона, тут нужен только результат

# TODO вывести расшифрованное сообщение
first_word = secret_message[0]
second_word = secret_message[1]
third_word = secret_message[2]
fourth_word = secret_message[3]
fifth_word = secret_message[4]
fourth_word = fourth_word[7:13]
fifth_word = fifth_word[16:21]

encrypte = first_word[3] + " " + second_word[9:13] + " "  + third_word[5:15:2] + " "  + fourth_word[::-1] + " "  + fifth_word[::-1]
print(encrypte)