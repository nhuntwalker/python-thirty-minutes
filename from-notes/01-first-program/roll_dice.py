# -- coding: utf-8 --
"""Simulate rolling one six-sided die."""
import random

print("🎲 Rolling one six-sided die 🎲")

roll_result = random.randint(1, 6)
if roll_result == 1:
    dice_img = """
 _______
|       |
|   o   |
|       |
 -------"""
elif roll_result == 2:
    dice_img = """
 _______
|     o |
|       |
| o     |
 -------"""
elif roll_result == 3:
    dice_img = """
 _______
|     o |
|   o   |
| o     |
 -------"""
elif roll_result == 4:
    dice_img = """
 _______
| o   o |
|       |
| o   o |
 -------"""
elif roll_result == 5:
    dice_img = """
 _______
| o   o |
|   o   |
| o   o |
 -------"""
else:
    dice_img = """
 _______
| o   o |
| o   o |
| o   o |
 -------"""

result = f"You rolled a { roll_result }!"
result = result + dice_img
print(result)