def gcd(greatest , smallest):
    remainder = greatest % smallest
    quotient = greatest // smallest

    if remainder != 0:
        gcd(smallest , remainder)
    else:
        print(f"GCD is {smallest}")
        return None


