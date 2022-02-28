![New Project(10)](https://user-images.githubusercontent.com/84568105/156011454-4b927e07-abe1-407c-97da-14dfbaa77ddc.png)

# Cambridge-Pseudo-Code-Transpiler
A transpiler to be able to run Cambridge's set pseudo-code language.  
**NOT AN OFFICIAL CAMBRIDGE DISTRIBUTION**  
This was solely made as a personal challenge and to create a helpful tool for my classmates that find it difficult to work with Pseudo-code, I came to the conclusion that it might be better if the code written can actually be executed to get a better understanding whether the code they write will return the expected outcome.  

## Author information
Name: Dominic  
Internet Username: DevNugget   

## Using
Download this repository. Open a terminal inside the download path.   
Enter the following commands.  

Linux Based Operating Systems:
```
./main {instructions file} {output file: should be a .py file}

// This would compile the app.cmps file included in the repository.
./main app.cmps output.py
```

Windows Operating Systems (Requires python3, I was only able to compile to Linux as I use Linux):
```
python3 main.py {instructions file} {output file: should be a .py file}

// This would compile the app.cmps file included in the repository.
python3 main.py app.cmps output.py
```

## Input and Output
```
OUTPUT "Hello World!"
PRINT "Hello World!" // Same as OUTPUT

MyCode <- "99B64" // Example variable
// This prints: My ID is 99B64 || this is also used only if the variable we are concatinating is a string.
OUTPUT "My ID is " , MyCode 

MyInt <- 58

// This prints: My integer is 58 || We use double commas to convert any non string value into a string, 
this is because it was difficult for me to type check these when writing the transpiler. This is not to
be taken over to an exam, we are slightly foregoing accuracy to make it runnable.
OUTPUT "My integer is " ,, MyInt 

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



