# Write a program that computes the molecular weight of a carbohydrate (in 
# grams per mole) based on the number of hydrogen, carbon, and oxygen atoms
# in the molecule. The program should prompt the user to enter the number of
# hydrogen atoms, the number of carbon atoms, and the number of oxygen atoms.
# The program then prints the total combined molecular weight of all the atoms
# based on these individual atom weights:
#   Atom        Weight (grams / mole)
#   ---------------------------------
#   H           1.00794
#   C           12.0107
#   O           15.9994
# For example, the molecular weight of water (H20) is: 2(1.00794) +
# 15.9994 = 18.01528.

GRAMS_PER_MOLE_HYDROGEN = 1.00794
GRAMS_PER_MOLE_CARBON  = 12.0107
GRAMS_PER_MOLE_OXYGEN = 15.9994

def main():
    num_hydrogen = int(input("Number of hydrogen: "))
    num_carbon = int(input("Number of carbon: "))
    num_oxygen = int(input("Number of oxygen: "))
    weight = GRAMS_PER_MOLE_HYDROGEN * num_hydrogen \
             + GRAMS_PER_MOLE_CARBON * num_carbon   \
             + GRAMS_PER_MOLE_OXYGEN * num_oxygen
    print("Molecular weight = ", weight)
    
main()