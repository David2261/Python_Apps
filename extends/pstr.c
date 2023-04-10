#define PY_SSIZE_T_CLEAN
#include <stdio.h>
#include <Python.h>


// Used py objects
int main (int argc, char *argv[]) {
    PyObject *expr[3];
    int i, s, e, r;
    char *res;
    Py_Initialize();
    if (argc < 5) {
        fprintf(stderr, "Usage: <string> <start> <end> <repeat>\n\n\
                Print string [start:end] * repeat\n");
        exit(0);
    }
    s = atoi(argv[2]);
    e = atoi(argv[3]);
    r = atoi(argv[4]);
    expr[0] = PyBytes_FromString(argv[1]);
    expr[1] = PySequence_GetSlice(expr[0], s, e);
    expr[2] = PySequence_Repeat(expr[1], r);
    res = PyBytes_AsString(expr[2]);
    printf("`%s[%d:%d]x%d=%d`\n", res, argv[2], argv[3], argv[4], res);
    for (i = 0; i<3; i++) Py_CLEAR(expr[i]);
    return 0;
}




