class BSPNode(object):
    def __init__(self, ):
        self.partition = None
        self.lines = None
        self.front = None
        self.back = None
        self.node = Triangle


class Triangle(object):

class BSPTree(object):
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
    public var room:Rectangle; // the room that is inside this Leaf
    public var halls:Vector.; // hallways to connect this Leaf to other Leafs

    public function Leaf(X:int, Y:int, Width:int, Height:int)
    {
        // initialize our leaf
        x = X;
        y = Y;
        width = Width;
        height = Height;
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