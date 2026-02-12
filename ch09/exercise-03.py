# The inner product of two vectors (sequences of numbers) is an important 
# measure of similarity and is an essential core operation in modern AI
# systems based on artificial neural networks. Write and test a function
# innerProd(x, y) that computes the inner product of two (same length) lists.
# The inner product of z and y is computed as:
#       summation(i=0, n-1) x_i * y_i
# For example, innerProd([1, 2, 3], [4, 5, 6]) produces 32
# since 1(4)+ 2(5) + 3(6) = 32

def innerProd(x, y):
    total = 0
    for i in range(len(x)):
        total = total + (x[i] * y[i])
    return total
