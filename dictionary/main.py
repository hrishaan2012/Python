student={"id": {"name": "John Doe", "age": 20, "subject": "Maths,Hindi,English"},
         
"id2": {"name": "Jane Smith", "age": 22,  "subject": "Maths,Hindi,English"},

"id3": {"name": "Alice Johnson", "age": 21,  "subject": "Maths,Hindi,English"},
 
"id4": {"name": "Jane Smith", "age": 22,  "subject": "Maths,Hindi,English"},
         }
result={}
for key, value in student.items():
    if value not in result.values():
        result[key] = value
print(result)