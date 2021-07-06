# Banking

Virtual banking system which utilizes SQL database to create, delete, and update accounts via user input.

Features include:
1. Randomly generated account, card, and pin numbers when user selects to create a new account
2. Real world account numbers based off standards in place
3. Real world card numbers are generated and validated by the Luhn algorithm
4. Once created these are then stored in the bank's database which is maintained seperate from user activity
5. Once logged in users have the choice to check balance, deposit money, make transfers, delete account, or log out
6. Transfers can only be made to existing bank accounts
7. Once a user selects to close account it is deleted from the database
