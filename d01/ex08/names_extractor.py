import sys

def names_extractor():
  if len(sys.argv) != 2:
    raise Exception("Error argument")
  with open('employees.tsv', 'a') as f_write: 
    f_write.write('Name\tSurname\tE-mail\n')
    with open(sys.argv[1], 'r') as f_read:
      line = f_read.readlines()
      for i in range(len(line)):
        name = line[i].split('@')[0].split('.')[0]
        surname = line[i].split('@')[0].split('.')[1]
        f_write.write(f'{name.capitalize()}\t{surname.capitalize()}\t{line[i]}')

if __name__ == '__main__':
  names_extractor()