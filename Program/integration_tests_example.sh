#!/usr/bin/bash



# Test 24. Permanently delete file if name changed

mkdir ./test
touch ./test/file.txt
tars add_rule -t /home/anton/Tars/Program/test/ \
    --event-types FILE_NAME_CHANGED \
    --extention-template txt \
    --action-type DELETE_FILE --is-permanent
mv ./test/file.txt ./test/file2.txt

if [ -f ./test/file2.txt ]
then
    echo "ERROR. File ./test/file2.txt was not deleted."
else
    echo "SUCCESS. File ./test/file2.txt was deleted."
fi

rm -rf ./test


# Test 25. Peplace file in subfolder if file moved from inside

mkdir -p ./test/sub
touch file.txt
tars add_rule -t /home/anton/Tars/Program/test/ \
    --event-types FILE_INCLUDED \
    --extention-template txt \
    --action-type REPLACE_FILE \
    --target-path /home/anton/Tars/Program/test/sub/
mv file.txt ./test/

if ! [ -f ./test/sub/file.txt ]
then
    echo "ERROR. File file.txt was not found in ./test/sub/."
else
    echo "SUCCESS. File file.txt was not found in ./test/sub/."
fi

