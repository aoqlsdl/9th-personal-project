import json
import sys, io, os
import django

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personalproj.settings")
django.setup()

from map.models import Tourism

def parsing():
    with open('posts.json') as json_file:
        json_data = json.load(json_file)

    post = []

    for i in range(10):
        post.append({
            'name': json_data['tourism'][i]['name'],
            'loc': json_data['tourism'][i]['loc'],
            'lat': json_data['tourism'][i]['lat'],
            'lon': json_data['tourism'][i]['lon']
        })

    return post

if __name__ == '__main__':
    post = parsing()

    for i in range(len(post)):
        Tourism(
            name = post['tourism'][i]['name'],
            location = post['tourism'][i]['loc'],
            latitude = post['tourism'][i]['lon']
        ).save()