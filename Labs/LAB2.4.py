day = int(input("Enter your birth day: "))
month = int(input("Enter your birth month (1-12): "))

if (month == 1 and day >= 20) or (month == 2 and day <= 18):
    sign = "Aquarius"
elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
    sign = "Pisces"
elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
    sign = "Aries"
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    sign = "Taurus"
elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
    sign = "Gemini"
elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
    sign = "Cancer"
elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
    sign = "Leo"
elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
    sign = "Virgo"
elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
    sign = "Libra"
elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
    sign = "Scorpio"
elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
    sign = "Sagittarius"
else:
    sign = "Capricorn"

print(f"Your horoscope sign is {sign}.")
