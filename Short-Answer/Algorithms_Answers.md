#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) for given n, loop runs n times before the condition is met. therefore O.time(n)

a as the stored variable is updated each time. therefore O.space(c)


b) for given n, i iterates n times, and everytime j starts at 1, therefore at every iteration of i, j*2 is equal to 2. for any n greater than 1 the while loop runs n times. therefore:
O.time(n)
at each iteration, stored variables (sum, j) get updated, therefore:
O.space(2c) -> O.space(c)


c) for given number of bunnies, function recurses equal times therefore:
O.time(n)

for given number of bunnies, recursion stores and return the number of recursions each time, therefore:
O.space(n)

## Exercise II

for any egg being thrown, if the floor number is greater than or equal to "f", the egg will break, otherwise the egg won't break. since we don't know the number of floors, this becomes a number guessing game.

given n (number of floors in the building), we can start guessing with n/2. if the thrown egg from n/2 floor broke then we need to guess a lower floor, otherwise we need to guess a higher floor.

we will follow above strategy until we get to the answer. this is a binary search problem with complexity of Log(n).
