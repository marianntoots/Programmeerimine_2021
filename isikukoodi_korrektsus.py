import datetime

def check_personal_code(personal_code_str):
    weights1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

        month = int(personal_code_str[3:5])
        day = int(personal_code_str[5:7])

        datetime.date(year, month, day)

        check_digit = int(personal_code_str[10])

        checksum = 0
        for i, digit_str in enumerate(personal_code_str[:-1]):
            checksum += int(digit_str) * weights1[i]
        checksum %= 11
        if checksum < 10:
            if checksum != check_digit:
                print("Viga: kontrollväärtus ei klapi")
                return False
        else:
            checksum = 0
            for i, digit_str in enumerate(personal_code_str[:-1]):
                checksum += int(digit_str) * weights2[i]
            checksum %= 11
            if checksum != check_digit:
                print("Viga: kontrollväärtus ei klapi")
                return False
    except ValueError as e:
        print("Viga: ebakorrektne väärtus isikukoodis:", e)
        return False
    return True


personal_code_str = input("Sisesta isikukood: ")
if check_personal_code(personal_code_str):
    print("Isikukood on korrektne")
else:
    print("Isikukood ei ole korrektne")
