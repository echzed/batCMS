import random
import requests
import json
import re
from googlesearch import search

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
    source = r.text

    if re.search(re.compile(r'wp-content|wordpress|xmlrpc.php'), source):

        return True

    else:
        return False


def joomla_detect(url):
    header = {'user-agent': random_user()}
    r = requests.get(url, headers=header)
    source = r.text

    if re.search(re.compile(r'<script type=\"text/javascript\" src=\"/media/system/js/mootools.js\"></script>|/media/system/js/|com_content|Joomla!'), source):

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
        if len(version) > 0 or version != '' or version != None:
            return version[0]
        
        else:
            return None


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
    
    q = str(plugins_name) + ' site:https://www.exploit-db.com'
    ex_array = []

    for data in search(q , num_results=20):

        if "https://www.exploit-db.com/exploits" in data:

            ex_array.append(data)

    if len(ex_array) != 0 :

        return ex_array

    else:
        return None
