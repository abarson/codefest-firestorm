def get_filetype(filename):
    """
    return the file extension of a filename
    """

    if filename.endswith(".png"):
        return "png"

    if filename.endswith(".docx"):
        return "docx"

    if filename.endswith(".pdf"):
        return "pdf"

    #if filename.endswith("

def convert(filename):
    ft = get_filetype(filename)

