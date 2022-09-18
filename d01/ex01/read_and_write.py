
def read_and_write():
    file1 = open("ds.csv", "r")
    file2 = open("ds.tsv", "w")
    file2.write(file1.read().replace("\",", "\"\t").replace("true,", "true\t")
        .replace("false,", "false\t"))
    file1.close()
    file2.close()

if __name__ == '__main__':
    read_and_write()