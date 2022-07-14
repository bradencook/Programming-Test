FIELD_VERIFIED = 112
LENGTH_YDS = 115

if __name__ == "__main__":
    streetProvo = open("../StreetProvo.csv")
    # skip the first line
    streetProvo.readline()

    dayTotals = {}
    count = 0
    for line in streetProvo:
        line = line.split(",")
        if line[FIELD_VERIFIED] != "" and count < 30:
            dateComplete = line[FIELD_VERIFIED].strip().split(" ")[0]
            # make the dates sortable yyyy/mm/dd
            rawDate = dateComplete.split("/")
            if len(rawDate[0]) == 1:
                rawDate[0] = "0" + rawDate[0]
            if len(rawDate[1]) == 1:
                rawDate[1] = "0" + rawDate[1]
            dateComplete = rawDate[2] + "/" + rawDate[0] + "/" + rawDate[1]

            print(dateComplete + "\t" + line[LENGTH_YDS])
            count += 1
            ydsTotal = float(line[LENGTH_YDS])
            if dateComplete in dayTotals:
                ydsTotal += float(dayTotals[dateComplete])
            dayTotals.update({dateComplete: ydsTotal})
        
    print(dayTotals)
    dates = list(dayTotals.keys())
    dates.sort()
    print(dates)

    streetProvo.close()
