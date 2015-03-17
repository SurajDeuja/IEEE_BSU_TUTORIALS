# Very simple make file

main: mul.o main.o
	$(CC) -o main $^

mul.o: mul.c
	$(CC) -c mul.c

main.o: main.c
	$(CC) -c main.c

clean:
	rm -rf *.o
