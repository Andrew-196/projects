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
    sort_data, name_data = process_data() 
    return render_template_string(render_html(sort_data, name_data))







@app.route('/download_pdf')
def download_pdf():
    sort_data = ["04670127280492", "04670127280478", "04670127280478"]
    stock_data = ["8", "6", "10"]
    pdf_path = "report.pdf"  

    generate_pdf(sort_data, stock_data, pdf_path)

    return send_file(pdf_path, as_attachment=True)

def generate_pdf(sort_data, stock_data, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    pdfmetrics.registerFont(TTFont('ArialUnicode', 'ARIALUNI.TTF'))  
    c.setFont("ArialUnicode", 12) 

  
    c.drawString(100, height - 50, "Отчет о товарах")
    c.drawString(100, height - 70, "GTIN")
    c.drawString(250, height - 70, "Остаток")
  

    y_position = height - 90  

    for gtin, stock in zip(sort_data, stock_data, ):
        c.drawString(100, y_position, gtin)
        c.drawString(250, y_position, stock)
        y_position -= 20  

    c.save()











def process_data():
    sort_data = {}
    name_data = {} 
    with open(r"C:/Users/User/Desktop/SortWaterTable/new.txt", 'r', encoding='utf-8') as f:
        current_sort = None
        for line in f:
            x = line.strip()

            # поиск первой строки в new.txt
            if '04670127280492 напиток безалкогольный сильногазированный «колокольчик» флэшшш тайм 1.5' in x.lower():
                current_sort = '04670127280492'
                name_data[current_sort] = 'Напиток безалкогольный сильногазированный «колокольчик» флэшшш тайм 1.5'
                if current_sort not in sort_data:
                    sort_data[current_sort] = []
            # поиск творой строки в new.txt и создан ли current_sort
            elif current_sort and 'напиток безалкогольный сильногазированный «колокольчик» флэшшш тайм количество' in x.lower():
                s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
                if s:
                    sort_data[current_sort].extend(map(int, s))
                current_sort = None  # сброс current_sort 

            
            elif '04670127280478 напиток безалкогольный сильногазированный «кола» флэшшш тайм 0,5' in x.lower():
                current_sort = '04670127280478'
                name_data[current_sort] = 'Напиток безалкогольный сильногазированный «кола» флэшшш тайм 0,5'  
                if current_sort not in sort_data:
                    sort_data[current_sort] = []
            elif current_sort and 'напиток безалкогольный сильногазированный «кола» флэшшш тайм количество' in x.lower():
                s = re.findall(r"[-+]?\d*\.\d+|\d+", x)
                if s:
                    sort_data[current_sort].extend(map(int, s))
                current_sort = None 

            
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
    print("sort_data:", sort_data)  
    print("name_data:", name_data)  
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
