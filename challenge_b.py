def determine_type(obj):
    #Find type of object
    try:
        if '.' in obj:
            float(obj)  
            return "real number"
        else:
            int(obj)
            return "integer"
    except ValueError:
        if obj.isalpha():
            return "alphabetical string"
        else:
            return "alphanumeric"

def process_file(filename):
    #Reads the file and prints each object with its type.
    with open(filename, 'r') as file:
        data = file.read().split(",")  
    
    for obj in data:
        obj = obj.strip()  # Strip spaces
        if obj:
            obj_type = determine_type(obj)
            print(f"{obj} ({obj_type})")

if __name__ == "__main__":
    process_file("objects.txt")
