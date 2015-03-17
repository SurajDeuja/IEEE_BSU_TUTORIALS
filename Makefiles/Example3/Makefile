CFLAGS += -Wall -Wconversion
SRC = mul.c main.c
OBJ = $(SRC:.c=.o)
PRGM = main

all: $(PRGM)

$(PRGM): $(OBJ)
	$(CC) -o main $^

.PHONY: clean all

clean:
	rm -rf *.o
	rm -rf $(PRGM)
