def domain_name(url):
    if ('http' in url or 'https' in url) and (not('www' in url)):
        url = url[url.index('/') + 2:url.index('.')]
    elif ('http' in url or 'https' in url) and ('www' in url):
        url = url[:url.index('.')] + url[url.index('.') + 1:]
        url = url[url.index('/') + 5: url.index('.')]
    elif 'www' in url:
        url = url[:url.index('.')] + url[url.index('.') + 1:]
        url = url[3:url.index('.')]
    else:
        url = url[:url.index('.')]
    return url