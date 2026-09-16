import json
from datetime import datetime

import requests


# Define timestamp
current_datetime = str(datetime.now())


def get_posts():

    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts

        else:
            print('Error:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:

        print('Error:', e)
        return None


def write_to_file(post):

    with open("demofile.txt", "a") as f:
        f.write(post)


def main():
    posts = get_posts()

    if posts:
        first_post = posts[0]
        print(first_post)
        print('Type:', type(first_post))        

        try:
            first_post = json.dumps(first_post, indent=4)
            write_to_file(f"{current_datetime}: {first_post}\n")

        except Exception as e:
            return (e,'Failed to write to file')

    else:
        return 'No result from API'


        
if __name__ == '__main__':
    main()
