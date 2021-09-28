### Take a look at examples/xml-responses/pak-dispatchadvice.xml to see the format and structure of the XML ###

from copaco.orders import CopacoOrders

orders = CopacoOrders(CUSTOMER_ID, SENDER_ID)
responses = orders.getResponses(type='PAK')

for resp in responses:
    print(resp.route)
    print(resp.dispatchheader.supplier)

