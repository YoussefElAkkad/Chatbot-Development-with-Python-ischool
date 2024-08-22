# import math
# #Finding the square root of a number
# number=25
# result=math.sqrt(number)
# print("The square root of", number,"is",result)
# #gettng the value of pi
# pi_Value=math.pi
# print("The value of pi is",pi_Value)







# import datetime
# #Getting the current date and time
# current_time=datetime.datetime.now()
# print("The current date and time are:",current_time)
# #Getting the current year
# current_year=current_time.year
# print("We are in the year", current_year)




# import math
# help(math)
# help(math.sqrt)




# #Alias ( Nick name )
# import math as m
# area_cirle= m.pi*5*5
# print(area_cirle)











# import datetime

# def calculate_age(birthdate):
#   current_date = datetime.datetime.now().date()
#   age = current_date.year - birthdate.year
# # Adjust age if birthdate hasn't occurred yet this year
#   if current_date.month < birthdate.month or (current_date.month == birthdate.month and current_date.day < birthdate.day):
#     age -= 1
#   return age


# def robot_interaction():
#   print("Welcome to the Marathon Registration!")
#   print("Please enter your birthdate (YYYY-MM-DD):")
#   birthdate_input = input()
#   try:
#     birthdate = datetime.datetime.strptime(birthdate_input, "%Y-%m-%d").date()
#     age = calculate_age(birthdate)
#     print("Your age is:", age, "years")
#   except ValueError:
#     print("Invalid input. Please enter the date in the correct format.")


# robot_interaction()





