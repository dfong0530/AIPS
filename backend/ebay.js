const eBayApi = require('ebay-api'); // Assume an eBay API SDK
const fs = require('fs');
const csvParser = require('csv-parser');
require('dotenv').config();

const devID = '811bfc1a-ccef-4627-82e3-ecc7bc652d71'

const eBay = new eBayApi({
    appId: process.env.CLIENT_ID,
    certId: process.env.CLIENT_SECRET,
    sandbox: false,
    siteId: eBayApi.SiteId.EBAY_US, // required for traditional APIs, see https://developer.ebay.com/DevZone/merchandising/docs/Concepts/SiteIDToGlobalID.html
    marketplaceId: eBayApi.MarketplaceId.EBAY_US, // default. required for RESTful APIs
    acceptLanguage: eBayApi.Locale.en_US, // default
    contentLanguage: eBayApi.Locale.en_US, // default.
});

eBay.OAuth2.setScope([
  'https://api.ebay.com/oauth/api_scope',
  'https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly',
  'https://api.ebay.com/oauth/api_scope/sell.fulfillment'
]);

// 2. Generate and open Url and Grant Access
const url = eBay.OAuth2.generateAuthUrl();
console.log('Open URL', url);

//Your eBay API credentials


// const createListing = (item) => {
//     eBayApi.addFixedPriceItem({
//         title: item.Title,
//         description: item.Description,
//         price: item.Price,
//         category_id: item.CategoryID,
//         condition_id: item.ConditionID,
//         quantity: item.Quantity,
//         location: {
//             country: item.Country,
//             postal_code: item.PostalCode,
//             location: item.Location
//         },
//         shipping_details: {
//             shipping_service: item.ShippingService,
//             shipping_cost: item.ShippingCost
//         }
//     }).then((response) => {
//         console.log('Listing created:', response);
//     }).catch((error) => {
//         console.error('Error creating listing:', error);
//     });
// };

// const listItemsFromCSV = (csvFilePath) => {
//     const items = [];

//     fs.createReadStream(csvFilePath)
//         .pipe(csvParser())
//         .on('data', (row) => {
//             items.push(row);
//         })
//         .on('end', () => {
//             console.log('CSV file successfully processed');
//             items.forEach(createListing);
//         });
// };

//listItemsFromCSV('./items.csv');