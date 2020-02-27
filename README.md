# XZZ
小智障,一个拓展 CoolQ HttpApi,快速构建命令式 QQ 机器人的框架.

## 如何使用

### 安装配置

#### 0.自己安装配置好 CoolQ 及其 HttpApi 插件.

包括上报过滤！

#### 1.clone 本仓库, 填写 `config.py`

其中 `APIURL` 为 CoolQ HttpApi 的 URL, `AUTHORIZATION` 为 CoolQ HttpApi 的 `access_token`, `PORT` 和 CoolQ HttpApi  `post_url` 中的端口保持一致.

#### 2.安装依赖, 启动服务

```shell
pip install -r req.txt
python main.py
```



### 拓展功能

在 `worker` 文件夹中添加 python 模块.文件名即受该文件响应的命令.

如果要响应 `/ping` 命令的话, 文件名应为 `ping.py`



在该模块实现一个 `Ans` 类, 此类继承自 `zzcore`里的 `StdAns` 类.

在这个类中你可选的重写以下属性和方法：

`AllowGroup` ,  int 类型的 list, 在此 list 中的群组可以执行此命令.默认为 [], 全部允许.

`AllowUser` ,  int 类型的 list, 在此 list 中的QQ号可以执行此命令.默认为 [], 全部允许.

`AllowRole` ,  string 类型的 list, 在此 list 中的角色可以执行此命令.默认为 [], 全部允许, 可选值为 owner、admin、member , 对应 群主、管理员、群员 三种角色.

`GroupNotAllow`、`UserNotAllow`、`RoleNotAllow` 三个字符串, 分别为当用户因为以上三个原因被拒绝使用本命令时的回复, 自己去看默认值吧..

`GETMSG()` 方法, 该方法应当返回一个字符串, 在此方法中你可以借助以下变量：

`self.uid `发起命令的用户的 QQ , int 类型

`self.gid` 发起命令的群组的群号, int 类型

`self.role` 发起命令的用户的角色,可能值 'owner'、'admin'、'member'

`self.parms` 命令详情, string 类型的 list. 看例子

如果用户发送了 /ping xxx 12

那么 self.parms 为 ['ping', 'xxx', '12']

self.raw_msg 详见 example.json