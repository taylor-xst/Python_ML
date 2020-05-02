def get_time(start_hour, start_min, start_sec, add_hour, add_min, add_sec):
    sec = start_sec + add_sec

    min = start_min + add_min + (sec / 60)

    sec = sec % 60

    hour = start_hour + add_hour + min / 60

    min = min % 60

    hour = hour % 24

    return hour, min, sec