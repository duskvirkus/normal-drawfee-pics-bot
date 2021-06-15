import tweepy
from dotenv import dotenv_values
import random
import os


def gen_captions():
    names = [
        'Jacob',
        'Julia',
        'Nathan',
        'Karina',
    ]

    fake_names = []
    for name in names:
        fake_names.append('fake {n}'.format(n=name))
        fake_names.append('imaginary {n}'.format(n=name))
        fake_names.append('{n} (maybe)'.format(n=name))
        fake_names.append("{n}'s non-existent twin".format(n=name))

    captions = [
        'Remember this episode?!',
        'Whhhhhhhyyyyyy?',
        'That looks nothing like the prompt.',
        'No no no my eyes!',
        "Oh god imagine if this was someone's first episode?"
    ]
    for name in fake_names:
        captions.append('Classic {n} :)'.format(n=name))
        captions.append('{n} whhhyyy?'.format(n=name))
        captions.append('Remember when {n} drew this abomination?'.format(n=name))
        captions.append("{n}, this shouldn't exist!".format(n=name))
        captions.append('What made you think that was a good idea {n}?'.format(n=name))
        captions.append('{n}! REALLY?!'.format(n=name))
        captions.append("In the name of all that's holy, this shouldn't be a thing {n}!".format(n=name))

    for i in range(len(captions)):
        captions[i] += ' #normaldrawfeepics'

    return captions


def get_random_caption():
    captions = gen_captions()
    index = random.randrange(len(captions))
    return captions[index]


def tweet(api):
    im_dir = './test-im'
    im_in_progress = './in-progress'
    im_tweeted = './tweeted'

    os.makedirs(im_in_progress, exist_ok=True)
    os.makedirs(im_tweeted, exist_ok=True)

    file = None
    for (dirpath, dirnames, filenames) in os.walk(im_dir):
        if len(filenames) <= 0:
            print('No files left in {dir}!'.format(dir=im_dir))
            exit(1)

        index = random.randrange(len(filenames))
        file = filenames[index]

    print(file)

    # move to in progress
    os.rename(os.path.join(im_dir, file), os.path.join(im_in_progress, file))

    api.update_with_media(os.path.join(im_in_progress, file), get_random_caption())

    # move to tweeted
    os.rename(os.path.join(im_in_progress, file), os.path.join(im_tweeted, file))


def main():
    config = dotenv_values(".env")
    # print(config)

    auth = tweepy.OAuthHandler(config['CONSUMER_KEY'], config['CONSUMER_SECRET'])
    auth.set_access_token(config['ACCESS_TOKEN'], config['ACCESS_TOKEN_SECRET'])

    api = tweepy.API(auth)

    tweet(api)


if __name__ == "__main__":
    main()
