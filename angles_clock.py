def angle_clock(h, m):
    minute_angle = 360/60
    hour_angle = minute_angle * 5

    hour_angle_by_minutes = hour_angle/60

    minutes = m*5
    hour_deg = h * hour_angle + minutes * hour_angle_by_minutes
    minute_deg = (m*5) * minute_angle
    
    angle_between =  abs(hour_deg - minute_deg)

    if angle_between <=180:
        return angle_between
    else:
        return 360 - angle_between


def main():
    result = angle_clock(2, 4)
    print(result)


if __name__ == "__main__":
    main()
