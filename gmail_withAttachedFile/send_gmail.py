from email.mime.text import MIMEText
import smtplib, ssl

# 添付に必要
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from os.path import basename

# Gmailの設定
account = "あなたのGmailアカウント@gmail.com"
password = "Gmailアカウントのパスワード"
# メールの送信先
mail_to = "送り先のアドレス"

# メールデータ
subject = "件名"
text = '''メール本文の内容をここに書きます。

改行だってできちゃうよ。
'''

#添付がある場合にはTrue、なければFalse
attach = False

if attach:
    msg=MIMEMultipart()
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = account
    msg.attach(MIMEText(text.encode("iso-2022-jp"),"plain", "iso-2022-jp"))
else:
    msg=MIMEText(text.encode("iso-2022-jp"),"plain", "iso-2022-jp")
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = account
    
# ファイルを添付
path="./添付ファイル"
with open(path, "rb") as file:
    part=MIMEApplication(file.read(), Name=basename(path))

part['Content-Disposition']='attachment; filename="%s"' % basename(path)
msg.attach(part)

# Gmailに接続 --- (*4)
server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
server.login(account, password)
server.send_message(msg) # メールの送信
print("Your mail was sent to" + mail_to)