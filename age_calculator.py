####age calculator  in this aplicarion the user enters a date of birth as a input  and the aplication gives his age as a output ##
def ageCalculator(y, m, d): ###define my fuction ##
    import datetime ## import datetime module
    today = datetime.datetime.now().date() ##todays date
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)
ageCalculator(1992,11,20)