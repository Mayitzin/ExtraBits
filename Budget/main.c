/* =================
 * Budget Controller
 * =================
 *
 * @author: Mario Garcia
**/

#include "transactions.h"

#define LINE_LENGTH 500

// ------------------------------- MAIN ROUTINE -------------------------------

int main(int argc, char *argv[]) {
    // First Transaction
    struct transaction t1 = {.id = 123, .name = "Mario", .email = "mario@mail.com"};
    transaction_print(&t1);

    // Second Transaction
    struct transaction *t2 = setTransaction(456, "Johanna", "johanna@mail.com");
    transaction_print(t2);

    return 0;
}
