def getId(name, list):
    for i in list:
        for j in i:
            if j == name.lower():
                return list.index(i)
