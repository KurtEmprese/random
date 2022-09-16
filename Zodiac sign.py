#A program that can determine your zodiac sign

#using .capitalize() method will convert the first character of a string to an uppercase letter 
#and all other alphabets to lowercase.
#therefore, you don't need to worry whether you type were lowercase or uppercase.
month = input("What month was your Birthday: ").capitalize() 
day  = int(input("What day was your Birthday: ").capitalize())

if month == "January":
    if day >= 1 and day <= 19:      #putting day >= 1 will make the code more accurate 
        print("Capricorn")          #because if the user input a negative value the condition was still met
    
    elif day >= 20 and day <= 31:   #making elif so that when the user asnwers an out of range number
        print("Aquarius")           #the condition was still met
    
    else:                           #adding error when the user answers an out of range number
        print("Error")

if month == "February":
    if day >= 1 and day <= 17:
        print("Aquarius")
    elif day >= 18 and day <= 28:
        print("Pisces")
    else:
        print("Error")
if month == "March":
    if day >= 1 and day <= 19:
        print("Pisces")
    elif day >= 20 and day <= 31:
        print("Aries")
    else:
        print("Error")
if month == "April":
    if day >= 1 and day <= 19:
        print("Aries")
    elif day >= 20 and day <= 30:
        print("Taurus")
    else:
        print("Error")
if month == "May":
    if day >= 1 and day <= 20:
        print("Taurus")
    elif day >= 21 and day <= 31:
        print("Gemini")
    else:
        print("Error")
if month == "June":
    if day >= 1 and day <= 20:
        print("Gemini")
    elif day >= 21 and day <= 30:
        print("Cancer")
    else:
        print("Error")
if month == "July":
    if day >= 1 and day <= 21:
        print("Cancer")
    elif day >= 21 and day <= 31:
        print("Leo")
    else:
        print("Error")
if month == "August":
    if day >= 1 and day <= 22:
        print("Leo")
    elif day >= 23 and day <= 31:
        print("Virgo")
    else:
        print("Error")
if month == "September":
    if day >= 1 and day <= 22:
        print("Virgo")
    elif day >= 23 and day <= 30:
        print("Libra")
    else:
        print("Error")
if month == "October":
    if day >= 1 and day <= 22:
        print("Libra")
    elif day >= 23 and day <= 31:
        print("Scorpio")
    else:
        print("Error")
if month == "November":
    if day >= 1 and day <= 21:
        print("Scorpio")
    elif day >= 22 and day <= 30:
        print("Sagittarius")
    else:
        print("Error")
if month == "December":
    if day >= 1 and day <= 20:
        print("Sagittarius")
    elif day >= 21 and day <= 31:
        print("Capricorn")
    else:
        print("Error")