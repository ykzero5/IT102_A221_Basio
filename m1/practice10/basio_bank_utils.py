"""
########## Learning Signature ##########
Programmed by: Yma Khaliya L. Basio
Date Submitted: September 14, 2026

Program Description: This file contains reusable utility functions for validating amounts and formatting currency.
Reflection: I learned how helper functions can reduce repeated code and keep a program organized.

AI Usage
[ ] No AI Assistance - Completed independently without AI.
[X] AI as Support Tool - Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner - Used AI to design, structure, or co-create significant code.
"""

def is_valid_amount(amount):

    return amount > 0


def format_currency(amount):

    return f"₱{amount:,.2f}"