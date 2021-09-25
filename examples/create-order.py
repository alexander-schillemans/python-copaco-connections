from copaco.orders import CopacoOrders

orders = CopacoOrders('XXXX', 'XXXX')

order = orders.create('Abcdef', 'COPACO', 'Order 12345', 'N')
order.setShippingAdress('Alexander', 'TEST', 'Straat', '2000', 'Antwerpen', 'BE')
order.addOrderLine('HPPE135T-ABH', 'PN', 1, 125.85, 'EUR', textqualifier='0001', text='Orderline text')
order.addOrderLine('HPPE135T-ABH', 'PN', 1, 125.85, 'EUR', textqualifier='BID', text='Special Bid Number')

orders.sendToCopaco(order)