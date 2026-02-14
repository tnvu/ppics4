# Redo Exercise 8 from Chapter 7 to get its data from a file.

def main():
    heating_days = 0
    cooling_days = 0
    inFile = input("Enter filename: ")
    with open(inFile, 'r') as f:
        for l in f:
            t = float(l.strip())
            if t < 60:
                heating_days = heating_days + (60 - t)
            elif t > 80:
                cooling_days = cooling_days + (t - 80)
    print("Number of heating days: " + str(heating_days) + 
          ", number of cooling days: " + str(cooling_days))

main()