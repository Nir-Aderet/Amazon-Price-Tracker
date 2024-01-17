import smtplib

def send_mail(url, title):
 try:
         """SMTP client session object that can be used to send mail to any internet machine
         with an SMTP or ESMTP listener daemon."""
         server = smtplib.SMTP('smtp.gmail.com', 587)
         server.ehlo()
         server.starttls()
         server.ehlo()
 
         server.login('nirisworking@gmail.com', 'skge ehbm wdgr loaj')
 
         subject = 'An Item you requested has a lower price!'
         body = 'The item ' + title + ' is on sale!\nCheck this link for more information: ' + url
         msg = f"subject: {subject}\n\n{body}"
 
         server.sendmail('nirisworking@gmail.com', 'nirisworking@gmail.com', msg)
         print('A massage has been sent')
     finally:
         server.quit()
