
# import os
# import re
# import matplotlib.pyplot as plt
# from flask import Flask





# with open(r"C:/Users/User/Desktop/sbor/new.txt", 'r', encoding='utf-8') as f:
    

#     current_sort = None
#     sort_data = {}
#     for line in f:
#         x = line.strip()  # Убираем пробелы в начале и конце строки


#         if '04670127280492 напиток безалкогольный сильногазированный «колокольчик» флэшшш тайм 1.5' in x.lower():
#             current_sort = '04670127280492'
#             if current_sort not in sort_data:
#                 sort_data[current_sort] = []
#         elif current_sort and 'напиток безалкогольный сильногазированный «колокольчик» флэшшш тайм количество' in x.lower():
#             s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
#             if s:
#                 sort_data[current_sort].extend(map(int,s))
#             current_sort = None
        
        
#         elif '04670127280478 напиток безалкогольный сильногазированный «кола» флэшшш тайм 0,5' in x.lower():
#             current_sort = '04670127280478'
#             if current_sort not in sort_data:
#                 sort_data[current_sort] = []
#         elif current_sort and 'напиток безалкогольный сильногазированный «кола» флэшшш тайм количество' in x.lower():
#             s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
#             if s:
#                 sort_data[current_sort].extend(map(int,s))
#             current_sort = None
    

#         elif '04670127280997 напиток безалкогольный сильногазированный специального назначения «баранчинский»' in x.lower():
#             current_sort = '04670127280997'
#             if current_sort not in sort_data:
#                 sort_data[current_sort] = []
#         elif current_sort and 'напиток безалкогольный сильногазированный специального назначения «баранчинский»' in x.lower():
#             s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
#             if s:
#                 sort_data[current_sort].extend(map(int,s))
#             current_sort = None


#         elif '04670127280461 напиток безалкогольный сильногазированный «кола» флэшшш тайм' in x.lower():
#             current_sort = '04670127280461'
#             if current_sort not in sort_data:
#                 sort_data[current_sort] = []
#         elif current_sort and 'напиток безалкогольный сильногазированный «кола» флэшшш тайм' in x.lower():
#             s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
#             if s:
#                 sort_data[current_sort].extend(map(int,s))
#             current_sort = None

   
        






        


# print(sort_data.items())
# for city, quantities in sort_data.items():
#     total_quantity = sum(quantities)
#     print(f'GTIN: {city}, Остаток: {total_quantity}, Из: {quantities}, Всего: {total_quantity}')
# print('//////////')




# # Записываем результаты в файл
# with open(r"C:/Users/User/Desktop/sbor/Города_результат.txt", 'w', encoding='utf-8') as output_file:
#     for city, quantities in sort_data.items(): # запись 19л
#         total_quantity = sum(quantities)
#         if total_quantity > 0:
#             output_file.write(f'GTIN: {city} Остаток: {total_quantity}\n'   )
#             output_file.write('----------------------\n')

#         else:
#             output_file.write(f'Данные {city} не найдены.\n')
    # output_file.write('----------------------\n')
   









########################################## MATPLOTLIB ##########################################
    # kushva_city = city_data['Кушва']
    # kushva_sum = sum(kushva_city)

    # nt_city = city_data['Тагил']
    # nt_sum = sum(nt_city)

    # br_city = city_data['Баранчинский']
    # br_sum = sum(br_city)

    # kr_city = city_data['Красноуральск']
    # kr_sum = sum(kr_city)
    
    # print(f'"bar", {kr_sum}')
    # a = br_sum
    # b = nt_sum
    # c = kushva_sum
    # d = kr_sum

    # bar = 'Баранчинский'
    # nt = 'Нижний тагил'
    # kh = 'Кушва, верхняя тура'
    # kr = 'Красноуральск'
    # # plt.axis([0,5,0,50])
    # # plt.title('График кол-во продаж(города) через сайт', fontsize=20, fontname='Times New Roman')
    # # plt.xlabel('Город', color='gray')
    # # plt.ylabel('Количество',color='gray')
    # # plt.text(1,a,f'Баранчинский - {br_sum}')
    # # plt.text(2,b,f'Нижний тагил - {nt_sum}')
    # # plt.text(3,c,f'Кушва, верхняя тура - {kushva_sum}')
    # # plt.text(4,d,f'Красноуральск - {kr_sum}')
    # # plt.plot([1,2,3,4],[a,b,c,d],'ro')

    # # plt.show()


    # left = [0, 1, 2, 3]

    # height = [a, b, c, d]

    # tick_label = [bar, nt, kh, kr]

    # plt.bar(left, height, tick_label = tick_label,
    #         width = 0.2, color = ['red', 'green'])

    # for i in range(len(height)):
    #     plt.text(left[i], height[i] + 0.1, str(height[i]), ha='center', va='bottom')
    # plt.xlabel('Город')
    # plt.ylabel('Количество')
    # plt.title('График кол-во продаж(города) через сайт за месяц')
    # plt.show()
########################################## MATPLOTLIB ##########################################





from flask import Flask, render_template_string, send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import re
import os

app = Flask(__name__)

@app.route('/')
def index():
    sort_data, name_data = process_data()  # Получаем оба словаря
    return render_template_string(render_html(sort_data, name_data))







@app.route('/download_pdf')
def download_pdf():
    # Пример данных
    sort_data = ["04670127280492", "04670127280478", "04670127280478"]
    stock_data = ["8", "6", "10"]
    # name_data = ["напиток безалкогольный", "кола"]
    pdf_path = "report.pdf"  # Путь к файлу PDF

    # Вызов функции с правильными аргументами
    generate_pdf(sort_data, stock_data, pdf_path)

    # Возврат сгенерированного PDF-файла
    return send_file(pdf_path, as_attachment=True)

def generate_pdf(sort_data, stock_data, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Регистрация шрифта
    pdfmetrics.registerFont(TTFont('ArialUnicode', 'ARIALUNI.TTF'))  # Убедитесь, что файл доступен
    c.setFont("ArialUnicode", 12)  # Установка шрифта

    # Заголовки таблицы
    c.drawString(100, height - 50, "Отчет о товарах")
    c.drawString(100, height - 70, "GTIN")
    c.drawString(250, height - 70, "Остаток")
  

    # Данные
    y_position = height - 90  # Начальная позиция для данных

    for gtin, stock in zip(sort_data, stock_data, ):
        c.drawString(100, y_position, gtin)
        c.drawString(250, y_position, stock)
        # c.drawString(350, y_position, name)
        y_position -= 20  # Уменьшаем позицию для следующей строки

    c.save()








def process_data():
    sort_data = {}
    name_data = {}  # Инициализируем как словарь
    with open(r"C:/Users/User/Desktop/SortWaterTable/new.txt", 'r', encoding='utf-8') as f:
        current_sort = None
        for line in f:
            x = line.strip()
            # Обработка первого продукта
            if '04670127280492 напиток безалкогольный сильногазированный «колокольчик» флэшшш тайм 1.5' in x.lower():
                current_sort = '04670127280492'
                name_data[current_sort] = 'Напиток безалкогольный сильногазированный «колокольчик» флэшшш тайм 1.5'  # Обновляем name_data
                if current_sort not in sort_data:
                    sort_data[current_sort] = []
            elif current_sort and 'напиток безалкогольный сильногазированный «колокольчик» флэшшш тайм количество' in x.lower():
                s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
                if s:
                    sort_data[current_sort].extend(map(int, s))
                current_sort = None  # Сбрасываем current_sort после обработки

            # Обработка второго продукта
            elif '04670127280478 напиток безалкогольный сильногазированный «кола» флэшшш тайм 0,5' in x.lower():
                current_sort = '04670127280478'
                name_data[current_sort] = 'Напиток безалкогольный сильногазированный «кола» флэшшш тайм 0,5'  # Обновляем name_data
                if current_sort not in sort_data:
                    sort_data[current_sort] = []
            elif current_sort and 'напиток безалкогольный сильногазированный «кола» флэшшш тайм количество' in x.lower():
                s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
                if s:
                    sort_data[current_sort].extend(map(int, s))
                current_sort = None  # Сбрасываем current_sort после обработки

            
            elif '04670127280997 напиток безалкогольный сильногазированный специального назначения «баранчинский»' in x.lower():
                current_sort ='04670127280997'
                name_data[current_sort] = 'Напиток безалкогольный сильногазированный специального назначения «баранчинский» 1.5'
                if current_sort not in sort_data:
                    sort_data[current_sort] = []
            elif current_sort and 'напиток безалкогольный сильногазированный специального назначения «баранчинский» Количество' in x.lower():
                s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
                if s:
                    sort_data[current_sort].extend(map(int,s))
                current_sort = None


            elif '04670127280515 напиток безалкогольный сильногазированный «лимонад» флэшшш тайм 0.5' in x.lower():
                current_sort = '04670127280515'
                name_data[current_sort] = 'Напиток безалкогольный сильногазированный «Лимонад» Флэшшш тайм 0.5'
                if current_sort not in sort_data:
                    sort_data[current_sort] = []
            elif current_sort and 'напиток безалкогольный сильногазированный «лимонад» флэшшш тайм количество' in x.lower():
                s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
                if s:
                    sort_data[current_sort].extend(map(int,s))
                current_sort = None

            
            elif '04670127280546 напиток безалкогольный сильногазированный «вкус тархуна» флэшшш тайм 1.5' in x.lower():
                current_sort = '04670127280546'
                name_data[current_sort] = 'Напиток безалкогольный сильногазированный «Вкус Тархуна» Флэшшш Тайм 1.5'
                if current_sort not in sort_data:
                    sort_data[current_sort] = []
            elif current_sort and 'напиток безалкогольный сильногазированный «вкус тархуна» флэшшш тайм количество' in x.lower():
                s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
                if s:
                    sort_data[current_sort].extend(map(int,s))
                current_sort = None

            elif '04670127280454 напиток безалкогольный сильногазированный «дюшес» флэшшш тайм 0.5' in x.lower():
                current_sort = '04670127280454'
                name_data[current_sort] = 'Напиток безалкогольный сильногазированный «Дюшес» Флэшшш тайм 0.5'
                if current_sort not in sort_data:
                    sort_data[current_sort] = []
            elif current_sort and 'напиток безалкогольный сильногазированный «дюшес» флэшшш тайм количество' in x.lower():
                s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
                if s:
                    sort_data[current_sort].extend(map(int,s))
                current_sort = None



    print('----------------------------')
    print("sort_data:", sort_data)  # Отладочное сообщение
    print("name_data:", name_data)  # Отладочное сообщение
    print('----------------------------')
    return sort_data, name_data







def render_html(sort_data, name_data):
    html_content = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Отчет о товарах</title>
    </head>
    <body>
        <h1>Отчет о товарах</h1>
        <table border="1">
            <tr>
                <th>Название</th>
                <th>GTIN</th>
                <th>Остаток</th>
                
                
            </tr>
    '''
    
    for gtin, quantities in sort_data.items():
        total_quantity = sum(quantities)
        # Получаем название продукта для текущего GTIN
        product_name = name_data.get(gtin, "Неизвестно")
        
        html_content += f'''
            <tr>
                <td>{product_name}</td>
                <td>{gtin}</td>
                <td>{total_quantity}</td>
                
                
            </tr>
        '''
    
    html_content += '''
        </table>
        <a href="/download_pdf">Скачать PDF</a>
    </body>
    </html>
    '''
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)