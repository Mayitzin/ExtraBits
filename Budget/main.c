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

#define LINE_LENGTH 500
#define NAME_LENGTH 100
#define MAIL_LENGTH 50

struct transaction {
    int id;
    char name[NAME_LENGTH];
    char email[MAIL_LENGTH];
};

// Declare Functions
void transaction_print(struct transaction *tran);
void die(const char *message);
void setInfo(struct transaction *tran, int id, char *name, char *email);
struct transaction *getTrans(int id, char *name, char *email);

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
    struct transaction *t4 = getTrans(456, "Johanna", "johanna@mail.com");
    transaction_print(t4);

    return 0;
}


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

struct transaction *getTrans(int id, char *name, char *email) {
    struct transaction *t4 = malloc(sizeof(struct transaction));
    if(!t4) die("Memory error");
    setInfo(t4, id, name, email);
    return t4;
}