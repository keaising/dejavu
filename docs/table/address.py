import pytablewriter

writer = pytablewriter.RstGridTableWriter()
# writer.table_name = "params list"
writer.headers = ["name", "type", "e.g.", "is_necessary"]
writer.value_matrix = [
    ["province", "string", "四川省", True],
    ["city", "string", "成都市", True],
    ["town", "string", "锦江区", False],
    ["detail", "string", "武侯大道233号", False],
]

with open("./docs/table/address.rst", "w") as f:
    writer.stream = f
    writer.write_table()
