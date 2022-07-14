FIELD_VERIFIED = 112
LENGTH_YDS = 115

if __name__ == "__main__":
    streetProvo = open("../StreetProvo.csv")
    # skip the first line
    streetProvo.readline()

    dayTotals = []
    for line in streetProvo:
        line = line.split(",")
        print(line[FIELD_VERIFIED])

    streetProvo.close()
