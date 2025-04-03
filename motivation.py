import random

quotes = [
    "Believe in yourself and all that you are.",
    "The secret to getting ahead is getting started.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Don't watch the clock; do what it does. Keep going."
    "Cine se trezeste de dimineata buturuga mica rastoarnca caru mare"
]

print("💬 Motivational Quote of the Day:\n")
print(random.choice(quotes))

#Editat editat editat am editat am pushat din nou

listt = ['ceva', 'mananc', 'frumos', 'turnu din pisa', 'caleidoscop', 'gargamel']
randomnum = random.randint(1, len(listt))
randomstring = ' '.join(random.sample(listt, randomnum))
print(randomstring)
