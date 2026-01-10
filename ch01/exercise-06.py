# The calculation performed in the chaos program can be written in a number of
# ways that are algebraically equivalent. Write a version of the program for 
# each of the following ways of doing the computation. Have your modified 
# programs print out 100 iterations of the calculation and compare the results
#  when run on the same input.
#       a) 3.9 * x * (1 - x)
#       b) 3.9 * (x - x * x)
#       c) 3.9 * x - 3.9 * x * x
# Explain the results of this experiment. Hint: See discussion question 
# number 4, above.

def chaos01():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
chaos01()
# Enter a number between 0 and 1: 0.25
# 0.73125
# 0.76644140625
# 0.6981350104385375
# 0.8218958187902304
# 0.5708940191969317
# 0.9553987483642099
# 0.166186721954413
# 0.5404179120617926
# 0.9686289302998042
# 0.11850901017563877

def chaos02():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * (x - x * x)
        print(x)
chaos02()
# Enter a number between 0 and 1: 0.25
# 0.73125
# 0.76644140625
# 0.6981350104385374
# 0.8218958187902304
# 0.5708940191969316
# 0.9553987483642099
# 0.16618672195441295
# 0.5404179120617923
# 0.9686289302998042
# 0.11850901017563896

def chaos03():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x - 3.9 * x * x
        print(x)
chaos03()
# Enter a number between 0 and 1: 0.25
# 0.73125
# 0.76644140625
# 0.6981350104385374
# 0.8218958187902304
# 0.5708940191969316
# 0.9553987483642099
# 0.16618672195441295
# 0.5404179120617923
# 0.9686289302998042
# 0.11850901017563896

# the values are different because the intermediate products are different
# approximations of the true values