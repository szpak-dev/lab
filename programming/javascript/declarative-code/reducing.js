/*
 * List of products, which needs to be indexed
 */

const products = [
    {id: 1, name: 'Soap'},
    {id: 2, name: 'Bread'},
    {id: 3, name: 'Milk'},
    {id: 4, name: 'Coffee'},
    {id: 5, name: 'Chewing Gum'},
    {id: 6, name: 'Banana'},
    {id: 7, name: 'Orange Juice'},
    {id: 8, name: 'Salad'},
];

/*
 * Create Index imperatively
 */

let index = [];

for (let i in products) {
    index[products[i]['id']] = products[i]['name'];
}

/*
 * And this is how you would do this declaratively
 */

index = products.reduce((index, product) => {
    index[product.id] = product.name;
    return index;
}, {});
