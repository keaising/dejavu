
图书/Book
=====================

根据类型查询列表
*********************

接口
+++++++++++++++++++++

/book/get_by_category

请求类型
+++++++++++++++++++++

POST

传入参数
+++++++++++++++++++++

.. table::

    +----------+-------+------------+------------+
    |   name   | type  |    e.g.    |is_necessary|
    +==========+=======+============+============+
    |category  |string | story      |True        |
    +----------+-------+------------+------------+


返回值
+++++++++++++++++++++

.. code:: json

    {
        "code": 200,
        "msg": "success",
        "data": [
            {
                "id": 1,
                "name": "SSH, The Secure Shell",
                "author": "Daniel J. Barrett",
                "price": 44.99,
                "surface_url": "",
                "press": "O'Reilly Media",
                "introduction": "Are you serious about network security? ",
                "toc": "Chapter 1 Introduction to SSH",
                "category": "ssh"
            }
        ]
    }

失败：

.. code:: json

    {
        "code": 400,
        "msg": "这里会有具体的失败原因",
        "data": null
    }


根据图书ID查询单本图书
******************************************

接口
+++++++++++++++++++++

/book/get_by_id

请求类型
+++++++++++++++++++++

POST

传入参数
+++++++++++++++++++++

.. table::

    +----------+-------+------------+------------+
    |   name   | type  |    e.g.    |is_necessary|
    +==========+=======+============+============+
    |book_id   |string | 233        |True        |
    +----------+-------+------------+------------+


返回值
+++++++++++++++++++++

.. code:: json

    {
        "code": 200,
        "msg": "success",
        "data": {
            "id": 1,
            "name": "SSH, The Secure Shell",
            "author": "Daniel J. Barrett",
            "price": 44.99,
            "surface_url": "",
            "press": "O'Reilly Media",
            "introduction": "Are you serious about network security? ",
            "toc": "Chapter 1 Introduction to SSH",
            "category": "ssh"
        }
    }

失败：

.. code:: json

    {
        "code": 400,
        "msg": "这里会有具体的失败原因",
        "data": null
    }
