KuxunHotelAppTest
=================
说明
---
1. 采用python+appium
2. 对UI和部分逻辑进行测试
3. testcase使用编号进行区分
4. 主要使用xpath的方式进行元素定位
5. 运行该脚本需要Android version >= 4.2
6. setup time.sleep(5)
7. 使用test suite 让用例逐条执行
8. 为用例添加编号是为了让用例按照顺序执行，不然unittest 会按照字母排列顺序进行执行

首页
----
### 页面说明
1. 首页包括HorizontalScrollView和ListView两个层
2. 首页在HorizontalScrollView层里面
3. 设置在ListView层里面
4. 由于关键字suggestion功能缺失，该处测试脚本未完成
5. 价格筛选视图暂时没有代码可以解决
6. 入住离店日期暂时无法测试，无法获得日期选择页面的UI

### 脚本说明
1. config.py 存放简化xpath的字典 dic = {'简化的xpath':'xpath（//android.widget.TextView）'}
2. getElement.py 存放获得各种元素的函数
3. HotelMain.py 首页UI测试脚本，17 testcase

### 首页元素index
1. buttonListMain（首页按钮列表）：setting:0 tel:2 near:3 city:4 date:5 keyword:6 price:7
2. button 有 text 属性

选择城市页面
----
###页面说明
城市搜索由于框架问题，暂时不支持汉字，只能使用拼音

### 脚本说明
1. 搜索框使用send_keys发送关键字
2. 预定义了几个会出现的关键字，后期会根据接口内容随机进行抽取测试
3. 使用try catch 避免 //android.widget.RelativeLayout[0] 后面无 android.widget.TextView元素导致运行错误的情况


酒店列表页
---
### 说明
1. 城市团购酒店的textView index 为 2??todo
2. textView[1].click 可以进入团购页面
3. 需要跟研发确认 HotelListActivity 前三个textView的层级关系






