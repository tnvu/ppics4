# (Advanced) Modify the chaos program so that it accepts two inputs and then 
# prints a table with two columns similar to the one shown in Section 1.9.
# (Note: You will probably not be able to get the columns to line up as nicely
# as those in the example. Chapter 8 discusses how to print numbers with a 
# fixed number of decimal places.)

def exercise08():
    print("This program illustrates a chaotic function")
    x = float(input("Enter first number between 0 and 1: "))
    y = float(input("Enter second number between 0 and 1: "))
    print("input   ", x, "   ", y)
    print("--------------------------")
    for i in range(10):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("       ", x, "    ", y)

exercise08()

# Enter first number between 0 and 1: 0.25
# Enter second number between 0 and 1: 0.26
# input    0.25     0.26
# --------------------------
#         0.73125      0.75036
#         0.76644140625      0.73054749456
#         0.6981350104385375      0.7677066257332165
#         0.8218958187902304      0.6954993339002887
#         0.5708940191969317      0.8259420407337192
#         0.9553987483642099      0.5606709657211202
#         0.166186721954413      0.9606442322820199
#         0.5404179120617926      0.14744687593470315
#         0.9686289302998042      0.49025454937601765
#         0.11850901017563877      0.9746296021493285