def boys_and_girls():
    # the probability that the student is a girl
    pg = 40 / 100

    # the probability that the student is a boy
    pb = 60 / 100

    # the probability of a randomly selected student wearing trousers.
    # All boys wear trousers and half of the girls wear trousers
    pt = pb + (pg / 2)

    # the probability of the student wearing trousers given that the student is a girl
    ptg = 1 / 2

    # the probability of a student to be a girl, given that the student is wearing trousers
    pgt = (ptg * pg) / pt

    print("P(g|t): ", pgt)


boys_and_girls()
