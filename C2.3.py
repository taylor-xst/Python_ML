


def get_time(start_hour, start_min, start_sec, add_hour, add_min, add_sec):
    sec = start_sec + add_sec

    min = start_min + add_min + sec / 60

    sec = sec % 60

    hour = start_hour + add_hour + min / 60

    min = min % 60

    hour = hour % 24

    return hour, min, sec


start_hour = 6
start_min = 52

easy_pace_min = 8
easy_pace_sec = 15

tempo_min = 7
tempo_sec = 12

sum_min, sum_sec = easy_pace_min * (1 + 1) + tempo_min * 3, easy_pace_sec * (1 + 1) + tempo_sec * 3

print get_time(start_hour, start_min, 0, 0, sum_min, sum_sec)