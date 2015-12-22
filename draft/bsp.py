import mpl_triangulation

def split (lambda (lo, hi)):
    w2 = (hi - lo)/2
    return ((lo, lo + w2), (lo + w2, hi))

def contains ((la, ra), (lb, rb)):
    return la <= lb and ra >= rb

def intersects ((la, ra), (lb, rb)):
    return ra >= lb and rb >= la

# L,T,R,B

class node (object):

    __slots__ = ('l', 'r', 'objects')

    def __init__ (self):
        self.l = None
        self.r = None
        self.objects = None

    def get (self, i):
        if i == 0:
            if self.l is None:
                self.l = node()
            return self.l
        else:
            if self.r is None:
                self.r = node()
            return self.r

    def insert (self, seg, needle):
        segs = split (seg)
        for i in (0, 1):
            s = segs[i]
            if contains (s, needle):
                return self.get(i).insert (s, needle)
        if self.objects is None:
            self.objects = [needle]
        else:
            self.objects.append (needle)

    def delete (self, seg, needle):
        segs = split (seg)
        for i in (0, 1):
            s = segs[i]
            if contains (s, needle):
                return self.get(i).delete (s, needle)
        try:
            self.objects.remove (needle)
            return True
        except ValueError:
            pass

    def search_apply (self, seg, needle, fun):
        if self.objects is not None:
            for ob in self.objects:
                if intersects (ob, needle):
                    fun (ob)
        segs = split (seg)
        for i in (0, 1):
            s = segs[i]
            if contains (s, needle):
                return self.get(i).search_apply (s, needle, fun)

    def dump (self, line, depth):
        print '  ' * depth, line,
        if self.objects:
            print self.objects
        else:
            print
        l, r = split (line)
        if self.l:
            self.l.dump (l, depth+1)
        if self.r:
            self.r.dump (r, depth+1)

class bsp:

    def __init__ (self, line=(0,1024)):
        self.tree = node()
        self.line = line
        self.size = 0

    def __repr__ (self):
        return '<bsp tree (objects:%d) line:%r >' % (
            self.size,
            self.line
            )

    def dump (self):
        self.tree.dump (self.line, 0)

    def insert (self, line):
        while 1:
            if contains (self.line, line):
                self.tree.insert (self.line, line)
                break
            else:
                n = node()
                ll, lr = line
                sl, sr = self.line
                w = sr - sl
                if ll < sl:
                    # outside to the left
                    self.line = sl - w, sr
                    n.r, self.tree = self.tree, n
                else:
                    self.line = sl, sr + w
                    n.l, self.tree = self.tree, n
        self.size += 1

    def delete (self, needle):
        return self.tree.delete (self.line, needle)

    def search (self, needle):
        r = []
        self.tree.search_apply (self.line, needle, r.append)
        return r

    def search_apply (self, needle, fun):
        self.tree.search_apply (self.line, needle, fun)

def t0():
    t = bsp()
    t.insert ((0, 200))
    t.insert ((180, 280))
    t.insert ((3000, 4000))
    t.insert ((3050, 3060))
    t.insert ((1000, 1500))
    t.insert ((1400, 1800))
    t.dump()
    t.delete ((3050, 3060))
    t.delete ((180, 280))
    t.dump()
    return t