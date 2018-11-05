import requests, json, bs4, datetime

FILE_COOKIES = 'cookie.txt'
CSRF_SELECTOR = 'input[name=csrf_token]'
CSRF_ATTR = 'value'

def saveCookies(cookies):
    """ Saves to file cookies from request for future using """
    with open(FILE_COOKIES, 'w') as f:
        json.dump(requests.utils.dict_from_cookiejar(cookies), f)

def loadCookies():
    """ Load cookies file """
    with open(FILE_COOKIES) as f:
        return requests.utils.cookiejar_from_dict(json.load(f))

def log(value):
    """ logging to file """
    with open('log.txt', 'a') as f:
        f.write(str(datetime.datetime.now()) + ': ' + value + '\n')
    raise Exception(value)

def getCsrf(url, session):
    """ Getting csrf value from forms input value.
        Return string or None """
    request = session.get(url)
    soup = bs4.BeautifulSoup(request.content, 'html.parser')
    for input in soup.select(CSRF_SELECTOR, limit=1):
        csrf = input.get(CSRF_ATTR)
        if csrf is not None:
            saveCookies(request.cookies)
            return csrf
        else:
            log('Input value not found.')
    else:
        log('Input not found.')

def add(fields, url='http://berkat.ru/board/add'):
    """ Add new adv """
    try:
        fields['csrf_token'] = getCsrf(url, requests.session())
        session = requests.session()
        request = session.post(url, data=fields, cookies=loadCookies())
    except Exception as e:
        pass