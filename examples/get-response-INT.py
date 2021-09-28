### Take a look at examples/xml-responses/int-orderresponse.xml to see the format and structure of the XML ###

from copaco.orders import CopacoOrders

orders = CopacoOrders(CUSTOMER_ID, SENDER_ID)
responses = orders.getResponses(type='INT')

for resp in responses:
    print(resp.supplier)
    print(resp.ordernumber)


