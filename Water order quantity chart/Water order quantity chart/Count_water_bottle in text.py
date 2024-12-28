import os
import re
import matplotlib.pyplot as plt






with open(r"C:/Users/User/Desktop/Water order quantity chart/test.txt", 'r', encoding='utf-8') as f:
    city_data = {}  
    city_5litr = {}
    current_city = None 
    current_5litr = None  

    for line in f:
        x = line.strip()  # Убираем пробелы в начале и конце строки

        # Проверяем, содержит ли строка название города
        if 'тагил - вода природная (19л.)' in x.lower():
            current_city = 'Тагил'  # Устанавливаем текущий город
            if current_city not in city_data:
                city_data[current_city] = [] 

        elif 'баранчинский - вода природная (19л.)' in x.lower():
            current_city = 'Баранчинский'  
            if current_city not in city_data:
                city_data[current_city] = []  
        elif 'баранчинский - вода природная (5л.)' in x.lower():
            print('11111')
            current_5litr = 'Баранчинский'
            if current_5litr not in city_5litr:
                city_5litr[current_5litr] = []
                print(city_5litr)
                
        elif 'кушва - вода природная (5л.)' in x.lower():
            print('11111')
            current_5litr = 'Кушва'
            if current_5litr not in city_5litr:
                city_5litr[current_5litr] = []
        elif 'тагил - вода природная (5л.)' in x.lower():
            print('11111')
            current_5litr = 'Тагил'
            if current_5litr not in city_5litr:
                city_5litr[current_5litr] = []        
        elif 'кушва - вода природная (19л.)' in x.lower():
            current_city = 'Кушва'
            if current_city not in city_data:
                city_data[current_city] = []
        elif 'красноуральск' in x.lower():
            current_city = 'Красноуральск'
            if current_city not in city_data:
                city_data[current_city] = []

        # Если текущий город найден, проверяем следующую строку на наличие "Количество"
        elif current_city and "количество" in x.lower():
            s = re.findall(r"[-+]?\d*\.\d+|\d+", x)  # Ищем все числа в строке
            if s:  # Если числа найдены true
                city_data[current_city].extend(map(int, s))  # Добавляем найденные количества в список для текущего города
            # current_city = None  # Сбрасываем текущий город после обработки
        elif current_city and "количество" in x.lower():
            s = re.findall(r"[-+]?\d*\.\d+|\d+", x)  # Ищем все числа в строке
            if s:  # Если числа найдены true
                city_data[current_city].extend(map(int, s))
            current_city = None  # Сбрасываем текущий город после обработки

        elif current_5litr and "количество" in x.lower():
            s = re.findall(r"[-+]?\d*\.\d+|\d+", x)  # Ищем все числа в строке
            if s:  # Если числа найдены true
                city_5litr[current_5litr].extend(map(int, s))  # Добавляем найденные количества в список для текущего города
            current_5litr = None  # Сбрасываем текущий город после обработки
        
        

# Выводим результаты
print(city_data.items(), city_5litr.items())
for city, quantities in city_data.items():
    total_quantity = sum(quantities)
    print(f'Город: {city}, Количество бутылок: {total_quantity}, Из: {quantities}, Всего: {total_quantity * 200}')
print('//////////')
for city_5, quantities_5 in city_5litr.items():
    total_quantity_5 = sum(quantities_5)




# Записываем результаты в файл
with open(r"C:/Users/User/Desktop/sbor/Города_результат.txt", 'w', encoding='utf-8') as output_file:
    for city, quantities in city_data.items(): # запись 19л
        total_quantity = sum(quantities)
        if total_quantity > 0:
            output_file.write(f'19л - Город: {city}, Количество: {total_quantity}, Всего: {total_quantity}\n')
        else:
            output_file.write(f'Данные для города {city} не найдены.\n')
    output_file.write('----------------------\n')
    for city_5, quantities_5 in city_5litr.items(): # запись 5л
        total_quantity_5 = sum(quantities_5)
        if total_quantity_5 > 0:

            output_file.write(f'5л - Город: {city_5}, Количество бутылок: {total_quantity_5}, Всего: {total_quantity_5}\n')


    




    kushva_city = city_data['Кушва']
    kushva_sum = sum(kushva_city)

    nt_city = city_data['Тагил']
    nt_sum = sum(nt_city)

    br_city = city_data['Баранчинский']
    br_sum = sum(br_city)

    kr_city = city_data['Красноуральск']
    kr_sum = sum(kr_city)
    
    print(f'"bar", {kr_sum}')
    a = br_sum
    b = nt_sum
    c = kushva_sum
    d = kr_sum

    bar = 'Баранчинский'
    nt = 'Нижний тагил'
    kh = 'Кушва, верхняя тура'
    kr = 'Красноуральск'


    left = [0, 1, 2, 3]

    height = [a, b, c, d]

    tick_label = [bar, nt, kh, kr]

    plt.bar(left, height, tick_label = tick_label,
            width = 0.2, color = ['red', 'green'])

    for i in range(len(height)):
        plt.text(left[i], height[i] + 0.1, str(height[i]), ha='center', va='bottom')
    plt.xlabel('Город')
    plt.ylabel('Количество')
    plt.title('График кол-во продаж(города) через сайт за месяц')
    plt.show()