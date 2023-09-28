import os

p = os.getcwd()
k = os.path.split(p)[-1]

for files in os.walk('C:\\Users\\obikb\\PycharmProjects\\sem8\\json'):
    print(files)
    for file in files[2]:
        print(os.path.getsize(os.path.join(files[0],file)))

def get_dir_size(path: str = os.getcwd()):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            print(entry)
            if entry.is_file():
                total += os.path.getsize(entry)
            elif entry.is_dir():
                print(entry.path)
                total += get_dir_size(entry.path)
    return total

print(get_dir_size('C:\\Users\\obikb\\PycharmProjects\\sem8\\Py'))