#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username.lower() == "admin" and password == "12345"):
        return "Access granted" 
    else:
        return "Access denied"


def hows_the_weather(temperature):
    # your code here
    if (temperature < 40):
        return "It's brisk out there!"
    elif(40 < temperature < 65):
        return "It's a little chilly out there!"
    elif (temperature > 85):
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

""" 
def hows_the_weather(temperature):
    weather_conditions = {
        33: "It's brisk out there!",
        55: "It's a little chilly out there!",
        75: "It's perfect out there!",
        99: "It's too dang hot out there!"
    }
    return weather_conditions.get(temperature, "Unknown weather condition")
"""

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
       return "FizzBuzz"
    elif num % 3 == 0:
       return "Fizz"
    elif num % 5 == 0:
       return "Buzz"
    else:
       return num

def calculator(operation, num1, num2):
    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            try:
                return num1 / num2
            except ZeroDivisionError:
                print("Error: num2 cannot be equal to 0")
        else:
            print("Invalid operation!")
            return None           
    except TypeError:
        print("Error: input must be of type int")      
        