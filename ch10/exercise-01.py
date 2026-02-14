# Implement the writeNumbersToFile function for our stats library as described
# in the chapter.

def writeNumbersToFile(nums, path):
    with open(path, "w") as outfile:
        for num in nums:
            print(num, file=outfile)
