/* =================
 * Budget Controller
 * =================
 *
 * @author: Mario Garcia
**/

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include "transactions.h"

#define LINE_LENGTH 500

// ------------------------------- MAIN ROUTINE -------------------------------

int main(int argc, char *argv[]) {
    // First Transaction
    struct transaction t1 = {.id = 123, .name = "Mario"};
    transaction_print(&t1);

    // Second Transaction
    struct transaction *t2 = malloc(sizeof(struct transaction));
    if(!t2) die("Memory error");
    t2->id = 234;
    strcpy(t2->name, "Eduardo");
    strcpy(t2->email, "eddy@gmail.com");
    transaction_print(t2);

    // Third Transaction
    struct transaction *t3 = malloc(sizeof(struct transaction));
    if(!t3) die("Memory error");
    setInfo(t3, 345, "Renske", "renske@mail.com");
    transaction_print(t3);

    // Fourth Transaction
    struct transaction *t4 = setTransaction(456, "Johanna", "johanna@mail.com");
    transaction_print(t4);

    return 0;
}
