import os, requests, random, configargparse

p = configargparse.ArgParser(formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter, default_config_files=['default.conf'])
p.add('-c', '--config', is_config_file=True, help='config file path')
p.add('--username', required=True, help='Photoprism username', env_var='PHOTOPRISM_ADMIN_USERNAME', default='admin')
p.add('--password', required=True, help='Photoprism password', env_var='PHOTOPRISM_ADMIN_PASSWORD')
p.add('--baseurl', required=True, help='The URL of the Photoprism server (ie, https://photoprism.example.com)')
p.add('--quantity', required=True, help='How many photos to download', default='10')
p.add('--query', required=True, help='The search query to give (ie, "landscape faces:no")')
p.add('--output_directory', required=True, help='Where to put the files.')

options = p.parse_args()




print ("Logging in...")

auth = {
    "username": options.username,
    "password": options.password
}

# First getting the auth token
res = requests.post(
    f"{options.baseurl}/api/v1/session", json=auth
)
res.raise_for_status()
session_id = res.headers["x-session-id"]
session = {"X-Session-ID": session_id}

# Then pulling the session information, which includes the download token (and lots more!)
print("Getting session information...")

res = requests.get(
    f"{options.baseurl}/api/v1/session/{session_id}",
    headers=session
)
res.raise_for_status()

download_token = res.json()['config']['downloadToken']


# Then doing the search
print("Searching now...")

res = requests.get(
    f"{options.baseurl}/api/v1/photos", params={'count': -1, 'q': options.query},
    headers=session
)
res.raise_for_status()


photos = res.json()
print (f"Found this many matches: {len(photos)}")

num = min(len(photos), int(options.quantity))

# Now gonna loop through and get as many as we need
for d in range(1, num + 1):
    
    print (f"Now doing image {d}")
    filename = os.path.expanduser(f"{options.output_directory}/wallpaper_{d}.jpg")
    
    chosen = random.choice(photos)
    print (f"Chosen this one: {chosen['Name']}")

    # Now downloading it
    res = requests.get(
        f"{options.baseurl}/api/v1/dl/{chosen['Hash']}", params={'t': download_token},
        headers=session
    )
    with open(filename, 'wb') as fd:
        fd.write(res.content)

    print("Downloaded file")
