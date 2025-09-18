import random
names = ['Korasaki', 'Monkey.D.Luffy', 'Sakuragi', 'Zoro', 'Sanji', 'Gon', 'Killua', 'Kibutsuji', 'Nami',
         'Teach', 'Ussop', 'Jimbe']
for _ in range(1,4):
    print(f"The winner of the {_} round is:... ")
    winner = random.choice(names)
    print(winner)