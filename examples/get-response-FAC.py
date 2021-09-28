### Take a look at examples/xml-responses/fac-invoice.xml to see the format and structure of the XML ###

from copaco.orders import CopacoOrders

orders = CopacoOrders(CUSTOMER_ID, SENDER_ID)
responses = orders.getResponses(type='FAC')

for resp in responses:
    for line in resp.invoiceline:
        print(line.invoice_item.serialnumbers.serialnumber)


