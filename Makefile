CFLAGS  := -g -Wall
SRCS    := $(shell ls *.c)
TARGETS := $(patsubst %.c,%.exe,$(SRCS))

all:	build

.PHONY :build
build: $(TARGETS)

.SUFFIXES: .c .exe
.c.exe:
	gcc $(CFLAGS) -o $@ $<
