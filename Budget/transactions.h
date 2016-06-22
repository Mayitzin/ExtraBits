/* =================
 * Budget Controller
 * Function declarations and method definitions
 * =================
 *
 * @author: Mario Garcia
**/

#ifndef TRANSACTIONS_H
#define TRANSACTIONS_H

#define NAME_LENGTH 100
#define MAIL_LENGTH 50

struct transaction {
    int id;
    char name[NAME_LENGTH];
    double amount;
    char email[MAIL_LENGTH];
};

// Declare Functions
void transaction_print(struct transaction *tran);
void die(const char *message);
void setInfo(struct transaction *tran, int id, char *name, double amount, char *email);
void printTime(void);
struct transaction *setTransaction(int id, char *name, double amount, char *email);

#endif // TRANSACTIONS_H
