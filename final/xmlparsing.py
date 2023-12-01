from lxml import etree

books_elements = etree.parse("test.xml")
# print(etree.tostring(books_elements))
books = books_elements.findall("book")
for book in books:
    # print(book.attrib) # dictionary of size one
    print(book.find("author").text)
    att = book.attrib
    book_id = att.get("id")
    print(book_id)

