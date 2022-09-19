import sys 

class Research:
    def __init__(self, path):
        self.file = path

    def file_reader(self):
        with open(self.file, "r") as csv:    
            data = csv.read()
        row = data.split('\n')
        if len(row) < 2 or len(row[0].split(',')) != 2:
            raise Exception("Error! Incorrect data-file..")
        for x in row[1:]:
            if x != '0,1' and x != '1,0':
                raise Exception("Error! Incorrect data-file..")
        row = '\n'.join(row)
        return row

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(Research(sys.argv[1]).file_reader())