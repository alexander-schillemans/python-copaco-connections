import datetime

from .base import BaseResponse
from copaco.constants.mappings import RESP_ATP_MAPPINGS, RESP_CODE_MAPPINGS

# INT
class OrderResponse(BaseResponse):
    
    def __init__(self,
        supplier=None,
        customer=None,
        customer_ordernumber=None,
        external_document_id=None,
        sequencenumber=None,
        document_source=None,
        responsecode=None,
        ordernumber=None
    ):

        self.supplier = supplier
        self.customer = customer
        self.customer_ordernumber = customer_ordernumber
        self.external_document_id = external_document_id
        self.sequencenumber = sequencenumber
        self.document_source = document_source
        self.responsecode = responsecode
        self.ordernumber = ordernumber

        self.beingProcessed = False
        self.error = None
    
    def parseJSON(self, json):
        self = super().parseJSON(json)

        if self.responsecode == '0':
            self.beingProcessed = True
        else:
            self.error = RESP_CODE_MAPPINGS[self.responsecode]
        
        return self

# OBV
class OrderConfirmation(BaseResponse):

    def __init__(self,
        documentsource=None,
        external_document_id=None,
        supplier=None,
        document_date=None,
        orderheader=None,
        Customer=None,
        ShipTo=None,
        VAT=None,
        costs=None,
        orderline=None,
        ordertrailer=None
    ):

        self.documentsource = documentsource
        self.external_document_id = external_document_id
        self.supplier = supplier
        self.document_date = document_date
        self.orderheader = orderheader if orderheader else OrderHeader()
        self.Customer = Customer if Customer else CustomerObj()
        self.ShipTo = ShipTo if ShipTo else ShipToObj()
        self.VAT = VAT if VAT else []
        self.costs = costs if costs else []
        self.orderline = orderline if orderline else []
        self.ordertrailer = ordertrailer if ordertrailer else OrderTrailer()

class VATObj(BaseResponse):

    def __init__(self,
        percentage=None,
        amount=None,
        currency=None
    ):

        self.percentage = percentage
        self.amount = amount
        self.currency = currency

class Costs(BaseResponse):

    def __init__(self,
        sign=None,
        code=None,
        description=None,
        amount=None,
        currency=None
    ):

        self.sign = sign
        self.code = code
        self.description = description
        self.amount = amount
        self.currency = currency

class OrderHeader(BaseResponse):

    def __init__(self,
        customer_ordernumber=None,
        order_number=None,
        sequencenumber=None,
        status=None,
        testflag=None,
        orderdate=None,
        completedelivery=None,
        currency=None,
        terms_of_payment_text=None,
        incoterms_text=None,
        recipientsreference=None,
    ):

        self.customer_ordernumber = customer_ordernumber
        self.order_number = order_number
        self.sequencenumber = sequencenumber
        self.status = status
        self.testflag = testflag
        self.orderdate = orderdate
        self.completedelivery = completedelivery
        self.currency = currency
        self.terms_of_payment_text = terms_of_payment_text
        self.incoterms_text = incoterms_text
        self.recipientsreference = recipientsreference

class CustomerObj(BaseResponse):

    def __init__(self,
        customer_id=None,
        customercontact=None
    ):

        self.customer_id = customer_id
        self.customercontact = customercontact if customercontact else CustomerContact()

class OrderLine(BaseResponse):

    def __init__(self,
        linenumber=None,
        customer_linenumber=None,
        item_id=None,
        item_description=None,
        manufacturer_item_id=None,
        first_requested_deliverydate=None,
        price=None,
        line_amount=None,
        currency=None,
        quantity_ordered=None,
        schedulelines=None
    ):

        self.linenumber = linenumber
        self.customer_linenumber = customer_linenumber
        self.item_id = item_id
        self.item_description = item_description
        self.manufacturer_item_id = manufacturer_item_id
        self.first_requested_deliverydate = first_requested_deliverydate
        self.price = price
        self.line_amount = line_amount
        self.currency = currency
        self.quantity_ordered = quantity_ordered
        self.schedulelines = schedulelines if schedulelines else ScheduleLines()

class ScheduleLines(BaseResponse):

    def __init__(self,
        quantity=None,
        atp_code=None,
        atp_date=None
    ):

        self.quantity = quantity
        self.atp_code = atp_code
        self.atp_date = atp_date
        self.atp_readable = None
    
    def parseJSON(self, json):
        self = super().parseJSON(json)
        self.atp_readable = RESP_ATP_MAPPINGS[self.atp_code]
        self.atp_date = datetime.datetime.strptime(self.atp_date, '%Y%M%d').date()
        return self


class OrderTrailer(BaseResponse):

    def __init__(self,
        order_amount_ex_VAT=None,
        order_VAT_amount=None,
        order_amount_incl_VAT=None
    ):

        self.order_amount_ex_VAT = order_amount_ex_VAT
        self.order_VAT_amount = order_VAT_amount
        self.order_amount_incl_VAT = order_amount_incl_VAT

class CustomerContact(BaseResponse):

    def __init__(self,
        email=None,
        telephone=None,
        fax=None
    ):

        self.email = email
        self.telephone = telephone
        self.fax = fax

class ShipToObj(BaseResponse):

     def __init__(self,
        name1=None,
        name2=None,
        name3=None,
        name4=None,
        street=None,
        postalcode=None,
        city=None,
        country=None
    ):

        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.name4 = name4
        self.street = street
        self.postalcode = postalcode
        self.city = city
        self.country = country

# FAC
class Invoice(BaseResponse):

    def __init__(self,
        invoiceheader=None,
        InvoiceSender=None,
        BillTo=None,
        invoicecustomer=None,
        InvoicePayer=None,
        invoiceline=None
    ):

        self.invoiceheader = invoiceheader if invoiceheader else InvoiceHeader()
        self.InvoiceSender = InvoiceSender
        self.BillTo = BillTo
        self.invoicecustomer = invoicecustomer
        self.InvoicePayer = InvoicePayer
        self.invoiceline = invoiceline

class InvoiceHeader(BaseResponse):

    def __init__(self,
        documentsource=None,
        invoice_type=None,
        supplier=None,
        document_date=None,
        supplier_vat_number=None,
        koers=None,
        TermsOfPaymentCoded=None,
        TermsOfPaymentDays=None,
        TermsOfPaymentPercentage=None,
        invoice_number=None,
        invoice_date=None,
        invoice_expiration_date=None,
        invoice_currency=None,
        invoice_terms_of_payment_text=None,
        invoice_terms_of_delivery=None
    ):

        self.documentsource = documentsource
        self.invoice_type = invoice_type
        self.supplier = supplier
        self.document_date = document_date
        self.supplier_vat_number = supplier_vat_number
        self.koers = koers
        self.TermsOfPaymentCoded = TermsOfPaymentCoded
        self.TermsOfPaymentDays = TermsOfPaymentDays
        self.TermsOfPaymentPercentage = TermsOfPaymentPercentage
        self.invoice_number = invoice_number
        self.invoice_date = invoice_date
        self.invoice_expiration_date = invoice_expiration_date
        self.invoice_currency = invoice_currency
        self.invoice_terms_of_payment_text = invoice_terms_of_payment_text
        self.invoice_terms_of_delivery = invoice_terms_of_delivery