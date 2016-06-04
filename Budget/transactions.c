/* =================
 * Budget Controller
 * Function declarations and method definitions
 * =================
 *
 * @author: Mario Garcia
**/

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

#include "transactions.h"

// Global initial variables
int id=0x00;
double amount=0.0;
char name[NAME_LENGTH] = "John Doe";
char email[MAIL_LENGTH] = "john@mail.com";

/**
* @brief Prints the information of the transaction.
*
* This information takes a pointer to a transaction (structure) and prints the
* data stored in it.
*
* @param [in] transaction is a pointer to a structure defined as a transaction.
*
* Example Usage:
* @code{.c}
*    struct transaction t1 = {.id=123, .name="Mario"};
*    transaction_print(&t1);
* @endcode
*/
void transaction_print(struct transaction *tran) {
    printf("\nTransaction No.:  %d\n", tran->id);
    printf("\tAccount holder:   %s\n", tran->name);
    printf("\tContact Email:    %s\n", tran->email);
}


/**
* @brief Exits the application with an error.
*
* @param [in] transaction is a pointer to a structure defined as a transaction.
*
* Example Usage:
* @code{.c}
*    if(!t_struct) die("Memory error");
* @endcode
*/
void die(const char *message) {
    if(errno) { perror(message); }
    else { printf("ERROR: %s\n", message); }
    exit(1);
}


/**
* @brief Sets information to a given transaction.
*
* This takes a pointer to a transaction (structure) and the required information
* to store in it, and saves accordingly.
*
* @param [in] transaction is a pointer to a structure defined as a transaction.
* @param [in] id is an integer defining the ID of the tranaction.
* @param [in] name is the string of the name.
* @param [in] email is the string of the email.
*
* Example Usage:
* @code{.c}
*     struct transaction *t3 = malloc(sizeof(struct transaction));
*     setInfo(t3, 345, "Mario", "mario@mail.com");
* @endcode
*/
void setInfo(struct transaction *tran, int id, char *name, char *email) {
    tran->id = id;
    strcpy(tran->name, name);
    strcpy(tran->email, email);
}


/**
* @brief Creates a transaction and sets its information.
*
* Creates a transaction (structure) and sets the required information to store
* in it.
*
* @param [in] transaction is a pointer to a structure defined as a transaction.
* @param [in] id is an integer defining the ID of the tranaction.
* @param [in] name is the string of the name.
* @param [in] email is the string of the email.
*
* Example Usage:
* @code{.c}
*     struct transaction *t4 = setTransaction(456, "Johanna", "johanna@mail.com");
* @endcode
*/
struct transaction *setTransaction(int id, char *name, char *email) {
    struct transaction *t_struct = malloc(sizeof(struct transaction));
    if(!t_struct) die("Memory error");
    setInfo(t_struct, id, name, email);
    return t_struct;
}
