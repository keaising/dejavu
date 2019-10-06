import pytablewriter

writer = pytablewriter.RstGridTableWriter()
# writer.table_name = "params list"
writer.headers = ["name", "type", "e.g.", "is_necessary"]
writer.value_matrix = [
    ["address_id", "string", "15522229999", True],
    ["fee", "string", "password123*", True],
    ["book_id_price", "string", "id1:price1,id2:price2,id3:price3", True],
]

with open("./docs/table/order.rst", "w") as f:
    writer.stream = f
    writer.write_table()
