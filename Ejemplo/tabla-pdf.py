import camelot
tabla = camelot.read_pdf('name.pdf', pages='1')
print (tabla)

tabla.export('foo.csv', f='csv',compress=True)
tabla[0].to_csv('foo.csv')

