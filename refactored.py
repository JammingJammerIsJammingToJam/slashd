from parse import *

class Compiler:
    
    def __init__(self):
        self.code = ['out/slash/', '/', 'out/slash/']
        self.split = []
    
    def set_file(self, filename):
        with open(filename, 'r') as k:
            self.code = k.readlines()

    def split_code(self):
        for line in self.code:
            if line[0] == '/':
                continue
            if len(line) == 0:
                continue

            start = 0
            index = 1
            tempstring = ''
            templine = []

            while True:
                try:
                    tempstring = parse(line, start, ['/'])
                    templine.append(tempstring)
                except:
                    raise ValueError(f'Parsing issue on line: {index}')
                
                index += 1
                start += len(tempstring) + 1
                
                if start == len(line):
                    break
            
            self.split.append(templine)

j = Compiler()
j.split_code()