# Задание 1 из домашней работы №8

class Date:
    current_date: str = "00-00-0000"

    def __init__(self, current_date):
        self.current_date = current_date

    def __str__(self):
        return self.current_date

    @classmethod
    def get_date(cls, current_date):
        c_day, c_month, c_year = (current_date.split("-"))
        return int(c_day), int(c_month), int(c_year)

    @staticmethod
    def validate(day, month, year):
        if year > 0:
            if 1 <= month <= 12:
                if 1 <= day <= 31:
                    return "Validation successful!"
                else:
                    return "Enter valid date please!"
            else:
                return "Enter valid date please!"
        else:
            return "Enter valid date please!"


curr_date = Date("01-02-1993")
print(curr_date)
print(curr_date.get_date("01-02-1993"))

date_to_validate = curr_date.get_date("01-01-1996")
print(Date.validate(date_to_validate[0], date_to_validate[1], date_to_validate[2]))

