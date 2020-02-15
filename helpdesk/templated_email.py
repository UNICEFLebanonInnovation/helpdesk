import os
import sendgrid
import mimetypes
import logging
import requests
from smtplib import SMTPException

from django.utils.safestring import mark_safe
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

logger = logging.getLogger('helpdesk')


def send_templated_mail(template_name,
                        context,
                        recipients,
                        sender=None,
                        submitter=None,
                        bcc=None,
                        fail_silently=False,
                        files=None,
                        extra_headers={}):
    """
    send_templated_mail() is a wrapper around Django's e-mail routines that
    allows us to easily send multipart (text/plain & text/html) e-mails using
    templates that are stored in the database. This lets the admin provide
    both a text and a HTML template for each message.

    template_name is the slug of the template to use for this message (see
        models.EmailTemplate)

    context is a dictionary to be used when rendering the template

    recipients can be either a string, eg 'a@b.com', or a list of strings.

    sender should contain a string, eg 'My Site <me@z.com>'. If you leave it
        blank, it'll use settings.DEFAULT_FROM_EMAIL as a fallback.

    bcc is an optional list of addresses that will receive this message as a
        blind carbon copy.

    fail_silently is passed to Django's mail routine. Set to 'True' to ignore
        any errors at send time.

    files can be a list of tuples. Each tuple should be a filename to attach,
        along with the File objects to be read. files can be blank.

    extra_headers is a dictionary of extra email headers, needed to process
        email replies and keep proper threading.

    """
    from django.core.mail import EmailMultiAlternatives
    from django.template import engines
    from_string = engines['django'].from_string

    from helpdesk.models import EmailTemplate
    from django.conf import settings
    from helpdesk.settings import HELPDESK_EMAIL_SUBJECT_TEMPLATE, \
        HELPDESK_EMAIL_FALLBACK_LOCALE

    locale = context['queue'].get('locale') or HELPDESK_EMAIL_FALLBACK_LOCALE

    try:
        t = EmailTemplate.objects.get(template_name__iexact=template_name, locale=locale)
    except EmailTemplate.DoesNotExist:
        try:
            t = EmailTemplate.objects.get(template_name__iexact=template_name, locale__isnull=True)
        except EmailTemplate.DoesNotExist:
            logger.warning('template "%s" does not exist, no mail sent', template_name)
            return  # just ignore if template doesn't exist

    subject_part = from_string(
        HELPDESK_EMAIL_SUBJECT_TEMPLATE % {
            "subject": t.subject
        }).render(context).replace('\n', '').replace('\r', '')

    footer_file = os.path.join('helpdesk', locale, 'email_text_footer.txt')

    text_part = from_string(
        "%s{%% include '%s' %%}" % (t.plain_text, footer_file)
    ).render(context)

    email_html_base_file = os.path.join('helpdesk', locale, 'email_html_base.html')
    # keep new lines in html emails
    if 'comment' in context:
        context['comment'] = mark_safe(context['comment'].replace('\r\n', '<br>'))

    html_part = from_string(
        "{%% extends '%s' %%}{%% block title %%}"
        "%s"
        "{%% endblock %%}{%% block content %%}%s{%% endblock %%}" %
        (email_html_base_file, t.heading, t.html)
    ).render(context)

    if isinstance(recipients, str):
        if recipients.find(','):
            recipients = recipients.split(',')
    elif type(recipients) != list:
        recipients = [recipients]

    # import smtplib
    #
    # gmail_user = ''
    # gmail_password = ''
    #
    # sent_from = gmail_user
    # to = ['achamseddine@unicef.org', ]
    # subject = 'OMG Super Important Message'
    # body = 'Hey, what'
    #
    # try:
    #     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    #     server.ehlo()
    #     server.login(gmail_user, gmail_password)
    #     server.sendmail(sent_from, to, body)
    #     server.close()
    #
    #     print('Email sent!')
    # except Exception as e:
    #     print(e)


    # using SendGrid's Python Library
    # https://github.com/sendgrid/sendgrid-python

    # from urllib2 import Request, urlopen
    # import json
    # response = requests.post("https://mailtrap.io/api/v1/inboxes.json?api_token=")
    # response_body = response
    # print(response_body)
    # credentials = json.loads(response_body)[0]
    # print(credentials)
    # 
    # EMAIL_HOST = credentials['domain']
    # EMAIL_HOST_USER = credentials['username']
    # EMAIL_HOST_PASSWORD = credentials['password']
    # EMAIL_PORT = credentials['smtp_ports'][0]
    # EMAIL_USE_TLS = True
    # 
    # 
    # 
    # message = Mail(
    #     from_email='achamseddine@unicef.org',
    #     to_emails='ali.chamseddine21@gmail.com',
    #     subject='Sending with Twilio SendGrid is Fun',
    #     html_content='<strong>and easy to do anywhere, even with Python</strong>')
    # try:
    #     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    #     response = sg.send(message)
    #     print(response.status_code)
    #     print(response.body)
    #     print(response.headers)
    # except Exception as e:
    #     print(e)

    # result = requests.post(
    #     "https://api.mailgun.net/v3//messages",
    #     auth=("api", ""),
    #     data={"from": "Excited User <@heroku.com>",
    #           "to": ["ali.chamseddine21@gmail.com", "achamseddine@unicef.org"],
    #           "subject": "Hello",
    #           "text": "Testing some Mailgun awesomness!"})
    #
    # print(result)
    # return True

    # message = Mail(
    #     from_email=submitter,
    #     to_emails=recipients,
    #     subject=subject_part,
    #     html_content=html_part)
    # try:
    #     sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    #     response = sg.send(message)
    # except Exception as e:
    #     print(str(e))
    # return True

    # api_url = 'https://api.mailgun.net/v3/{}/messages'.format(settings.MAILGUN_DOMAIN)
    # print(api_url)
    #
    # try:
    #     result = requests.post(
    #         api_url,
    #         auth=("api", settings.MAILGUN_API_KEY),
    #         files=[("attachment", ("test.jpg", open("files/test.jpg","rb").read())),
    #                ("attachment", ("test.txt", open("files/test.txt","rb").read()))],
            # data={"from": "Excited User <{}>".format(settings.DEFAULT_FROM_EMAIL),
            #       "to": recipients,
            #       "cc": "baz@example.com",
            #       "bcc": "bar@example.com",
                  # "subject": subject_part,
                  # "text": text_part,
                  # "html": html_part})
        # print(result)
        # logger.debug('Sending email to: {!r}'.format(recipients))
        # return result
    # except Exception as e:
    #     print('Exception')
    #     print(e.message)
    #     logger.exception('SMTPException raised while sending email to {}'.format(recipients))
    #     return 0
    #

    # msg = EmailMultiAlternatives(subject_part, text_part,
    #                              sender or settings.DEFAULT_FROM_EMAIL,
    #                              recipients, bcc=bcc)
    #
    # msg.attach_alternative(html_part, "text/html")
    #
    # if files:
    #     for filename, filefield in files:
    #         filefield.open('rb')
    #         content = filefield.read()
    #         msg.attach(filename, content)
    #         filefield.close()
    # logger.debug('Sending email to: {!r}'.format(recipients))
    #
    # try:
    #     return msg.send()
    # except SMTPException as e:
    #     logger.exception('SMTPException raised while sending email to {}'.format(recipients))
    #     if not fail_silently:
    #         raise e
    #     return 0


    # sg = sendgrid.SendGridAPIClient(os.environ.get(''))
    # data = {
    #   "personalizations": [
    #     {
    #       "to": [
    #         {
    #           "email": "achamseddine@unicef.org"
    #         }
    #       ],
    #       "subject": "Hello World from the SendGrid Python Library!"
    #     }
    #   ],
    #   "from": {
    #     "email": "achamseddine@unicef.org"
    #   },
    #   "content": [
    #     {
    #       "type": "text/plain",
    #       "value": "Hello, Email!"
    #     }
    #   ]
    # }
    # response = sg.client.mail.send.post(request_body=data)
    # print(response.status_code)
    # print(response.body)
    # print(response.headers)
