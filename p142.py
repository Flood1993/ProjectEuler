"""
The sequence of square numbers can be defined as follows:
a(n) = 2*a(n-1) - a(n-2) + 2, with a(1) = 1 and a(2) = 4

We are looking for the difference of two values of this sequence for which the difference is also square.

Let's say we want to check if the difference between terms a(p) and a(q) is a square.

Lets suppose p > q.

a(p) - a(q) = a(c)
2*a(p-1) - a(p-2) + 2 - a(q)
2*(2*a(p-2) - a(p-3) + 2) + a(p-2) + 2 - a(q)
4*a(p-2) - 2*a(p-3) + 4 + a(p-2) + 2 - a(q)
5*a(p-2) - 2*a(p-3) + 6 - a(q)
"""
