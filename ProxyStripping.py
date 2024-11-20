def stripProxy(proxy):
    proxy_stripped=proxy.split(':')
    #proxy_stripped[0] = IP, proxy_stripped[1] = Port, proxy_stripped[2] = username, proxy_stripped[3] = password
    ip_auth = f"{proxy_stripped[2]}:{proxy_stripped[3]}@{proxy_stripped[0]}:{proxy_stripped[1]}".replace("\n", "")
    return ip_auth

def setProxy(proxy):
    proxy_http_https={
    'http': f'{proxy}',
    'https': f'{proxy}',
    }
    return proxy_http_https