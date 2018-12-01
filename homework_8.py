#Homework 8
#1. Use the file random_numbers.txt that you have created in the lab. I want you to split the file into 2
#files called positive_numbers.txt and negative_numbers.txt. The average should be calculated and
#reported in the last line of each file

fileh = open("random_numbers.txt", "r")
file_positive = open("positive_numbers.txt", "w")
file_positive = open("positive_numbers.txt", "r")
file_negative = open("negative_numbers.txt", "w")
file_negative = open("negative_numbers.txt", "r")
positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0
positive_average = 0
negative_average = 0
with open("random_numbers.txt") as fh:
    lines = fh.readlines()
    for i in lines:
        words = i.split()
        for i in words:
            int_i = int(i)
            if int_i >= 0:
                positive_sum += int_i
                positive_count += 1
                print("{} is greater than zero".format(int_i))
                positive_average = int(positive_sum) / int(positive_count)
                positive_append = open("positive_numbers.txt", "a")
                positive_append.write(i)
            elif int_i < 0:
                negative_sum += int_i
                negative_count += 1
                print("{} is less than zero".format(int_i))
                negative_average = int(negative_sum) / int(negative_count)
                negative_append = open("negative_numbers.txt", "a")
                negative_append.write(i)
            positive_average = int(positive_sum) / int(positive_count)
            print("Positive Average: {}".format(positive_average))
            print("Negative Average: {}".format(negative_average))

with open("positive_numbers.txt") as pn:
    positive_average_file = open("positive_numbers.txt", "a")
    positive_average_file.write("\nAverage of all positive values in 'positive_numbers.txt': {}".format(positive_average))

with open("negative_numbers.txt") as nn:
    negative_average_file = open("negative_numbers.txt", "a")
    negative_average_file.write("\nAverage of all negative values in 'negative_numbers.txt': {}".format(negative_average))

#2. Enhance your program 1 so
#- it handles any IOError exceptions that are raised when the file is opened and data is read from it
#- it handles any ValueError exceptions that are raised when the items that are read from the file
#are converted to a number
#- it handles any other exceptions that you feel are needed (BONUS)

fileh = open("random_numbers.txt", "r")
file_positive = open("positive_numbers.txt", "w")
try:
    file_positive = open("positive_numbers.txt", "r")
except IOError:
    print("Error! IOError! Please Try Again!")
file_negative = open("negative_numbers.txt", "w")
try:
    file_negative = open("negative_numbers.txt", "r")
except IOError:
    print("Error! IOError! Please Try Again!")
positive_sum = 0
positive_count = 0
negative_sum = 0
negative_count = 0
positive_average = 0
negative_average = 0
with open("random_numbers.txt") as fh:
    try:
        lines = fh.readlines()
        for i in lines:
            words = i.split()
            for i in words:
                try:
                    int_i = int(i)
                except ValueError:
                    print("Error! Value Error In Attempting To Convert {} into an integer!".format(i))
                if int_i >= 0:
                    positive_sum += int_i
                    positive_count += 1
                    print("{} is greater than zero".format(int_i))
                    positive_average = int(positive_sum) / int(positive_count)
                    positive_append = open("positive_numbers.txt", "a")
                    positive_append.write(i)
                elif int_i < 0:
                    negative_sum += int_i
                    negative_count += 1
                    print("{} is less than zero".format(int_i))
                    negative_average = int(negative_sum) / int(negative_count)
                    negative_append = open("negative_numbers.txt", "a")
                    negative_append.write(i)
                positive_average = int(positive_sum) / int(positive_count)
                print("Positive Average: {}".format(positive_average))
                print("Negative Average: {}".format(negative_average))
    except IOError:
        print("Error! Unable to open file 'random_numbers.txt'!")

with open("positive_numbers.txt") as pn:
    try:
        positive_average_file = open("positive_numbers.txt", "a")
        positive_average_file.write("\nAverage of all positive values in 'positive_numbers.txt': {}".format(positive_average))
    except IOError:
        print("Error! Unable to open file 'positive_numbers.txt'!")

with open("negative_numbers.txt") as nn:
    try:
        negative_average_file = open("negative_numbers.txt", "a")
        negative_average_file.write("\nAverage of all negative values in 'negative_numbers.txt': {}".format(negative_average))
    except IOError:
        print("Error! Unable to open file 'negative_numbers.txt'!")

#3. Personal web page generator (BONUS)
#Write a program that asks the user for his or her name, then asks the user to enter a sentence that
#describes himself or herself.
#Once the user has entered the info, the program should create an HTML file.
#An example:
#<html>
#<head>
#</head>
#<body>
#<center>
#<h1> Jack Ho </h1>
#</center>
#<hr />
#I am an adjunct professor in the Computer Science Department at SJCC/EVC. While I am not
#working, I like to spend time with my family. I have 2 nine-year-old daughters. They like to swim,
#draw and read.
#<hr />
#</body>
#</html>

user_name = input("What is your name? ")
print("User Name: {}".format(user_name))
user_info = input("Describe yourself in a sentence or two: ")
print("User Information: {}".format(user_info))

user_html = open("user.html", "w")

with open("user.html") as uh:
    user_html = open("user.html", "a")
    user_html.write("<html>\n")
    user_html.write("<head>\n")
    user_html.write("<body>\n")
    user_html.write("<center>\n")
    user_html.write("<h1> {} </h1>\n".format(user_name))
    user_html.write("</center>\n")
    user_html.write("<hr />\n")
    user_html.write("<p> {} </p>\n".format(user_info))
    user_html.write("<hr />\n")
    user_html.write("</body>\n")
    user_html.write("</html>\n")

with open("user.html") as ou:
    lines = ou.readlines()
    print(ou)
#<head>
#</head>
#<body>
#<center>
#<h1> Jack Ho </h1>
#</center>
#<hr />
#I am an adjunct professor in the Computer Science Department at SJCC/EVC. While I am not
#working, I like to spend time with my family. I have 2 nine-year-old daughters. They like to swim,
#draw and read.
#<hr />
#</body>
#</html>)



