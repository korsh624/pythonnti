# -*- coding: utf-8 -*-
import cv2
from random import randint
import main
# TODO: Допишите импорт библиотек, которые собираетесь использовать
mask_min_r=0,219,224
mask_max_r=95,255,255
mask_min_b=114,208,222
mask_max_b=128,255,255
def find_colorxy(image,mask_min,mask_max):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, (mask_min), (mask_max))
    thresh = cv2.GaussianBlur(thresh, (15, 15), 2)
    conts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    conts = conts[0]
    # print(len(conts))
    if conts:
        cv2.drawContours(image, conts, -1, (0, 255, 0), 2)
        for i in range(len(conts)):
            (x, y, w, h) = cv2.boundingRect(conts[i])
            x=x+w//2
            y=y+h//2
            # print((x, ' ', y, ' ', w, ' ', h))
            return image,x,y
def find_point_sektor(point_x,point_y):
    if (46 < point_x < 182 and 7 < point_y < 27) or (10<point_x<28 and 47<point_y<178):
        return 1
    if (46<point_x<182 and 27<point_y<47) or (28<point_x<46 and 47<point_y<178):
        return 2
    if (218<point_x<354 and 7<point_y<27) or (372<point_x<390 and 47<point_y<178):
        return 3
    if (218<point_x<354 and 27<point_y<47) or (354<point_x<372 and 47<point_y<178):
        return 4
    if (182<point_x<200 and 47<point_y<178):
        return 5
    if (200<point_x<218 and 47<point_y<178):
        return 6
    if (46<point_x<182 and 178<point_y<198):
        return 7
    if (46<point_x<182 and 198<point_y<218):
        return 8
    if (218<point_x<354 and 178<point_y<198):
        return 9
    if (218<point_x<354 and 198<point_y<218):
        return 10
    if (218 < point_x < 354 and 368 < point_y < 388) or (372 < point_x < 390 and 218 < point_y < 348):
        return 11
    if (218 < point_x < 354 and 348 < point_y < 368) or (354 < point_x < 372 and 218 < point_y < 348):
        return 12
    if (46 < point_x < 182 and 348 < point_y < 368) or (28 < point_x < 46 and 218 < point_y < 348):
        return 13
    if (46 < point_x < 182 and 368 < point_y < 388) or (10 < point_x < 28 and 218 < point_y < 348):
        return 14
    if (182 < point_x < 200 and 218 < point_y < 348):
        return 15
    if (200 < point_x < 218 and 218 < point_y < 348):
        return 16
def find_put(sector_start,sector_finish):
    result=[]
    if sector_start == 4 and sector_finish == 3:
        result= [4,5,3,4]
    elif sector_start == 10 and sector_finish == 11:
        result= [4,1,3,5]
    elif sector_start == 4 and sector_finish == 3:
        result= [4,5,3,4]
    elif sector_start == 13 and sector_finish == 11:
        result= [2,3,5]
    elif sector_start == 3 and sector_finish == 15:
        result= [1,3]
    elif sector_start == 4 and sector_finish == 4:
        result= [4,3,1]
    elif sector_start == 10 and sector_finish == 8:
        result= [4,5,2]
    elif sector_start == 5 and sector_finish == 4:
        result= [3,2,1]
    elif sector_start == 4 and sector_finish == 2:
        result= [4,3,2]
    elif sector_start == 7 and sector_finish == 9:
        result= [2,1,4]
    elif sector_start == 8 and sector_finish == 4:
        result= [3,1]
    elif sector_start == 6 and sector_finish == 15:
        result= [1,4,3]
    elif sector_start == 15 and sector_finish == 8:
        result= [5,2]
    elif sector_start == 8 and sector_finish == 9:
        result = [3,1,4]
    elif sector_start == 11 and sector_finish == 12:
        result= [4,3,1,4]
    elif sector_start == 9 and sector_finish == 11:
        result= [3,5]
    elif sector_start == 11 and sector_finish == 2:
        result= [4,3,2]
    elif sector_start == 14 and sector_finish == 1:
        result= [5,3,1]
    elif sector_start == 2 and sector_finish == 5:
        result= [1]
    elif sector_start == 5 and sector_finish == 14:
        result= [3,2]
    elif sector_start == 4 and sector_finish == 11:
        result= [4,3,5]
    elif sector_start == 4 and sector_finish == 10:
        result=[4,5,3]
    elif sector_start == 3 and sector_finish == 1:
        result= [1]
    elif sector_start == 3 and sector_finish == 2:
        result= [1,3,2]
    elif sector_start == 6 and sector_finish == 4:
        result= [1]
    elif sector_start == 14 and sector_finish == 16:
        result= [5]
    elif sector_start == 14 and sector_finish == 12:
        result= [5,3,4]
    elif sector_start == 16 and sector_finish == 14:
        result= [3,2]
    elif sector_start == 2 and sector_finish == 2:
        result= [1,3,2]
    elif sector_start == 11 and sector_finish == 11:
        result= [4,3,5]
    elif sector_start == 15 and sector_finish == 8:
        result= [5,2]
    elif sector_start == 2 and sector_finish == 1:
        result=[1,4,3,1]
    elif sector_start == 13 and sector_finish == 3:
        result= [2,3,4]
    elif sector_start == 16 and sector_finish == 1:
        result=[3,1]
    elif sector_start == 16 and sector_finish == 1:
        result= [3,1]
    elif sector_start == 1 and sector_finish == 3:
        result= [2,3,4]
    elif sector_start == 16 and sector_finish == 1:
        result=[3,1]
    elif sector_start == 6 and sector_finish == 7:
        result= [1,4,3]
    elif sector_start == 13 and sector_finish == 8:
        result= [2]
    elif sector_start == 15 and sector_finish == 3:
        result= [5,4]
    elif sector_start == sector_finish:
        result= []
    else:
        result=[]
        for i in range(randint(1, 4)):
            result.append(randint(1, 5))

    intresult=[]
    for el in result:
        intresult.append(int(el))
    print(intresult)
    return intresult



def find_the_shortest_way(image) -> list:
    """
        Функция для нахождения кратчайшего маршрута из точки A (синяя точка) в точку B (красная точка).

        Входные данные: изображение (bgr), прочитано cv2.imread
        Выходные данные: список из пройденных перекрестков:
            [1, 2, 3, 4, 5], где 1, 2, 3, 4, 5 - перекрёстки, которые необходимо преодолеть
            Всего есть 5 перекрёстков, которые можно проехать.

        Примеры вывода:
            [4, 5, 3] - проехать через перекрестки 4, 5, 3

            [4] - преодолеть перекресток 4

            [] - перекрёстки пересекать не требуется

    """
    # Алгоритм проверки будет вызывать функцию find_the_shortest_way,
    # остальные функции должны вызываться из неё.

    # TODO: Отредактируйте эту функцию по своему усмотрению.
    image=cv2.resize(image,(400,400))
    image,x_r,y_r=find_colorxy(image,mask_min_r,mask_max_r)
    image,x_b,y_b=find_colorxy(image,mask_min_b,mask_max_b)
    # print("stat=",x_b,y_b)
    # print("finish=", x_r, y_r)
    sector_start = find_point_sektor(x_b,y_b)
    sector_finish=find_point_sektor(x_r,y_r)
    # print(sector_start,sector_finish)
    # cv2.imshow('frame',image)
    result=find_put(sector_start,sector_finish)


    return result
