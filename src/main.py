import datetime


def get_deposit():
    money_amount = float(
        input("How much money you want to deposit?\nAnswer: "))
    return money_amount


def get_withdraw():
    money_amount = float(
        input("How much money you want to withdraw?\nAnswer: "))
    return money_amount


def get_operation():
    user_answer = input(
        "What do you want to do?\n1) Make a deposit, 2) Make a withdrawal, 3) See the account's total amount\nAnswer: ")
    return user_answer


def see_total_amount(file_name):
    up_money = []
    down_money = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            if line[0] == "+":
                up_money.append(float(line[16:]))
            else:
                down_money.append(float(line[16:]))
        result = sum(up_money) - sum(down_money)
        return result


def readable_date():
    date = datetime.datetime.now()
    formatted_date = date.strftime("%x")
    return formatted_date


def has_money(file_name):
    total_amount = see_total_amount(file_name)
    if total_amount > 0:
        return True
    else:
        return False


def write_deposit(file_name, date, deposit_amount):
    with open(file_name, "a") as file:
        file.write(f"+ {date} ---> {deposit_amount}\n")


def write_withdraw(file_name, date, withdraw_amount):
    with open(file_name, "a") as file:
        file.write(f"- {date} ---> {withdraw_amount}\n")


def main():
    date = readable_date()
    operation = get_operation()
    file_name = "money_record.txt"
    file_path = "./money_record.txt"
    total_amount = see_total_amount(file_path)
    if operation == "1":
        try:
            user_deposit = get_deposit()
        except ValueError:
            print("\nInvalid amount.")
        else:
            write_deposit(file_name, date, user_deposit)
            print("\nDeposit completed succesfully!")
    elif operation == "2":
        if has_money(file_path):
            try:
                user_withdraw = get_withdraw()
            except ValueError:
                print("\nInvalid amount.")
                return
            else:
                if user_withdraw > total_amount:
                    print(
                        "\nThere's not enough money in your account to complete the process.")
                    return
                else:
                    write_withdraw(file_name, date, user_withdraw)
                    print("\nWithdraw completed succesfully!")
        else:
            print("\nYou don't have money in your account.")
            return
    elif operation == "3":
        print(total_amount)
    else:
        print("\nInvalid operation.")
        return


main()
