test: librecast.so
	gcc -L. -Wall -o test test.c -lrecast

librecast.so: recast.o
	gcc -shared -o librecast.so recast.o

recast.o: recast.c
	gcc -c -Wall -Werror -fpic recast.c

clean:
	rm librecast.so recast.o
