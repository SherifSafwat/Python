for i in range(3, 6):
    print(i)
    with open("test1.txt", "a") as myfile:
        myfile.write(str(i) + '\n')
        
'''
with open("test.txt", "a") as myfile:
        with open("test.txt", "a") as myfile:
        myfile.write("zzz" + '\n')
        myfile.write(str(i) + '\n')

with open("r") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
print(lines)        


with open("r") as f:
    content = f.read().splitlines()
print(content)  

for e in content:
    print(e)  
'''

'''with open("test.txt", "a") as myfile:
        myfile.write(first[i] + " " + last[i])
        myfile.write('\n'.join(name_elem) + '\n')
        myfile.write('\n'.join(data_elem) + '\n')
            

with open("test.txt", "a") as myfile:
        myfile.write('\n'.join(e.text) + '\n')'''