Template generator for Project written in python
**Features:**
  1. *Generates language specific projects.*
  2. *C++ is still only the supported language.*

**Incoming Features:**
  1. *TUI Support*
  2. *Other language support*

**Files:**

**cpp.py:**
  1. *This is where the function's used to generate project templates*

**generate.py:** 
  1. *This is the main file where there is used to parse arguments*
  2. *and initialize any sub modules needed for language support.*


**Directories:**

**test:**
   1. *A test C++ Project* 
   2. *Is generated*


**Example:**

```sh
$ ./generate.py 
.USAGE: generate.py <lang> <path>
  lang - The language you want to work with. 
  path - The name of the project that you want to create. 

No arguments provided!
```
