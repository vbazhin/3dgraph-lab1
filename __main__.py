import mpl_triangulation
import pprint

if __name__ == '__main__':
    res = mpl_triangulation.Polygons().create_triangles(plot=True)
    pprint.pprint(res)
    pprint.pprint(len(res))
    S = {}
    for i in range(3):
        S[i] = 0
        for j in range(len(res)):
            S[i] += res[j][i]
        print(S[i]/len(res))


