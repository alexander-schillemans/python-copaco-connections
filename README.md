# python-copaco-connections
Easy python integrations for the Copaco Customer Connections

## Limitations

This package is limited to the Copaco BE - Dutch Productlist in CSV format via FTP. Might be extended in the future.

More info here: https://www.copaco.com/en-be/customer-service-e-commerce-fulfillment

## Getting started

### Install

Install with pip.

```python
pip install python-copaco-connections
```

### Import

Import the package and the CopacoConnectionBE object.

```python
from copaco.connection import CopacoConnectionBE
```

### Setup connection

Make the connection with your provided FTP credentials.

```python
conn = CopacoConnectionBE(FTP_HOST, FTP_LOGIN, FTP_PASSWD)
```


## Pricelist

You can retrieve the pricelist as follows:

```python
priceList = conn.priceList.get()
```

This will return an ordinary list which contains PriceListItem objects.

You can find the attributes of this object and their use below:

**PriceListItem object**

| Attribute  | Contains | Type |
| ------------- | ------------- |-------------|
| article  | Article number  | string |
| vendorCode  | Unique vendor code  | string |
| description  | Short description  | string |
| price  | Price, excluding levies  | float |
| priceWithLevies  | Price, including levies | float |
| stock  | Amount of stock available  | integer |
| hierarchy  | Product hierarchy  | string |
| unspscCode  | UNSPSC code  | string |
| EAN  | EAN code  | string |
| statusCode  | Status code (0 - 12). Refer to docs.  | integer |
| status  | Human-readable status  | string |
| auvibel  | Price of Auvibel  | float |
| reprobel  | Price of Reprobel  | float |
| recupel  | Price of Recupel  | float |
| bebat  | Price of Bebat  | float |
| nextDelivery  | Next delivery date of this product | date |
| nextDeliveryAmount  | Amount that will be delivered on next delivery | integer |
| inventoryStatusCode  | ATP code | string |
| inventoryStatus  | Human-readable ATP code | string |


## Sample script

Show all articles with their prices, including levies.

```python
from copaco.connection import CopacoConnectionBE

HOST = 'ftp.copaco.com'
LOGIN = 'XXXX'
PASSWD = 'XXXX'

conn = CopacoConnectionBE(HOST, LOGIN, PASSWD)

priceList = conn.priceList.get()
for item in priceList:
  formattedStr = '{description} - {number} - € {price}'.format(description=item.description, number=item.article, price=item.priceWithLevies)
  print(formattedStr)

```
