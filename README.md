KuxunHotelAppTest
=================
说明
---
1. 采用python+appium
2. 对UI和部分逻辑进行测试
3. testcase使用编号进行区分
4. 主要使用xpath的方式进行元素定位

首页
----
### 页面说明
1. 首页包括HorizontalScrollView和ListView两个层
2. 首页在HorizontalScrollView层里面
3. 设置在ListView层里面
4. 由于关键字suggestion功能缺失，该处测试脚本未完成
5. 价格筛选视图暂时没有代码可以解决

### 脚本说明
1. config.py 存放简化xpath的字典 dic = {'简化的xpath':'xpath（//android.widget.TextView）'}
2. getElement.py 存放获得各种元素的函数
3. HotelMain.py 首页UI测试脚本，15 testcase

### 首页元素index
1. buttonListMain（首页按钮列表）：setting:0 tel:2 near:3 city:4 date:5 keyword:6 price:7
2. buttonListMain[2] is nil----还未与研发沟通，为什么存在一个空的按钮
3. button 有 text 属性

选择城市页面
----
###页面说明
城市搜索由于框架问题，暂时不支持汉字，只能使用拼音这种方式

### 脚本说明
1. 搜索框使用send_keys发送关键字




