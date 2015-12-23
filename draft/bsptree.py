'''
1. Select a partition plane.
2. Partition the set of polygons with the plane.
3. Recurse with each of the two new sets.
'''
import mpl_triangulation

def split ():
    w2 = (hi - lo)/2
    return ((lo, lo + w2), (lo + w2, hi))

def contains ([la, ra], [lb, rb]):
    return la <= lb and ra >= rb

def intersects ((la, ra), (lb, rb)):
    return ra >= lb and rb >= la



class BSPNode(object):
     __slots__ = ('partition', 'poligons', 'front', 'back', 'leaf')

    def __init__(self, ):
        self.partition = None  #H_PLANE секущая плоскость
        self.poligons = mpl_triangulation.Polygons.create_triangles(plot=False) #P_LIST список полигонов
        #Указатели на дочерние узлы и на родителя
        self.front = None
        self.back = None
        # self.parent = None
        self.leaf = Triangle #LEAF указатель на лист


    def finCenter(self):


class Triangle(object):

class BuildBSPTree(object):
     def __init__(self, rootid):
        self.left = None
        self.right = None
        self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self, value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid
    def line(x, y):
        a=(y2-y1)/(x2-x1)
        b=(x2y1-x1y2)/(x2-x1)


'''public class Leaf
{

    private const MIN_LEAF_SIZE:uint = 6;

    public var y:int, x:int, width:int, height:int; // the position and size of this Leaf

    public var leftChild:Leaf; // the Leaf's left child Leaf
    public var rightChild:Leaf; // the Leaf's right child Leaf
    public var poligon:Triangle; // the poligon that is inside this Leaf
    public var halls:Vector.; // hallways to connect this Leaf to other Leafs

    public function Leaf(X:int, Y:int, Z:int)
    {
        // initialize our leaf
        x = X;
        y = Y;
        z = Z;
    }

    public function split():Boolean
    {
        // begin splitting the leaf into two children
        if (leftChild != null || rightChild != null)
            return false; // we're already split! Abort!

        // determine direction of split
        // if the width is >25% larger than height, we split vertically
        // if the height is >25% larger than the width, we split horizontally
        // otherwise we split randomly
        var splitH:Boolean = FlxG.random() > 0.5;
        if (width > height && width / height >= 1.25)
            splitH = false;
        else if (height > width && height / width >= 1.25)
            splitH = true;

        var max:int = (splitH ? height : width) - MIN_LEAF_SIZE; // determine the maximum height or width
        if (max <= MIN_LEAF_SIZE)
            return false; // the area is too small to split any more...

        var split:int = Registry.randomNumber(MIN_LEAF_SIZE, max); // determine where we're going to split

        // create our left and right children based on the direction of the split
        if (splitH)
        {
            leftChild = new Leaf(x, y, width, split);
            rightChild = new Leaf(x, y + split, width, height - split);
        }
        else
        {
            leftChild = new Leaf(x, y, split, height);
            rightChild = new Leaf(x + split, y, width - split, height);
        }
        return true; // split successful!
    }
}'''