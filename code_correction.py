
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


        print(provin_code)
        print(sex_code)
        print(birth_code)
        print(random_code)

if __name__ == '__main__':
    code_serial = '037153000257'
    seg_code(code_serial)


