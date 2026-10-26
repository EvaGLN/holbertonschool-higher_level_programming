<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# JavaScript - Warm up

## Table of Contents :

  - [0. First constant, first print](#subparagraph0)
  - [1. 3 languages](#subparagraph1)
  - [2. Arguments](#subparagraph2)
  - [3. Value of my argument](#subparagraph3)
  - [4. Create a sentence](#subparagraph4)
  - [5. An Integer](#subparagraph5)
  - [6. Loop to languages](#subparagraph6)
  - [7. I love C](#subparagraph7)
  - [8. Square](#subparagraph8)
  - [9. Add](#subparagraph9)
  - [10. Factorial](#subparagraph10)
  - [11. Second biggest!](#subparagraph11)
  - [12. Object](#subparagraph12)
  - [13. Add file](#subparagraph13)
  - [14. Const or not const](#subparagraph14)
  - [15. Call me Moby](#subparagraph15)
  - [16. Add me maybe](#subparagraph16)
  - [17. Increment object](#subparagraph17)
## Background Context

JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

- Scripting (same as we did with Python)
- Web front-end

For the moment, and for learning all basic concepts of this language, we will do some scripting.
After, we will make our AirBnB project dynamic by using Javascript and JQuery.

![JS](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/303/Javascript-535.png.jpeg)

## Resources

**Read or watch**:

- [Writing JavaScript Code](/rltoken/fQUkQNjfE1Dw47vcgps6Ig) 
- [Variables](/rltoken/FX6qEtLyELhXUg7u23eMDg) 
- [Data Types](/rltoken/R5-aJ7W7ypXbTAcI54Ut-g) 
- [Operators](/rltoken/fQUkQNjfE1Dw47vcgps6Ig) 
- [Operator Precedence](/rltoken/4PdyDQJJuDXEZmbALqttug) 
- [Controlling Program Flow](/rltoken/N0Np7QFZVwSnRopkHsN4ow) 
- [Functions](/rltoken/21XrxDV4cjQfW8v7r2FNMw) 
- [Objects and Arrays](/rltoken/LSNtL9tP1DBU0bnBLdF2uA) 
- [Intrinsic Objects](/rltoken/LSNtL9tP1DBU0bnBLdF2uA) 
- [Module patterns](/rltoken/OOAH-N9qs-oT4Y32ErUELQ) 
- [var, let and const](/rltoken/5dIWvs6Zn5XjcsP18Ti9Uw) 
- [JavaScript Tutorial](/rltoken/PzZBOx5Ms7RL0FX1fihHKw) 
- [Modern JS](/rltoken/toueHB-cJAYoXNscJtr3Jw) 

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/7IvdhdUBt8B_PxSqLjfz9A), __without the help of Google__:

### General

- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants
- What are differences between `var`, `const` and `let`
- What are all the data types available in JavaScript
- How to use the `if`, `if ... else` statements
- How to use comments
- How to affect values to variables
- How to use `while` and `for` loops
- How to use `break` and `continue` statements
- What is a function and how do you use functions
- What does a function that does not use any `return` statement return
- Scope of variables
- What are the arithmetic operators and how to use them
- How to manipulate dictionary
- How to import a file

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](/rltoken/Wz4slq1c0LivUbiR88Kj_Q) + [semicolons on top](/rltoken/n6FW86eM_laCRYFfuHKjXA). Also as reference: [AirBnB style](/rltoken/7O__u3p-BU24HUBUh7QXoQ)
- All your files must be executable
- The length of your files will be tested using `wc`

## More Info

### Install Node 14

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

[Documentation](/rltoken/n6FW86eM_laCRYFfuHKjXA)

```
$ sudo npm install semistandard --global
```


## Task
### 0. First constant, first print <a name='subparagraph0'></a>

Write a script that prints "JavaScript is amazing":

* You must create a constant variable called `myVar` with the value "JavaScript is amazing"
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```ruby
guillaume@ubuntu:~/$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `0-javascript_is_amazing.js`

---

### 1. 3 languages <a name='subparagraph1'></a>

Write a script that prints 3 lines:

* The first line: "C is fun"
* The second line: "Python is cool"
* The third line: "JavaScript is amazing"
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```kotlin
guillaume@ubuntu:~/$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `1-multi_languages.js`

---

### 2. Arguments <a name='subparagraph2'></a>

Write a script that prints a message depending of the number of arguments passed:

* If no arguments are passed to the script, print "No argument"
* If only one argument is passed to the script, print "Argument found"
* Otherwise, print "Arguments found"
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

Reference: process.argv

```ruby
guillaume@ubuntu:~/$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `2-arguments.js`

---

### 3. Value of my argument <a name='subparagraph3'></a>

Write a script that prints the first argument passed to it:

* If no arguments are passed to the script, print "No argument"
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `length`

```ruby
guillaume@ubuntu:~/$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/$ ./3-value_argument.js School
School
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `3-value_argument.js`

---

### 4. Create a sentence <a name='subparagraph4'></a>

Write a script that prints two arguments passed to it, in the following format: " is "

* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```ruby
guillaume@ubuntu:~/$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `4-concat.js`

---

### 5. An Integer <a name='subparagraph5'></a>

Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

* If the argument can't be converted to an integer, print "Not a number"
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `try/catch`

```ruby
guillaume@ubuntu:~/$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `5-to_integer.js`

---

### 6. Loop to languages <a name='subparagraph6'></a>

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

* The first line: "C is fun"
* The second line: "Python is cool"
* The third line: "JavaScript is amazing"
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use any `if/else` statement
* You can use only one `console.log`
* You must use a loop (`while`, `for`, etc.)

```kotlin
guillaume@ubuntu:~/$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `6-multi_languages_loop.js`

---

### 7. I love C <a name='subparagraph7'></a>

Write a script that prints `x` times "C is fun"

* Where `x` is the first argument of the script
* If the first argument can't be converted to an integer, print "Missing number of occurrences"
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You can use only two `console.log`
* You must use a loop (`while`, `for`, etc.)

```kotlin
guillaume@ubuntu:~/$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/$ ./7-multi_c.js -3
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `7-multi_c.js`

---

### 8. Square <a name='subparagraph8'></a>

Write a script that prints a square

* The first argument is the size of the square
* If the first argument can't be converted to an integer, print "Missing size"
* You must use the character `X` to print the square
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You must use a loop (`while`, `for`, etc.)

```ruby
guillaume@ubuntu:~/$ ./8-square.js
Missing size
guillaume@ubuntu:~/$ ./8-square.js School
Missing size
guillaume@ubuntu:~/$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/$ ./8-square.js -3
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `8-square.js`

---

### 9. Add <a name='subparagraph9'></a>

Write a script that prints the addition of 2 integers

* The first argument is the first integer
* The second argument is the second integer
* You have to define a function with this prototype: `function add(a, b)`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```ruby
guillaume@ubuntu:~/$ ./9-add.js 
NaN
guillaume@ubuntu:~/$ ./9-add.js 1
NaN
guillaume@ubuntu:~/$ ./9-add.js 1 7
8
guillaume@ubuntu:~/$ ./9-add.js 13 89
102
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `9-add.js`

---

### 10. Factorial <a name='subparagraph10'></a>

Write a script that computes and prints a factorial

* The first argument is integer (argument can be cast as integer) used for computing the factorial
* Factorial of `NaN` is `1`
* You must do it recursively
* You must use a function
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```ruby
guillaume@ubuntu:~/$ ./10-factorial.js 
1
guillaume@ubuntu:~/$ ./10-factorial.js 3
6
guillaume@ubuntu:~/$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `10-factorial.js`

---

### 11. Second biggest! <a name='subparagraph11'></a>

Write a script that searches the second biggest integer in the list of arguments.

* You can assume all arguments can be converted to integer
* If no argument passed, print `0`
* If the number of arguments is 1, print `0`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```ruby
guillaume@ubuntu:~/$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `11-second_biggest.js`

---

### 12. Object <a name='subparagraph12'></a>

Update this script to replace the value `12` with `89`:

* You are not allowed to use `var`

```scss
guillaume@ubuntu:~/$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `12-object.js`

---

### 13. Add file <a name='subparagraph13'></a>

Write a function that returns the addition of 2 integers.

* The function must be visible from outside
* The name of the function must be `add`
* You are not allowed to use `var`

Tip

```ruby
guillaume@ubuntu:~/$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/$ ./13-main.js
8
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `13-add.js`

---

### 14. Const or not const <a name='subparagraph14'></a>

Write a file that modifies the value of `myVar` to `333`

```ruby
guillaume@ubuntu:~/$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/$ ./100-main.js
333
guillaume@ubuntu:~/$
```

Do you get it? Tweet! Post! Talk about it!

Hint: Scope

**This exercise doesn't pass `semistandard`** so don't worry about it.

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `100-let_me_const.js`

---

### 15. Call me Moby <a name='subparagraph15'></a>

Write a function that executes `x` times a function.

* The function must be visible from outside
* Prototype: `function (x, theFunction)`
* You are not allowed to use `var`

```kotlin
guillaume@ubuntu:~/$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `101-call_me_moby.js`

---

### 16. Add me maybe <a name='subparagraph16'></a>

Write a function that increments and calls a function.

* The function must be visible from outside
* Prototype: `function (number, theFunction)`
* You are not allowed to use `var`

```ruby
guillaume@ubuntu:~/$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/$ ./102-main.js
New value: 5
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `102-add_me_maybe.js`

---

### 17. Increment object <a name='subparagraph17'></a>

Update this script by adding a new function `incr` that increments the integer `value`.

* You are not allowed to use `var`

```scss
guillaume@ubuntu:~/$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/$ ./103-object_fct.js 
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/$
```

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `javascript-warm_up`
* File: `103-object_fct.js`

---


## Authors
Ksyv - [GitHub Profile](https://github.com/ksyv)
