CC=gcc
CFLAGS=-c
TESTSRC=test.c messaging.c
TESTOBJ=$(TESTSRC:.c=.o)
TESTNAME=messaging_test

all: messaging_test

messaging_test: $(TESTOBJ)
	$(CC) $(TESTOBJ) -o $(TESTNAME) -lzmq

$(TESTOBJ): $(TESTSRC)
	$(CC) $(CFLAGS) $(TESTSRC)

clean:
	rm *.o
	rm $(TESTNAME)
