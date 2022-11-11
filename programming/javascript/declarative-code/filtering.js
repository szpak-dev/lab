/*
 * Email addresses passed in the form
 */

const emails = [
    'pied#piper',
    'peter@pan',
    'john.rambo',
    'john@example.com',
    'ma!donna',
];

const is_valid_email = email => /^\S+@\S+\.\S+$/.test(email);

/*
 * Imperatively find valid emails
 */

let valid_emails = [];

for (let i in emails) {
    const email = emails[i];
    if (is_valid_email(email)) {
        valid_emails.push(email);
    }
}

/*
 * Declarative way
 */

valid_emails = emails.filter(email => is_valid_email(email));

/*
 * Resulting Array
 */
['john@example.com'];
