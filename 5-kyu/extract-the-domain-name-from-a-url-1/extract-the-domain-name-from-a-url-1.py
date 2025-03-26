def domain_name(url):
    url = (url.split("://")[-1]).split("/")[0]
    
    if url.startswith("www."):
        url = url[4:]
        
    return url.split(".")[0]