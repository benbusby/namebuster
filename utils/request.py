from io import BytesIO
import pycurl

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Mobile Firefox/59.0'


def fetch(curl_url):
    b_obj = BytesIO()
    crl = pycurl.Curl()
    crl.setopt(crl.URL, curl_url)
    crl.setopt(crl.USERAGENT, user_agent)
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.setopt(pycurl.FOLLOWLOCATION, 1)
    crl.perform()
    crl.close()

    return b_obj.getvalue().decode('utf-8', 'ignore')
