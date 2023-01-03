import requests
import json
import random


# creates translated text
def owoizer(phrase):
    translation: str = ""
    for letter in phrase:
        if letter.lower() in "o":
            if letter.isupper():
                translation = translation + "Owo"
            else:
                translation = translation + "owo"
        elif letter.lower() in "u":
            if letter.isupper():
                translation = translation + "Uwu"
            else:
                translation = translation + "uwu"
        elif letter.lower() in "w":
            if letter.isupper():
                translation = translation + "Uwu"
            else:
                translation = translation + "uwu"
        elif letter.lower() in "r":
            if letter.isupper():
                translation = translation + "W"
            else:
                translation = translation + "w"
        else:
            translation = translation + letter
    return translation

# gets a quote
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote  

# gets a translated quote
def get_owo_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = owoizer(json_data[0]['q']) + " - " + json_data[0]['a'] + "\'s fursona."
    return quote  

# gets an idea
def get_idea():
    response = requests.get("https://www.boredapi.com/api/activity")
    json_data = json.loads(response.text)
    quote = json_data['activity']
    return quote

# gets a translated idea
def get_owo_idea():
    response = requests.get("https://www.boredapi.com/api/activity")
    json_data = json.loads(response.text)
    quote = owoizer(json_data['activity'])
    return quote    

# gets random xkcd comic
def get_xkcd():
    response = requests.get("https://xkcd.com/info.0.json")
    json_data = json.loads(response.text)
    number_of_total_xkcd = json_data['num']
    xkcd_comic_number = random.randint(1, number_of_total_xkcd)

    response = requests.get(f"https://xkcd.com/{xkcd_comic_number}/info.0.json")
    json_data = json.loads(response.text)
    quote = json_data['img']
    return quote  


def get_response(message: str) -> str:
    p_message: str = message.lower()

    # gives a quote
    if p_message == '!quote':
        return get_quote()

    # owo version of quote command
    if p_message == '!owoquote':
        return get_owo_quote()

    # gives a suggestion
    if p_message == '!bored':
        return get_idea()

    # owo version of bored command
    if p_message == '!owobored':
        return get_owo_idea()

    # summons random xkcd
    if p_message == '!xkcd':
        return get_xkcd()

    # links phelix
    if p_message == '!phelix':
        return 'https://www.furaffinity.net/view/45792375/'

    # links twitch account
    if p_message == '!twitch':
        return 'https://www.twitch.tv/phelix_the_cat_'

    # the secret word
    if 'rock' in p_message:
        return 'https://tenor.com/view/the-rock-gif-25266750'
