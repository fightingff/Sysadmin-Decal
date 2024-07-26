 # COMMIT 2: Add dice rolling logic and output dice sum and sequence
    diceSum = random.randint(1, iterations * 6)

    print("{} roll(s) of a {}-sided die resulted in a sum of {}:"
            .format(iterations, sides, diceSum))
