# XZZ
小智障,一个拓展 go-cqhttp ,快速构建命令式 QQ 机器人的框架.

## 如何使用

> 阅读完以下内容后可以参考我的 blog -> [部署一个自己的智障机器人](https://blog.sakuya.love/archives/xzz/)
> 其中 go-cqhttp 配置文件部分格式可能有点过时，但是不影响理解🙈

### 安装配置

#### 0.自己安装配置好 go-cqhttp.

`XZZ` 需要的配置有

- 相对应的上报地址与 `go-cqhttp` api 地址
- 上报消息类型为 `array`
- 上报消息过滤为以下条件

```json
{
    "message_type": "group",
    "raw_message":{
        ".regex":"^\/"
    },
    "user_id":{
        ".neq": 80000000
    }
}
```

#### 1.clone 本仓库, 填写 `config.py`

其中 `APIURL` 为 go-cqhttp 的 api 地址, `AUTHORIZATION` 为 go-cqhttp 的 `access_token`, `PORT` 和 go-cqhttp 反向 http post 设置的端口保持一致.

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