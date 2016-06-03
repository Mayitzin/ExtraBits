#
# Makefile for Budget Planner
#
CC = gcc
CFLAGS = -Wextra -std=c99 -pedantic

SRC = main.c transactions.c

OBJS = $(SRC:.c=.o)

MAIN = budget

.PHONY: depend clean

# For a strange reason it only runs if the definition for the SHELL is present
SHELL=C:\Windows\System32\cmd.exe

all: $(MAIN)
	@echo Executable named budget has been compiled

$(MAIN): $(SRC)
	$(CC) $(CFLAGS) -o $(MAIN) $(SRC)

clean:
	$(RM) *.o *~ $(MAIN)
