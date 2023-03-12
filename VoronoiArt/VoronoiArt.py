'''
VoronoiArt.py

Combine set of pts with a picture to create a voronoi tessellation mosaic.

Created by: Benjamin Metha
Last Updated: Apr 05, 2021
'''

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import euclidean_distances
import itertools

def voronoi_pic(photo, points):
    '''
    Parameters
    ----------
    photo: image
    The image that will be transformed into a mosaic
    
    points: array of 2-tuples
    a set of pixels on the image that will generate the Voronoi 
    tessellation
    
    Returns
    -------
    mosaic: image
    The final product :)
    '''
    # Make a final im object that matches the shape of the first
    # For each pixel in the image:
    # # Find which pixel in the point set it is closest to
    # # Replace its value with the value of that point
    photo_array  = np.array(photo)
    mosaic_array = photo_array
    width, height = photo.size
    print("Generating pixel list...")
    all_pix = np.array(list(itertools.product(np.arange(width),np.arange(height))))
    print("Finding distances...")
    dists = euclidean_distances(all_pix, points)
    print("Assigning Voronoi cells...")
    closest_pixels = points[np.argmin(dists,1)]
    print("Coloring in...")
    for ii in range(width):
        for jj in range(height):
            mosaic_array[ii,jj] = photo_array[tuple(closest_pixels[ii*width+jj])]
    
    return Image.fromarray(mosaic_array)
    
def make_point_set(photo, n_points):
    '''
    The most basic way to get a point set for Voronoi tesselation purposes
    
    Randomly samples n_points, uniformly distributed, from the grid
    
    Parameters
    ----------
    photo: image
    The image that will be transformed into a mosaic    
    
    n_points: int
    the number of mesh-generating points wanted
    
    Returns
    -------
    point_set: array of 2-tuples
    a set of pixels on the image that will generate the Voronoi 
    tessellation
    '''
    x = np.random.randint(0, photo.size[0], n_points)
    y = np.random.randint(0, photo.size[1], n_points)
    return np.column_stack((x,y))
    
def make_face_central_set(n_pts, a=1):
    '''
    This will use a power law, gradient -1, to sample so that more points are 
    near the center.
    '''
    face_x, face_y = 392, 1196
    face_size = 100
    im_size = 2440
    theta = np.random.uniform(0, 2*np.pi, n_pts)
    r = face_size * np.random.pareto(a, n_pts)
    x = r*np.cos(theta) + face_x
    y = r*np.sin(theta) + face_y
    all_pix = np.column_stack((x,y)).astype(int)
    good_pix = [x>=0 and x<im_size and y>=0 and y<im_size for x,y in all_pix]
    return all_pix[good_pix]
    
if __name__=='__main__':
    photo = Image.open('beach.jpg')
    pt_set = make_face_central_set(1000)
    mosaic = voronoi_pic(photo, pt_set)
    mosaic.show()
    
