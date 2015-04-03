def tagsdel(text):
    """
    delete tags from html source code
    """
    for i in text:
        if i == "<":
            index1 = text.index(i)
        elif i == ">":
            index2 = text.index(i)
            text = text.replace(text[index1:index2+1],"")
    return text
