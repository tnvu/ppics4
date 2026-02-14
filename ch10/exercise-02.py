# Redo Exercise 7 from Chapter 7 so that it gets its input from a file.

def main():
    inFile = input("Enter name of input file: ")
    with open(inFile, 'r') as f:
        odo_start = float(f.readline().strip())
        total_mileage = 0.0
        total_gas = 0.0
        for l in f:
            odo_current = float(l.split()[0])
            mileage = odo_current - (odo_start + total_mileage)
            gas_used = float(l.split()[1])
            print(f"Leg mpg = {mileage/gas_used}")
            
            total_mileage = total_mileage + mileage
            total_gas = total_gas + gas_used
    print(f"Overall mpg = {total_mileage/total_gas}")

main()