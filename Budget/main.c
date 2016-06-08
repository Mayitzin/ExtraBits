/* =================
 * Budget Controller
 * =================
 *
 * @author: Mario Garcia
**/

#include <time.h>
#include <stdio.h>
#include "transactions.h"

#define LINE_LENGTH 500

// ------------------------------- MAIN ROUTINE -------------------------------

int main(int argc, char *argv[]) {
    // Obtain current time
    time_t current_time;
    current_time = time(NULL);
    // Convert to local time format
    char* c_time_string;
    c_time_string = ctime(&current_time);
    printf("Current time is %s", c_time_string);

    // First Transaction
    struct transaction t1 = {.id = 123, .name = "Mario", .email = "mario@mail.com"};
    transaction_print(&t1);

    // Second Transaction
    struct transaction *t2 = setTransaction(456, "Johanna", 500.0, "johanna@mail.com");
    transaction_print(t2);

    return 0;
}
