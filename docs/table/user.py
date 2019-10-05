import pytablewriter

writer = pytablewriter.RstGridTableWriter()
# writer.table_name = "params list"
writer.headers = ["name", "type", "e.g.", "is_necessary"]
writer.value_matrix = [
    ["mobile", "string", "15522229999", True],
    ["password", "string", "password123*", True],
    ["username", "string", "user_name", False],
    ["nick_name", "string", "nick_name", False],
    ["avatar_url", "string", "15522229999", False],
    ["whats_up", "string", "whats_up", False],
]

with open("./docs/table/user.rst", "w") as f:
    writer.stream = f
    writer.write_table()
