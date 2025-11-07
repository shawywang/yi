## 安装：

    同文：https://github.com/osfans/trime/releases/tag/nightly
    1.安卓手机内存8G及以上的下载安装arm64-v8a的apk
    2.安装好后，进入手机内部储存中rime/目录，删掉所有内容
    3.将此代码仓全部内容放进去，重命名包含"【同文】"的文件名，如"default【同文】.custom.yaml"重命名为"default.custom.yaml"
    4.进入同文app，右上角部署，选择方案为"逸码V20"，主题为"逸码助记皮肤"即可正常使用。
    5.如果助记皮肤有问题：同文app右上角关于，查看RIME版本，是否和"逸码助记皮肤.trime.yaml"中第2行一致

    小狼毫、鼠须管：
	1.官网安装Squirrel-0.16.1.pkg（macOS11 bigsur最高支持的版本）、weasel-0.17.4.0-installer.exe
		C:\Program Files\Rime\weasel-0.17.4
		/Library/Input Methods
	2.用户设定，打开文件夹，删除其中所有文件，将代码仓yi的所有放入其中
		C:\Users\wangxiao\AppData\Roaming\Rime
		/Users/wangxiao/Library/Rime（command+shift+g进）
	3.文件名有【小狼毫】【鼠须管】字样的文件，删掉对应平台的
	4.重新部署
	mac注：鼠须管是按ctrl+~，切换方案，注意此快捷键和pinpix截图工具冲突，配置-快捷键/动作-切换贴图组，叉掉；
	设置皮肤，编辑squirrel.custom.yaml，如加入：style/color_scheme: mac_green

## 同文皮肤：
    1.安装仓库内的98WB-U.otf、98WB-V.otf
    2.执行 字根画键.py

## 链接：

〔方案選單〕
逸码官网：
https://yb6b.github.io/yima/
https://gitee.com/peng52050/chen_yi
https://github.com/Peng52050/yima
顶功集萃：https://ding.tansongchen.com/tutorial/collection/second/lxsy
知乎：https://www.zhihu.com/question/376022178/answer/3165035735
安装字根字体：http://98wb.ysepan.com/，其中98WB-V.otf可覆盖100%的逸码字根，必装
天珩全字库：http://cheonhyeong.com/Simplified/download.html
主题文件：https://github.com/osfans/trime/wiki/trime.yaml#trime-default-style-settings

## 用户文件夹介绍：

```yaml
#build/*，内容可以删，重新部署自动生成
#  *.userdb/*，方案产生的数据，内容可以删，重新部署自动生成
#default.custom.yaml：
#----------
customization:
distribution_code_name: Weasel
distribution_version: 0.17.4
generator: "Rime::SwitcherSettings"
modified_time: "Sun Aug 10 14:54:22 2025"
rime_version: 1.13.1
patch:
schema_list:
  - { schema: luna_quanpin }
#  installation.yaml：
#  ----------
distribution_code_name: Weasel
distribution_name: "小狼毫"
distribution_version: 0.17.4
install_time: "Fri Jun 13 00:31:32 2025"
installation_id: "3c5bfd5d-d77b-466b-ab73-f853198bcd39"
rime_version: 1.13.1
#  user.yaml：
#  ----------
var:
last_build_time: 1754808871
#  weasel.custom.yaml：可以删，自动生成
#  -------------
customization:
distribution_code_name: Weasel
distribution_version: 0.17.4
generator: "Weasel::UIStyleSettings"
modified_time: "Fri Jun 13 00:31:32 2025"
rime_version: 1.13.1
patch:
"style/color_scheme": youtube

#  程序入口：dafault.yaml：schema_list会引导去读对应的schema.yaml
#  方案依赖关系：
#  逸 -> pinyin_simp、radical_pinyin部首拼音 -> stroke（应该是五笔画）
#  词典：dict.yaml
#  symbols.yaml、punctuation.yaml系统推荐的
#  build/*、方案.userdb/* 的内容为自动生成的，可以都删掉，重新部署就有了
#  opencc/*，反查提示拆字
```

QQ 小群：790835977（码云上的不一定是最新的，还是进群找吧！！）
群文件最新码表：逸码单字-rime(内置同文助记皮肤).zip
