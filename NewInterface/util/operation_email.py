import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from log.get_log import UserLog


class Mailer(object):
    def __init__(self):
        self.log = UserLog()
        self.logger = self.log.get_log()

        self.email_host = "smtp.163.com"
        self.send_user = "andong5456@163.com"
        self.password = "an5456"

    def sendMail(self, mail_list, mail_title, mail_content):
        me = "安晓东" + "<" + self.send_user + ">"  # 发送者
        # me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        msg = MIMEMultipart()
        msg['Subject'] = mail_title
        msg['From'] = me
        msg['To'] = ",".join(mail_list)

        # puretext = MIMEText('<h1>你好，<br/>'+self.mail_content+'</h1>', 'html', 'utf-8')
        puretext = MIMEText('运行结果：' + mail_content)
        msg.attach(puretext)

        # jpg类型的附件
        # jpgpart = MIMEApplication(open('/home/mypan/1949777163775279642.jpg', 'rb').read())
        # jpgpart.add_header('Content-Disposition', 'attachment', filename='beauty.jpg')
        # msg.attach(jpgpart)

        # 首先是xlsx类型的附件
        # te1 = os.path.join(os.path.dirname(os.getcwd()))  获取当前路径的上一层路径
        # te = os.path.join(os.getcwd())  获取当前路径
        # print(te1)
        # print(te)
        xlsxpart = MIMEApplication(open(r"C:\Users\Administrator\PycharmProjects\Interface\dataconfig\interface.xlsx", 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename='interface.xlsx')
        msg.attach(xlsxpart)

        # mp3类型的附件
        # mp3part = MIMEApplication(open('kenny.mp3', 'rb').read())
        # mp3part.add_header('Content-Disposition', 'attachment', filename='benny.mp3')
        # msg.attach(mp3part)

        # pdf类型附件
        # part = MIMEApplication(open('foo.pdf', 'rb').read())
        # part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
        # msg.attach(part)

        try:
            s = smtplib.SMTP()  # 创建邮件服务器对象
            s.connect(self.email_host)  # 连接到指定的smtp服务器。参数分别表示smpt主机和端口
            s.login(self.send_user, self.password)  # 登录到你邮箱
            s.sendmail(me, mail_list, msg.as_string())  # 发送内容
            s.close()
            self.logger.info("邮件发送成功")
            return True
        except Exception as e:
            print(str(e))
            self.logger.info("邮件发送失败")
            return False

    def send_main(self, pass_list, fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        conut_num = pass_num + fail_num
        pass_num1 = len(pass_list)
        fail_num1 = len(fail_list)
        pass_result = "%.2f%%" % (pass_num / conut_num * 100)
        fail_result = "%.2f%%" % (fail_num / conut_num * 100)
        mail_list = ['andong5456@163.com', '527011764@qq.com', '1652159699@qq.com']
        mail_title = "接口自动化测试报告"
        mail_content = "此次运行接口用例为%d个,通过%d个,失败%d个,通过率%s,失败率%s" % (
            int(conut_num), int(pass_num1), int(fail_num1), pass_result, fail_result)
        self.logger.info("运行结果："+mail_content)
        self.sendMail(mail_list, mail_title, mail_content)

        # if self.sendMail(mail_list, mail_title, mail_content):
        #     print("邮件发送成功")
        # else:
        #     print("邮件发送失败")


if __name__ == '__main__':
    # print(ad)
    dd = Mailer()
    dd.send_main([1, 2, 3], [3, 4, 5, 6, 9])