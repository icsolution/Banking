import random


class Bank:

    def __init__(self):
        self.card_number = None
        self.pin = None
        self.balance = 0
        self.active()

    def active(self):
        while True:
            print('1. Create an account')
            print('2. Log into account')
            print('0. Exit')
            choice = input()
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.log_in()
            elif choice == '0':
                self.exit()

    def exit(self):
        print('\nBye!')
        quit()

    def create_account(self):
        account_number = str(random.randrange(100000000, 999999999))
        check_sum = str(random.randrange(0, 9))
        self.card_number = '400000' + account_number + check_sum
        self.pin = str(random.randrange(1000, 9999))
        print('\nYour account has been created')
        print(f'Your card number:\n{self.card_number}')
        print(f'Your card PIN:\n{self.pin}\n')

    def log_in(self):
        card_number = input('\nEnter your card number:\n')
        pin = input('Enter your pin:\n')
        if card_number == self.card_number:
            if pin == self.pin:
                print('\nYou have successfully logged in!\n')
                self.account_status()
            else:
                print('\nWrong card number or PIN!\n')
                self.active()

    def account_status(self):
        print('1. Balance')
        print('2. Log out')
        print('3. Exit')
        choice = input()
        if choice == '1':
            print(f'\nBalance: {self.balance}\n')
            self.account_status()
        elif choice == '2':
            print('\nYou have successfully logged out!\n')
            self.active()
        elif choice == '3':
            self.exit()


b = Bank()
