#Reading Text File by Chakori Chaturvedi 
def read_file(file):
    fp= open(file,"r",encoding='utf8',errors='ignore')
    text=fp.readlines()
    return text
