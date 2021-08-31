from .base import ConnectionType

from copaco.utils import getFile
from copaco.constants.mappings import PRICELISTITEM_MAPPINGS
from copaco.models.pricelist import PriceListItem, PriceList

class PriceListType(ConnectionType):

    def __init__(self, connection):
        super().__init__(connection)
    
    def get(self):
        """
            Retrieves the pricelist from the Copaco FTP server and creates objects for each row in the list.
            Looks at the mapping to determine which column in the file maps to which attribute on the object.
            Returns a PriceList object that contains a list of PriceListItem objects.
        """

        externalPath = '{login}/Out/CopacoBE_prijslijst_{loginNoBE}.csv'.format(login=self.connection.login, loginNoBE=self.connection.login.replace('BE', ''))
        internalPath = self.connection.ftpHandler.retrFile(externalPath)

        pdFile = getFile(internalPath)

        priceList = PriceList()

        for index, row in pdFile.iterrows():
            item = PriceListItem()

            for mAttr, mValues in PRICELISTITEM_MAPPINGS.items():

                for value in mValues:
                    if value in row: setattr(item, mAttr, row[value])
            
            priceList.add(item)
        
        return priceList