# -*- coding:utf-8 -*-
# @Time   :2020/12/15 15:50
# @Author :
# @File   :aaaa.py
# @Version：1.0


import random
import math
import time
import datetime
import string
import sys


sys.setdefaultencoding('utf-8')

class RandomUtil:
    # 1 姓氏（所有姓氏）
    NAME_XING = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                 '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
                 '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
                 '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
                 '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
                 '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                 '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闵', '席', '季', '麻', '强', '贾', '路', '娄', '危',
                 '江', '童', '颜', '郭', '梅', '盛', '林', '刁', '锺', '徐', '丘', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍',
                 '虞', '万', '支', '柯', '昝', '管', '卢', '莫', '经', '房', '裘', '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓',
                 '郁', '单', '杭', '洪', '包', '诸', '左', '石', '崔', '吉', '钮', '龚', '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁',
                 '荀', '羊', '於', '惠', '甄', '麹', '家', '封', '芮', '羿', '储', '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫',
                 '乌', '焦', '巴', '弓', '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬', '全', '郗', '班', '仰', '秋', '仲', '伊', '宫',
                 '甯', '仇', '栾', '暴', '甘', '钭', '厉', '戎', '祖', '武', '符', '刘', '景', '詹', '束', '龙', '叶', '幸', '司', '韶',
                 '郜', '黎', '蓟', '薄', '印', '宿', '白', '怀', '蒲', '邰', '从', '鄂', '索', '咸', '籍', '赖', '卓', '蔺', '屠', '蒙',
                 '池', '乔', '阴', '鬱', '胥', '能', '苍', '双', '闻', '莘', '党', '翟', '谭', '贡', '劳', '逄', '姬', '申', '扶', '堵',
                 '冉', '宰', '郦', '雍', '郤', '璩', '桑', '桂', '濮', '牛', '寿', '通', '边', '扈', '燕', '冀', '郏', '浦', '尚', '农',
                 '温', '别', '庄', '晏', '柴', '瞿', '阎', '充', '慕', '连', '茹', '习', '宦', '艾', '鱼', '容', '向', '古', '易', '慎',
                 '戈', '廖', '庾', '终', '暨', '居', '衡', '步', '都', '耿', '满', '弘', '匡', '国', '文', '寇', '广', '禄', '阙', '东',
                 '欧', '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂', '晁', '勾', '敖', '融', '冷', '訾', '辛', '阚',
                 '那', '简', '饶', '空', '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯', '相', '查', '后', '荆', '红',
                 '游', '竺', '权', '逯', '盖', '益', '桓', '公', '万俟', '司马', '上官', '欧阳', '夏侯', '诸葛', '闻人', '东方', '赫连', '皇甫',
                 '尉迟', '公羊', '澹台', '公冶', '宗政', '濮阳', '淳于', '单于', '太叔', '申屠', '公孙', '仲孙', '轩辕', '令狐', '锺离', '宇文',
                 '长孙', '慕容', '鲜于', '闾丘', '司徒', '司空', '亓官', '司寇', '仉', '督', '子车', '颛孙', '端木', '巫马', '公西', '漆雕', '乐正',
                 '壤驷', '公良', '拓跋', '夹谷', '宰父', '穀梁', '晋', '楚', '闫', '法', '汝', '鄢', '涂', '钦', '段干', '百里', '东郭', '南门',
                 '呼延', '归海', '羊舌', '微生', '岳', '帅', '缑', '亢', '况', '後', '有', '琴', '梁丘', '左丘', '东门', '西门', '商', '牟',
                 '佘', '佴', '伯', '赏', '南宫', '墨', '哈', '谯', '笪', '年', '爱', '阳', '佟', '第五', '言', '福']
    # 2 名字（这里只用几个名字 做演示即可）
    # 2.1 男孩名字
    NAME_BODY_MING = ['壮', '昱杰', '开虎', '凯信', '永斌', '方洲', '长发', '可人', '天弘', '炫锐', '富明', '俊枫']
    # 2.2 女孩名字
    NAME_GIRL_MING = ['小玉', '蓝', '琬郡', '琛青', '予舴', '妙妙', '梓茵', '海蓉', '语娜', '馨琦', '晓馥', '佳翊']


    """
    各身份前两位地址码
    """
    province_id = [11, 12, 13, 14, 15, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46,
                   50, 51, 52, 53, 54, 61, 62, 63, 65, 65, 81, 82, 83]

    def get_random_attribute(self,attribute_name):
        """
        从指定的list中获取随机值
        attribute_name表示对应的list名
        """
        attributestr = random.choice(attribute_name)
        return attributestr
    def get_random_attribute_many(self,attribute_name):
        """
        从指定的list中获取随机的n个值
        attribute_name表示对应的list名
        """
        n = random.randint(1,len(attribute_name))
        print(n)
        attributelist = random.sample(attribute_name,n)
        attributestr=",".join(attributelist)
        return attributestr


    def random_name_str(self, gender, is_two_xing=False):
        """
        生成随机姓名
        :param gender: 性别（男、女）
        :param is_two_xing: 姓是否是2个字的（默认是1一个字的姓）
        """
        # step1 生成姓
        xing = ''
        if is_two_xing:
            while True:
                xing_two = self.NAME_XING[random.randint(0, len(self.NAME_XING) - 1)]
                if len(xing_two) == 2:
                    xing = xing_two
                    break
        else:
            while True:
                xing_one = self.NAME_XING[random.randint(0, len(self.NAME_XING) - 1)]
                print (xing_one)
                if len(xing_one) == 1:
                    xing = xing_one
                    break

        # step2 生成名
        ming = ''
        if gender == '男':
            ming = self.NAME_BODY_MING[random.randint(0, len(self.NAME_BODY_MING) - 1)]
        elif gender == '女':
            ming = self.NAME_GIRL_MING[random.randint(0, len(self.NAME_GIRL_MING) - 1)]
        else:
            print('性别错误')

        return xing + ming

    def generate_random_gps(self,base_log, base_lat, radius):
        """
        生成gps

        """
        radius_in_degrees = radius / 111300
        u = float(random.uniform(0.0, 1.0))
        v = float(random.uniform(0.0, 1.0))
        w = radius_in_degrees * math.sqrt(u)
        t = 2 * math.pi * v
        x = w * math.cos(t)
        y = w * math.sin(t)
        longitude = y + base_log
        latitude = x + base_lat
        # 这里是想保留6位小数点
        loga = '%.6f' % longitude
        lata = '%.6f' % latitude
        aa='['+loga+','+lata+']'
        return aa

    # 随机生成出生日期
    def get_birthday(self,starttime=1960,endtime=2000):
        """
        生成随机出生日期
        :param starttime 开始时间，默认值为1960
        :param endtime 结束时间，默认值为2000
        """

        # 随机生成年月日
        year = random.randint(starttime, endtime)
        month = random.randint(1, 12)
        # 判断每个月有多少天随机生成日
        if year % 4 == 0:
            if month in (1, 3, 5, 7, 8, 10, 12):
                day = random.randint(1, 31)
            elif month in (4, 6, 9, 11):
                day = random.randint(1, 30)
            else:
                day = random.randint(1, 29)
        else:
            if month in (1, 3, 5, 7, 8, 10, 12):
                day = random.randint(1, 31)
            elif month in (4, 6, 9, 11):
                day = random.randint(1, 30)
            else:
                day = random.randint(1, 28)
        # 小于10的月份前面加0
        if month < 10:
            month = '0' + str(month)
        if day < 10:
            day = '0' + str(day)
        birthday = str(year) + str(month) + str(day)
        return birthday

    # 匿名函数
    # get_sex = lambda: random.choice(['男', '女'])

    # 随机生成身份证号
    province_id = [11, 12, 13, 14, 15, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46,
                   50, 51, 52, 53, 54, 61, 62, 63, 65, 65, 81, 82, 83]

    def get_idnum(self):
        """
        随机生成身份证号
        """
        id_num = ''
        # 随机选择地址码
        id_num += str(random.choice(self.province_id))
        # 随机生成4-6位地址码
        for i in range(4):
            ran_num = str(random.randint(0, 9))
            id_num += ran_num
        b = self.get_birthday()
        id_num += b
        # 生成15、16位顺序号
        num = ''
        for i in range(2):
            num += str(random.randint(0, 9))
        id_num += num
        # 通过性别判断生成第十七位数字 男单 女双
        # s = self.get_sex()
        s=lambda: random.choice(['男', '女'])
        print("性别:", s)
        if s == '男':
            # 生成奇数
            seventeen_num = random.randrange(1, 9, 2)
        else:
            seventeen_num = random.randrange(2, 9, 2)
        id_num += str(seventeen_num)
        eighteen_num = str(random.randint(1, 10))
        if eighteen_num == '10':
            eighteen_num = 'X'
        id_num += eighteen_num
        return id_num

    def get_time(self):
        """生成随机时间"""
        a1 = (2000, 1, 1, 0, 0, 0, 0, 0, 0)
        a2 = (2022, 12, 31, 23, 59, 59, 0, 0, 0)
        start = time.mktime(a1)
        end=time.mktime(a2)
        for i in range(10):
            t = random.randint(start, end)# 在开始和结束时间戳中随机取出一个
            date_touple = time.localtime(t)# 将时间戳生成时间元组
            date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串(1976-05-21)
        return date

    # 随机生成手机号
    def get_tel(self):
        """随机生成手机号"""
        phone_number=[139,138,137,136,135,134,159,158,15,150,151,152,188,
                130,131,132,156,155,133,153,189,199]
        tel = ''
        tel += str(random.choice(phone_number))
        ran = ''
        for i in range(8):
            ran += str(random.randint(0, 9))
        tel += ran
        return tel

    def get_chepaihao(self,strlen=6):
        """随机生成车牌号"""
        char0 = ['京','津','沪','渝','冀','豫','云','辽','黑','湘','皖','鲁','新','苏','浙','赣','鄂','桂','甘','晋','蒙','陕','吉','闽','赣','粤','青','藏','川','宁','琼']
        char1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
        char2 = '1234567890'
        len0 = len(char0) - 1
        len1 = len(char1) - 1
        len2 = len(char2) - 1
        code = ''
        index0 = random.randint(1, len0)
        index1 = random.randint(1, len1)
        #print char0[index0]
        code += char0[index0]
        code += char1[index1]
        for i in range(1, strlen):
            index2 = random.randint(1, len2)
            code += char2[index2]
        return code



    def get_timestamp(self,d=0,h=0,m=0,s=0):
        """获取n天前的时间戳
        第1个参数表示几天前，第2、3、4表示指定的时分秒
        无参表示当天的0点
        """
        now = datetime.datetime.now()
        timestr=now-datetime.timedelta(days=d,hours =now.hour-h,minutes=now.minute-m, seconds=now.second-s,microseconds=now.microsecond)
        ts = int(round(time.mktime(timestr.timetuple())*1000))
        return ts
    def get_timestampByday(self,t):
        """获取指定日期的时间戳
        入参格式：2019-5-10 23:40:00
        """
        ts = int(round(time.mktime(time.strptime(t,"%Y-%m-%d %H:%M:%S"))*1000))
        return ts
    def get_timestr1(self,d=0,h=0,m=0,s=0):
        """获取n天前的时间，时间格式为2022-03-07T09:44:26
        第1个参数表示几天前，第2、3、4表示指定的时分秒
        无参表示当天的0点
        """
        now=datetime.datetime.now()
        timestr=now - datetime.timedelta(days=d,hours =now.hour-h,minutes=now.minute-m, seconds=now.second-s,microseconds=now.microsecond)
        timestr=(timestr).strftime('%Y-%m-%dT%H:%M:%S')
        return timestr

    def get_strbystart(self,s="",strlen=6,flag=True,hastime =True ):
        """
        获取某个开始的随机字符串
        s为开始的字符串，默认为空
        strlen需要生成的随机字符的数量
        flag控制生成的随机字符是否为中文
        """
        #获取日期
        if hastime:
            timestr = datetime.datetime.now().strftime('%m%d')
            s=s+timestr
        #获取随机编号
        sample = random.sample(string.ascii_letters + string.digits, 62)
        #sample = sample + list('!@#$%^&*()-+=.')
        if flag:
            for i in range(strlen):
                s=s+random.choice(sample)
        else:
            for i in range(strlen):
                s=s+str(self.Unicode())

        return s

    def Unicode(self):
        "随机中文字符生成"
        val = random.randint(0x4E00, 0x9FBF)
        return chr(val)

    def get_random_decimal(self):
        number = random.randrange(0, 90, 1)/100.0
        return number

    def get_random_number(self,n,m):
        number = random.randint(n,m)
        return number




