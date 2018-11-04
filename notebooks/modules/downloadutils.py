import requests

def download_file(url, output_file, expected_content_type):
    r = requests.get(url)
    r.raise_for_status()
    if expected_content_type in r.headers['Content-Type']:
        with open(output_file, 'wb') as file:
            file.write(r.content)
    else:
        raise Exception('Invalid content-type: ' + r.headers['Content-Type'])
