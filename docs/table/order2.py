import pytablewriter

writer = pytablewriter.RstGridTableWriter()
# writer.table_name = "params list"
writer.headers = ["name", "type", "e.g.", "is_necessary"]
writer.value_matrix = [
    ["order_id", "string", "beb5cd6e-aba4-4e78-8a3e-13c40d3ba438", True]
]

with open("./docs/table/order2.rst", "w") as f:
    writer.stream = f
    writer.write_table()
