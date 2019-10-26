slogan=str(input("Введіть слово:"))[::-1]
words=slogan.split()
slogan_reverse=" ".join(reserved(words))
ptint(slogan_reverse)
    