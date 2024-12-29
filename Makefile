CFLAGS   := -g -Wall
CPPFLAGS := -g -Wall -std=c++17
SRCS    := $(shell ls *.c)

DFLAGS   := -de -w
DSRCS    := $(shell ls *.d)
DTARGETS := $(patsubst %.d,%,$(DSRCS))

CTARGETS := $(patsubst %.c,%.exe,$(SRCS))
TARGETS  := $(CTARGETS) $(DTARGETS)
TEST_TARGETS := $(TARGETS) $(shell ls *.rb)
CLEAN	:= *~ */*~ */_*.in */_*.out _test.diff
CLOBBER	:= *.dSYM

all:	build

.PHONY: build
build: $(TARGETS)

.SUFFIXES: .c .exe
.c.exe:
	gcc $(CFLAGS) -o $@ $<

.SUFFIXES: .cpp .exe
.cpp.exe:
	g++ $(CPPFLAGS) -o $@ $<

.SUFFIXES: .d
.d.exe:
	dmd $(DFLAGS) $< -of$@
	rm $*.o

.PHONY: test
test: build
	./test $(TEST_TARGETS)

.PHONY: clean
clean:
	rm -f $(CLEAN)

.PHONY: clobber
clobber: clean
	rm -f $(TARGETS)

.PHONY: init-auth
init-auth:
	.auth/gen_pem_keypair.sh && .auth/encrypt_save_auth_yaml.sh
