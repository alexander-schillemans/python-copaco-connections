from .xmlhandler import XMLHandler
from .models.order import *
import datetime
import xml.etree.ElementTree as ET

class CopacoOrdersBE:

    def __init__(self, customerId, senderId):

        self.senderId = senderId
        self.customerId = customerId
        self.method = 'HTTP'
        self.xmlHandler = XMLHandler()
    
    def create(self,
        external_document_id,
        supplier,
        customer_ordernumber,
        completedelivery,
        requested_deliverydate=None,
        recipientsreference=None,
    ):
        ''' Simplified create function to create a basic Order object, returns an Order object '''

        today = datetime.datetime.today().strftime('%d-%m-%Y')
        customer = Customer().create(customerid=self.customerId)
        ship_to = ShipTo()
        ordertext = OrderText()
        header = OrderHeader().create(ship_to=ship_to, ordertext=ordertext, requested_deliverydate=requested_deliverydate, recipientsreference=recipientsreference, sender_id=self.senderId, orderdate=today, customer_ordernumber=customer_ordernumber, customer=customer, completedelivery=completedelivery)
        orderlines = OrderLines()
        
        order = Order().create(
            external_document_id=external_document_id,
            supplier=supplier,
            orderheader=header,
            orderlines=orderlines,
        )

        return order
    
    def sendToCopaco(self, order):
        ''' Takes an Order object, generates XML file and sends the file to Copaco '''
        
        json = order.getJSON()
        # print(json)
        xml = self.xmlHandler.parseJSON(json)
        tree = ET.ElementTree(xml)
        tree.write("test.xml")
    





