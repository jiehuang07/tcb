from discord import Webhook, RequestsWebhookAdapter, Embed, Color
import datetime

def avatar_url():
    return 'https://cdn.discordapp.com/avatars/322161539987668993/35d11d7518eb736cb9b3fdb31a231010.png?size=128'

def send_webhook_Cyber():
    url = '......'
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    dateTimeObj = datetime.datetime.now()

    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    embed = Embed(title='Successfully checked out!',  description ='Supreme®/The North Face® Paper Print Nuptse Jacket',  color=Color.from_rgb(50, 205, 50))
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/qSpFTd5QMg-NHGXozwKvzgkDYtukLz-KO5af_ZIMZY8/https/assets.supremenewyork.com/181204/rs/jMbSE4n6tHM.jpg?width=80&height=80")
    embed.add_field(name="Store", value="Supreme US")
    embed.add_field(name="Size", value="XLarge")
    embed.add_field(name="Profile", value="||Jie32||")
    embed.add_field(name="Order", value="||12345678||", inline = True)
    embed.add_field(name="Color", value = '\u200b', inline = True)
    embed.add_field(name="Category", value="Jackets", inline = True)
    embed.add_field(name="Captcha Bypass", value="Enabled")
    embed.add_field(name="Mode", value="Safe")
    embed.set_footer(icon_url = "https://images-ext-2.discordapp.net/external/AFl8btw6-OdaFIC4DU6c8as5gTG8SIVdsOx_hLOXnEs/https/cdn.cybersole.io/media/discord-logo.png", text="CyberAIO • {}".format(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]))
    webhook.send(embed=embed,avatar_url=avatar_url(),username='Jay#0238')

send_webhook_Cyber()