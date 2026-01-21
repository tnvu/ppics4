# Write a program to print the lyrics of the song “Old MacDonald.” Your
# program should print the lyrics for five different animals, similar to the
# # example verse below.
#       Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
#       And on that farm he had a cow, Ee-igh, Ee-igh, Oh!
#       With a moo, moo here and a moo, moo there.
#       Here a moo, there a moo, everywhere a moo, moo.
#       Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!

def eieio():
    return "Ee-igh, Ee-igh, Oh!"

def hadAFarm():
    return "Old MacDonald had a farm, " + eieio() + "\n"

def onThatFarm(animal):
    return "And on that farm he had a " + animal + ", " + eieio() + "\n"

def animalSound(sound):
    line = "With a " + sound + ", " + sound + " here and a "
    line = line + sound + ", " + sound + " there\n"
    line = line + "Here a " + sound + ", there a " + sound + ", everwhere a "
    line = line + sound + ", " + sound + "\n"
    return line

def oldMacDonaldLyrics(animal, sound):
    return hadAFarm() + onThatFarm(animal) + animalSound(sound) + hadAFarm()

def main():
    print(oldMacDonaldLyrics("cow", "moo"))
    print(oldMacDonaldLyrics("pig", "oink"))
    print(oldMacDonaldLyrics("duck", "quack"))
    print(oldMacDonaldLyrics("sheep", "baah"))
    print(oldMacDonaldLyrics("chicken", "cluck"))

main()