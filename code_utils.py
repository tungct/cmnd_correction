
def load_provin_code(file):
    provin_code_dict = {}
    with open(file, 'r') as f:
        datas = f.readlines()
    for i in range(len(datas)):
        data = datas[i].strip()
        provin, code = data.split('\t')
        provin_code_dict[provin] = code

    return provin_code_dict

def seg_code(code_serial):
    seg_code_dict = {}
    # code of cccd
    if len(code_serial) == 12:
        provin_code = code_serial[:3]
        sex_code = code_serial[3]
        birth_code = code_serial[4:6]
        random_code = code_serial[6:]

        if sex_code == 0 or sex_code == 1:
            century = 20
        elif sex_code == 2 or sex_code == 3:
            century = 21
        elif sex_code == 4 or sex_code == 5:
            century = 22
        elif sex_code == 6 or sex_code == 7:
            century = 23
        elif sex_code == 8 or sex_code == 9:
            century = 24
        else:
            century = 0

        seg_code_dict = {
            'provin_code': provin_code,
            'sex_code': sex_code,
            'birth_code': birth_code,
            'random_code': random_code,
            'century': century
        }

    return seg_code_dict

if __name__ == '__main__':
    code_serial = '037153000257'
    seg_code_dict = seg_code(code_serial)
    print(seg_code_dict)


