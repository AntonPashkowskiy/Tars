CC=gcc
CFLAGS=-c -I/usr/include/glib-2.0 -I/usr/lib/glib-2.0/include -lglib-2.0
TESTSRC=monitoring.c
TESTOBJ=$(TESTSRC:.c=.o)
TESTNAME=monitoring_test

all: monitoring_test

monitoring_test: $(TESTOBJ)
	$(CC) $(TESTOBJ) -o $(TESTNAME)

$(TESTOBJ): $(TESTSRC)
	$(CC) $(CFLAGS) $(TESTSRC)

clean:
	rm *.o
	rm $(TESTNAME)
