import xlwt 
#from pandas import DataFrame

with open(r"./all.txt") as f:
    lines = f.read().splitlines()

book = xlwt.Workbook()
sh = book.add_sheet("sheet")

r = 0
c = 0

for i, item in enumerate(lines):
    if(item != "zzz"):
        sh.write(r,c,item)
        c = c +1
    if(item == "zzz"):
        c = 0
        r = r + 1


book.save("xlsall.xls")





