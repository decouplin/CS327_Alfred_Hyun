import datetime

class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def get_name(self) -> str:
        return self.name

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age

    def calculate_age_in_years_and_days(self):
        today = datetime.date.today()
        age = today - self.birth_date
        years = age.days // 365
        remaining_days = age.days % 365
        return years, remaining_days

    def __str__(self) -> str:
        y, d = self.calculate_age_in_years_and_days()
        return f"{self.get_name()}'s age is {y} years and {d} days."

# Example usage
if __name__ == "__main__":
    # datetime.date object is in (year, month, date) 
    eco = Person("Adam Smith", datetime.date(1723, 6, 16))
    print(eco)
