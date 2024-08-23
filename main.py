# import datetime

# current_datetime = datetime.datetime.now()
# formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# print("The current date and time is:", formatted_datetime)
# print("The current date and time is:", current_datetime)









# import random

# outcomes = ["Heads", "Tails"]
# result = random.choice(outcomes)
# print(result)





# def count_vowels(string):
#   vowels = ['a', 'e', 'i', 'o', 'u']
#   lowercase_string = string.lower()
#   count = 0

#   for vowel in vowels:
#       count += lowercase_string.count(vowel)

#   return count


# def Another_count_vowels(string):
#   vowels = ['a', 'e', 'i', 'o', 'u']
#   lowercase_string = string.lower()
#   count = 0

#   for char in lowercase_string:
#     if(char in vowels):  
#       count += 1

#   return count
# print(count_vowels("Hello, World!"))  # Output: 3
# print(count_vowels("Python Programming"))  # Output: 4

# print(Another_count_vowels("Hello, World!"))  # Output: 3
# print(Another_count_vowels("Python Programming"))  # Output: 4








# def find_common_elements(list1, list2):
#   common_elements = []

#   for element1 in list1:
#       for element2 in list2:
#           if element1 == element2 and element1 not in common_elements:
#               common_elements.append(element1)

#   return common_elements

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# result = find_common_elements(list1, list2)
# print(result)