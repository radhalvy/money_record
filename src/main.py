import datetime


def deposit():
    try:
        money_amount = float(
            input("How much money you want to deposit?\nAnswer: "))
    except ValueError:
        print("Invalid amount.")
        return
    return money_amount


def withdraw():
    try:
        money_amount = float(
            input("How much money you want to withdraw?\nAnswer: "))
    except ValueError:
        print("Invalid amount.")
        return
    return money_amount


def get_operation():
    try:
        user_answer = int(
            input("What do you want to do?\n1) Make a deposit, 2) Make a withdrawal, 3) See the account's total amount\nAnswer: "))
    except ValueError:
        print("Invalid option.")
        return
    return user_answer


def total_amount(file_name):
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


def main():
    date = readable_date()
    operation = get_operation()
    if operation == 1:
        user_deposit = deposit()
        with open("money_record.txt", "a") as file:
            file.write(f"+ {date} ---> {user_deposit}\n")
        print("Deposit completed succesfully!")
    elif operation == 2:
        user_withdraw = withdraw()
        with open("money_record.txt", "a") as file:
            file.write(f"- {date} ---> {user_withdraw}\n")
        print("Withdraw completed succesfully!")
    elif operation == 3:
        print(total_amount("./money_record.txt"))
    else:
        print("Invalid operation.")
        return


main()
