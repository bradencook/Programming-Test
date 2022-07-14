FIELD_VERIFIED = 112
LENGTH_YDS = 115
YDS_PER_MILE = 1760

if __name__ == "__main__":
    streetProvo = open("../StreetProvo.csv")
    streetProvo.readline()  # skip the first line

    dayTotals = {}
    for line in streetProvo:
        line = line.split(",")
        if line[FIELD_VERIFIED] != "":
            dateComplete = line[FIELD_VERIFIED].strip().split(" ")[0]

            # make the dates sortable yyyy/mm/dd
            rawDate = dateComplete.split("/")
            if len(rawDate[0]) == 1:
                rawDate[0] = "0" + rawDate[0]
            if len(rawDate[1]) == 1:
                rawDate[1] = "0" + rawDate[1]
            dateComplete = rawDate[2] + "/" + rawDate[0] + "/" + rawDate[1]

            ydsTotal = float(line[LENGTH_YDS])
            if dateComplete in dayTotals:
                ydsTotal += float(dayTotals[dateComplete])
            dayTotals.update({dateComplete: ydsTotal})

    dates = list(dayTotals.keys())
    dates.sort()

    # write results to a file
    file = open("../RESULTS.txt", "w")
    print(f"""MILES OF ROAD COMPLETED FROM {dates[0]} TO {dates[-1]}  

DATE       | MILES COMPLETED
-----------|-----------------""", file=file)

    totalYds = 0
    for date in dates:
        print(f"{date} | {dayTotals[date] / YDS_PER_MILE: .5f}", file=file)
        totalYds += dayTotals[date]

    print(f"\nTOTAL MILES: {totalYds / YDS_PER_MILE: .5f}", file=file)
    print(f"AVERAGE: {(totalYds / YDS_PER_MILE) / len(dates): .5f}", file=file)

    streetProvo.close()
    file.close()
