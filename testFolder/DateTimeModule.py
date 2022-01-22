import datetime as dt

#the datetime module contains various classes. Popular classes include: date class, time class and datetime class

#print(dt.date.today())
#print(dt.time.)

#datetime.date class
date1 = dt.date(2022,1,16)
print(date1)
print("Year: ", date1.year)
print("Month: ", date1.month)
print("Day: ", date1.day)
##################################################################################################################

#datetime.time class
time1 = dt.time(23,23,23,256687)
print(time1)
print(time1.hour)
print(time1.minute)
print(time1.second)
print(time1.microsecond)
##################################################################################################################

#datetime.datetime class
datetime1 = dt.datetime(1991, 6, 23, 10, 20, 45, 655256)
print(datetime1)
print(datetime1.date())
print(datetime1.time())

###################################################################################################################

#To get current date and time
print(dt.datetime.now())

##################################################################################################################
#datetime.timedelta class: This object represents diffrence between 2 datestimes

current_time = dt.datetime.now()
next_year = dt.datetime(2023,1,1,00,00,1)

#Difference between 2 date time returns a timedelta object
timediff = next_year - current_time
print(timediff)
print(type(timediff))

#This timedelta obj can also be added/subtracted to the datetime object to get new datetime object

##################################################################################################################

#datetime.strftime(): returns a string representing date and time for the datetime object
current_time = dt.datetime.now()
string_date = current_time.strftime("%a, %B %d, %Y")        #Diff format codes to achieve different formats 
print(string_date)

string_date1 = current_time.strftime("%b %d, %Y, %I %p")
print(string_date1)

##################################################################################################################

#datetime.strptime(): Opposite to .strftime(): converts string to datetime object

date_string = "21 June, 2021"

datetime_object = dt.datetime.strptime(date_string, "%d %B, %Y")

print(datetime_object)


