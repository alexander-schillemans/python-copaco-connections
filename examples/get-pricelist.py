from copaco.connection import CopacoConnectionBE

HOST = 'ftp.copaco.com'
LOGIN = 'XXXX'
PASSWD = 'XXXX'

conn = CopacoConnectionBE(HOST, LOGIN, PASSWD)

priceList = conn.priceList.get()
for item in priceList:
  formattedStr = '{description} - {number} - € {price}'.format(description=item.description, number=item.article, price=item.priceWithLevies)
  print(formattedStr)