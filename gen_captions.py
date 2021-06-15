
names = [
    'Jacob',
    'Julia',
    'Nathan',
    'Karina',
]

fakeNames = []

for name in names:
    fakeNames.append('fake {n}'.format(n=name))
    fakeNames.append('imaginary {n}'.format(n=name))
    fakeNames.append('{n} (maybe)'.format(n=name))
    fakeNames.append("{n}'s non-existent twin".format(n=name))

print(fakeNames)

captions = [
    'Remember this episode?!',
    'Whhhhhhhyyyyyy?',
    'That looks nothing like the prompt.',
    'No no no my eyes!',
    "Oh god imagine if this was someone's first episode?"
]

for name in fakeNames:
    captions.append('Classic {n} :)'.format(n=name))
    captions.append('{n} whhhyyy?'.format(n=name))
    captions.append('Remember when {n} drew this abomination?'.format(n=name))
    captions.append("{n}, this shouldn't exist!".format(n=name))
    captions.append('What made you think that was a good idea {n}?'.format(n=name))
    captions.append('{n}! REALLY?!'.format(n=name))
    captions.append("In the name of all that's holy, this shouldn't be a thing {n}!".format(n=name))

print(captions)

for i in range(len(captions)):
    captions[i] += ' #normaldrawfeepics'

print(captions)

