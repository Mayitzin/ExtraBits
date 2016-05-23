/* =================
 * Budget Controller
 * Function declarations and method definitions
 * =================
 *
 * @author: Mario Garcia
**/

#include "transactions.h"

// Define Functions

void transaction_print(struct transaction *tran) {
    printf("%d %s %s\n",  tran->id,  tran->name,  tran->email);
}

void die(const char *message) {
    if(errno) { perror(message); }
    else { printf("ERROR: %s\n", message); }
    exit(1);
}

void setInfo(struct transaction *tran, int id, char *name, char *email) {
    tran->id = id;
    strcpy(tran->name, name);
    strcpy(tran->email, email);
}

struct transaction *setTransaction(int id, char *name, char *email) {
    struct transaction *t_struct = malloc(sizeof(struct transaction));
    if(!t_struct) die("Memory error");
    setInfo(t_struct, id, name, email);
    return t_struct;
}
