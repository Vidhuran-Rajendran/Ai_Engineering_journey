import json

class FileReader:
    def __init__(self,file_path):
        self.file_path = file_path
        
    def open_file(self):
        f = open(self.file_path)
        f=f.read()
        return f
    def print_content(self):
        content = self.open_file()
        print(content)
        
    def count_line(self):
        content = self.open_file()
        word_count = 0
        lines = content.splitlines()
        for line in lines:
            words = line.split()
            word_count += len(words)
        print(f"line{len(lines)} and words: {word_count}")
            
file_path = r"D:\new_train\Ai_Engineering_journey\day_1\data.json"
classreader = FileReader(file_path)
print(classreader.print_content())
print(classreader.count_line())