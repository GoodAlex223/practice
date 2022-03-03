def product_special_pythagorean_triplet(sum_of_triplet):

    """Special Pythagorean triplet. Problem 9. 14.01.21

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2
    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc. Only for natural numbers"""
    for b in range(1, sum_of_triplet):      # Only for natural numbers
        for a in range(1, b):
            c = (a**2 + b**2)**(1/2)
            if a + b == sum_of_triplet - c:
                return a*b*int(c)
    # listed = []
    # [[" ".join([str(a), str(b), str(int((a**2 + b**2)**(1/2)))])
    #   for a in range(1, b) if a + b == sum_of_triplet - (a**2 + b**2)**(1/2)]
    #  for b in range(1, sum_of_triplet)]
    # return listed


print(product_special_pythagorean_triplet(1000))
