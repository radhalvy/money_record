from functions import *


def main():
    date = get_readable_date()
    operation = get_operation()
    file_path = "/home/tiger/Deposito_Local/python_projects/money_record/src/money_record.txt"
    total_amount = see_total_amount(file_path)
    if operation == "1":
        try:
            user_deposit = get_deposit()
        except ValueError:
            print("\nInvalid amount.")
        else:
            if user_deposit > 0:
                write_deposit(file_path, date, user_deposit)
                print("\nDeposit completed succesfully!")
            else:
                print("\nInvalid amount.")
                return
    elif operation == "2":
        if has_money(file_path):
            try:
                user_withdraw = get_withdraw()
            except ValueError:
                print("\nInvalid amount.")
                return
            else:
                if (user_withdraw > total_amount) or (user_withdraw <= 0):
                    print(
                        "\nThere's not enough money in your account to complete the process \nor you're entering a negative number/zero.")
                    return
                else:
                    write_withdraw(file_path, date, user_withdraw)
                    print("\nWithdraw completed succesfully!")
        else:
            print("\nYou don't have money in your account.")
            return
    elif operation == "3":
        print(f"\n${total_amount}\n")
    elif operation == "4":
        print(f"\n{get_history(file_path)}")
    else:
        print("\nInvalid operation.")
        return


main()
