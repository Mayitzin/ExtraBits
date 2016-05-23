/* =================
 * Budget Controller
 * Function declarations and method definitions
 * =================
 *
 * @author: Mario Garcia
**/

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
