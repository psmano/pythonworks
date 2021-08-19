def simple_gen():
    for x in range(3):
        yield x

for x in simple_gen():
    print(x)
