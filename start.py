"""
   @File        :    更改下载的ad广告规则for Quantumultx.py
   Description  :
   Author       :    laoyahoo
   @Time        :    2022/7/5 11:24
   @Software    :    PyCharm
"""
import urllib.request
import time, os, ssl
from urllib.request import urlretrieve

#path_url = os.path.abspath('.')  # 相对路径,可以 ..
path_url = "/Users/super/PycharmProjects/Review/List"  # 存放下载文件的目录

class Download_IPCIDR(object):
    """
    Quantumultx
    """

    def get_url(self, download_url):

        # 二进制读取url
        self.url = r"{}".format(download_url)
        # 打开url
        self.page = urllib.request.urlopen(self.url)
        # 读取内容
        self.html = self.page.read().decode("utf-8")
        # 截取url最后的名称，用于多个文件下载保存
        self.filename = download_url.split("/")[-1]

    def download_file(self, download_url, fork_file_path):
        # 执行下载数据的函数
        self.get_url(download_url)

        # 拼接文件保存路径
        self.someone_path = os.path.join(fork_file_path, self.filename)

        # 下载url数据且写入存放文件内
        with open(self.someone_path, mode="w", encoding="utf-8") as f:
            f.write(self.html)

            # 判断文件是否为空
            anti_size = os.path.getsize(fork_file_path)
            # 数据转化成整数
            int_anti = int(anti_size)
            if int_anti < 90:  # 如果数据没有100字节，则退出
                exit(1)

    def urlSet(self):
        # 文件存放上级目录
        #fork_file_path = os.path.join(path_url, "fork", "Surge")
        fork_file_path = path_url
        # 多个数据下载源
        dicts = {
            "anti-ad-surge": "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge.txt",
            "Advertising":"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/release/rule/QuantumultX/Advertising/Advertising.list",
            "SystemOTA":"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/release/rule/QuantumultX/SystemOTA/SystemOTA.list",
            "Apple":"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/release/rule/QuantumultX/Apple/Apple.list",
            "Proxy":"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/release/rule/QuantumultX/Proxy/Proxy.list",
            "Microsoft":"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/release/rule/QuantumultX/Microsoft/Microsoft.list",
            "China":"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/release/rule/QuantumultX/China/China.list",
            "Privacy":"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Privacy/Privacy.list",
            "Hijacking":"https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/release/rule/QuantumultX/Hijacking/Hijacking.list"
        }
        # 循环字典下载每条数据
        for dict in dicts.items():
            # print(dict)
            time.sleep(0.5)
            if dict[1]:
                self.download_file(dict[1], fork_file_path)


    def antiAd(self):
        # 原始下载的数据
        old_path_url = os.path.join(path_url, "anti-ad-surge.txt")
        # 更改后的数据
        new_path_url = os.path.join(path_url,"AntiadQx.list")

        temp_host = os.path.join(path_url,"AntiadQxhost.list")
        temp_suffx = os.path.join(path_url, "AntiadQxsuffx.list")

        if os.path.exists(new_path_url):  # 如果文件存在则删除，第一次没有文件，后面每次更新都有
            os.remove(new_path_url)  # 删除文件

        if os.path.exists(temp_host):  # 如果文件存在则删除，第一次没有文件，后面每次更新都有
            os.remove(temp_host)  # 删除文件

        if os.path.exists(temp_suffx):  # 如果文件存在则删除，第一次没有文件，后面每次更新都有
            os.remove(temp_suffx)  # 删除文件

        with open(old_path_url, mode="r", encoding="utf-8") as f:
            for line in f.readlines():
                with open(temp_suffx, mode="a+", encoding="utf-8") as new_f:
                    if "#" not in line: # 不要注释写入
                        line_sum = line.split(".")
                        if len(line_sum) < 3:  # 如果切割的是域名后缀，用len长度判断是否主机名还是后缀域名
                            str_e = line.replace("DOMAIN-SUFFIX","HOST-SUFFIX")
                            new_str = str_e.replace("\n",",REJECT") # 把换行符替换成 ,DIRECT
                            new_f.write(new_str+"\n") # 写入的时候需要写入换行符
                        else:
                            with open(temp_host, mode="a+", encoding="utf-8") as new_f:
                                str_e = line.replace("DOMAIN-SUFFIX", "HOST")
                                new_str = str_e.replace("\n", ",REJECT")  # 把换行符替换成 ,DIRECT
                                new_f.write(new_str + "\n")  # 写入的时候需要写入换行符

        # 把两个文件合并成一个
        with open(temp_host, mode="a+", encoding="utf-8") as host_f:
            with open(temp_suffx, mode="r", encoding="utf-8") as host_suffx:
                for line in host_suffx:
                    host_f.write(line)

        # 重命名文件
        os.rename(temp_host,new_path_url)

        # 删除文件
        os.remove(temp_suffx)


    def Advertising(self):
        # 原始下载的数据
        old_path_url = os.path.join(path_url, "Advertising.list")
        # 更改后的数据
        new_path_url = os.path.join(path_url,"AdvertisingQx.list")

        if os.path.exists(new_path_url):  # 如果文件存在则删除，第一次没有文件，后面每次更新都有
            os.remove(new_path_url)  # 删除文件

        with open(old_path_url, mode="r", encoding="utf-8") as f:
            for line in f.readlines():
                with open(new_path_url, mode="a+", encoding="utf-8") as new_f:
                    str_e = line.replace("Advertising","REJECT")
                    #new_str = str_e.replace("\n",",REJECT") # 把换行符替换成 ,DIRECT
                    new_f.write(str_e) # 写入的时候需要写入换行符

    def SystemOTA(self):
        # 原始下载的数据
        old_path_url = os.path.join(path_url, "SystemOTA.list")
        # 更改后的数据
        new_path_url = os.path.join(path_url,"SystemOTAQx.list")

        if os.path.exists(new_path_url):  # 如果文件存在则删除，第一次没有文件，后面每次更新都有
            os.remove(new_path_url)  # 删除文件

        with open(old_path_url, mode="r", encoding="utf-8") as f:
            for line in f.readlines():
                with open(new_path_url, mode="a+", encoding="utf-8") as new_f:
                    str_e = line.replace("SystemOTA","REJECT")
                    #new_str = str_e.replace("\n",",REJECT") # 把换行符替换成 ,DIRECT
                    new_f.write(str_e) # 写入的时候需要写入换行符

    def Apple(self):
        # 原始下载的数据
        old_path_url = os.path.join(path_url, "Apple.list")
        # 更改后的数据
        new_path_url = os.path.join(path_url, "AppleQx.list")

        if os.path.exists(new_path_url):  # 如果文件存在则删除，第一次没有文件，后面每次更新都有
            os.remove(new_path_url)  # 删除文件

        with open(old_path_url, mode="r", encoding="utf-8") as f:
            for line in f.readlines():
                with open(new_path_url, mode="a+", encoding="utf-8") as new_f:
                    str_e = line.replace("Apple", "DIRECT")
                    # new_str = str_e.replace("\n",",REJECT") # 把换行符替换成 ,DIRECT
                    new_f.write(str_e)  # 写入的时候需要写入换行符

    def Proxy(self):
        # 原始下载的数据
        old_path_url = os.path.join(path_url, "Proxy.list")
        # 更改后的数据
        new_path_url = os.path.join(path_url, "ProxyQx.list")

        if os.path.exists(new_path_url):  # 如果文件存在则删除，第一次没有文件，后面每次更新都有
            os.remove(new_path_url)  # 删除文件

        with open(old_path_url, mode="r", encoding="utf-8") as f:
            for line in f.readlines():
                with open(new_path_url, mode="a+", encoding="utf-8") as new_f:
                    str_e = line.replace("Proxy", "Proxy")
                    # new_str = str_e.replace("\n",",REJECT") # 把换行符替换成 ,DIRECT
                    new_f.write(str_e)  # 写入的时候需要写入换行符


    def Microsoft(self):
        # 原始下载的数据
        old_path_url = os.path.join(path_url, "Microsoft.list")
        # 更改后的数据
        new_path_url = os.path.join(path_url, "MicrosoftQx.list")

        if os.path.exists(new_path_url):  # 如果文件存在则删除，第一次没有文件，后面每次更新都有
            os.remove(new_path_url)  # 删除文件

        with open(old_path_url, mode="r", encoding="utf-8") as f:
            for line in f.readlines():
                with open(new_path_url, mode="a+", encoding="utf-8") as new_f:
                    str_e = line.replace("Microsoft", "DIRECT")
                    # new_str = str_e.replace("\n",",REJECT") # 把换行符替换成 ,DIRECT
                    new_f.write(str_e)  # 写入的时候需要写入换行符


    def China(self):
        # 原始下载的数据
        old_path_url = os.path.join(path_url, "China.list")
        # 更改后的数据
        new_path_url = os.path.join(path_url, "ChinaQx.list")

        if os.path.exists(new_path_url):  # 如果文件存在则删除，第一次没有文件，后面每次更新都有
            os.remove(new_path_url)  # 删除文件

        with open(old_path_url, mode="r", encoding="utf-8") as f:
            for line in f.readlines():
                with open(new_path_url, mode="a+", encoding="utf-8") as new_f:
                    str_e = line.replace("China", "DIRECT")
                    # new_str = str_e.replace("\n",",REJECT") # 把换行符替换成 ,DIRECT
                    new_f.write(str_e)  # 写入的时候需要写入换行符

    def Privacy(self):
        # 原始下载的数据
        old_path_url = os.path.join(path_url, "Privacy.list")
        # 更改后的数据
        new_path_url = os.path.join(path_url, "PrivacyQx.list")

        if os.path.exists(new_path_url):  # 如果文件存在则删除，第一次没有文件，后面每次更新都有
            os.remove(new_path_url)  # 删除文件

        with open(old_path_url, mode="r", encoding="utf-8") as f:
            for line in f.readlines():
                with open(new_path_url, mode="a+", encoding="utf-8") as new_f:
                    str_e = line.replace("Privacy", "REJECT")
                    # new_str = str_e.replace("\n",",REJECT") # 把换行符替换成 ,DIRECT
                    new_f.write(str_e)  # 写入的时候需要写入换行符

    def Hijacking(self):
        # 原始下载的数据
        old_path_url = os.path.join(path_url, "Hijacking.list")
        # 更改后的数据
        new_path_url = os.path.join(path_url, "HijackingQx.list")

        if os.path.exists(new_path_url):  # 如果文件存在则删除，第一次没有文件，后面每次更新都有
            os.remove(new_path_url)  # 删除文件

        with open(old_path_url, mode="r", encoding="utf-8") as f:
            for line in f.readlines():
                with open(new_path_url, mode="a+", encoding="utf-8") as new_f:
                    str_e = line.replace("Hijacking", "REJECT")
                    # new_str = str_e.replace("\n",",REJECT") # 把换行符替换成 ,DIRECT
                    new_f.write(str_e)  # 写入的时候需要写入换行符

Download_IPCIDR().urlSet()
Download_IPCIDR().antiAd()
Download_IPCIDR().Advertising()
Download_IPCIDR().SystemOTA()
Download_IPCIDR().Apple()
Download_IPCIDR().Proxy()
#Download_IPCIDR().SystemOTA()
Download_IPCIDR().China()
Download_IPCIDR().Microsoft()
Download_IPCIDR().Privacy()
Download_IPCIDR().Hijacking()