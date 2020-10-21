# SeedCup2020


### 环境配置
- 此处选择使用WSL(`Windows SubSystem for Linux`)
  - 本人是安装 `docker` 自动装的wsl
  - 可以参考 [这个](https://docs.microsoft.com/en-us/windows/wsl/install-win10) 
    - 装完`wsl`之后，在应用商城下载`ubuntu20.04`
    - 打开`ubuntu20.04` 配置信息
  - 如何使用？：
    - (目标文件夹)在目标文件夹内(`shift`+右键)打开`powershell` ，输入`wsl -d ubuntu-20.04`
    - (家目录)左下角放大镜找ubuntu点一下

- 开启客户端
  - 在`subg.client`所在的文件夹内下terminal输入
  ```bash
  ./subg.client --seed=2020 --port=23333
  ```
  - 记得python文件中每次连接前都要重启一下客户端
    - 否则容易出现`socket.recv()`的阻塞

- 手动玩蛇
  - 详见赛题 pdf(调用`socket`来完成)
  - 或者查看 trial 文件

