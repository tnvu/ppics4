# Review Questions

# True/False
# 1.  F Object-oriented design is the process of finding and defining a useful
#       set of functions for solving a problem.
# 2.  F Candidate objects can be found by looking at the verbs in a problem
#       description.
# 3.  T Typically, the design process involves considerable trial and error.
# 4.  T GUIs are often built with a model-view architecture.
# 5.  F Hiding the details of an object in a class definition is called 
#       instantiation.
# 6.  T In an interactive animation, the animation loop and the event loop are
#       combined.
# 7.  T A modal dialog demands user interaction.
# 8.  T Polymorphism literally means “many changes.”
# 9.  F A superclass inherits behaviors from its subclasses.
# 10. F GUIs are generally easier to write than text-based interfaces.

# Multiple Choice
# 1.    Which of the following was not a class in the racquetball simulation?
#       a) Player
#       b) SimStats
#       c) RBallGame
#     X d) Score
# 2.    What is the data type of server in an RBallGame?
#       a) int
#     X b) Player
#       c) bool
#       d) SimStats
# 3.    The isOver method is defined in which class of the racquetball simulation?
#       a) SimStats
#     X b) RBallGame
#       c) Player
#       d) PokerApp
# 4.    In the ProjectileApp class, what is stored in the instance variable shots?
#     X a) ShotTracker objects
#       b) Circle objects
#       c) Projectile objects
#       d) ints
# 5.    What is the purpose of a ShotTracker?
#       a) It keeps track of all the shots that have been fired.
#     X b) It keeps track of a single shot.
#       c) It combines a Circle and a Projectile.
#       d) Both b) and c) are correct.
# 6.    What do the arrows in a class diagram show?
#       a) how information is passed via parameters and return values
#       b) that a class uses (depends on) another class
#       c) where a class is defined
#     X d) all of the above
# 7.    Which of the following is not one of the fundamental characteristics of
#       object-oriented design/programming?
#       a) inheritance
#       b) polymorphism
#     X c) generality
#       d) encapsulation
# 8.    Which of the following is not part of the object-oriented design
#       process?
#       a) look for object candidates
#       b) refine nontrivial methods
#       c) try out alternatives
#     X d) embrace complexity
# 9.    Separating the user interface from the “guts” of an application is 
#       called a(n) ___ approach.
#       a) abstract
#       b) object-oriented
#       c) model-theoretic
#     X d) model-view
# 10.   Inheritance is when
#       a) one class uses another
#       b) data is hidden
#       c) a method uses data from self
#     X d) a class borrows data and/or behavior from another class

# Discussion
# 1.    In your own words, describe the process of OOD.
#           Reading the problem
#           Finding objects
#           Finding data and methods
#           Cooking it all together
# 2.    In your own words, define encapsulation, polymorphism, and inheritance.
#           Encapsulation - hiding implementation details
#           Polymorphism - Same call can be used on multiple objects
#           Inheritance - Class hierarchy
# 3.    The termination condition for the cannonball simulation is written as
#           if key in ["q", "Q"]:
#       Since in is a sequence operator and strings are also sequences, it 
#       seems like this condition could also be written as:
#           if key in "qQ":
#       Unfortunately the second version doesn’t work. Explain what is wrong 
#       with the second approach. Hint: What does checkKey return when no key
#       has been pressed?
#           An empty string is a substring of every string,
#           so if "" in <any string> will always be True.