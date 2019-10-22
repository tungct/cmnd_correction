from lxml import html
import requests
page = requests.get('https://danluat.thuvienphapluat.vn/tu-so-the-can-cuoc-cong-dan-co-the-xac-dinh-duoc-ban-sinh-nam-nao-gioi-tinh-gi-151527.aspx')
tree = html.fromstring(page.content)

item = tree.xpath('//tr/td/p/span/span/text()')
indexs, provines, codes = [], [], []
for i in range(len(item)):
    if i < 63 * 3:
        value = item[i]
        if i % 3 == 0:
            indexs.append(value)
        elif i % 3 == 1:
            provines.append(value)
        elif i % 3 == 2:
            codes.append(value)

with open('cccd_provin_code.txt', 'w') as f:
    for i in range(len(indexs)):
        row = indexs[i] + '\t' + provines[i] + '\t' + codes[i] + '\n'
        f.write(row)

# cmnd
page = requests.get('http://nhankiet.vn/en/w1278/Ma-so-CMND-cua-cac-tinh-thanh.html')
tree = html.fromstring(page.content)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

item = tree.xpath('//tr/td/p/span/text()')
with open('cmnd_provin_code.txt', 'w') as f:
    for i in range(len(item)):
        data = item[i]
        data_list = data.split()
        codes, provines = [], []
        for word in data_list:
            if hasNumbers(word) == True:
                codes.append(word)
            else:
                provines.append(word)
        code = '-'.join(codes)
        provine = ' '.join(provines)
        row = provine + '\t' + code + '\n'
        f.write(row)
