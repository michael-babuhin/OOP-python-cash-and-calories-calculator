# OOP project (Money and calories calculator)
**My goals**:
I took this task and the tests from Yandex context to check my knowledge of the basics of the language, OOP and also working with git.

Money and calorie calculator - tools for controlling expenses and income

**Mission Statement**

Create two calculators: for counting money and calories. You only need logic - a separate class for each of the calculators.

The money calculator should be able to:
- Save a new expense record using the add_record() method
- count how much money is spent today using get_today_stats() method
- Determine how much more money can be spent today in rubles, dollars, or euros - get_today_cash_remained(currency) method
- Count how much money has been spent over the last 7 days - get_week_stats() method

The calorie calculator should be able to:
- Save a new record of food intake - add_record() method
- Count how many calories have been eaten today - get_today_stats() method
- Determine how many more calories you can/need to get today - get_calories_remained() method
- Count how many calories you have received in the last 7 days - get_week_stats() method

General functionality of calculators (must be included in Calculator class):
- They should be able to store some records (of food or money, but essentially all numbers and dates) 
- Know a daily limit (how much money you can spend per day or how many calories you can get)
- Add up the entries for specific dates.

The constructor of the Calculator class must accept one argument: 
- number limit (the daily spending/calorie limit that the user has set).

----------------------------------------------------------------------------------------------------
For testing use pytest in requrements.txt

