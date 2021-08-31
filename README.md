# python-copaco-connections
Easy python integrations for the Copaco Customer Connections

## Limitations

This package is limited to the Copaco BE - Dutch Productlist in CSV format via FTP. Might be extended in the future.

## Getting started

### Install

Install with pipenv.

```
pipenv install python-copaco-connections
```

### Import

Import the package and the CopacoConnectionBE object.

```
from copaco.connection import CopacoConnectionBE
```

### Setup connection

Make the connection with your provided FTP credentials.

```
conn = CopacoConnectionBE(FTP_HOST, FTP_LOGIN, FTP_PASSWD)
```


## Pricelist

You can retrieve the pricelist as follows:

```
priceList = conn.priceList.get()
```

This will return an ordinary list which contains PriceListItem objects.

You can find the attributes of this object and their use below:

**PriceListItem object**

| Attribute  | Contains |
| ------------- | ------------- |
| article  | Article number  |
| vendorCode  | Unique vendor code  |
| description  | Short description  |
| price  | Price, excluding levies  |
| priceWithLevies  | Price, including levies |
| stock  | Amount of stock available  |
| hierarchy  | Product hierarchy  |
| unspscCode  | UNSPSC code  |
| EAN  | EAN code  |
| statusCode  | Status code (0 - 12). Refer to docs.  |
| status  | Human-readable status  |
| auvibel  | Price of Auvibel  |
| reprobel  | Price of Reprobel  |
| recupel  | Price of Recupel  |
| bebat  | Price of Bebat  |
| nextDelivery  | Next delivery date of this product |
| nextDeliveryAmount  | Amount that will be delivered on next delivery |
| inventoryStatusCode  | ATP code |
| inventoryStatus  | Human-readable ATP code |
