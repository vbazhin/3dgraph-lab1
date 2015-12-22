import mpl_triangulation
import pprint

if __name__ == '__main__':
    res = mpl_triangulation.Polygons().create_triangles(plot=True)
    pprint.pprint(res)
