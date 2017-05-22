import smtplib

HOST = "mySMTP.server.com"
SUBJECT = "Sending email from python"
TO = "star.milan@gamil.com"
FROM = "daskoushik49@gmail.com"
text = "Python rules them all"

BODY = "\r\n".join((
    "From:%s" % FROM,
    "To:%s" % TO,
    "Subject:%s" % SUBJECT,
    "",
    text
))

server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()
