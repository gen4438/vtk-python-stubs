"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkIncrementalOctreeNode(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkIncrementalOctreeNode - Octree node constituting incremental
     octree (in support of both point location and point insertion)
    
    Superclass: vtkObject
    
    Octree nodes serve as spatial sub-division primitives to build the
    search
     structure of an incremental octree in a recursive top-down manner.
    The
     hierarchy takes the form of a tree-like representation by which a
    parent
     node contains eight mutually non-overlapping child nodes. Each child
    is
     assigned with an axis-aligned rectangular volume (Spatial Bounding
    Box)
     and the eight children together cover exactly the same region as
    governed
     by their parent. The eight child nodes / octants are ordered as
    
    
     { (xBBoxMin, xBBoxMid] & (yBBoxMin, yBBoxMid] & (zBBoxMin, zBBoxMid]
    },
     { (xBBoxMid, xBBoxMax] & (yBBoxMin, yBBoxMid] & (zBBoxMin, zBBoxMid]
    },
     { (xBBoxMin, xBBoxMid] & (yBBoxMid, yBBoxMax] & (zBBoxMin, zBBoxMid]
    },
     { (xBBoxMid, xBBoxMax] & (yBBoxMid, yBBoxMax] & (zBBoxMin, zBBoxMid]
    },
     { (xBBoxMin, xBBoxMid] & (yBBoxMin, yBBoxMid] & (zBBoxMid, zBBoxMax]
    },
     { (xBBoxMid, xBBoxMax] & (yBBoxMin, yBBoxMid] & (zBBoxMid, zBBoxMax]
    },
     { (xBBoxMin, xBBoxMid] & (yBBoxMid, yBBoxMax] & (zBBoxMid, zBBoxMax]
    },
     { (xBBoxMid, xBBoxMax] & (yBBoxMid, yBBoxMax] & (zBBoxMid, zBBoxMax]
    },
    
    
     where { xrange & yRange & zRange } defines the region of each 3D
    octant.
     In addition, the points falling within and registered, by means of
    point
     indices, in the parent node are distributed to the child nodes for
    delegated
     maintenance. In fact, only leaf nodes, i.e., those without any
    descendants,
     actually store point indices while each node, regardless of a leaf
    or non-
     leaf node, keeps a dynamically updated Data Bounding Box of the
    inhabitant
     points, if any. Given a maximum number of points per leaf node, an
    octree
     is initialized with an empty leaf node that is then recursively
    sub-divided,
     but only on demand as points are incrementally inserted, to
    construct a
     populated tree.
    
    
     Please note that this octree node class is able to handle a large
    number
     of EXACTLY duplicate points that is greater than the specified
    maximum
     number of points per leaf node. In other words, as an exception, a
    leaf
     node may maintain an arbitrary number of exactly duplicate points to
    deal
     with possible extreme cases.
    
    @sa
     vtkIncrementalOctreePointLocator
    """
    def ContainsPoint(self, ):
        """
        V.ContainsPoint((float, float, float)) -> int
        C++: vtkTypeBool ContainsPoint(const double pnt[3])
        
        A point is in a node if and only if MinBounds[i] < p[i] <=
        MaxBounds[i], which allows a node to be divided into eight
        non-overlapping children.
        """
        ...
    
    def ContainsPointByData(self, ):
        """
        V.ContainsPointByData((float, float, float)) -> int
        C++: vtkTypeBool ContainsPointByData(const double pnt[3])
        
        A point is in a node, in terms of data, if and only if
        MinDataBounds[i] <= p[i] <= MaxDataBounds[i].
        """
        ...
    
    def DeleteChildNodes(self):
        """
        V.DeleteChildNodes()
        C++: void DeleteChildNodes()
        
        Delete the eight child nodes.
        """
        ...
    
    def ExportAllPointIdsByDirectSet(self, *int, **kwargs):
        """
        V.ExportAllPointIdsByDirectSet([int, ...], vtkIdList)
        C++: void ExportAllPointIdsByDirectSet(vtkIdType *pntIdx,
            vtkIdList *idList)
        
        Export all the indices of the points (contained in or under this
        node) by directly setting them in an allocated vtkIdList object.
        pntIdx indicates the starting location (in terms of vtkIdList)
        from which new point indices are added to vtkIdList by
        vtkIdList::SetId().
        """
        ...
    
    def ExportAllPointIdsByInsertion(self, vtkIdList):
        """
        V.ExportAllPointIdsByInsertion(vtkIdList)
        C++: void ExportAllPointIdsByInsertion(vtkIdList *idList)
        
        Export all the indices of the points (contained in or under this
        node) by inserting them to an allocated vtkIdList via
        vtkIdList::InsertNextId().
        """
        ...
    
    def GetBounds(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetBounds([float, float, float, float, float, float])
        C++: void GetBounds(double bounds[6])
        
        Get the spatial bounding box of the node. The values are returned
        via an array in order of: x_min, x_max, y_min, y_max, z_min,
        z_max.
        """
        ...
    
    def GetChild(self, p_int):
        """
        V.GetChild(int) -> vtkIncrementalOctreeNode
        C++: vtkIncrementalOctreeNode *GetChild(int i)
        
        Get quick access to a child of this node. Note that this node is
        assumed to be a non-leaf one and no checking is performed on the
        node type.
        """
        ...
    
    def GetChildIndex(self, ):
        """
        V.GetChildIndex((float, float, float)) -> int
        C++: int GetChildIndex(const double point[3])
        
        Determine which specific child / octant contains a given point.
        Note that the point is assumed to be inside this node and no
        checking is performed on the inside issue.
        """
        ...
    
    def GetDistance2ToBoundary(self, , vtkIncrementalOctreeNode, p_int):
        """
        V.GetDistance2ToBoundary((float, float, float),
            vtkIncrementalOctreeNode, int) -> float
        C++: double GetDistance2ToBoundary(const double point[3],
            vtkIncrementalOctreeNode *rootNode, int checkData)
        V.GetDistance2ToBoundary((float, float, float), [float, float,
            float], vtkIncrementalOctreeNode, int) -> float
        C++: double GetDistance2ToBoundary(const double point[3],
            double closest[3], vtkIncrementalOctreeNode *rootNode,
            int checkData)
        
        Compute the minimum squared distance from a point to this node,
        with all six boundaries considered. The data bounding box is
        checked if checkData is non-zero.
        """
        ...
    
    def GetDistance2ToInnerBoundary(self, , vtkIncrementalOctreeNode):
        """
        V.GetDistance2ToInnerBoundary((float, float, float),
            vtkIncrementalOctreeNode) -> float
        C++: double GetDistance2ToInnerBoundary(const double point[3],
            vtkIncrementalOctreeNode *rootNode)
        
        Given a point inside this node, get the minimum squared distance
        to all inner boundaries. An inner boundary is a node's face that
        is shared by another non-root node.
        """
        ...
    
    def GetMaxBounds(self):
        """
        V.GetMaxBounds() -> (float, float, float)
        C++: virtual double *GetMaxBounds()
        
        Get access to MaxBounds. Do not free this pointer.
        """
        ...
    
    def GetMaxDataBounds(self):
        """
        V.GetMaxDataBounds() -> (float, ...)
        C++: double *GetMaxDataBounds()
        
        Get access to MaxDataBounds. Note that MaxDataBounds is not valid
        until point insertion.
        """
        ...
    
    def GetMinBounds(self):
        """
        V.GetMinBounds() -> (float, float, float)
        C++: virtual double *GetMinBounds()
        
        Get access to MinBounds. Do not free this pointer.
        """
        ...
    
    def GetMinDataBounds(self):
        """
        V.GetMinDataBounds() -> (float, ...)
        C++: double *GetMinDataBounds()
        
        Get access to MinDataBounds. Note that MinDataBounds is not valid
        until point insertion.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Given a the name of a base class of this class type, return the
        distance of inheritance between this class type and the named
        class (how many generations of inheritance are there between this
        class and the named class). If the named class is not in this
        class's inheritance tree, return a negative value. Valid
        responses will always be nonnegative. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Given a the name of a base class of this class type, return the
        distance of inheritance between this class type and the named
        class (how many generations of inheritance are there between this
        class and the named class). If the named class is not in this
        class's inheritance tree, return a negative value. Valid
        responses will always be nonnegative. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def GetNumberOfPoints(self):
        """
        V.GetNumberOfPoints() -> int
        C++: virtual int GetNumberOfPoints()
        
        Get the number of points inside or under this node.
        """
        ...
    
    def GetPointIdSet(self):
        """
        V.GetPointIdSet() -> vtkIdList
        C++: virtual vtkIdList *GetPointIdSet()
        
        Get the list of point indices, nullptr for a non-leaf node.
        """
        ...
    
    def InsertPoint(self, vtkPoints, , p_int, *int, **kwargs):
        """
        V.InsertPoint(vtkPoints, (float, float, float), int, [int, ...],
            int) -> int
        C++: int InsertPoint(vtkPoints *points, const double newPnt[3],
            int maxPts, vtkIdType *pntId, int ptMode)
        
        This function is called after a successful point-insertion check
        and only applies to a leaf node. Prior to a call to this
        function, the octree should have been retrieved top-down to find
        the specific leaf node in which this new point (newPt) will be
        inserted. The actual index of the new point (to be inserted to
        points) is stored in pntId. Argument ptMode specifies whether the
        point is not inserted at all but instead only the point index is
        provided upon 0, the point is inserted via vtkPoints::
        InsertPoint() upon 1, or it is inserted via
        vtkPoints::InsertNextPoint() upon 2. For case 0, pntId needs to
        be specified. For cases 1 and 2, the actual point index is
        returned via pntId. Note that this function always returns 1 to
        indicate the success of point insertion.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Return 1 if this class is the same type of (or a subclass of) the
        named class. Returns 0 otherwise. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def IsLeaf(self):
        """
        V.IsLeaf() -> int
        C++: int IsLeaf()
        
        Determine whether or not this node is a leaf.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Return 1 if this class type is the same type of (or a subclass
        of) the named class. Returns 0 otherwise. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkIncrementalOctreeNode
        C++: vtkIncrementalOctreeNode *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkIncrementalOctreeNode
        C++: static vtkIncrementalOctreeNode *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetBounds(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5):
        """
        V.SetBounds(float, float, float, float, float, float)
        C++: void SetBounds(double x1, double x2, double y1, double y2,
            double z1, double z2)
        
        Set the spatial bounding box of the node. This function sets a
        default data bounding box.
        """
        ...
    
    def __delattr__(self, *args, **kwargs):
        """ Implement delattr(self, name). """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        ...
    
    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        ...
    
    def __setattr__(self, *args, **kwargs):
        """ Implement setattr(self, name, value). """
        ...
    
    def __str__(self, *args, **kwargs) -> str:
        """ Return str(self). """
        ...
    
    __this__ = ...
    __dict__ = ...
    __vtkname__ = ...


