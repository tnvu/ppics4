# Write a program to print the lyrics for ten verses of “The Ants Go
# Marching.” A couple of sample verses are given below. You may choose your
# own activity for the “little one” in each verse, but be sure to choose
# something that makes the rhyme work (or almost work).
#       The ants go marching one by one, hurrah! hurrah!
#       The ants go marching one by one, hurrah! hurrah!
#       The ants go marching one by one,
#       The little one stops to suck his thumb,
#       And they all go marching down...
#       In the ground...
#       To get out....
#       Of the rain.
#       Boom! Boom! Boom!
#       The ants go marching two by two, hurrah! hurrah!
#       The ants go marching two by two, hurrah! hurrah!
#       The ants go marching two by two,
#       The little one stops to tie his shoe,
#       And they all go marching down...
#       In the ground...
#       To get out...
#       Of the rain.
#       Boom! Boom! Boom!

def hurrah():
    return "hurrah! hurrah!"

def goMarching(num):
    return "The ants go marching " + num + " by " + num + ", "

def littleOne(activity):
    return "The little one stops to " + activity

def end():
    lyrics = ""
    lyrics = lyrics + "And they all go marching down..." + "\n"
    lyrics = lyrics + "In the ground..." + "\n"
    lyrics = lyrics + "To get out..." + "\n"
    lyrics = lyrics + "Of the rain." + "\n"
    lyrics = lyrics + "Boom! Boom! Boom!"
    return lyrics

def verse(num, activity):
    lyrics = ""
    lyrics = lyrics + goMarching(num) + hurrah() + "\n"
    lyrics = lyrics + goMarching(num) + hurrah() + "\n"
    lyrics = lyrics + goMarching(num) + "\n"
    lyrics = lyrics + littleOne(activity) + "\n"
    lyrics = lyrics + end()
    return lyrics

def main():
    print(verse("one", "suck his thumb"))
    print(verse("two", "tie his shoe"))
    print(verse("three", "go pee"))
    print(verse("four", "close the door"))
    print(verse("five", "feel alive"))
    print(verse("six", "draw some pics"))
    print(verse("seven", "go to heaven"))
    print(verse("eight", "eat a date"))
    print(verse("nine", "snort a line"))
    print(verse("ten", "do it all again"))

main()