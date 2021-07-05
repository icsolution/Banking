import random
import sqlite3


def create_db():
    conn = sqlite3.connect('card.s3db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);')
    conn.commit()
    # cur.execute('SELECT * FROM card')
    # print(cur.fetchall())


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
                self.exit()
            self.choice = None

    def exit(self):
        print('\nBye!')
        quit()

    def create_account(self):
        card_number = self.identifier('400000' + str(random.randrange(100000000, 999999999)))
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
        if inquiry:
            print('\nYou have successfully logged in!\n')
            self.account_status(inquiry)
        else:
            print('\nWrong card number or PIN!\n')
            self.active()

    def account_status(self, inquiry):
        print('1. Balance')
        print('2. Log out')
        print('0. Exit')
        choice = input()
        if choice == '1':
            print(f"\nBalance: {inquiry[0][-1]}\n")
            self.account_status(inquiry)
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


create_db()
b = Bank()

