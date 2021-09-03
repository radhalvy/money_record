import datetime


def get_operation():
    user_answer = input(
        "What do you want to do?\n1) Make a deposit, 2) Make a withdrawal, 3) See the account's total amount, 4) See the history\nAnswer: ")
    return user_answer


def get_deposit():
    money_amount = float(
        input("How much money you want to deposit?\nAnswer: "))
    return money_amount


def get_withdraw():
    money_amount = float(
        input("How much money you want to withdraw?\nAnswer: "))
    return money_amount


def get_readable_date():
    date = datetime.datetime.now()
    formatted_date = date.strftime("%x")
    return formatted_date


def get_history(file_path):
    with open(file_path) as file:
        file_lines = file.read()
        return file_lines


def write_deposit(file_path, date, deposit_amount):
    with open(file_path, "a") as file:
        file.write(f"+ {date} ---> {deposit_amount}\n")


def write_withdraw(file_path, date, withdraw_amount):
    with open(file_path, "a") as file:
        file.write(f"- {date} ---> {withdraw_amount}\n")


def see_total_amount(file_path):
    up_money = []
    down_money = []
    with open(file_path) as file:
        lines = file.readlines()
        for line in lines:
            if line[0] == "+":
                up_money.append(float(line[16:]))
            else:
                down_money.append(float(line[16:]))
        result = sum(up_money) - sum(down_money)
        return result


def has_money(file_path):
    total_amount = see_total_amount(file_path)
    if total_amount > 0:
        return True
    else:
        return False
