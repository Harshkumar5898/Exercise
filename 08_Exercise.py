import os


def Captiliser(apath, aext):
    os.chdir(apath)
    count = 1

    for file in os.listdir('.'):
        name, ext = os.path.splitext(file)
        if ext == "":
            continue
        else:
            if ext == aext:
                os.rename(file, f"{count}{ext}")
                count += 1
            else:
                os.rename(file, file.capitalize())


path = input("Enter a path : ")
# ucfile = input("Enter the name of the file which contain list of name of file which you do not want to change")
ext = input("Enter type of file you want to arrange : ")

Captiliser(path, ext)
