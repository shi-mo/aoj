CFLAGS   := -g -Wall
CPPFLAGS := -g -Wall -std=c++17
SRCS    := $(shell ls *.c)
IDS     := $(patsubst %.c,%,$(SRCS))
TARGETS := $(patsubst %.c,%.exe,$(SRCS))
TEST_TARGETS := $(TARGETS) $(shell ls *.rb)
CLEAN	:= *~ */*~ */_*.in */_*.out _test.diff

all:	build

.PHONY: build
build: $(TARGETS)

.SUFFIXES: .c .exe
.c.exe:
	gcc $(CFLAGS) -o $@ $<

.SUFFIXES: .cpp .exe
.cpp.exe:
	g++ $(CPPFLAGS) -o $@ $<

.PHONY: test
test: build
	./test $(TEST_TARGETS)

.PHONY: clean
clean:
	rm -f $(CLEAN)

.PHONY: clobber
clobber: clean
	rm -f $(TARGETS)
