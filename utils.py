import urllib
import requests

def get_zip_code(address):
    encoded_address = urllib.parse.quote_plus(address.replace("/", " "))
    r = requests.get("https://api.post.kz/api/byAddress/%s?from=0" % encoded_address)
    rJson = r.json()

    code = rJson['data'][0]['postcode']
    oldCode = rJson['data'][0]['fullAddress']['oldPostcode']
    address_rus = rJson['data'][0]['addressRus']
    return (address_rus, code, oldCode)

