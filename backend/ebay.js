const eBay = require('ebay-node-api'); // Assume an eBay API SDK
const fs = require('fs');
const csvParser = require('csv-parser'); // npm package to parse CSV

// Your eBay API credentials
const eBayApi = new eBay({
    clientID: 'EkSzWVMAhsfXEGr8wgryhKscVB6o4dRU1IRyZGMJ26E',
    clientSecret: 'lV_bwv1FIdf1rhtNYWCR-3LLd2vtzWc5tPQE_SOO69LnKr2rt7-4_ikUZS0YrqNO',
    body: {
        grant_type: 'client_credentials',
        scope: 'https://api.ebay.com/oauth/api_scope'
    }
});

const createListing = (item) => {
    eBayApi.addFixedPriceItem({
        title: item.Title,
        description: item.Description,
        price: item.Price,
        category_id: item.CategoryID,
        condition_id: item.ConditionID,
        quantity: item.Quantity,
        location: {
            country: item.Country,
            postal_code: item.PostalCode,
            location: item.Location
        },
        shipping_details: {
            shipping_service: item.ShippingService,
            shipping_cost: item.ShippingCost
        }
    }).then((response) => {
        console.log('Listing created:', response);
    }).catch((error) => {
        console.error('Error creating listing:', error);
    });
};

const listItemsFromCSV = (csvFilePath) => {
    const items = [];

    fs.createReadStream(csvFilePath)
        .pipe(csvParser())
        .on('data', (row) => {
            items.push(row);
        })
        .on('end', () => {
            console.log('CSV file successfully processed');
            items.forEach(createListing);
        });
};

listItemsFromCSV('./items.csv');