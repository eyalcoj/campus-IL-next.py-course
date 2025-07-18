def get_fibo():
    x1 = 0
    x2 = 1
    yield 0
    yield 1
    while True:
        new_x = x1 + x2
        x1 = x2
        x2 = new_x
        yield new_x


if __name__ == "__main__":
    fibo_gen = get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
