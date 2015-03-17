CFLAGS += -Wall -Wconversion

all: main

main: mul.o main.o
	$(CC) -o main $^

# Following implicit rule can be commented out
%.o : %.c
	$(CC) $(CFLAGS) -c $<

.PHONY: clean all

clean:
	rm -rf *.o
