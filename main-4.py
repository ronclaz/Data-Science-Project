rarebirds = {
    'Gold-crested Toucan': {
        'Height (m)': 1.1,
        'Weight (kg)': 35,
        'Color': 'Gold',
        'Endangered': True,
        'Aggressive': True
        },
    'Pearlescent Kingfisher': {
        'Height (m)': 0.25,
        'Weight (kg)': 0.5,
        'Color': 'White',
        'Endangered': False,
        'Aggressive': False,
    },
    'Four-metre Hummingbird': {
        'Height (m)': 0.6,
        'Weight (kg)': 0.5,
        'Color': 'Blue',
        'Endangered': True,
        'Aggressive': False,
    },
    'Giant Eagle': {
        'Height (m)': 1.5,
        'Weight (kg)': 52,
        'Color': 'Black and White',
        'Endangered': True,
        'Aggressive': True
        },
    'Ancient Vulture': {
        'Height (m)': 2.1,
        'Weight (kg)': 70,
        'Color': 'Brown',
        'Endangered': False,
        'Aggressive': False
        },
    }
birdlocation = ['In the canopy directly above our heads.','Between my 6 and 9 o’clock above.','Between my 9 and 12 o’clock above.','Between my 12 and 3 o’clock above.','Between my 3 and 6 o’clock above.','In a nest on the ground.','Right behind you.']
codes = {
    '111': birdlocation[0],
    '110': birdlocation[1],
    '110': birdlocation[2],
    '101': birdlocation[3],
    '100': birdlocation[4],
    '011': birdlocation[5],
    '010': birdlocation[6],
}
actions = ['Back Away','Cover your Head','Take a Photograph']
for key, values in rarebirds.items():
    if key == 'Giant Eagle':
        xx = rarebirds.get(key)
        for key1, values1 in xx.items():
            if key1 == 'Aggressive':
                print(values1)
for i in rarebirds:
    print('The names of the birds are ' + i)
for y in rarebirds:
    xx1 = rarebirds.get(y)
    for key1, values1 in xx1.items():
        if key1 == 'Aggressive' and values1 == True:
            print('The ' + y + ' is an Aggressive bird so ' + actions[1])
        if key1 == 'Endangered' and values1 == True:
            print('The ' + y + ' is an Endangered bird so ' + actions[0])
for key3 in codes:
    print('Code ' + key3, 'is ' + codes[key3])
for key4, values4 in rarebirds.items():
    xx2 = rarebirds.get(key4)
    xx2['seen'] = False
    print(key4, values4)
encounter = True
while encounter == True:
    sighting = input('what do you see: ')
    #print(sighting.lower())
    rarebirdsList = rarebirds.keys()
    #for key5 in rarebirds.keys():
    if sighting in rarebirds:
        print('this is one of the birds we’re looking for!')
        encounter = False
        code = input('Where do you see it: ')
        location = codes[code]
        print('So youve seen a', sighting, location, 'My goodness.')
        bird_dict = rarebirds.get(sighting)
        #print(bird_dict)
        if bird_dict['Aggressive'] == True:
            print('So youve seen a', sighting, actions[1],actions[0],' it is Aggressive so just photograph the ', sighting, 'at its location: ',location)
        elif bird_dict['Endangered'] == True:
            print('So youve seen a', sighting,actions[0],' it is Endangered so just photograph the ', sighting, 'at its location: ',location)
        else:
            print('So youve seen a', sighting,'it is not Aggressive or Endangered so just photograph the ', sighting, 'at its location: ',location)
    else:
        print('this is not one of the birds we’re looking for!')
