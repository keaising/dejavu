收货地址/Address
=====================

添加收货地址
*********************

接口
+++++++++++++++++++++

/address/add

请求类型
+++++++++++++++++++++

POST

传入参数
+++++++++++++++++++++

.. table::

    +--------+------+-------------+------------+
    |  name  | type |    e.g.     |is_necessary|
    +========+======+=============+============+
    |province|string|四川省       |True        |
    +--------+------+-------------+------------+
    |city    |string|成都市       |True        |
    +--------+------+-------------+------------+
    |town    |string|锦江区       |True        |
    +--------+------+-------------+------------+
    |detail  |string|武侯大道233号|True        |
    +--------+------+-------------+------------+



返回值
+++++++++++++++++++++

.. code:: json

    {
        "code": 200,
        "msg": "success",
        "data": null
    }

失败：

.. code:: json

    {
        "code": 400,
        "msg": "这里会有具体的失败原因",
        "data": null
    }