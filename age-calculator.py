from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    age_years = today.year - birthdate.year
    age_months = today.month - birthdate.month
    age_days = today.day - birthdate.day

    if age_days < 0:
        age_months -= 1
        age_days += 30  # Approximate handling for negative days

    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

def main():
    print("📅 Welcome to the Age Calculator!")
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

    try:
        birthdate = datetime.strptime(dob_input, "%Y-%m-%d")
        years, months, days = calculate_age(birthdate)
        print(f"🧓 Your age is: {years} years, {months} months, and {days} days.")
    except ValueError:
        print("❌ Invalid date format! Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()