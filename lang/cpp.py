# Import associated modules
import subprocess
import os


class handle_cpp():
    def __init__(self, path):
        """Initialize all function's"""

        self.path = path

        # Creates specified directory
        try:
            os.system(f"mkdir {path}")
        # Check if file exist and if it is the it will remove it
        # and create another one again
        except FileExistsError:
            os.removedirs(path)
            os.system(f"mkdir {path}")

        # Creates makefile's
        self.mkMakefile()
        # Create main file
        self.mkMain()
        # Create folder where the main binary will be stored
        # neither it is debug nor release
        os.system(f"mkdir {path}/bin")
        os.system(f"mkdir {path}/bin/Debug")
        os.system(f"mkdir {path}/bin/Release")

    def mkMain(self):
        """Write and Create the C++ main file"""

        file = f"{self.path}/main.cpp"
        with open(file, "w") as f:
            # Writes the nessesary includes
            f.write("#include <iostream>\n")

            # Adds newline to the code
            f.write("\n")

            # Writes the namespace needed
            f.write("using namespace std;\n")

            # Adds newline to the code
            f.write("\n")

            # And writes the c++ main function
            f.write("int main(int argc, char* argv[])\n")
            f.write("{\n")
            f.write('    cout << "Hello World" << endl;\n')
            f.write("    return 0\n")
            f.write("}\n")

    def mkMakefile(self):
        """Write and Create the Makefile used for auto compile project"""

        file = f"{self.path}/Makefile"

        with open(file, "w") as f:
            # Writes the variable CC
            f.write("CC=g++ \n")
            f.write("\n")

            # Writes the variable LIBS and CFLAGS
            f.write("LIBS= \n")
            f.write("CFLAGS= \n")

            f.write("\n")

            # Writes the target debug to file
            f.write("debug: main.cpp \n")
            f.write("     $(CC) $(CFLAGS) main.cpp -o bin/Debug/main $(LIBS) \n") 
            f.write("     . bin/Debug/main \n")

            # Adds newline to the code
            f.write("\n")

            # Writes the target release to file
            f.write("release: main.cpp \n")
            f.write("     $(CC) $(CFLAGS) main.cpp -o bin/Release/main $(LIBS) \n") 
            f.write("     . bin/Release/main \n")

            # Adds newline to the code
            f.write("\n")

            # Writes the target clean to file
            f.write("clean: \n")
            f.write("     rm bin/Debug/main \n")
            f.write("     rm bin/Release/main \n")

            # Adds newline to the code
            f.write("\n")


if __name__ == '__main__':
    print("This module is not a standalone module and cannot be run directly!")
    exit(1)
