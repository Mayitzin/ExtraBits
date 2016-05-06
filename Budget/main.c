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


void transaction_print(struct transaction *tran) {
    printf("%d %s %s\n",  tran->id,  tran->name,  tran->email);
}

void die(const char *message) {
    if(errno) { perror(message); }
    else { printf("ERROR: %s\n", message); }
    exit(1);
}

// void setInfo(char *name, int id, char *name, char *email){}


// ------------------------------- MAIN ROUTINE -------------------------------

int main(int argc, char *argv[]){
    printf("First Test\n");

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

    return 0;
}