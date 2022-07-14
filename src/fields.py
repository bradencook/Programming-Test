if __name__ == '__main__':
    streetProvo = open("../StreetProvo.csv")
    fields = streetProvo.readline().split(',')
    file = open("../fields.txt", "w")
    for i in range(len(fields)):
        print(f"{i}   {fields[i]}", file=file)
    streetProvo.close()
    file.close()
