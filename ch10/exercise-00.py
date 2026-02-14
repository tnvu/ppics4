# Review Questions

# True/False
# 1.    A file is a sequence of data stored in secondary memory.        True
# 2.    In order to use text files in Python, you need to know the
#       end-of-line marking convention for your operating system.       False
# 3.    Associating a file with an object in a program is called
#       reading the file.                                               False
# 4.    Operating on a file inside a with statement ensures that
#       the file gets closed.                                           True
# 5.    The best way to loop over the lines of text file is to
#       use a while loop.                                               False
# 6.    A relative file path gives the location of the file starting
#       from the root directory.                                        False
# 7.    Different operating systems have slightly different standard
#       notation for specifying file paths.                             True
# 8.    Batch mode programs do their input and output on files.         True
# 9.    Iterating over files whose paths match a certain pattern is
#       known as file surfing.                                          False
# 10.   Text files are generally opened in binary mode.                 False

# Multiple Choice
# 1.    What character does Python use to indicate end-of-line in text files?
#     X a) \n
#       b) \r
#       c) \t
#       d) It depends on the OS.
# 2.    The easiest type of files to work with are
#     X a) text files
#       b) binary files
#       c) case files
#       d) nail files
# 3.    Which of the following is not part of the basic file-processing
#       outline?
#       a) opening the file
#       b) reading from the file
#     X c) renaming the file
#       d) closing the file
# 4.    Which of the following is not a legal mode for opening a file?
#       a) "r"
#     X b) "rw"
#       c) "rb"
#       d) "w"
# 5.    What character(s) in a file path indicates “the current working
#       directory?”
#     X a) .
#       b) ..
#       c) \
#       d) cwd
# 6.    What character(s) in a file path means “go up one level”?
#       a) .
#     X b) ..
#       c) \
#       d) up
# 7.    A Path object is useful for
#       a) extracting the parts of a path string
#       b) determining if a file already exists
#       c) renaming a file
#     X d) all of the above
# 8.    Which of the following files would match the globbing pattern, "exam?.*"?
#       a) exam.txt
#     X b) examl.jpg
#       c) examl0.txt
#       d) exams
# 9.    When a file is opened in binary mode, data is read/written as what
#       type?
#     X a) bytes
#       b) string
#       c) float
#       d) file
# 10.   One disadvantage of using the pickle module to save data is
#       a) it won’t work with Python’s built-in types
#       b) the data can’t be loaded back in again
#       c) it requires a lot of salt
#     X d) the data is not stored in a human-readable format.

# Discussion
# 1.    Explain why it is generally a good idea to use a with statement to handle
#       opening files.
#       It will automatically handle closing the files using the context manager.
# 2.    Consider the following simple file system contents (the circles represent
#       directories).
#                               /
#                             home
#                   user1               user2
#             prog1.py prog2.py     prog1.py prog2.py
#       Suppose the current working directory is /home/user1.
#       a) What is the absolute path to user1’s prog1?
#           /home/user1/prog1.py
#       b) What is the relative path to user1’s prog1?
#           prog1.py
#       c) What is the absolute path to user2’s prog2?
#           /home/user2/prog2.py
#       d) What is the relative path to user2’s prog2?
#           ../user2/prog2.py
#       e) What glob pattern would find all of user1’s Python programs?
#           /home/user1/*.py
#       f) What glob pattern would find all of user2’s Python programs?
#           /home/user2/*.py
#       g) What glob pattern would find all the Python programs of both users?
#           /home/*/*.py
