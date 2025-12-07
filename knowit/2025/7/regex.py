import re

def troll(word):
    if re.search('t.*r.*o.*l.{1,5}l', word) != None:
        return True
    if re.search('t.*r.*o.{1,5}l.*l', word) != None:
        return True
    if re.search('t.*r.{1,5}o.*l.*l', word) != None:
        return True
    if re.search('t.{1,5}r.*o.*l.*l', word) != None:
        return True
    return False

def nisse(word):
    if re.search('(?!n).*n.*i.*s.*s.{0,2}e.*(?<!e)', word) != None:
        return True
    if re.search('(?!n).*n.*i.*s.{0,2}s.*e.*(?<!e)', word) != None:
        return True
    if re.search('(?!n).*n.*i.{0,2}s.*s.*e.*(?<!e)', word) != None:
        return True
    if re.search('(?!n).*n.{0,2}i.*s.*s.*e.*(?<!e)', word) != None:
        return True
    return False

if __name__ == "__main__":
    count = 0

    with open('knowit/2025/7/ordliste.txt') as f:
        for line in f.readlines():
            word = line.strip()

            if troll(word):
                count += 1

            if nisse(word):
                count += 1
    
    print(f'Result = {count}')
    




    # print(troll('controll'))