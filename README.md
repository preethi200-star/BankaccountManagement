#BankaccountManagementSystem
🏦 What this project does

It acts like a mini bank system where:
You can create accounts
You can deposit money
You can withdraw money
You can check your balance

👥 Types of accounts

There are two types of accounts:

1. Savings Account
You can only withdraw what you have
No extra money allowed (no negative balance)
👉 Example:
If you have ₹1000, you can only withdraw up to ₹1000

2. Current Account
You can withdraw more than your balance
But only up to a fixed limit (overdraft)
👉 Example:
If balance is ₹1000 and overdraft limit is ₹500, you can withdraw up to ₹1500

⚙️ How it works 
This project uses OOP (Object-Oriented Programming) concepts:

🧱 Classes & Objects
A class is like a blueprint (e.g., “Account”)
An object is an actual account created from that blueprint
🔗 Inheritance
Savings and Current accounts are based on a common Account class
They reuse common features like deposit & balance
🔒 Encapsulation
Data like balance is protected inside the class
You access it using methods like deposit() or withdraw()
🔄 Polymorphism
The withdraw() function behaves differently:
Savings → strict withdrawal
Current → allows overdraft
🖥️ User interaction

The program shows a menu like:

1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Exit
User enters a number → program performs that action
🎯 What you learn from this
How to structure code using classes
How to reuse code using inheritance
How to control access using encapsulation
How to change behavior using polymorphism
How to build interactive console programs
This is a simple banking simulator that helps you practice OOP concepts in Python in a real-world way.
