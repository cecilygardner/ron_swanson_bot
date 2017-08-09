from __future__ import print_function

import json
import os
import os.path
import random

import asana


RON_QUOTES = (
    "Clear alcohols are for rich women on diets.",
    "there's only one thing i hate more than lying. Skim milk. Which is water."
    " That's lying about being milk.",
    "Never half-ass two things. Whole-ass one thing.",
    "Turkey can never beat cow.",
    "When people get a little too chummy with me I like to call them by the "
    "wrong name to let them know I don't really care about them.",
    "Crying: acceptable at funerals and the Grand Canyon.",
    "Shorts over six inches are capri pants, shorts under six inches are "
    "European.",
    "One rage every three months is permitted. Try not to hurt anyone who "
    "doesn't deserve it.",
    "Dear frozen yogurt, you are the celery of desserts. "
    "Be ice cream, or be nothing. ",
    "I regret nothing. The end. ",
    "And I hate everything",
    "I keep a sizable supply of ground chuck in my desk. "
    "Remove it or it will begin to smell. ",
    "Give 100%. 110% is impossible.",
    "There is no such thing as bad weather. "
    "Only inadequate clothing and methods of transportation. ",
)


def create_task_with_ron(asana_client, asana_config):

    ron_quote = random.sample(RON_QUOTES, 1)[0]
    print('Grabbing random Ron Swanson quote')
    task_name = "Ron Quote and Ron Image"

    params = {
        'workspace': asana_config['workspace_id'],
        'projects': [asana_config['project_id']],
        'name': task_name,
        'notes': ron_quote
    }

    response = asana_client.tasks.create(params)
    print("Ron task created in Asana workspace")

    return response['id']


def attach_ron_image(asana_client, task_id):

    if os.path.exists("images"):
        ron_images = [
            fname for fname in os.listdir(
                "images") if not fname.startswith(".")
        ]

        random_image_name = random.sample(ron_images, 1)[0]

        with open(os.path.join("images", random_image_name), "rb") as ron_file:
            asana_client.attachments.create_on_task(
                task_id, ron_file, "ron_quote.jpg", "image/jpeg")
    else:
        print("no ron images :(")


def read_config():
    with open('asana_config.json') as config_fobj:
        return json.load(config_fobj)


def main():
    asana_config = read_config()
    asana_client = asana.Client.access_token(
        asana_config['personal_access_token'])
    task_id = create_task_with_ron(asana_client, asana_config)
    attach_ron_image(asana_client, task_id)


if __name__ == "__main__":
    main()
