import lib
if __name__ == '__main__':
    start_hour = 6
    start_min = 52

    easy_pace_min = 8
    easy_pace_sec = 15

    tempo_min = 7
    tempo_sec = 12

    sum_min, sum_sec = easy_pace_min * (1 + 1) + tempo_min * 3, easy_pace_sec * (1 + 1) + tempo_sec * 3

    print lib.get_time(start_hour, start_min, 0, 0, sum_min, sum_sec)


