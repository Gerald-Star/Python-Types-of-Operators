#

## 2. Using the Python Interpreter
2.1. Invoking the Interpreter
The Python interpreter is usually installed as /usr/local/bin/python3.12 on those machines where it is available; putting /usr/local/bin in your Unix shell’s search path makes it possible to start it by typing the command:

The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a script from that file.

A second way of starting the interpreter is python -c command [arg] ..., which executes the statement(s) in command, analogous to the shell’s -c option. Since Python statements often contain spaces or other characters that are special to the shell, it is usually advised to quote command in its entirety.

### Built-in Types

The following sections describe the standard types that are built into the interpreter.

- The principal built-in types are numerics, sequences, mappings, classes, instances and exceptions.

Some collection classes are mutable. The methods that add, subtract, or rearrange their members in place, and don’t return a specific item, never return the collection instance itself but None.


## 3. Python divides the operators in the following groups:

## Arithmetic operators
## Assignment operators
## Comparison operators
## Logical operators
## Identity operators
## Membership operators
## Bitwise operators


### Truth Value Testing¶

Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below.

By default, an object is considered true unless its class defines either a __bool__() method that returns False or a __len__() method that returns zero, when called with the object. [1] Here are most of the built-in objects considered false:

- constants defined to be false: None and False*

- zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)*

- empty sequences and collections: '', (), [], {}, set(), range(0)*

Operations and built-in functions that have a Boolean result always return 0 or False for false and 1 or True for true, unless otherwise stated. (Important exception: the Boolean operations or and and always return one of their operands.)

The while loop executes as long as the condition (here: a < 10) remains true. In Python, like in C, any non-zero integer value is true; zero is false. The condition may also be a string or list value, in fact any sequence; anything with a non-zero length is true, empty sequences are false. The test used in the example is a simple comparison. The standard comparison operators are written the same as in C: < (less than), > (greater than), == (equal to), <= (less than or equal to), >= (greater than or equal to) and != (not equal to).

The body of the loop is indented: indentation is Python’s way of grouping statements. At the interactive prompt, you have to type a tab or space(s) for each indented line

# Fibo

The Fibonacci numbers may be defined by the recurrence relation[6]

## Boolean Operations — and, or, not

### These are the Boolean operations, ordered by ascending priority:

Operation  Result  Notes

- x or y  if x is true, then x, else y  (1)

- x and y if x is false, then x, else y (2)

- not x, if x is false, then True, else False  (3)

Notes:

This is a short-circuit operator, so it only evaluates the second argument if the first one is false.

This is a short-circuit operator, so it only evaluates the second argument if the first one is true.

not has a lower priority than non-Boolean operators, so not a == b is interpreted as not (a == b), and a == not b is a syntax error.

#### Comparisons

There are eight comparison operations in Python.


#### Numeric Types — int, float, complex

There are three distinct numeric types: integers, floating point numbers, and complex numbers. In addition, Booleans are a subtype of integers.


### OPERATORS

x // y - floored quotient of x and y

x % y - remainder of x / y


-x - x negated

+x - x unchanged

abs(x) - absolute value or magnitude of x

int(x) - x converted to integer

float(x) - x converted to floating point

complex(re, im) - a complex number with real part re, imaginary part im. im defaults to zero.

c.conjugate() - conjugate of the complex number c

divmod(x, y) -  the pair (x // y, x % y)

pow(x, y) - x to the power y

x ** y  - x to the power y


### Boolean Type - bool / Logical operators

Booleans represent truth values. The bool type has exactly two constant instances: True and False.

The built-in function bool() converts any value to a boolean, if the value can be interpreted as a truth value (see section Truth Value Testing above).

For logical operations, use the boolean operators *and, or and not.* When applying the bitwise operators &, |, ^ to two booleans, they return a bool equivalent to the logical operations “and”, “or”, “xor”. However, the logical operators and, or and != should be preferred over &, | and ^.

### Common Sequence Operations

- in and  not in
- You can use the if and while method to iterate the sequence operator's truth value


x in s - True if an item of s is equal to x, else False

x not in s - False if an item of s is equal to x, else True

*While the in and not in operations are used only for simple containment testing in the general case, some specialised sequences (such as str, bytes and bytearray) also use them for subsequence testing:*