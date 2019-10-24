
def load_provin_code(file):
    provin_code_dict = {}
    with open(file, 'r') as f:
        datas = f.readlines()
    for i in range(len(datas)):
        data = datas[i].strip()
        provin, code = data.split('\t')
        provin_code_dict[code] = provin

    return provin_code_dict

def seg_code(code_serial):
    seg_code_dict = {}
    # code of cccd
    if len(code_serial) == 12:
        provin_code = code_serial[:3]
        gender_code = code_serial[3]
        birth_code = code_serial[4:6]
        random_code = code_serial[6:]
        gender_code = int(gender_code)

        if gender_code == 0 or gender_code == 1:
            century = 20
        elif gender_code == 2 or gender_code == 3:
            century = 21
        elif gender_code == 4 or gender_code == 5:
            century = 22
        elif gender_code == 6 or gender_code == 7:
            century = 23
        elif gender_code == 8 or gender_code == 9:
            century = 24
        else:
            century = 0

        seg_code_dict = {
            'provin_code': str(provin_code),
            'gender_code': str(gender_code),
            'birth_code': str(birth_code),
            'random_code': str(random_code),
            'century': str(century)
        }
    # cmnd
    elif len(code_serial) == 9:
        provin_code = code_serial[:3]
        seg_code_dict = {
            'provin_code': str(provin_code),
            'gender_code': '',
            'birth_code': '',
            'random_code': '',
            'century': ''
        }
    return seg_code_dict

def get_info_code(code_serial):
    # cccd
    if len(code_serial) == 12:
        seg_code_dict = seg_code(code_serial)
        provin_code_dict = load_provin_code('cccd_provin_code.txt')
        provin_code, gender_code, birth_code, century = seg_code_dict['provin_code'], seg_code_dict['gender_code'], seg_code_dict['birth_code'], seg_code_dict['century']
        provin = provin_code_dict[str(provin_code)]
        birth_year = str(int(century) - 1) + str(birth_code)
        if int(gender_code) % 2 == 1:
            gender = 'nữ'
        else:
            gender = 'nam'
        info_dict = {
            'gender' : gender,
            'provin' : provin,
            'birth_year' : birth_year
        }
    elif len(code_serial) == 9:
        seg_code_dict = seg_code(code_serial)
        provin_code_dict = load_provin_code('cmnd_provin_code.txt')
    return info_dict

if __name__ == '__main__':
    code_serial = '017466812'
    seg_code_dict = seg_code(code_serial)
    print(seg_code_dict)
    print(get_info_code(code_serial))


