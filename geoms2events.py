'''
Extract position and orientation from .geom files
'''

import glob

geoms = glob.glob('*.geom')


def make_geom_kvp(geom):  # Create a dictionary of geom key/values
    gkvp = {}
    for line in geom:
        line = line.split(':')
        gkvp[line[0]] = (line[1].rstrip("\n\r")).lstrip()
    return gkvp


def parse_geom(geom):
    with open(geom,'r') as fin: 
        fread = fin.readlines()
        gkvp = make_geom_kvp(fread)
        image_id = gkvp['image_id']
        lat = gkvp['latlonh_platform_position'].split()[0]
        lon = gkvp['latlonh_platform_position'].split()[1]
        easting = gkvp['utm_platform_position'].split()[0]
        northing = gkvp['utm_platform_position'].split()[1]
        utm_zone = gkvp['utm_zone']
        orthometric_height = gkvp['utm_platform_position'].split()[2]
        omega = gkvp['omega']
        phi = gkvp['phi']
        kappa = gkvp['kappa']
        sub_strings = (image_id, lon, lat, easting, northing, utm_zone, orthometric_height, omega, phi, kappa)
        geom_txt = '\n%s, %s, %s, %s, %s, %s, %s, %s, %s, %s' % sub_strings
    return geom_txt


with open('events.csv', 'w') as events:
    events.write('image_id, lon, lat, easting, northing, utm_zone, orthometric_height, omega, phi, kappa')
    for geom in geoms:
        geom_txt = parse_geom(geom)
        events.write(geom_txt)

