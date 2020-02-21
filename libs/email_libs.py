import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
from exchangelib import DELEGATE, Account, Credentials, Configuration, Message, \
    Mailbox, HTMLBody, FileAttachment

logger = logging.getLogger(__name__)


def send_email(display, username, password, host, port, sendto, title,
               content, ssl=False, timeout=10, debug=0):
    if not isinstance(sendto, list):
        sendto = [sendto]

    me = "%s<%s>" % (display, username)
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = title
    msg['From'] = me
    msg['To'] = ';'.join(sendto)
    if ssl:
        server = smtplib.SMTP_SSL('%s:%d' % (host, port), timeout=timeout)
    else:
        server = smtplib.SMTP('%s:%d' % (host, port), timeout=timeout)
    server.set_debuglevel(debug)
    server.login(username, password)
    server.sendmail(me, sendto, msg.as_string())
    server.quit()


def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage


def send_with_exchange(username, password, server, address, content,
                       subject='', to_recipients=[], attachements=[]):
    credentials = Credentials(username=username, password=password)
    config = Configuration(server=server, credentials=credentials)
    account = Account(
        primary_smtp_address=address,
        autodiscover=False,
        config=config,
        credentials=credentials,
        access_type=DELEGATE)

    _to_recipients = []
    for item in to_recipients:
        _to_recipients.append(Mailbox(email_address=item['email']))

    m = Message(
        account=account,
        subject=subject,
        body=HTMLBody(content),
        to_recipients=_to_recipients)

    if attachements:
        for item in attachements:
            with open(item['src'], 'rb') as f:
                img_attach = FileAttachment(name=item['name'], content=f.read())
            m.attach(img_attach)
    m.send()
