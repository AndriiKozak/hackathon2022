path = "D:/db/cdek/cdek/client.csv"
if __name__=="__main__":
    with open(path, encoding="utf-8") as file:
        d = 10
        c = 0
        emails = set()
        for line in file:
            if d>0:
                print(line)
                d-=1
            c+=1
            email = line.split("\t")[-1]
            emails.add(email[:-1])
        print(c)
        print(len(emails))
        print(list(emails)[:100])