import json
class Student_manager:
    def __init__(self,name,file_path):
        self.name = name
        self.file_path = file_path
    
    def create_data(self):
        with open(r"day_2\student_data.json","w")as file:
            json.dump([],file)
        self.file_path = r"day_2\student_data.json"
    
    def read_data(self):
        with open(self.file_path,"r")as files:
            content = json.load(files)
            print(content)
            return content
        
    def add(self,new_data):
        content = self.read_data()
        content.append(new_data)
        with open("day_2/student_data.json","w")as file:
            json.dump(content,file)
        return content
    
    def search(self,keyword):
        content = self.read_data()    
        for student in content:
            if student["name"] == keyword:
                print ("yes")
                return
            print("no")
            
    def delete(self,keyword):
        content = self.read_data()
        
        content = [student for student in content if student["name"] != keyword]

        with open(self.file_path, "w") as file:
            json.dump(content, file, indent=4)
        print("done")
    
student_mgr = Student_manager("Vidhuran", None)

student_mgr.create_data()

new_student = {
    "id": 1,
    "name": "Rahul"
}

student_mgr.add(new_student)

print(student_mgr.read_data())

# Search
student_mgr.search("Rahul")

# Delete
student_mgr.delete("Rahul")
        
