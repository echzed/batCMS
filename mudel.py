import json
import random
import re

import cloudscraper
import requests


def random_user():
    user_agent_list = [
        "Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1"]
    random_select = random.choice(user_agent_list)

    return random_select


def wp_detect(url):
    header = {"user-agent": random_user()}
    r = requests.get(url, headers=header)
    source = r.content

    if re.search(re.compile(r'wp-content|wordpress|xmlrpc.php'), str(source)):

        return True

    else:
        return False


def joomla_detect(url):
    header = {'user-agent': random_user()}
    r = requests.get(url, headers=header)
    source = r.content

    if re.search(re.compile(
            r'<script type=\"text/javascript\" src=\"/media/system/js/mootools.js\"></script>|/media/system/js/|com_content|Joomla!'),
                 str(source)):

        return True

    else:
        pass


def wp_version(url):
    header = {"user-agent": random_user()}
    r = requests.get(url, headers=header)
    source = r.text

    matches = re.search(re.compile(r'content=\"WordPress (\d{0,9}.\d{0,9}.\d{0,9})?\"'), source)

    if matches:
        version = matches.group(1)
        return version


def joomla_version(url):
    finally_url = url + "/administrator/manifests/files" + '/joomla.xml'
    header = {'user-agent': random_user()}
    r = requests.get(finally_url, headers=header)
    source = r.text

    regex = r'<version>(.+?)</version>'
    pattern = re.compile(regex)
    version = re.findall(pattern, source)
    if version:
        return version


def wp_theme(url):
    header = {"user-agent": random_user()}
    r = requests.get(url, headers=header)
    source = r.text
    themes_array = []

    theme = re.findall(r"\/wp-content\/themes\/([a-zA-Z\-0-9]*)", r.text)

    for i in theme:

        if i not in themes_array:
            themes_array.append(i)

        else:
            pass

    return themes_array


def joomla_template(url):
    header = {'user-agent': random_user()}
    r = requests.get(url, headers=header)
    source = r.text

    template = re.findall(r".*\/templates\/([a-zA-Z0-9\-]*)", source)

    return template[0]


def wp_plugin(url):
    header = {'user-agent': random_user()}
    r = requests.get(url, headers=header)
    source = r.text
    plugin_array = []

    plugins = re.findall(r'\/wp-content\/plugins\/(.*?)\/', source)

    for i in plugins:

        if i not in plugin_array:
            plugin_array.append(i)

        else:
            pass

    return plugin_array


def ex_search(plugins_name):
    url = f"https://www.exploit-db.com/search?q={plugins_name}"
    cf = cloudscraper.create_scraper()
    headers = {

        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'referer': f'https://www.exploit-db.com/',
        'x-requested-with': 'XMLHttpRequest',

    }
    get = cf.get(url, headers=headers)
    tex = get.json()
    x = json.dumps(tex)
    d2 = json.loads(x)
    data = d2['data']
    ex_array = []
    for i in data:
        download = (i['download'])
        reg = re.search("href=[\"\'](.*?)[\"\']", download)
        pp = (reg.group())
        split = "https://www.exploit-db.com" + (pp.split("\"")[1])
        des = (i['description'][1])
        # print(des + " ---> " + split)
        
        ex_array.append(split)
    
    if len(ex_array) != 0:

        return ex_array
    
    else:
        return None
