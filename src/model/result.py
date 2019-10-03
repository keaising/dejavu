class Result:
    def __init__(self, data, code=200, msg=""):
        self.data = data
        self.code = code
        self.msg = msg

    @classmethod
    def error(cls, msg):
        return Result(None, 400, msg)

    @classmethod
    def success(cls, data):
        return Result(data)
