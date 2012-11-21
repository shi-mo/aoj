set -u

if [ $# -lt 1 ]; then
    echo "usage: $0 0001" >&2
    exit 1
fi

ID=$1
DIR=${ID}
BIN=./${DIR}.exe

for TEST_INPUT in ${DIR}/*.input; do
    TEST_NAME=`echo ${TEST_INPUT} | sed "s/^${DIR}\///" | sed "s/\.input$//"`
    TEST_OUTPUT=${DIR}/${TEST_NAME}.output

    echo "${DIR}: ${TEST_NAME}"
    ${BIN} < ${TEST_INPUT} | diff -u ${TEST_OUTPUT} -
    # pending: check for exit status
done
