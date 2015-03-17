INC_DIR = inc

CFLAGS += -Wall 
CFLAGS += -Wconversion
CFLAGS += $(foreach d, $(INC_DIR), -I$d)

SRC_PATH = src
include src/makefile.mk

OBJ = $(SRC:.c=.o)
PRGM = main

all: $(PRGM)

$(PRGM): $(OBJ)
	$(CC) -o main $^

.PHONY: clean all

clean:
	rm -rf $(SRC_PATH)/*.o
	rm -rf *.o
	rm -rf $(PRGM)

