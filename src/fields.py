if __name__ == '__main__':
    streetProvo = open("../StreetProvo.csv")
    fields = streetProvo.readline().split(',')
    line1 = streetProvo.readline().split(',')
    file = open("../fields.txt", "w")
    print("FIELD\tNAME\tEXAMPLE DATA", file=file)
    for i in range(len(fields)):
        print(f"{i}\t{fields[i]}\t\t\t{line1[i]}", file=file)
    streetProvo.close()
    file.close()
