### SCRIPTING IN TERMINAL

Scripting
- Python Installation and Environment Setup (see: https://github.com/m8kin/conda_tips)
- Running and Editing Python Scripts
- Interacting with User Input
- Handling Exceptions
- Reading and Writing Files
- Importing Local, Standard, and Third-Party Modules
- Experimenting with an Interpreter

### FILES
python files end in the suffix ".py"


### RUNNING THE FIRST SCRIPT
Open a terminal and run either

OSX/Linux:
```
python3 ./scripts/first_script.py
python ./scripts/first_script.py
```

### ERROR TYPES (EXCEPTIONS)

1. SYNTAX error: erros in the actualy code itself
2. EXCEPTION error: errors when unexpected things happen during the execution of the code
    - **AssertionError**: Raised when the assert statement fails.
    - **AttributeError**: Raised on the attribute assignment or reference fails.
    - **EOFError**: Raised when the input() function hits the end-of-file condition.
    - **FloatingPointError**: Raised when a floating point operation fails.
    - **GeneratorExit**: Raised when a generator's close() method is called.
    - **ImportError**: Raised when the imported module is not found.
    - **IndexError**: Raised when the index of a sequence is out of range.
    - **KeyError**: Raised when a key is not found in a dictionary.
    - **KeyboardInterrupt**: Raised when the user hits the interrupt key (Ctrl+c or delete).
    - **MemoryError**: Raised when an operation runs out of memory.
    - **NameError**: Raised when a variable is not found in the local or global scope.
    - **NotImplementedError**: Raised by abstract methods.
    - **OSError**: Raised when a system operation causes a system-related error.
    - **OverflowError**: Raised when the result of an arithmetic operation is too large to be represented.
    - **ReferenceError**: Raised when a weak reference proxy is used to access a garbage collected referent.
    - **RuntimeError**: Raised when an error does not fall under any other category.
    - **StopIteration**: Raised by the next() function to indicate that there is no further item to be returned by the - iterator.
    - **SyntaxError**: Raised by the parser when a syntax error is encountered.
    - **IndentationError**: Raised when there is an incorrect indentation.
    - **TabError**: Raised when the indentation consists of inconsistent tabs and spaces.
    - **SystemError**: Raised when the interpreter detects internal error.
    - **SystemExit**: Raised by the sys.exit() function.
    - **TypeError**: Raised when a function or operation is applied to an object of an incorrect type.
    - **UnboundLocalError**: Raised when a reference is made to a local variable in a function or method, but no value - has been bound to that variable.
    - **UnicodeError**: Raised when a Unicode-related encoding or decoding Error occurs.
    - **UnicodeEncodeError**: Raised when a Unicode-related error occurs during encoding.
    - **UnicodeDecodeError**: Raised when a Unicode-related error occurs during decoding.
    - **UnicodeTranslateError**: Raised when a Unicode-related error occurs during translation.
    - **ValueError**: Raised when a function gets an argument of correct type but improper value.
    - **ZeroDivisionError**: Raised when the second operand of a division or module operation is zero.