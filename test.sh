#!/bin/sh

set -u

if [ $# -lt 1 ]; then
    echo "usage: $0 0001 0002 ..." >&2
    exit 1
fi

for ID in $*; do
    DIR=${ID}
    BIN=./${DIR}.exe

    echo -n "${ID} "
    if [ ! -e ${DIR}/ ]; then
        echo ""
        continue
    fi

    (
        cd ${DIR}
        ls gen_*.rb >/dev/null 2>&1
        if [ 0 -eq $? ]; then
            for SCRIPT in gen_*.rb; do
                ruby ${SCRIPT}
            done
        fi
    )

    for TEST_INPUT in ${DIR}/*.input; do
        TEST_NAME=`echo ${TEST_INPUT} | sed "s/^${DIR}\///" | sed "s/\.input$//"`
        TEST_OUTPUT=${DIR}/${TEST_NAME}.output

        ${BIN} < ${TEST_INPUT} | diff -u ${TEST_OUTPUT} -
        STATUS=$?
        if [ 0 -ne ${STATUS} ]; then
            echo "Test failed: ${TEST_NAME} (status ${STATUS})"
        else
            echo -n "."
        fi
    done
    echo ""
done
