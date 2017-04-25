CC=gcc
CFLAGS=-c
TESTSRC=./utils/linked_list.c ./actions/monitor_action.c
TESTOBJ=./*.o
TESTNAME=common_test

all: common_test

common_test: $(TESTOBJ)
	$(CC) $(TESTOBJ) -o $(TESTNAME)

$(TESTOBJ): $(TESTSRC)
	$(CC) $(CFLAGS) $(TESTSRC)

clean:
	rm *.o
	rm $(TESTNAME)
