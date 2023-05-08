
############################################################################################################
from colorama import *
import os
import requests
import re
############################################################################################################
def search_words_in_file(file_path, words):
    grabber_found = False
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file):
            for word in words:
                if word in line:
                    grabber_found = True
                    os.system('title WARNING GRABBER WAS BEEN FOUNDED!')
                    print(f"{Fore.RED}[!]: {line.strip()}")
                    webhook_regex = r'(https?://(?:www\.)?discord(?:app)?\.com/api/webhooks/[^\s]+)'
                    webhook_match = re.search(webhook_regex, line)
                    if webhook_match:
                        webhook_url = webhook_match.group(1)
                        print(f"{Fore.LIGHTGREEN_EX}[SENDING]{Fore.WHITE} Sending a message to webhook :)")
                        title = '**Found Your Webhook LOL**'
                        description = f'Dont Grab People Nigga [>]: \nIf we see your webhook aigan its getting deleted this is a **WARNING**'
                        color = 0xFF5733
                        send_embed_to_webhook(webhook_url, title, description, color)
    if not grabber_found:
        print(f"{Fore.LIGHTGREEN_EX}NO GRABBER FOUND! :)")
        os.system('title NO GRABBER FOUND!')
############################################################################################################
def send_embed_to_webhook(webhook_url, title, description, color):
    embed = {
        "title": title,
        "description": description,
        "color": color
    }
    payload = {
        "username": "RainBow Blooded",
        "embeds": [embed]
    }
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status() 
        print(f"{Fore.LIGHTBLUE_EX}[SENT] {Fore.WHITE}Sent a warning to user's webhook")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.LIGHTBLUE_EX}[ERROR] {Fore.WHITE}Failed to send message to webhook: {e}")
############################################################################################################
namefile = input(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}>{Fore.LIGHTBLUE_EX}]: {Fore.WHITE}Filename?: ")
file_path = f'{namefile}'
words = ['b64decode', 'exec', "https://discord.com/api/webhooks/", "__t3mp__", "grabber", "stealer", "Hyperion", "OrionGrabber", "LunarStealer", "__import__('base64')", "__import__('builtins')", ".exec", ";exec", "__import__('tempfile')", "paste.fo", "paste.website", "<string>"]
search_words_in_file(file_path, words)
rem = input(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]: {Fore.WHITE}do you want to remove the file? [y/n]: ")
if rem == "y":
    os.remove(namefile)
else:
    pass
############################################################################################################
