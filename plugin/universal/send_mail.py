import smtplib
from email.mime.text import MIMEText


# server 定义服务
# user 账号
# passwd 密码或者授权码
# content 内容
# subject 设置主题
# to_user 收件人
def send_mail(server, user, passwd, content, subject, to_user):
    message = MIMEText(content, "HTML")
    message["subject"] = subject
    message["From"] = user
    message["To"] = to_user
    try:
        smtp_email = smtplib.SMTP_SSL(server, 465)  # 定义邮箱服务器
        smtp_email.login(user=user, password=passwd)  # 登陆邮箱
        smtp_email.sendmail(from_addr=user, to_addrs=to_user,
                            msg=message.as_string())  # 发送
        smtp_email.quit()  # 断开退出邮箱
    except Exception as e:
        print(e)
