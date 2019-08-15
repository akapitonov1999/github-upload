# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 17:05:57 2019

@author: Andrey Kapitonov

akapitonov1999@gmail.com

"""

import tkinter as tk
import easygui
import numpy as np
import numpy.random.common
import numpy.random.bounded_integers
import numpy.random.entropy
import pandas as pd
import itertools
import statistics as stat
import re
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

plt.style.use('bmh')  # bmh, fivethirtyeight, ggpolt, dark_background, grayscale, seaborn (special lib!)
from PIL import Image


class Application:
    def __init__(self):
        pass

    if __name__ == '__main__':
        pass


# supportive function for licence agreement function

def button_clicked():
    a = var.get()
    if a == 0:
        root.destroy()
    if a == 1:
        quit()


# licence agreement function
def page():
    global root
    global button2, var
    root = tk.Tk()
    root.title("licence agreement")
    var = tk.IntVar()
    text = tk.Text(root)
    text.pack(side='left')
    text.insert(tk.END, '''SportReviewer 1.0.0
Copyright (c) 2019 - 2029 Andrey Kapitonov

*** END USER LICENSE AGREEMENT ***

IMPORTANT: PLEASE READ THIS LICENSE CAREFULLY BEFORE USING THIS SOFTWARE.

1. LICENSE

By receiving, opening the file package, and/or using SportReviewer 1.0.0("Software") containing this software, you agree that this End User User License Agreement(EULA) is a legally binding and valid contract and agree to be bound by it. You agree to abide by the intellectual property laws and all of the terms and conditions of this Agreement.

Unless you have a different license agreement signed by Andrey Kapitonov your use of SportReviewer 1.0.0 indicates your acceptance of this license agreement and warranty.

Subject to the terms of this Agreement, Andrey Kapitonov grants to you a limited, non-exclusive, non-transferable license, without right to sub-license, to use SportReviewer 1.0.0 in accordance with this Agreement and any other written agreement with Andrey Kapitonov. Andrey Kapitonov does not transfer the title of SportReviewer 1.0.0 to you; the license granted to you is not a sale. This agreement is a binding legal agreement between Andrey Kapitonov and the purchasers or users of SportReviewer 1.0.0.

If you do not agree to be bound by this agreement, remove SportReviewer 1.0.0 from your computer now and, if applicable, promptly return to Andrey Kapitonov by mail any copies of SportReviewer 1.0.0 and related documentation and packaging in your possession.

2. DISTRIBUTION

SportReviewer 1.0.0 and the license herein granted shall not be copied, shared, distributed, re-sold, offered for re-sale, transferred or sub-licensed in whole or in part except that you may make one copy for archive purposes only. For information about redistribution of SportReviewer 1.0.0 contact Andrey Kapitonov.

3. USER AGREEMENT

3.1 Use

Your license to use SportReviewer 1.0.0 is limited to the number of licenses purchased by you. You shall not allow others to use, copy or evaluate copies of SportReviewer 1.0.0.

3.2 Use Restrictions

You shall use SportReviewer 1.0.0 in compliance with all applicable laws and not for any unlawful purpose. Without limiting the foregoing, use, display or distribution of SportReviewer 1.0.0 together with material that is pornographic, racist, vulgar, obscene, defamatory, libelous, abusive, promoting hatred, discriminating or displaying prejudice based on religion, ethnic heritage, race, sexual orientation or age is strictly prohibited.

Each licensed copy of SportReviewer 1.0.0 may be used on one single computer location by one user. Use of SportReviewer 1.0.0 means that you have loaded, installed, or run SportReviewer 1.0.0 on a computer or similar device. If you install SportReviewer 1.0.0 onto a multi-user platform, server or network, each and every individual user of SportReviewer 1.0.0 must be licensed separately.

You may make one copy of SportReviewer 1.0.0 for backup purposes, providing you only have one copy installed on one computer being used by one person. Other users may not use your copy of SportReviewer 1.0.0 . The assignment, sublicense, networking, sale, or distribution of copies of SportReviewer 1.0.0 are strictly forbidden without the prior written consent of Andrey Kapitonov. It is a violation of this agreement to assign, sell, share, loan, rent, lease, borrow, network or transfer the use of SportReviewer 1.0.0. If any person other than yourself uses SportReviewer 1.0.0 registered in your name, regardless of whether it is at the same time or different times, then this agreement is being violated and you are responsible for that violation!

3.3 Copyright Restriction

This Software contains copyrighted material, trade secrets and other proprietary material. You shall not, and shall not attempt to, modify, reverse engineer, disassemble or decompile SportReviewer 1.0.0. Nor can you create any derivative works or other works that are based upon or derived from SportReviewer 1.0.0 in whole or in part.

Andrey Kapitonov's name, logo and graphics file that represents SportReviewer 1.0.0 shall not be used in any way to promote products developed with SportReviewer 1.0.0 . Andrey Kapitonov retains sole and exclusive ownership of all right, title and interest in and to SportReviewer 1.0.0 and all Intellectual Property rights relating thereto.

Copyright law and international copyright treaty provisions protect all parts of SportReviewer 1.0.0, products and services. No program, code, part, image, audio sample, or text may be copied or used in any way by the user except as intended within the bounds of the single user program. All rights not expressly granted hereunder are reserved for Andrey Kapitonov.

3.4 Limitation of Responsibility

You will indemnify, hold harmless, and defend Andrey Kapitonov , its employees, agents and distributors against any and all claims, proceedings, demand and costs resulting from or in any way connected with your use of Andrey Kapitonov's Software.

In no event (including, without limitation, in the event of negligence) will Andrey Kapitonov , its employees, agents or distributors be liable for any consequential, incidental, indirect, special or punitive damages whatsoever (including, without limitation, damages for loss of profits, loss of use, business interruption, loss of information or data, or pecuniary loss), in connection with or arising out of or related to this Agreement, SportReviewer 1.0.0 or the use or inability to use SportReviewer 1.0.0 or the furnishing, performance or use of any other matters hereunder whether based upon contract, tort or any other theory including negligence.

Andrey Kapitonov's entire liability, without exception, is limited to the customers' reimbursement of the purchase price of the Software (maximum being the lesser of the amount paid by you and the suggested retail price as listed by Andrey Kapitonov ) in exchange for the return of the product, all copies, registration papers and manuals, and all materials that constitute a transfer of license from the customer back to Andrey Kapitonov.

3.5 Warranties

Except as expressly stated in writing, Andrey Kapitonov makes no representation or warranties in respect of this Software and expressly excludes all other warranties, expressed or implied, oral or written, including, without limitation, any implied warranties of merchantable quality or fitness for a particular purpose.

3.6 Governing Law

This Agreement shall be governed by the law of the Belarus applicable therein. You hereby irrevocably attorn and submit to the non-exclusive jurisdiction of the courts of Belarus therefrom. If any provision shall be considered unlawful, void or otherwise unenforceable, then that provision shall be deemed severable from this License and not affect the validity and enforceability of any other provisions.

3.7 Termination

Any failure to comply with the terms and conditions of this Agreement will result in automatic and immediate termination of this license. Upon termination of this license granted herein for any reason, you agree to immediately cease use of SportReviewer 1.0.0 and destroy all copies of SportReviewer 1.0.0 supplied under this Agreement. The financial obligations incurred by you shall survive the expiration or termination of this license.

4. DISCLAIMER OF WARRANTY

THIS SOFTWARE AND THE ACCOMPANYING FILES ARE SOLD "AS IS" AND WITHOUT WARRANTIES AS TO PERFORMANCE OR MERCHANTABILITY OR ANY OTHER WARRANTIES WHETHER EXPRESSED OR IMPLIED. THIS DISCLAIMER CONCERNS ALL FILES GENERATED AND EDITED BY SportReviewer 1.0.0 AS WELL.

5. CONSENT OF USE OF DATA

You agree that Andrey Kapitonov may collect and use information gathered in any manner as part of the product support services provided to you, if any, related to SportReviewer 1.0.0.Andrey Kapitonov may also use this information to provide notices to you which may be of use or interest to you.
''')
    rbutton1 = tk.Radiobutton(root, text='Accept', variable=var, value=0)
    rbutton2 = tk.Radiobutton(root, text='Decline', variable=var, value=1)
    rbutton1.pack()
    rbutton2.pack()
    button2 = tk.Button(root, bg="red", text="Ok", command=button_clicked)
    button2.pack()
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side='left')
    scrollbar['command'] = text.yview
    text['yscrollcommand'] = scrollbar.set
    root.mainloop()


# supportive function for licence agreement function
def licence_select():
    root = root

    root.mainloop()


# function for password
def passwording():
    msg = 'Enter the password'
    title = 'Password_Box'
    fieldNames = ['Password']
    fieldValues = []
    fieldValues = easygui.passwordbox(msg, title, fieldNames)
    if fieldValues != 'vasko':
        passwording()
    else:
        pass


def getlist():
    global start_lines
    with open('BigList.dat') as file:
        start_lines = file.readlines()
    file.close()


def List_check():
    for index, value in enumerate(TeamList, 1):
        print("{}. {}".format(index, value))


def adding_sp():
    msg = 'Введите ФИО добавляемого спортсмена'
    title = 'Добавление спортсмена'
    FieldNames = ['ФИО']
    sportsman = easygui.enterbox(msg, title, FieldNames)
    TeamList.append(sportsman)
    z = open('BigList.dat', 'a')
    z.write(sportsman + '\n')
    f = open('file_' + (sportsman) + '.dat', 'a')
    f.write(sportsman + '\n')
    f.close()
    MainMenuFront()


def deleting_sp():
    msg = 'Выберете спортсмена'
    title = 'Удаление спортсмена'
    choises = TeamList
    choise = easygui.choicebox(msg, title, choises)
    ch = choise
    main_file = open('BigList.dat').read()  # your main dataBase file
    filter_file = open('Filter.dat', 'w')
    filter_file.write(main_file)
    filter_file.close()
    main_file = open('BigList.dat', 'w')
    for line in open('Filter.dat'):
        if ch not in line:  # remove a specific string
            main_file.write(line)  # put all strings back to your db except deleted
        else:
            pass
    main_file.close()
    MainMenu()


def sp_choise():
    msg = 'Выберете спортсмена'
    title = 'Выбор спортсмена'
    choises = TeamList
    choise = easygui.choicebox(msg, title, choises)
    global spch
    spch = choise
    spch = re.sub('\n', '', spch)
    MainSPMenu()


def MainMenu():
    getlist()
    global TeamList
    TeamList = start_lines
    msg = 'Выбор действия'
    title = 'Главное меню'
    choises = ['Добавление спортсмена', 'Удаление спортсмена', 'Выбор спортсмена', 'Инфо']
    choise = easygui.choicebox(msg, title, choises)
    if choise == 'Добавление спортсмена':
        adding_sp()
    elif choise == 'Удаление спортсмена':
        deleting_sp()
    elif choise == 'Выбор спортсмена':
        sp_choise()
    elif choise == 'Инфо':
        Information()


def MainMenuBack():
    getlist()
    page()
    passwording()
    global TeamList
    TeamList = start_lines
    msg = 'Выбор действия'
    title = 'Главное меню'
    choises = ['Добавление спортсмена', 'Удаление спортсмена', 'Выбор спортсмена', 'Инфо']
    choise = easygui.choicebox(msg, title, choises)
    if choise == 'Добавление спортсмена':
        adding_sp()
    elif choise == 'Удаление спортсмена':
        deleting_sp()
    elif choise == 'Выбор спортсмена':
        sp_choise()
    elif choise == 'Инфо':
        Information()

def MainMenuFront():
    msg = 'Выбор действия'
    title = 'Главное меню'
    choises = ['Добавление спортсмена', 'Удаление спортсмена', 'Выбор спортсмена', 'Инфо']
    choise = easygui.choicebox(msg, title, choises)
    if choise == 'Добавление спортсмена':
        adding_sp()
    elif choise == 'Удаление спортсмена':
        deleting_sp()
    elif choise == 'Выбор спортсмена':
        sp_choise()
    elif choise == 'Инфо':
        Information()

def Information():
    msg = ''
    title = 'Info'
    choises = ['Инструкция', 'Информация об авторе']
    choises = easygui.choicebox(msg, title, choises)
    if choises == 'Инструкция':
        Instruction()
    elif choises == 'Информация об авторе':
        Author()


def Instruction():
    easygui.msgbox('Coming coon!')
    MainMenu()


def Author():
    easygui.msgbox('Капитонов Андрей Андреевич\n akapitonov1999@gmail.com')
    MainMenu()


def MainSPMenu():
    msg = 'Профиль спортсмена'
    title = spch
    choises = ['Добавление тренировки за сегодня', 'Просмотр результатов', 'max Пульс проба', 'Антропометрия', 'Назад']
    choise = easygui.choicebox(msg, title, choises)
    if choise == 'Добавление тренировки за сегодня':
        TLoad()
    elif choise == 'Просмотр результатов':
        ResultsMenu()
    elif choise == 'max Пульс проба':
        MPPinput()
    elif choise == 'Антропометрия':
        KI()
    elif choise == 'Назад':
        MainMenu()


def ResultsMenu():
    msg = ''
    title = 'Меню результатов'
    choises = ['Суммарная нагрузка за 5 тренировок', 'Суммарная нагрузка за 20 тренировок', 'Freshness Index',
               'Суммарное время последних 5 тренировок', 'Неравномерность нагрузок', 'Напряжение за тренировку',
               'Напряжение по 5 тренировок', 'Динамика ИМТ', 'Динамика пульсовой пробы',
               'Распределение текущей нагрузки', 'Распределение хронической нагрузки', 'Назад']
    choise = easygui.choicebox(msg, title, choises)
    if choise == 'Суммарная нагрузка за 5 тренировок':
        fWLoad()
    elif choise == 'Суммарная нагрузка за 20 тренировок':
        fChronicLoad()
    elif choise == 'Freshness Index':
        fFreshnessIndex()
    elif choise == 'Суммарное время последних 5 тренировок':
        fWTH()
    elif choise == 'Неравномерность нагрузок':
        fMonotony()
    elif choise == 'Напряжение за тренировку':
        fDStrain()
    elif choise == 'Напряжение по 5 тренировок':
        fWStrain()
    elif choise == 'Динамика ИМТ':
        fdIMT()
    elif choise == 'Динамика пульсовой пробы':
        fdMPP()
    elif choise == 'Распределение текущей нагрузки':
        currentLoad5()
    elif choise == 'Распределение хронической нагрузки':
        currentLoad20()
    elif choise == 'Назад':
        MainSPMenu()


def currentLoad5():
    data = []
    with open('SLoadFile' + spch + '.dat', 'r') as f:
        for line in f:
            data.append([float(x) for x in line.split()])
    yData = list(itertools.chain(*data))
    yData = list(map(float, yData))
    sfdata = yData[-5:]
    fdata = sum(sfdata)
    fdata = str(fdata)
    GlobalData = {'Result': tuple(sfdata)}
    df = pd.DataFrame(GlobalData)
    fig = df.plot()
    fig.get_figure().savefig('result.png')
    with Image.open('result.png') as img:
        img.show()
    ResultsMenu()


def currentLoad20():
    data = []
    with open('SLoadFile' + spch + '.dat', 'r') as f:
        for line in f:
            data.append([float(x) for x in line.split()])
    yData = list(itertools.chain(*data))
    yData = list(map(float, yData))
    sfdata = yData[-20:]
    fdata = sum(sfdata)
    fdata = str(fdata)
    GlobalData = {'Result': tuple(sfdata)}
    df = pd.DataFrame(GlobalData)
    fig = df.plot()
    fig.get_figure().savefig('result.png')
    with Image.open('result.png') as img:
        img.show()
    ResultsMenu()


def fWLoadBack():
    data = []
    with open('SLoadFile' + spch + '.dat', 'r') as f:
        for line in f:
            data.append([float(x) for x in line.split()])
    yData = list(itertools.chain(*data))
    yData = list(map(float, yData))
    global LoadData
    LoadData = yData.copy()
    lenght = len(yData)
    counter = lenght // 5
    i = 1
    x = 2
    z = -5
    data = []
    global fiveData
    fiveData = yData[-5:]
    fdata = sum(fiveData)
    data.append(fdata)
    sfdata = []
    while i != counter:
        y = (-5) * x
        sfdata = yData[y:z]
        fdata = sum(sfdata)
        data.append(fdata)
        i = i + 1
        x = x + 1
        z = z - 5
    global WLoadData
    WLoadData = data[::-1]


def fWLoad():
    fWLoadBack()
    rdata = WLoadData[-1]
    rdata = str(rdata)
    GlobalData = {'Result': tuple(WLoadData)}
    df = pd.DataFrame(GlobalData)
    fig = df.plot()
    fig.get_figure().savefig('result.png')
    with Image.open('result.png') as img:
        img.show()
    easygui.msgbox('Суммарная нагрузка за 5 тренировок составила: ' + rdata)
    ResultsMenu()


def fChronicLoad():
    data = []
    with open('SLoadFile' + spch + '.dat', 'r') as f:
        for line in f:
            data.append([float(x) for x in line.split()])
    yData = list(itertools.chain(*data))
    yData = list(map(float, yData))
    lenght = len(yData)
    counter = lenght // 5
    i = 1
    x = 2
    z = -5
    data = []
    sfdata = yData[-20:]
    fdata = sum(sfdata)
    data.append(fdata)
    list.clear(sfdata)
    while i != counter:
        y = (-20) * x
        sfdata = yData[y:z]
        fdata = sum(sfdata)
        data.append(fdata)
        i = i + 1
        x = x + 1
        z = z - 20
    zdata = data[::-1]
    rdata = zdata[-1]
    rdata = str(rdata)
    GlobalData = {'Result': tuple(zdata)}
    df = pd.DataFrame(GlobalData)
    fig = df.plot()
    fig.get_figure().savefig('result.png')
    with Image.open('result.png') as img:
        img.show()
    easygui.msgbox('Суммарная нагрузка за 20 тренировок составила: ' + rdata)
    ResultsMenu()


def fFreshnessIndex():
    fWLoadBack()
    x = WLoadData[-1]
    y = WLoadData[-4:]
    z = np.mean(y)
    Index = x / z
    Index = str(Index)
    easygui.msgbox('Freshness Index: ' + Index + '\nWarning! Fresness Index должен быть в диапазоне 0.8-1.3')
    ResultsMenu()


def fWTH():
    data = []
    with open('timingFile' + spch + '.dat') as f:
        for line in f:
            data.append([float(x) for x in line.split()])
    yData = list(itertools.chain(*data))
    yData = list(map(float, yData))
    sfData = yData[-5:]
    fData = sum(sfData)
    fData = fData / 60
    fData = str(fData)
    easygui.msgbox('Суммарное время последних пяти тренировок: ' + fData + ' часов')
    ResultsMenu()


def fMonotonyBack():
    fWLoadBack()
    lenght = len(LoadData)
    i = 1
    o = LoadData[:5]
    st = stat.stdev(o)
    global Mdata
    Mdata = []
    Mdata.append(st)
    z = 1
    y = 6
    while i != lenght:
        x = LoadData[z:y]
        l = len(x)
        if l < 5:
            break
        st = stat.stdev(x)
        Mdata.append(st)
        z = z + 1
        y = y + 1
        i = i + 1


def fMonotony():
    fMonotonyBack()
    GlobalData = {'Result': tuple(Mdata)}
    df = pd.DataFrame(GlobalData)
    fig = df.plot()
    fig.get_figure().savefig('result.png')
    with Image.open('result.png') as img:
        img.show()
    ResultsMenu()


def fDStrain():
    fMonotonyBack()
    a = LoadData
    b = Mdata
    c = [a[i] * b[i] for i in range(len(b))]
    GlobalData = {'Result': tuple(c)}
    df = pd.DataFrame(GlobalData)
    fig = df.plot()
    fig.get_figure().savefig('result.png')
    with Image.open('result.png') as img:
        img.show()
    ResultsMenu()


def fWStrain():
    fMonotonyBack()
    fWLoadBack()
    a = WLoadData
    b = Mdata
    i = (len(b) // 5) + 1
    print(i)
    x = 0
    n = -1
    data = []
    while x != i:
        s = b[n]
        data.append(s)
        x = x + 1
        n = n - 5
    idata = data[::-1]
    c = [a[i] * idata[i] for i in range(len(idata))]
    GlobalData = {'Result': tuple(c)}
    df = pd.DataFrame(GlobalData)
    fig = df.plot()
    fig.get_figure().savefig('result.png')
    with Image.open('result.png') as img:
        img.show()
    ResultsMenu()


def fdIMT():
    data = []
    with open('IMTFile' + spch + '.dat', 'r') as f:
        for line in f:
            data.append([float(x) for x in line.split()])
    yData = list(itertools.chain(*data))
    yData = map(float, yData)
    GlobalData = {'Result': tuple(yData)}
    df = pd.DataFrame(GlobalData)
    fig = df.plot()
    fig.get_figure().savefig('result.png')
    with Image.open('result.png') as img:
        img.show()
    ResultsMenu()


def fdMPP():
    data = []
    with open('MPPFile' + spch + '.dat', 'r') as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    yData = list(itertools.chain(*data))
    yData = map(float, yData)
    GlobalData = {'Result': tuple(yData)}
    df = pd.DataFrame(GlobalData)
    fig = df.plot()
    fig.get_figure().savefig('result.png')
    with Image.open('result.png') as img:
        img.show()
    ResultsMenu()


def TLoad():
    msg = 'Введите время тренировки в минутах'
    title = 'Сбор информации о тренировке'
    default = '0'
    lowerbound = 0
    upperbound = 360
    fieldValues = easygui.integerbox(msg, title, default, lowerbound, upperbound)
    time = fieldValues
    msg1 = 'Введите оценку напряженности тренировки'
    title1 = 'Сбор информации о тренировке'
    default1 = '0'
    lowerbound1 = 0
    upperbound1 = 10
    fieldValues1 = easygui.integerbox(msg1, title1, default1, lowerbound1, upperbound1)
    Load = fieldValues1
    SLoad = time * Load
    strtime = str(time)
    strLoad = str(Load)
    strSLoad = str(SLoad)
    f = open('timingFile' + spch + '.dat', 'a')
    f.write('\n' + strtime)
    g = open('markFile' + spch + '.dat', 'a')
    g.write('\n' + strLoad)
    h = open('SLoadFile' + spch + '.dat', 'a')
    h.write('\n' + strSLoad)
    f.close()
    g.close()
    h.close()
    MainSPMenu()


def MPPinput():
    msg = 'Введите результат пульсовой пробы'
    title = 'Сбор информации о пульсовой пробе'
    default = '0'
    lowerbound = 0
    upperbound = 360
    fieldValues = easygui.integerbox(msg, title, default, lowerbound, upperbound)
    MPP = fieldValues
    strMPP = str(MPP)
    f = open('MPPFile' + spch + '.dat', 'a')
    f.write('\n' + strMPP)
    f.close()
    MainSPMenu()


def KI():
    msg = 'Введите рост спортсмена'
    title = 'Сбор антропометрических данных'
    default = '0'
    lowerbound = 0
    upperbound = 250
    fieldValues = easygui.integerbox(msg, title, default, lowerbound, upperbound)
    rost = fieldValues
    msg1 = 'Введите массу тела спортсмена'
    title1 = 'Сбор антропометрических данных'
    default1 = '0'
    lowerbound1 = 0
    upperbound1 = 250
    fieldValues1 = easygui.integerbox(msg1, title1, default1, lowerbound1, upperbound1)
    mass = fieldValues1
    IMT = float((mass * 10000) / (rost * rost))
    strrost = str(rost)
    strmass = str(mass)
    strIMT = str(IMT)
    f = open('rostFile' + spch + '.dat', 'a')
    f.write('\n' + strrost)
    g = open('massFile' + spch + '.dat', 'a')
    g.write('\n' + strmass)
    h = open('IMTFile' + spch + '.dat', 'a')
    h.write('\n' + strIMT)
    easygui.msgbox('Индекс массы тела равен ' + strIMT)
    f.close()
    g.close()
    h.close()
    MainSPMenu()


A = Application()
A.Appl = MainMenuBack
A.Appl()
