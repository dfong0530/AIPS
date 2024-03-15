const fs = require('fs');
const csv = require('csv-parser');
const request = require('request');

const API_ENDPOINT = 'https://api.ebay.com/ws/api.dll';
const USER_TOKEN = 'YOUR_USER_TOKEN_HERE';

function createEbayListing(item) {
  const xmlRequest = `<?xml version="1.0" encoding="utf-8"?>
<AddItemRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <RequesterCredentials>
    <eBayAuthToken>${USER_TOKEN}</eBayAuthToken>
  </RequesterCredentials>
  <ErrorLanguage>en_US</ErrorLanguage>
  <WarningLevel>High</WarningLevel>
  <Item>
    <Title>${item.Title}</Title>
    <Description>${item.Description}</Description>
    <PrimaryCategory>
      <CategoryID>${item.CategoryID}</CategoryID>
    </PrimaryCategory>
    <StartPrice>${item.Price}</StartPrice>
    <ConditionID>${item.ConditionID}</ConditionID>
    <Country>US</Country>
    <Currency>USD</Currency>
    <DispatchTimeMax>3</DispatchTimeMax>
    <ListingDuration>Days_7</ListingDuration>
    <ListingType>FixedPriceItem</ListingType>
    <PaymentMethods>PayPal</PaymentMethods>
    <PayPalEmailAddress>seller@example.com</PayPalEmailAddress>
    <PostalCode>95125</PostalCode>
    <Quantity>1</Quantity>
    <ReturnPolicy>
      <ReturnsAcceptedOption>ReturnsAccepted</ReturnsAcceptedOption>
      <RefundOption>MoneyBack</RefundOption>
      <ReturnsWithinOption>Days_30</ReturnsWithinOption>
      <Description>If not satisfied, return the item for refund.</Description>
      <ShippingCostPaidByOption>Buyer</ShippingCostPaidByOption>
    </ReturnPolicy>
    <ShippingDetails>
      <ShippingType>Flat</ShippingType>
      <ShippingServiceOptions>
        <ShippingServicePriority>1</ShippingServicePriority>
        <ShippingService>USPSMedia</ShippingService>
        <ShippingServiceCost>2.50</ShippingServiceCost>
      </ShippingServiceOptions>
    </ShippingDetails>
    <Site>US</Site>
  </Item>
</AddItemRequest>`;
}