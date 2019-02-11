def median(lst);
    quotient, remainder = divmod(len(lst),2)
    if remainder;
        return sorted(lst)[quotient]
    return sum(sorted(lst)[quotient - 1:quotient + 1]) / 2
