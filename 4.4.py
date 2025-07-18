def gen_secs():
    for i in range(0, 60):
        yield i


def gen_minutes():
    for i in range(0, 60):
        yield i


def gen_hours():
    for i in range(0, 24):
        yield i


def gen_time():
    is_roll = True
    secs = gen_secs()
    minutes = gen_minutes()
    hours = gen_hours()

    secs_value = next(secs)
    minutes_value = next(minutes)
    hours_value = next(hours)
    while is_roll:
        try:
            yield f"{hours_value}:{minutes_value}:{secs_value}"
            secs_value = next(secs)
        except:
            try:
                yield f"{hours_value}:{minutes_value}:{secs_value}"
                minutes_value = next(minutes)
                secs = gen_secs()
                secs_value = next(secs)
            except:
                try:
                    yield f"{hours_value}:{minutes_value}:{secs_value}"
                    hours_value = next(hours)
                    minutes = gen_minutes()
                    minutes_value = next(minutes)


                except:
                    is_roll = False


if __name__ == "__main__":
    for gt in gen_time():
        print(gt)

# I get the hang of it, form now on it just to do it over and over again