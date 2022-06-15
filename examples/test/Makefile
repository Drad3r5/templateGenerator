CC=g++ 

LIBS= 
CFLAGS= 

debug: main.cpp
	$(CC) $(CFLAGS) main.cpp -o bin/Debug/main $(LIBS)
	./bin/Debug/main 

release: main.cpp 
	$(CC) $(CFLAGS) main.cpp -o bin/Release/main $(LIBS) 
	./bin/Release/main 

clean: 
	rm bin/Debug/main 
	rm bin/Release/main 

