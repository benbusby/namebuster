from io import BytesIO
import pycurl

def fetch(curl_url):
    b_obj = BytesIO()
    crl = pycurl.Curl()
    crl.setopt(crl.URL, curl_url)
    crl.setopt(crl.WRITEDATA, b_obj)
    crl.setopt(pycurl.FOLLOWLOCATION, 1)
    crl.perform()
    crl.close()

    return b_obj.getvalue().decode('utf-8', 'ignore')
