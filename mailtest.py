#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Test message")
msg['Subject'] = 'Test header'
msg['From'] = 'mailtest-noreply@sandtrout.local'
msg['To'] = 'brock@brocktice.com'

s = smtplib.SMTP('localhost')
s.sendmail(msg['From'], [msg['To']], msg.as_string())
s.quit()


