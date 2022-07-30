Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def positive(lst1):
    temp = []
    for i in lst1:
        if i >= 0:
            temp.append(i)
    return temp

positive([1, -5, 3, 7])
[1, 3, 7]
