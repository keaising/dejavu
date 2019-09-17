from tornado.util import ObjectDict
from tornado.web import RequestHandler


class NoResultError(Exception):
    pass


class BaseHandler(RequestHandler):
    def row_to_obj(self, row, cur):
        """Convert a SQL row to an object supporting dict
        and attribute access.
        """
        obj = ObjectDict()
        for val, desc in zip(row, cur.description):
            obj[desc.name] = val
        return obj

    async def execute(self, stmt, *args):
        """Execute a SQL statement.
        Must be called with ``await self.execute(...)``
        """
        with (await self.application.db.cursor()) as cur:
            await cur.execute(stmt, args)

    async def query(self, stmt, *args):
        """Query for a list of results.
        Typical usage::
            results = await self.query(...)
        Or::
            for row in await self.query(...)
        """
        with (await self.application.db.cursor()) as cur:
            await cur.execute(stmt, args)
            return [self.row_to_obj(row, cur) for row in await cur.fetchall()]

    async def queryone(self, stmt, *args):
        """Query for exactly one result.
        Raises NoResultError if there are no results, or ValueError if
        there are more than one.
        """
        results = await self.query(stmt, *args)
        if len(results) == 0:
            raise NoResultError()
        elif len(results) > 1:
            raise ValueError("Expected 1 result, got %d" % len(results))
        return results[0]

    async def prepare(self):
        # get_current_user cannot be a coroutine, so set
        # self.current_user in prepare instead.
        user_id = self.get_secure_cookie("honnya")
        if user_id:
            self.current_user = await self.queryone(
                "SELECT * FROM users WHERE id = %s", user_id
            )
