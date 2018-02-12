import xml.etree.ElementTree as ET
import csv


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
    return 'End of parse. {0} rows written to CSV'.format(count)

def start_parse(file):
    tree = ET.parse(source_file)
    root = tree.getroot()
    return itter(root)

source_file = 'formatta.wordpress.2018-02-11.xml'
print(start_parse(source_file))