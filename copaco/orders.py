import datetime
import requests

from .xmlhandler import XMLHandler
from .models.order import *
from .constants.errors import FailedRequest
from .utils import removeFile

class CopacoOrders:

    def __init__(self, customerId, senderId):

        self.senderId = senderId
        self.customerId = customerId
        self.method = 'HTTP'
        self.xmlHandler = XMLHandler()

        self.testURL = 'https://connect.copaco.com/xmlorder-test'
        self.URL = 'https://connect.copaco.com/xmlorder'
    
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
        ''' 
            Takes an Order object, generates XML file and sends the file to Copaco
            Deletes the file in the temp folder afterwards to save space
            Returns True if HTTP 200 is received, raises FailedRequest with response content otherwise
        '''
        
        json = order.getJSON()
        xml = self.xmlHandler.parseJSON(json)

        filePath = self.xmlHandler.writeToFile('test.xml', xml)
        with open(filePath, 'rb') as f: data = f.read()
        removeFile(filePath)

        response = requests.post(self.testURL, data=data)
        if response.status_code == 200: return True
        else: raise FailedRequest(response.content)