# Expand your solution to the previous problem to allow the calculation of
# a complete name such as ‘John Marvin Zelle” or “John Jacob Jingleheimer
# Smith.” The total value is just the sum of the numeric values of all the
# names.

### COPIED FROM CH08 EXERCISE 04 ###
def calc_name_value(name):
    value = 0
    for c in name:
        if c.isalpha():
            value = value + (ord(c.lower()) - ord('a') + 1)
    return value

def main():
    complete_name = input("Enter a complete name: ")
    names = complete_name.split()
    value = 0
    for n in names:
        value = value + calc_name_value(n)
    print("Complete name value =", value)

main()