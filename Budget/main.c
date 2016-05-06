/* =================
 * Budget Controller
 * =================
 *
 * @author: Mario Garcia
**/

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

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


// ------------------------------- MAIN ROUTINE -------------------------------

int main(int argc, char *argv[]){
    printf("First Test\n");

    struct transaction t1 = {.id = 123, .name = "Mario"};

    transaction_print(&t1);

    return 0;
}