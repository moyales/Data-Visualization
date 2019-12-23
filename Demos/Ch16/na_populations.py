from pygal_maps_world.maps import World

wm = World()
wm.title = 'Populations of North American Countries'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 11342300})

wm.render_to_file('na_populations.svg')