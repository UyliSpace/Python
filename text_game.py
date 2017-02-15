# -*- coding: utf-8 -*-
import time
from random import randint

def validation_alpha():
    switch_alpha = False
    while switch_alpha == False:
        global user_name
        user_name = input()
        if user_name.isalpha() == False:
            print("Спробуй літери.")
            print("Ще раз...")
        else:
            switch_alpha = True
    if user_name == 'так':
        exit()
    return 0

def validation_digit():
    switch_digit = False
    while switch_digit == False:
        global user_age
        user_age = input()
        if user_age.isdigit() == False:
            print("Спробуй цифри.")
            print("Ще раз...")
        else:
            switch_digit = True
    return 0

def validation_choice():
    switch_digit = False
    while switch_digit == False:
        global user_choice
        user_choice = input()
        if user_choice.isdigit() == False:
            print("Спробуй цифри.")
            print("Ще раз...")
        else:
            switch_digit = True
    if int(user_choice) == 0:
        exit()
    return 0

def age_limit():
    if int(user_age) >= 36:
        print("...")
        time.sleep(1)
        print("Фізична оболонка твого персонажа занадто потріпана і не витримає проходження моєї гри.")
        print("Пропоную випити еліксир молодості і повернутися до моєї гри :)")
        exit()
    elif int(user_age) <= 9:
        print("...")
        time.sleep(1)
        print("Попий растішки і повертайся до гри ;)")
        exit()
    return 0

def bad_end():
    print("Ти програв, {0}, але в мене є для тебе подарунок:".format(user_name))
    presents = {1: "Тримай кілограмову цукерочку ;)\n",
                2: "Перстень Слави і Витримки\n",
                3: "Ручний дракон\n",
                4: "Еліксир безсмерття\n"}
    print(presents[randint(1,4)])
    print("Бувай!")

def happy_end():
    print("Вітаю, {0}!!! Ти вийшов на щасливий фінал, лови приз:".format(user_name))
    prizes = {1: "Літачок на радіоуправлінні\n",
              2: "1г темної матерії\n",
              3: "Мішок з подарунками Діда Мороза - 2018\n"}
    print(prizes[randint(1,3)])
    print("Бувай!")

def quick_exit(user_data):
    if int(user_data) == 0:
        exit()
    return 0

# Початок гри
print("========= Рада вітати тебе у грі \"Випробування долі!\" =========")
time.sleep(1)

print("Введи ім\'я свого персонажу(лише літери).....Вийти? так-> 0")
validation_alpha()

print("Скільки тобі років?.....Вийти? так-> 0")
validation_digit()
age_limit()

# Початок гри
print("--------- Починаймо гру! ---------")
print("Пустеля. Ти вже 3 дні не їв. В тебе є ніж і трішки води, щоб добратися або до найближчого міста або до оазиса.")
print("Тут ти бачиш скорпіона, який повзе в твою сторону.")
print("Твої дії?")
print("\t1. З\'їсти його. Виглядає апетитно.")
print("\t2. Вбити його, героїчно захищаючи своє життя.")
print("\t3. Просто пройти мимо. Він тобі нічого не зробив і ти не зробиш.")
print("\t0. Вийти з гри.")

print("Що ти вибираєш (цифра)?")
validation_choice()
quick_exit(user_choice)

if int(user_choice) == 1:
    print("В процесі він боляче жалить тебе, все ще хочеш його з\'їсти?")
    print("\t1. З\'їсти.")
    print("\t2. Викинути подалі.")
    print("\t0. Вийти з гри.")
    print("Що ти вибираєш (цифра)?")
    validation_choice()
    quick_exit(user_choice)

    if int(user_choice) == 1:
        print("Тебе починає охоплювати біль. Тепер все вирішить лише твоя сила волі.")
        print("Терпіти?")
        print("\t1. Терпіти.")
        print("\t2. Ні!!")
        print("\t0. Вийти з гри.")
        print("Що ти вибираєш (цифра)?")
        validation_choice()
        quick_exit(user_choice)

        if int(user_choice) == 1:
            print("Ти молодець! В свої {0} років ти все витримав!".format(user_age))
            print("Тепер ти царь скорпіонів і це хороша новина, але...")
            print("Це означає, що ти тепер босс цього рівня, тому ти мусиш залишатися тут і боротися з гравцями,")
            print("поки хтось не замінить тебе (також з\'їсть скорпіона) або вб\'є.")
            print("HAPPY END 50-50%\n")
            happy_end()

        elif int(user_choice) == 2:
            print("Ти не витримав. Ти труп, в твої-то {0} років..ех.. --> BAD END\n".format(user_age))
            bad_end()
        else:
            print("Ти вилетів за межі гри. Упс")
            exit()
    elif int(user_choice) == 2:
        print("Твій організм не зміг витримати отруту скорпіона.")
        print("Ти труп, в твої-то {0} років..ех.. --> BAD END\n".format(user_age))
        bad_end()
    else:
        print("Ти вилетів за межі гри. Упс")
        exit()
elif int(user_choice) == 2:
    print("Ти отримав рідкісну отруту скорпіона. Сонце припікає. Зупинитися під пальмою для відпочинку?")
    print("\t1. Йти далі.")
    print("\t2. Перепочити.")
    print("\t0. Вийти з гри.")
    print("Що ти вибираєш (цифра)?")
    validation_choice()
    quick_exit(user_choice)

    if int(user_choice) == 1:
        print("На останніх силах ти дійшов до оазиса. Напився води.")
        print("Набрав води в баклашку. Вилити туди отруту скорпіона?")
        print("\t1. Так.")
        print("\t2. Ні.")
        print("\t0. Вийти з гри.")
        print("Що ти вибираєш (цифра)?")
        validation_choice()
        quick_exit(user_choice)

        if int(user_choice) == 1:
            print("І ти пішов далі. По дорозі зустрів чоловіка, який просив дати йому води.")
            print("Ти вже забув про отруту. Поділитися водою?")
            print("\t1. Так.")
            print("\t2. Ні.")
            print("\t0. Вийти з гри.")
            print("Що ти вибираєш (цифра)?")
            validation_choice()
            quick_exit(user_choice)

            if int(user_choice) == 1:
                print("Чисто випадково ти переміг царя скорпіонів його ж отрутою. Оце так удача.")
                print("HAPPY END 100%\n")
                happy_end()
            elif int(user_choice) == 2:
                print("Він накинувся на тебе і...")
                print("Ти труп, в твої-то {0} років..ех.. --> BAD END\n".format(user_age))
                bad_end()
            else:
                print("Ти вилетів за межі гри. Упс")
                exit()
        elif int(user_choice) == 2:
            print("І ти пішов далі. І навіть наявність води не врятувала тебе від сухої смерті.")
            print("Ти труп, в твої-то {0} років..ех.. --> BAD END\n".format(user_age))
            bad_end()
        else:
            print("Ти вилетів за межі гри. Упс")
            exit()
    elif int(user_choice) == 2:
        print("Так приємно побути в тіні. Ти і не помітив як заснув.")
        print("Поки ти спав тебе наздогнали родичі вбитого скорпіона і зажалили тебе.")
        print("Ти труп, в твої-то {0} років..ех.. --> BAD END\n".format(user_age))
        bad_end()
    else:
        print("Ти вилетів за межі гри. Упс")
        exit()
elif int(user_choice) == 3:
    print("Твій вибір зберіг тобі трішки більше сил, яких вистачило, щоб добратися до найближчого міста.")
    print("Ти дуже голодний. Куди підеш?")
    print("\t1. В трактир.")
    print("\t2. В пекарню.")
    print("\t0. Вийти з гри.")
    print("Що ти вибираєш (цифра)?")
    validation_choice()
    quick_exit(user_choice)

    if int(user_choice) == 1:
        print("Ти напився і наївся. Сидиш задоволений і тут до тебе підходять якісь чоловіки.")
        print("Заговорити першим?")
        print("\t1. Так.")
        print("\t2. Ні.")
        print("\t0. Вийти з гри.")
        print("Що ти вибираєш (цифра)?")
        validation_choice()
        quick_exit(user_choice)

        if int(user_choice) == 1:
            print("В тебе хороший настрій, тому ти занадто самовпевнено і нагло (на думку тих чоловіків) з ними заговорив.")
            print("Ви побилися, тебе підстрелив хтось з них.")
            print("Ти труп, в твої-то {0} років..ех.. --> BAD END\n".format(user_age))
            bad_end()
        elif int(user_choice) == 2:
            print("Вони заговорили до тебе, почали задирати, хотіли пограбувати. Раптово в трактир зашла поліція.")
            print("Ти вже встиг зрадіти...")
            print("як раптом один з них неочікувано вистрелив в тебе. Ти був подібний на бандита, якого вони вже довго")
            print("розшукували. Неповезло тобі.")
            print("Ти труп, в твої-то {0} років..ех.. --> BAD END\n".format(user_age))
            bad_end()
        else:
            print("Ти вилетів за межі гри. Упс")
            exit()
    elif int(user_choice) == 2:
        print("Тут якраз напекли свіжий хліб, булочки, багети. Ти смачно поїв. Хочеш розплатитися. Яку офіціантку покличеш?")
        print("\t1. Брюнетку.")
        print("\t2. Блондинку.")
        print("\t0. Вийти з гри.")
        print("Що ти вибираєш (цифра)?")
        validation_choice()
        quick_exit(user_choice)

        if int(user_choice) == 1:
            print("Дівчина виявилася дуже приємною і милою. Запропонуєш їй зустрітися ввечері?")
            print("\t1. Так.")
            print("\t2. Ні.")
            print("\t0. Вийти з гри.")
            print("Що ти вибираєш (цифра)?")
            validation_choice()
            quick_exit(user_choice)

            if int(user_choice) == 1:
                print("Вона погодилася. Ви чудово провели час. Ти знайшов своє щастя.")
                print("HAPPY END 100%\n")
                happy_end()
            elif int(user_choice) == 2:
                print("Ти шкодував про це і потім хтось тебе підстрелив.")
                print("Ти моральний труп і просто труп, в твої-то {0} років..ех.. --> BAD END\n".format(user_age))
                bad_end()
            else:
                print("Ти вилетів за межі гри. Упс")
                exit()
        elif int(user_choice) == 2:
            print("Дівчина виявилася грубою та непривітливою. Чи залишиш ти їй на чай?")
            print("\t1. Так")
            print("\t2. Ні")
            print("\t0. Вийти з гри.")
            print("Що ти вибираєш (цифра)?")
            validation_choice()
            quick_exit(user_choice)

            if int(user_choice) == 1:
                print("Ти був настільки задоволений обідом, що залишив їй на чай.")
                print("Вийшов з пекарні і радісно крокуючи впав в колодязь.")
                print("Ти труп, в твої-то {0} років..ех.. --> BAD END\n".format(user_age))
                bad_end()
            elif int(user_choice) == 2:
                print("Блондинка сильно розізлилася на тебе. Вона була відьмою, тому вона наклала на тебе прокляття")
                print("і ти неочікувано вмер він сердечного приступу.")
                print("Ти труп, в твої-то {0} років..ех.. --> BAD END\n".format(user_age))
                bad_end()
            else:
                print("Ти вилетів за межі гри. Упс")
                exit()
        else:
            print("Ти вилетів за межі гри. Упс")
            exit()
    else:
        print("Ти вилетів за межі гри. Упс")
        exit()
else:
    print("Ти вилетів за межі гри. Упс")
    exit()
