import os
import sys

def convertstr(string):
	list1 = []
	list1[:0]=string
	return list1

stack = []

cls_com = "clear"
os.system(cls_com)

f = open(sys.argv[1], "r")
source_content = f.read()
f.close()

splitstack = []

print(source_content)

results = [[]]
quote = None
for c in source_content:
        if c == "'" or c == '"':
                if c == quote:
                        quote = None
                elif quote == None:
                        quote = c

        results[-1].append(c)

splitstack = [''.join(x) for x in results]

print(splitstack)
counti = 0

stack = []
tabstack = []
finalstack = []
riddle = []
ripped_content = ""

counterf = 0
ripple = ""

for i in range(len(splitstack)):
        plit = convertstr(splitstack[i])
        for i in range(len(plit)):
                print(plit[i])
                if plit[i] == "\n":
                        riddle.append(ripple)
                        riddle.append("\n")
                        ripple = ""
                else:
                        ripple += plit[i]

print(riddle)
nimble = []

for i in riddle:
        results2 = [[]]
        quote2 = None
        for c in i:
                if c == "'" or c == '"':
                        if c == quote2:
                                quote2 = None
                        elif quote2 == None:
                                quote2 = c
                elif c == ' ':
                        if quote2 == None:
                                results2.append([])
                                continue
                results2[-1].append(c)

        nimble.append([''.join(x) for x in results2])

for sublist in nimble:
        for value in sublist:
                tabstack.append(value)
print(tabstack)
                        
for i in range(len(tabstack)):
	if tabstack[i].startswith("\t"):
		for c in range(len(tabstack[i])):
			if tabstack[i][c] == "\t": finalstack.append("\t")
		finalstack.append(tabstack[i].replace("\t", ""))
	else: finalstack.append(tabstack[i])


counter = 0
counter2 = 0
output = ""
print(finalstack)
stack = finalstack
ifs = 0
endifs = 0

ignores = [
        ">",
        "<",
        "=",
        "<>"
]

print(stack)

cont = 0

output += "running = True\n"

for i in stack:

        if i == "OUTPUT" or i == "PRINT":
                nickle = []
                push_content = ""
                orig = counter
                for i in stack[counter+1:]:
                        if i == ",":
                                nickle.append("+")
                        elif i == ",,":
                                nickle.append("+ str(" + stack[counter+2] + ")")
                                counter += 1
                        elif i == "\n":
                                break
                        else:
                                nickle.append(stack[counter+1])
                        counter += 1
                for i in nickle:
                        push_content += i
                output += "print(" + push_content + ")"
                counter = orig

        elif i == "INPUT":
                output += stack[counter+1] + "= input()"

        elif i == "<-":
                if stack[counter-2] != "FOR":
                        regf = ""
                        for i in stack[counter+1:]:
                                if i == "\n":
                                        break
                                else:
                                        regf += i 
                        output += stack[counter-1] + " = " + regf

        elif i == "IF":
                ifs += 1
                output += "if"
                for j in stack[counter+1:]:
                        if j == "THEN":
                                output += ":"
                                break
                        elif j == "=":
                                output += " =="
                        elif j == "<>":
                                output += " !="
                        else:
                                output += " " + j

        elif i == "ENDIF":
                endifs += 1

        elif i == "\n":
                output += "\n"

        elif i == "\t":
                output += "\t"

        elif i == "FOR":
                lpp = int(stack[counter+5]) + 1
                output += "for " + stack[counter+1] + " in range(" + stack[counter+3] + "," + str(lpp) + "):"
        
        elif i == "WHILE":
                ripplit = ""
                output += "while"
                for j in stack[counter+1:]:
                        if j == "DO":
                                output += ":"
                                break
                        elif j == "=":
                                output += " =="
                        elif j == "<>":
                                output += " !="
                        else:
                                output += " " + j

        elif i == "REPEAT":
                output += "while running:\n"
                for j in stack[counter+1:]:
                        if j == "UNTIL":
                                output += "\tif"
                                for k in stack[counter2+1:]:
                                        if k == "=":
                                                output += " =="
                                        elif k == "<>":
                                                output += " !="
                                        elif k == "\n":
                                                output += ":"
                                                output += "\n\t\tbreak"
                                                break
                                        else:
                                                if k != "UNTIL":
                                                        output += " " + k
                        counter2 += 1
        counter2 += 1
        counter += 1

fw = open(sys.argv[2], "w")
fw.write(output)
fw.close()

os.system("python3 " + sys.argv[2])

