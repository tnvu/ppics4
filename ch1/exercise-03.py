# Modify the chaos program using 2.0 in place of 3.9 as the multiplier in the 
# logistic function. Your modified line of code should look like this:
#     x = 2.0 * x * (1 - x)
# Run the program for various input values and compare the results to those
# obtained from the original program. Write a short paragraph describing any
# differences that you notice in the behavior of the two versions.

def main():
    print("This program illustrates a chaotic function")
    x = float(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)


main()

# Enter a number between 0 and 1: 0.25
# 0.375
# 0.46875
# 0.498046875
# 0.49999237060546875
# 0.4999999998835847
# 0.5
# 0.5
# 0.5
# 0.5
# 0.5

# Enter a number between 0 and 1: 0.26
# 0.38480000000000003
# 0.47345792000000003
# 0.49859103597854726
# 0.4999960296407725
# 0.4999999999684725
# 0.49999999999999994
# 0.49999999999999994
# 0.49999999999999994
# 0.49999999999999994
# 0.49999999999999994

# the values seem to want to converge on 0.5