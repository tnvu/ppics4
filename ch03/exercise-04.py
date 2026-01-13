# Write a program that determines the distance to a lightning strike based on
# the time elapsed between the flash and the sound of thunder. The speed
# of sound is approximately 1100 ft/sec and 1 mile is 5280 ft.

SPEED_OF_SOUND_FT_PER_SEC = 1100
FEET_PER_MILE = 5280

def main():
    elapsed_time = float(input(
        "Elapsed time between flash and sound of thunder: "))
    miles_distance = elapsed_time * SPEED_OF_SOUND_FT_PER_SEC / FEET_PER_MILE
    print("Distance in miles: ", miles_distance)

main()