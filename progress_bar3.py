# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:28:06 2019

@author: Андрей
"""
from time import sleep

percentage = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%']

def progress_bar3():
    global i
    i = 0
    while i!=10:
        print ('\r', '{0:_^20}'.format(percentage[i]), end='')
        i+=1 
        sleep (0.5)
#Вызывает значение % из списка соответственно порядковому номеру

progress_bar3()


def progress_bar4():
    i=0
    while i!=10:
        print ('\b'*25, '{0:_^20}'.format(percentage[i]), end='')
        i+=1
        sleep (0.5)
        
progress_bar4 ()

closer = input('\nНажмите Enter для закрытия программы')
quit()
    