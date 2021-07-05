import random


class Bank:

    def __init__(self):
        self.accounts = {}
        self.choice = None
        self.active()

    def active(self):
        while not self.choice:
            print('1. Create an account')
            print('2. Log into account')
            print('0. Exit')
            self.choice = input()
            if self.choice == '1':
                self.create_account()
            elif self.choice == '2':
                self.log_in()
            elif self.choice == '0':
                self.exit()
            self.choice = None


    def exit(self):
        print('\nBye!')
        quit()

    def create_account(self):
        account_number = str(random.randrange(100000000, 999999999))
        check_sum = str(random.randrange(0, 9))
        card_number = '400000' + account_number
        card_number = self.identifier(card_number)
        if card_number not in self.accounts:
            self.accounts[card_number] = dict(pin=str(random.randrange(1000, 9999)), balance=0)
            print('\nYour account has been created')
            print(f'Your card number:\n{card_number}')
            print(f'Your card PIN:\n{self.accounts[card_number]["pin"]}\n')
            self.active()
        else:
            self.active()

    def log_in(self):
        global current_card
        current_card = None
        card_number = input('\nEnter your card number:\n')
        pin = input('Enter your pin:\n')
        if card_number in self.accounts and pin == self.accounts[card_number]['pin']:
            print('\nYou have successfully logged in!\n')
            current_card = card_number
            self.account_status()
        else:
            print('\nWrong card number or PIN!\n')
            self.active()

    def account_status(self):
        global current_card
        print('1. Balance')
        print('2. Log out')
        print('0. Exit')
        choice = input()
        if choice == '1':
            print(f"\nBalance: {self.accounts[current_card]['balance']}\n")
            self.account_status()
        elif choice == '2':
            print('\nYou have successfully logged out!\n')
            self.active()
        elif choice == '0':
            self.exit()

    def identifier(self, number):
        result = []
        for index, digit in enumerate(number):
            if index == 0 or index % 2 == 0:
                new = int(digit) * 2
                if new > 9:
                    result.append(new - 9)
                else:
                    result.append(new)
            else:
                result.append(int(digit))
        result = sum(result)
        if result % 10 == 0:
            sum_check = '0'
        else:
            target = (result // 10 + 1) * 10
            sum_check = str(target - result)

        return number + sum_check

b = Bank()
