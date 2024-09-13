with open(input.txt) as input_file:
    n=read(input_file)
k=n//2
subtask=[]
for i in range(k+1):
    print(" "*(k-i) + "*"*((2*i)+1))
    subtask.append(line)
for i in range(k):
    print(" "*(i+1)+ "*"*(n-2*(i+1)))
    subtask.append(line)
with open(output.txt) as outputfile:
    for line in subtask:
        output_file.write(line + "\n")