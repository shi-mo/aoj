import sys
from sys import stderr
import yaml
import json
import requests as req
import subprocess

LANG = {
    'c': 'C',
    'cpp': 'C++17',
    'd': 'D',
    'rb': 'Ruby',
    'py': 'Python3'
}

URI_AOJ = 'https://judgeapi.u-aizu.ac.jp'

def main():
    check_argv()

    id, ext = sys.argv[1].split('.')
    auth = load_auth()
    submit_aoj(id, ext, auth)

def check_argv():
    if len(sys.argv) != 2:
        stderr.write(f'usage: python {sys.argv[0]} 0001\n')
        sys.exit(1)

def load_auth():
    result = subprocess.run(['bash', './.auth/decrypt_auth_yaml.sh'],
                            capture_output=True, text=True)
    if 0 != result.returncode:
        stderr.write(f'Error executing bash script: {result.stderr}\n')
        sys.exit(1)

    return yaml.safe_load(result.stdout)

def submit_aoj(id, ext, auth):
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }

    with req.Session() as sess:
        send_request_to_aoj(sess, 'POST', '/session',
                            json=auth, headers=headers)

        json_answer = json.loads(json.dumps(post_data_for(id, ext)))
        send_request_to_aoj(sess, 'POST', '/submissions',
                            json=json_answer, headers=headers)

class AojApiError(Exception):
    pass

def send_request_to_aoj(session, method, uri, **kwargs):
    request_uri = f'{URI_AOJ}{uri}'

    res = None
    if 'POST' == method:
        res = session.post(request_uri, **kwargs)
    else:
        res = session.get(request_uri, **kwargs)

    if 200 != res.status_code:
        raise AojApiError(f'API request error:' \
                          f' method:{method} uri:{uri}' \
                          f' response:{res.json()}')
    return res

def post_data_for(id, ext):
    data = {
        'problemId': id,
        'language': LANG.get(ext),
        'sourceCode': load_code_for(id, ext)
    }
    return data

def load_code_for(id, ext):
    with open(f"{id}.{ext}", 'rb') as file:
        return file.read().decode('utf-8')

if __name__ == "__main__":
    main()
