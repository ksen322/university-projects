def bilet(people, child_7, child_14, cost):
    bilet_cost = (people + child_7 * 0.5 + child_14 * 0.7) * cost
    return (bilet_cost)


def habitation(people, cost_day, amount_day, dop_cost):
    habitation_cost = cost_day * amount_day + dop_cost
    return (habitation_cost)


def transport(people, n_trips, amount_day, transport_cost_p, transport_cost_7, transport_cost_14, child_7, child_14, a):
    transport_cost = (
                                 a * transport_cost_p + child_7 * transport_cost_7 + child_14 * transport_cost_14) * n_trips * amount_day
    return (transport_cost)


def food(people, food_cost_p, food_cost_7, food_cost_14, n_once, amount_day, child_7, child_14):
    food_cost = ((people * food_cost_p + child_7 * food_cost_7 + child_14 * food_cost_14) * n_once) * amount_day
    return (food_cost)


def total(a, people, child_7, child_14, cost, cost_day, amount_day, n_trips, transport_cost_p, transport_cost_7,
          transport_cost_14, food_cost_p, food_cost_7, food_cost_14, n_once, dop_cost):
    total_cost = bilet(people, child_7, child_14, cost) + habitation(people, cost_day, amount_day,
                                                                     dop_cost) + transport(people, n_trips, amount_day,
                                                                                           transport_cost_p,
                                                                                           transport_cost_7,
                                                                                           transport_cost_14, child_7,
                                                                                           child_14, a) + food(people,
                                                                                                               food_cost_p,
                                                                                                               food_cost_7,
                                                                                                               food_cost_14,
                                                                                                               n_once,
                                                                                                               amount_day,
                                                                                                               child_7,
                                                                                                               child_14)
    print('Стоимость Вашей поездки без учета дополнительных расходов будет равна: ', total_cost)


print('В какой город желаете осуществить поедку?')
print('Есть следующие города на выбор:')
print('1.Санкт-Петербург')
print('2.Тунис')
print('3.Анталья')
print('4.Сочи')
print('5.Токио')
town = input('Пожалуйста введите номер или название города: ')
if (
        town == '1' or town == '2' or town == '3' or town == '4' or town == '5' or town == 'Санкт-Петербург' or town == 'Тунис' or town == 'Анталья' or town == 'Сочи' or town == 'Токио'):
    print('Выберите класс поездки: ')
else:
    while (
            town != '1' or town != '2' or town != '3' or town != '4' or town != '5' or town != 'Санкт-Петербург' or town != 'Тунис' or town != 'Анталья' or town != 'Сочи' or town != 'Токио'):
        print('Извините, названного Вами города нет в списке. Пожалуйста введите город из списка')
        town = input('Пожалуйста введите номер или название города: ')
        if (
                town == '1' or town == '2' or town == '3' or town == '4' or town == '5' or town == 'Санкт-Петербург' or town == 'Тунис' or town == 'Анталья' or town == 'Сочи' or town == 'Токио'):
            print('Выберите класс поездки: ')
            break
print('1.Эконом')
print('2.Комфорт')
print('3.Бизнес')
print('Учтите, что в городе Анталья класса "Комфорт" нет')
CLASS = input('Пожалуйста введите номер или название класса: ')
if (CLASS == '1' or CLASS == '2' or CLASS == '3' or CLASS == 'Эконом' or CLASS == 'Комфорт' or CLASS == 'Бизнес'):
    people = int(input('Пожалуйста укажите количество взрослых пассажиров: '))
else:
    while (
            CLASS != '1' or CLASS != '2' or CLASS != '3' or CLASS != 'Эконом' or CLASS != 'Комфорт' or CLASS != 'Бизнес'):
        print('Извините, выбранного Вами класса нет в списке. Пожалуйста введите класс из списка')
        CLASS = input('Пожалуйста введите номер или название класса: ')
        if (
                CLASS == '1' or CLASS == '2' or CLASS == '3' or CLASS == 'Эконом' or CLASS == 'Комфорт' or CLASS == 'Бизнес'):
            people = int(input('Пожалуйста укажите количество взрослых пассажиров: '))
            break
child_7 = int(input('Пожалуйста укажите количество пассажиров возрастом до 14 лет: '))
child_14 = int(input('Пожалуйста укажите количество пассажиров возрастом до 7 лет: '))
amount_day = int(input('Пожалуйста введите количество дней для проживания: '))
print('Пожалуйста выберите каким транспортом будете пользоваться: ')
print('1.Общественный транспорт')
print('2.Такси')
transport_choice = input()
n_trips = int(input('Пожалуйста укажите примерную цифру, сколько Вы желаете делать поездок в день: '))
n_once = int(input('Пожалуйста укажите примерную цифру, сколько раз Вы желаете ходить в кафе/рестораны в день: '))
print(
    'Если у Вас есть дети до 3 лет, нужно ли дополнительное спальное место в номер? Если нужно, введите "Да", если не нужно, введите "Нет"')
dop_place = input()

if (town == '1' or town == 'Санкт-Петербург'):
    a = people
    if (CLASS == '1' or CLASS == 'Эконом'):
        cost = 5048
        if (dop_place == 'Да' or 'да'):
            dop_cost = 770
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(только 3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 1100
                c = c + b
                n = 1
            elif room == '2':
                b = 1500
                c = c + b
                n = 2
            elif room == '3':
                b = 2750
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 330
        food_cost_14 = 330
        food_cost_7 = 251
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 35
            transport_cost_14 = 35
            transport_cost_7 = 35
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 220
            transport_cost_7 = 0
            transport_cost_14 = 0
    if (CLASS == '2' or CLASS == 'Комфорт'):
        cost = 9919
        if (dop_place == 'Да' or 'да'):
            dop_cost = 1176
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 3700
                c = c + b
                n = 1
            elif room == '2':
                b = 5600
                c = c + b
                n = 2
            elif room == '3':
                b = 6560
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 1170
        food_cost_14 = 1170
        food_cost_7 = 819
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 35
            transport_cost_14 = 35
            transport_cost_7 = 35
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 650
            transport_cost_7 = 0
            transport_cost_14 = 0
    if (CLASS == '3' or CLASS == 'Бизнес'):
        cost = 29176
        if (dop_place == 'Да' or 'да'):
            dop_cost = 3922
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k > 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 7000
                c = c + b
                n = 1
            elif room == '2':
                b = 9360
                c = c + b
                n = 2
            elif room == '3':
                b = 16800
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 3000
        food_cost_14 = 3000
        food_cost_7 = 2100
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 35
            transport_cost_14 = 35
            transport_cost_7 = 35
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 1820
            transport_cost_7 = 0
            transport_cost_14 = 0

if (town == '2' or town == 'Тунис'):
    a = people
    if (CLASS == '1' or CLASS == 'Эконом'):
        cost = 50244
        if (dop_place == 'Да' or 'да'):
            dop_cost = 1400
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 3873
                c = c + b
                n = 1
            elif room == '2':
                b = 4929
                c = c + b
                n = 2
            elif room == '3':
                b = 5633
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 221
        food_cost_14 = 221
        food_cost_7 = 155
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 15
            transport_cost_14 = 15
            transport_cost_7 = 15
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 1755
            transport_cost_7 = 0
            transport_cost_14 = 0
    if (CLASS == '2' or CLASS == 'Комфорт'):
        cost = 56884
        if (dop_place == 'Да' or 'да'):
            dop_cost = 2038
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 6267
                c = c + b
                n = 1
            elif room == '2':
                b = 7746
                c = c + b
                n = 2
            elif room == '3':
                b = 11971
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 1090
        food_cost_14 = 1090
        food_cost_7 = 763
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 15
            transport_cost_14 = 15
            transport_cost_7 = 15
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 2777
            transport_cost_7 = 0
            transport_cost_14 = 0
    if (CLASS == '3' or CLASS == 'Бизнес'):
        cost = 118582
        if (dop_place == 'Да' or 'да'):
            dop_cost = 2573
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 8380
                c = c + b
                n = 1
            elif room == '2':
                b = 12127
                c = c + b
                n = 2
            elif room == '3':
                b = 19560
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 3750
        food_cost_14 = 3750
        food_cost_7 = 2625
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 15
            transport_cost_14 = 15
            transport_cost_7 = 15
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 5700
            transport_cost_7 = 0
            transport_cost_14 = 0

if (town == '3' or town == 'Анталья'):
    a = people
    if (CLASS == '1' or CLASS == 'Эконом'):
        cost = 15041
        if (dop_place == 'Да' or 'да'):
            dop_cost = 1232
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 2425
                c = c + b
                n = 1
            elif room == '2':
                b = 3486
                c = c + b
                n = 2
            elif room == '3':
                b = 4690
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 327
        food_cost_14 = 327
        food_cost_7 = 229
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 50
            transport_cost_14 = 50
            transport_cost_7 = 50
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 2125
            transport_cost_7 = 0
            transport_cost_14 = 0
    if (CLASS == '2' or CLASS == 'Комфорт'):
        print('Такого класса нет в данном городе, приносим свои извинения')
    if (CLASS == '3' or CLASS == 'Бизнес'):
        cost = 112772
        if (dop_place == 'Да' or 'да'):
            dop_cost = 17232
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 10140
                c = c + b
                n = 1
            elif room == '2':
                b = 14083
                c = c + b
                n = 2
            elif room == '3':
                b = 21125
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 2500
        food_cost_14 = 2500
        food_cost_7 = 1750
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 50
            transport_cost_14 = 50
            transport_cost_7 = 50
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 4000
            transport_cost_7 = 0
            transport_cost_14 = 0

if (town == '4' or town == 'Сочи'):
    a = people
    if (CLASS == '1' or CLASS == 'Эконом'):
        cost = 6119
        if (dop_place == 'Да' or 'да'):
            dop_cost = 1136
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 1800
                c = c + b
                n = 1
            elif room == '2':
                b = 3900
                c = c + b
                n = 2
            elif room == '3':
                b = 4200
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 400
        food_cost_14 = 400
        food_cost_7 = 280
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 19
            transport_cost_14 = 19
            transport_cost_7 = 19
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 199
            transport_cost_7 = 0
            transport_cost_14 = 0
    if (CLASS == '2' or CLASS == 'Комфорт'):
        cost = 12224
        if (dop_place == 'Да' or 'да'):
            dop_cost = 2131
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 3650
                c = c + b
                n = 1
            elif room == '2':
                b = 5150
                c = c + b
                n = 2
            elif room == '3':
                b = 7100
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 1000
        food_cost_14 = 1000
        food_cost_7 = 700
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 19
            transport_cost_14 = 19
            transport_cost_7 = 19
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 399
            transport_cost_7 = 0
            transport_cost_14 = 0
    if (CLASS == '3' or CLASS == 'Бизнес'):
        cost = 42774
        if (dop_place == 'Да' or 'да'):
            dop_cost = 8435
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 7100
                c = c + b
                n = 1
            elif room == '2':
                b = 9700
                c = c + b
                n = 2
            elif room == '3':
                b = 12800
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 2550
        food_cost_14 = 2550
        food_cost_7 = 1785
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 19
            transport_cost_14 = 19
            transport_cost_7 = 0
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 2300
            transport_cost_7 = 0
            transport_cost_14 = 0

if (town == '5' or town == 'Токио'):
    a = people
    if (CLASS == '1' or CLASS == 'Эконом'):
        cost = 48095
        if (dop_place == 'Да' or 'да'):
            dop_cost = 1034
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 3342
                c = c + b
                n = 1
            elif room == '2':
                b = 4011
                c = c + b
                n = 2
            elif room == '3':
                b = 6016
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 388
        food_cost_14 = 388
        food_cost_7 = 272
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 128
            transport_cost_14 = 128
            transport_cost_7 = 128
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 11911
            transport_cost_7 = 0
            transport_cost_14 = 0
    if (CLASS == '2' or CLASS == 'Комфорт'):
        cost = 139347
        if (dop_place == 'Да' or 'да'):
            dop_cost = 2241
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 8088
                c = c + b
                n = 1
            elif room == '2':
                b = 12875
                c = c + b
                n = 2
            elif room == '3':
                b = 18088
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 1331
        food_cost_14 = 1331
        food_cost_7 = 932
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost = 128
            transport_cost_14 = 128
            transport_cost_7 = 128
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 12349
            transport_cost_7 = 0
            transport_cost_14 = 0
    if (CLASS == '3' or CLASS == 'Бизнес'):
        cost = 177795
        if (dop_place == 'Да' or 'да'):
            dop_cost = 4925
        elif (dop_place == 'Нет' or 'нет'):
            dop_cost = 0
        print('Доступны следующие типы номеров:')
        print('1.Одноместный(только 1 человек)')
        print('2.Двухместный(только 2 человека)')
        print('3.Трехместный(3 человека)')
        print(
            'Обратите внимание, что в каждом номере определенное количество места, т.е., например, если Вы выбирате двухместный номер, то вас должно быть 2 человека. Не больше и не меньше')
        k = people + child_7 + child_14
        c = 0
        while k != 0:
            room = input('Пожалуйста введите номер комнаты, в которой собираетесь жить: ')
            if room == '1':
                b = 35589
                c = c + b
                n = 1
            elif room == '2':
                b = 45873
                c = c + b
                n = 2
            elif room == '3':
                b = 86712
                c = c + b
                n = 3
            k = k - n
        cost_day = c
        food_cost_p = 3327
        food_cost_14 = 3327
        food_cost_7 = 2329
        if (transport_choice == '1' or transport_choice == 'Общественный транспорт'):
            transport_cost_p = 128
            transport_cost_14 = 128
            transport_cost_7 = 128
        elif (transport_choice == '2' or transport_choice == 'Такси'):
            a = people
            a = 1
            transport_cost_p = 35511
            transport_cost_7 = 0
            transport_cost_14 = 0

total(a, people, child_7, child_14, cost, cost_day, amount_day, n_trips, transport_cost_p, transport_cost_7,
      transport_cost_14, food_cost_p, food_cost_7, food_cost_14, n_once, dop_cost)

