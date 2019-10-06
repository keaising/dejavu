# De Javu

The homework from dejavu.

I've seen this before.

[![Build Status](https://travis-ci.org/keaising/dejavu.svg?branch=master)](https://travis-ci.org/keaising/dejavu)  ![](https://github.com/keaising/dejavu/workflows/dejavu/badge.svg)

---------------------------------------

## 项目文档

文档地址：[shuxiao.wang/dejavu](https://shuxiao.wang/dejavu)

文档中包含以下内容：

+ 本项目的开发情况
+ 产品需求实现
+ 技术方案使用
+ 项目亮点
+ 待改进的内容和不足
+ 未来展望

总需求 实现书店系统必要的 API

#### 产品需求
1. 用户信息添加获取：

    + 通过手机号密码注册和登录
    + 查看个人信息，购买历史，余额等
    + 可以充值余额，实现一个假的就好

2. 用户可以查看图书信息：

    + 获取图书列表，展示书名，作者，价格等
    + 获取图书详情，除展示列表中已有信息之外，还需要简介，目录等

3. 用户可以购买图书：

    + 把书放入购物车，可以从购物车删除
    + 从购物车中的部分或全部图书生成订单
    + 填写收货地址，使用余额支付订单
    + 订单可以取消

#### 技术需求

1. 使用 Tornado 作为应用框架, SQLAlchemy 作为 ORM

2. 使用 Python 3，符合 PEP-8

3. 接口文档，遵循 RESTful

4. 带有单元测试/集成测试

5. 总代码量不用太多，使用 Git 管理

6. 做好依赖管理

