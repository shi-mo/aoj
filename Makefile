CFLAGS  := -g -Wall
SRCS    := $(shell ls *.c)
TARGETS := $(patsubst %.c,%.exe,$(SRCS))
CLEAN	:= *~ */*~

all:	build

.PHONY: build
build: $(TARGETS)

.SUFFIXES: .c .exe
.c.exe:
	gcc $(CFLAGS) -o $@ $<

.PHONY: clean
clean:
	rm -f $(CLEAN)

.PHONY: clobber
clobber: clean
	rm -f $(TARGETS)
