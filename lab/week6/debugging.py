
def read_file(path) :

    db = {}
    
    with open (path, "r", encoding="utf-8") as f :
        data = f.readlines()

        for line in data :
            clean_line = line.strip()
            for c in clean_line :
                if c in db : db[c] += 1
                else : db[c] = 1

    return db

def main() :
    path = "lab\week6\string_count.txt"
    print(read_file(path))

if __name__ == "__main__" :
    main()