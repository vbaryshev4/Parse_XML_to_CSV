'''
TODO:
    1) Вытащить заголовки и ссылки статей
    2) Для каждого </item>, для которого 
        <category domain="category" nicename="articles”>, 
        вытащить <title> и <link>. 
        NB: Всего 636 item

    3) Результат записать в csv в котором есть два столбца: title и link. 
        Должно получится в районе 167 строк

    4) Сдача: 14 февраля
'''
import xml.etree.ElementTree as ET
import csv

# Write new line to new CSV
def write_to_csv(row):
    with open('formatta.csv', 'a', newline='') as new_csv:
        w = csv.writer(new_csv)
        w.writerow(row)

def itter(root):
    for child in root:
        count = 0
        for item in child:
            data = []
            for tag in item:
                if tag.tag == 'title':
                    data.append(tag.text)
                if tag.tag == 'link':
                    data.append(tag.text)
                if tag.attrib == {'domain': 'category', 'nicename': 'articles'}:
                    count += 1
                    write_to_csv(data)
    return print('End of parse')

def start_parse(file):
    tree = ET.parse(source_file)
    root = tree.getroot()
    return itter(root)

source_file = 'formatta.wordpress.2018-02-11.xml'
start_parse(source_file)