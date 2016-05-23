#
# Makefile for Budget Planner
#
CC = gcc
CFLAGS = -Wextra -std=c99 -pedantic

SRC = main.c transactions.c

OBJS = $(SRC:.c=.o)

MAIN = kf

.PHONY: depend clean

# For a strange reason it only runs if the definition for the SHELL is present
SHELL=C:\Windows\System32\cmd.exe

all: $(MAIN)
	@echo Simple executable named kf has been compiled

$(MAIN): $(OBJS)
	$(CC) $(CFLAGS) -o $(MAIN) $(OBJS)

clean:
	$(RM) *.o *~ $(MAIN)
