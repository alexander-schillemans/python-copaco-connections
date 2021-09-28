from copaco.orders import CopacoOrders

orders = CopacoOrders(CUSTOMER_ID, SENDER_ID)
responses = orders.getResponses(type='ALL')

# INT
for resp in responses['INT']:
    print(resp.supplier)
    print(resp.ordernumber)

# OBV
for resp in responses['OBV']:
    print(resp.orderheader.order_number)

# FAC
for resp in responses['FAC']:
    for line in resp.invoiceline:
        print(line.invoice_item.serialnumbers.serialnumber)

# PAK
for resp in responses['PAK']:
    print(resp.route)
    print(resp.dispatchheader.supplier)
