"""
########## Learning Signature ##########
Programmed by: Yma Khaliya L. Basio
Date Submitted: September 23, 2026

Program Description: This file defines the bank account classes and demonstrates the main OOP concepts.
Reflection: I learned how encapsulation, abstraction, inheritance, and polymorphism can work together in one class structure.

AI Usage
[ ] No AI Assistance - Completed independently without AI.
[X] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""

from abc import ABC, abstractmethod


class BankAccount(ABC):

    def __init__(
        self,
        account_number,
        name,
        pin,
        starting_balance
    ):
        self.account_number = account_number
        self.account_name = name

        # Encapsulation
        self._pin = pin
        self._balance = starting_balance

    # Encapsulation
    def check_balance(self):

        return self._balance

    def deposit(self, amount):

        if amount <= 0:
            return False

        self._balance += amount

        return True

    def withdraw(self, amount):

        if amount <= 0:
            return False

        if amount > self._balance:
            return False

        self._balance -= amount

        return True

    def verify_pin(self, pin):

        return self._pin == pin

    # Used by storage when the account
    # needs to be saved.
    def get_pin(self):

        return self._pin

    # Improvement:
    # Update balance using a method instead
    # of directly accessing _balance.
    def update_balance(self, new_balance):

        if new_balance < 0:
            return False

        self._balance = new_balance

        return True

    # Abstraction
    @abstractmethod
    def get_account_type(self):

        pass


# Inheritance
class SavingsAccount(BankAccount):

    # Polymorphism
    def get_account_type(self):

        return "Savings Account"


# Inheritance
class StudentAccount(BankAccount):

    # Polymorphism
    def get_account_type(self):

        return "Student Account"