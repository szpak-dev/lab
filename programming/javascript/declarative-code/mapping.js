/*
 * Data from API
 */
const users = [
    {
        data: {
            id: 1,
            admin: false,
            active: true,
        },
        info: {
            username: 'user1',
            has_discount: true,
        }
    },
    {
        data: {
            id: 2,
            admin: false,
            active: false,
        },
        info: {
            username: 'user2',
            has_discount: false,
        }
    }
];

/*
 * Imperative way of transforming the response, verbose and complex
 */

let views = [];

for (let i in users) {
    views.push({
        id: users[i].data.id,
        username: users[i].info.username,
    });
}

/*
 * Declarative way of transforming the response, simple yet meaningful
 * Mind that this method doesn't mutate the original Array
 */

views = users.map(user => ({id: user.data.id, username: user.info.username}));

/*
 * In both cases, the views variable will be transformed API response
 */

[
    {id: 1, username: 'user1'},
    {id: 2, username: 'user2'},
]
