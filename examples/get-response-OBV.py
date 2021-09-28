### Take a look at examples/xml-responses/obv-orderconfirmation.xml to see the format and structure of the XML ###

from copaco.orders import CopacoOrders

orders = CopacoOrders(CUSTOMER_ID, SENDER_ID)
responses = orders.getResponses(type='OBV')

for resp in responses:
    print(resp.orderheader.order_number)