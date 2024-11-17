import random
import string
import os

#alphabetical string
def alphabetical_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

#real number
def real_number():
    return f"{random.uniform(-100, 100):.10f}"

#integer
def integer():
    return str(random.randint(-100, 100))

#alphanumeric
def alphanumeric():
    alphanumeric = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 20)))
    #random spaces before and after
    spaces_before = ' ' * random.randint(0, 10)
    spaces_after = ' ' * random.randint(0, 10)
    return f"{spaces_before}{alphanumeric}{spaces_after}"

def main():
    filename = "objects.txt"
    # 10 MB in size
    target_size = 10 * 1024 * 1024 


    with open(filename, "w") as file:
        while os.path.getsize(filename) < target_size:
            objects = [
                alphabetical_string(random.randint(10, 50)),
                real_number(),
                integer(),
                alphanumeric()
            ]
            # Write objects and separate by commas
            file.write(",".join(objects) + ",")

if __name__ == "__main__":
    main()
