def conversion(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    print("Converted sec value in hour:", hour)
    print("Converted sec value in minutes:", min)


sec = 3600
conversion(sec)
