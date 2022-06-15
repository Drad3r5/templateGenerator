Project Template Generator written in python

Features:
  - generates language specific projects.
  - C++ is still only the supported language.

Incoming Features:
  - TUI Support 
  - Other language support

templateGenerator
├── examples
│   └── test
│       ├── bin
│       │   ├── Debug
│       │   └── Release
│       ├── main.cpp
│       └── Makefile
├── lang
│   └── cpp.py
├── main.py
├── __pycache__
│   └── cpp.cpython-310.pyc
└── README.md

Files:
  cpp.py:
    - This is where the function's used to generate project templates 

  main.py: 
    - This is the main file where there is used to parse arguments
    - and initialize any sub modules needed for language support.


Directories:
  test:
    - A test C++ Project 
    - Is generated


