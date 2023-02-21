import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    """Метод add_record добавляет запись в список records."""

    def add_record(self, record):
        self.records.append(record)

    """Метод get_today_stats возращает сумму операций за день."""

    def get_today_stats(self):
        today = dt.datetime.now().date()
        amount_today = [record.amount for record in self.records if today == record.date]
        return sum(amount_today)

    """Метод week_stats возвращает сумму операций за неделю"""

    def get_week_stats(self):
        now = dt.datetime.now().date()
        week_ago = now - dt.timedelta(days=7)
        amount_week = [record.amount for record in self.records if week_ago <= record.date]
        return sum(amount_week)


class CashCalculator(Calculator):
    """Константы валютных курсов."""
    USD_RATE = 74.04
    EURO_RATE = 79.13

    """Метод для подсчета свободных денег."""

    def get_today_cash_remained(self, currency):
        currency_name = {"rub": ("руб", 1),
                         "usd": ("USD", self.USD_RATE),
                         "eur": ("Euro", self.EURO_RATE)}
        total_amount = self.get_today_stats()

        if currency in currency_name:
            currency_presentation, exchange_rate = currency_name[currency]
            balance = abs((self.limit - total_amount) / exchange_rate)
            if total_amount < self.limit:
                return f'На сегодня осталось {balance:.2f} {currency_presentation}'
            elif total_amount == self.limit:
                return 'Денег нет, держись'
            else:
                return f'Денег нет, держись: твой долг - {balance:.2f} {currency_presentation}'


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        total_amount = self.get_today_stats()
        balance = self.limit - total_amount
        if self.limit > total_amount:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {balance} кКал'
        elif self.limit < total_amount:
            return f'Хватит есть!'


class Record:
    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        date_format = '%d.%m.%Y'
        if isinstance(date, str):
            self.date = dt.datetime.strptime(date, date_format).date()
        else:
            self.date = date
        self.amount = amount
        self.comment = comment

    """Метод вывода информации о записе в строковом формате."""

    def __str__(self):
        print(f"{self.amount} - ammount,\n {self.comment} - comment,\n"
              f"{self.date} - date")
