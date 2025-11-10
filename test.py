proxy = {
  'https': 'http://127.0.0.1:8090',
}
auth_dict = {'username': 'admin', 'password': 'admin123'}
login = requests.post(target_url + '/login',
                      proxies=proxies, json=auth_dict)
if login.status_code == 200:  # if login is successful
    auth_token = login.headers['Authorization']
    auth_header = {"Authorization": auth_token}