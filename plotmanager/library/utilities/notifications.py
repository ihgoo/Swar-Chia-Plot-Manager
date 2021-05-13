import discord_notify
import playsound
import pushover
from urllib import request


def _send_notifications(title, body, settings):
    if settings.get('pushplus') is True:
        url = 'http://www.pushplus.plus/send?token='+settings.get('pushplus_key')+'&title='+title+'&content='+body+'&template=html';
        req = request.Request(url)
        res = request.urlopen(req)
        
    if settings.get('notify_discord') is True:
        notifier = discord_notify.Notifier(settings.get('discord_webhook_url'))
        notifier.send(body, print_message=False)

    if settings.get('notify_sound') is True:
        playsound.playsound(settings.get('song'))

    if settings.get('notify_pushover') is True:
        client = pushover.Client(settings.get('pushover_user_key'), api_token=settings.get('pushover_api_key'))
        client.send_message(body, title=title)


def send_notifications(title, body, settings):
    try:
        _send_notifications(title=title, body=body, settings=settings)
    except:
        pass
