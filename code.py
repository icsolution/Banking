import random
import sqlite3


def create_db():
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS card ('
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'number TEXT, pin TEXT, '
                'balance INTEGER DEFAULT 0);')
    conn.commit()


def identifier(number):
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


def exit():
    print('\nBye!')
    quit()


class Bank:

    def __init__(self):
        self.choice = None
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
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
                exit()
            self.choice = None

    def create_account(self):
        card_number = identifier('400000' + str(random.randrange(100000000, 999999999)))
        pin= str(random.randrange(1000, 9999))
        self.update_db(card_number, pin)
        print('\nYour account has been created')
        print(f'Your card number:\n{card_number}')
        print(f'Your card PIN:\n{pin}\n')
        self.active()

    def update_db(self, card, pin):
        self.cur.execute(f'INSERT INTO card (number, pin) VALUES ({card}, {pin});')
        self.conn.commit()

    def log_in(self):
        card = input('\nEnter your card number:\n')
        pin = input('Enter your pin:\n')
        self.cur.execute(f'SELECT * FROM card WHERE number = {card} AND pin = {pin}')
        inquiry = self.cur.fetchall()
        self.conn.commit()
        if inquiry:
            print('\nYou have successfully logged in!\n')
            self.account_status(inquiry)
        else:
            print('\nWrong card number or PIN!\n')
            self.active()

    def account_status(self, inquiry):
        card = inquiry[0][1]
        self.cur.execute(f'SELECT * FROM card WHERE number = {card};')
        inquiry = self.cur.fetchall()
        self.conn.commit()
        print('1. Balance')
        print('2. Add income')
        print('3. Do transfer')
        print('4. Close account')
        print('5. Log out')
        print('0. Exit')
        choice = input()
        balance = inquiry[0][-1]
        if choice == '1':
            print(f"\nBalance: {balance}\n")
            self.account_status(inquiry)
        elif choice == '2':
            income = int(input('\nEnter income:\n'))
            self.cur.execute(f'UPDATE card SET balance + {income} WHERE number = {card};')
            self.conn.commit()
            print('Income was added!\n')
            self.account_status(inquiry)
        elif choice == '3':
            print('\nTransfer')
            card_2 = input('Enter card number:\n')
            if card_2 == card:
                print("You can't transfer money to the same account!\n")
                self.account_status(inquiry)
            elif card_2 != identifier(card_2[:-1]):
                print('Probably you made a mistake in the card number. Please try again!\n')
                self.account_status(inquiry)
            else:
                self.cur.execute(f'SELECT * FROM card WHERE number = {card_2}')
                inquiry_2 = self.cur.fetchall()
                self.conn.commit()
                if not inquiry_2:
                    print('Such a card does not exist.\n')
                    self.account_status(inquiry)
                else:
                    amount = int(input('Enter how much money you want to transfer:\n'))
                    if amount > balance:
                        print('Not enough money!\n')
                        self.account_status(inquiry)
                    else:
                        self.cur.execute(f'UPDATE card SET balance = balance - {amount} WHERE number = {card}')
                        self.cur.execute(f'UPDATE card SET balance = balance + {amount} WHERE number = {card_2}')
                        self.conn.commit()
                        print('Success!\n')
                        self.account_status(inquiry)
        elif choice == '4':
            self.cur.execute(f'DELETE FROM card WHERE number = {card}')
            self.conn.commit()
            print('\nThe account has been closed!\n')
            self.active()

        elif choice == '5':
            print('\nYou have successfully logged out!\n')
            self.active()
        elif choice == '0':
            exit()


create_db()
b = Bank()
