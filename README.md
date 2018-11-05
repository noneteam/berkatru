# API for website - [berkat.ru](http://berkat.ru)

### Setup:

```
pip install -r requirements.txt
```

### Usage:

```
import berkat

berkat.add({
    'category_id': 28,
    'props[16]': 1, # price
    'props[21]': 1, # deal type
    'title': 'Sell cat',
    'content': 'Pretty cat',
    'city': 5548,
    'contacts[1]': '79876543210',
    'contact_name': 'Me',
    'captcha': 1,
    'pub_days': 90,
    'is_org': None,
    'org_name': None,
    'file': None,
    'map': None,
    'submit': 'Сохранить'
})
```
