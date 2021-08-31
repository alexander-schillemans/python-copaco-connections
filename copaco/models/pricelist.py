from .base import BaseModel

class PriceList(BaseModel):

    def __init__(self,
        items=None
    ):
        self.items = items if items else []
    
    def add(self, item):
        self.items.append(item)

class PriceListItem(BaseModel):
    
    def __init__(self,
        article=None,
        vendorCode=None,
        description=None,
        price=None,
        priceWithLevies=None,
        stock=None,
        hierarchy=None,
        unspscCode=None,
        EAN=None,
        status=None,
        auvibel=None,
        reprobel=None,
        recupel=None,
        bebat=None
    ):
        super().__init__()

        self.article = article
        self.vendorCode = vendorCode
        self.description = description
        self.price = price
        self.priceWithLevies = priceWithLevies
        self.stock = stock
        self.hierarchy = hierarchy
        self.unspscCode = unspscCode
        self.EAN = EAN
        self.status = status
        self.auvibel = auvibel
        self.reprobel = reprobel
        self.recupel = recupel
        self.bebat = bebat