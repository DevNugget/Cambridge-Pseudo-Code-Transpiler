![New Project(10)](https://user-images.githubusercontent.com/84568105/156011454-4b927e07-abe1-407c-97da-14dfbaa77ddc.png)

# Cambridge-Pseudo-Code-Transpiler
A transpiler to be able to run Cambridge's set pseudo-code language.  
**NOT AN OFFICIAL CAMBRIDGE DISTRIBUTION**  
This was solely made as a personal challenge and to create a helpful tool for my classmates that find it difficult to work with Pseudo-code, I came to the conclusion that it might be better if the code written can actually be executed to get a better understanding whether the code they write will return the expected outcome.  

## Input and Output
```
OUTPUT "Hello World!"
PRINT "Hello World!" // Same as OUTPUT

MyCode <- "99B64" // Example variable
OUTPUT "My ID is " , MyCode // This prints: My ID is 99B64 || this is also used only if the variable we are concatinating is a string.

MyInt <- 58
OUTPUT "My integer is " ,, MyInt // This prints: My integer is 58 || We use double commas to convert any non string value into a string, this is because it was difficult for me to type check these when writing the transpiler.

INPUT Text
```

## Variables
```
MyNum <- 0
MyReal <- 0.1
MyText <- ""
```

## If Statements
```
IF 20 > 10 THEN
  OUTPUT "20 is greater than 10"
ENDIF
```
  
## For loops
```
FOR Count <- 1 TO 5
  OUTPUT Count
NEXT Count
```

## While loops
```
WHILE Counter < 10 DO
  OUTPUT Counter
  Counter <- Counter + 1
ENDWHILE
```

## Repeat loops
```
REPEAT
  OUTPUT Counter
  Counter <- Counter + 1
UNTIL Counter = 20
```



