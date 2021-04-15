"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkKdNode(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkKdNode - This class represents a single spatial region
        in an 3D axis aligned binary spatial partitioning.
    
    Superclass: vtkObject
    
    It is assumed
        the region bounds some set of points.  Regions are represented
        as nodes in a binary tree.
    
    @sa
         vtkKdTree vtkOBSPCuts
    """
    def AddChildNodes(self, vtkKdNode, vtkKdNode_1):
        """
        V.AddChildNodes(vtkKdNode, vtkKdNode)
        C++: void AddChildNodes(vtkKdNode *left, vtkKdNode *right)
        
        Add the left and right children.
        """
        ...
    
    def ContainsBox(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5, p_int):
        """
        V.ContainsBox(float, float, float, float, float, float, int)
            -> int
        C++: int ContainsBox(double x1, double x2, double y1, double y2,
            double z1, double z2, int useDataBounds)
        
        Return 1 if this spatial region entirely contains a box specified
        by it's bounds. Use the possibly smaller bounds of the points
        within the region if useDataBounds is non-zero.
        """
        ...
    
    def ContainsPoint(self, p_float, p_float_1, p_float_2, p_int):
        """
        V.ContainsPoint(float, float, float, int) -> int
        C++: vtkTypeBool ContainsPoint(double x, double y, double z,
            int useDataBounds)
        
        Return 1 if this spatial region entirely contains the given
        point. Use the possibly smaller bounds of the points within the
        region if useDataBounds is non-zero.
        """
        ...
    
    def DeleteChildNodes(self):
        """
        V.DeleteChildNodes()
        C++: void DeleteChildNodes()
        
        Delete the left and right children.
        """
        ...
    
    def GetBounds(self, *float):
        """
        V.GetBounds([float, ...])
        C++: void GetBounds(double *b)
        
        Set/Get the bounds of the spatial region represented by this
        node. Caller allocates storage for 6-vector in GetBounds.
        """
        ...
    
    def GetDataBounds(self, *float):
        """
        V.GetDataBounds([float, ...])
        C++: void GetDataBounds(double *b)
        
        Set/Get the bounds of the points contained in this spatial
        region. This may be smaller than the bounds of the region itself.
        Caller allocates storage for 6-vector in GetDataBounds.
        """
        ...
    
    def GetDim(self):
        """
        V.GetDim() -> int
        C++: virtual int GetDim()
        
        Set/Get the dimension along which this region is divided. (0 - x,
        1 - y, 2 - z, 3 - leaf node (default)).
        """
        ...
    
    def GetDistance2ToBoundary(self, p_float, p_float_1, p_float_2, p_int):
        """
        V.GetDistance2ToBoundary(float, float, float, int) -> float
        C++: double GetDistance2ToBoundary(double x, double y, double z,
            int useDataBounds)
        V.GetDistance2ToBoundary(float, float, float, [float, ...], int)
            -> float
        C++: double GetDistance2ToBoundary(double x, double y, double z,
            double *boundaryPt, int useDataBounds)
        
        Calculate the distance squared from any point to the boundary of
        this region.  Use the boundary of the points within the region if
        useDataBounds is non-zero.
        """
        ...
    
    def GetDistance2ToInnerBoundary(self, p_float, p_float_1, p_float_2):
        """
        V.GetDistance2ToInnerBoundary(float, float, float) -> float
        C++: double GetDistance2ToInnerBoundary(double x, double y,
            double z)
        
        Calculate the distance from the specified point (which is
        required to be inside this spatial region) to an interior
        boundary.  An interior boundary is one that is not also an
        boundary of the entire space partitioned by the tree of
        vtkKdNode's.
        """
        ...
    
    def GetDivisionPosition(self):
        """
        V.GetDivisionPosition() -> float
        C++: virtual double GetDivisionPosition()
        
        Get the location of the division plane along the axis the region
        is divided.  See also GetDim().  The result is undertermined if
        this node is not divided (a leaf node).
        """
        ...
    
    def GetID(self):
        """
        V.GetID() -> int
        C++: virtual int GetID()
        
        Set/Get the ID associated with the region described by this node.
         If this is not a leaf node, this value should be -1.
        """
        ...
    
    def GetLeft(self):
        """
        V.GetLeft() -> vtkKdNode
        C++: virtual vtkKdNode *GetLeft()
        
        Set/Get a pointer to the left child of this node.
        """
        ...
    
    def GetMaxBounds(self):
        """
        V.GetMaxBounds() -> (float, float, float)
        C++: double *GetMaxBounds()
        """
        ...
    
    def GetMaxDataBounds(self):
        """
        V.GetMaxDataBounds() -> (float, float, float)
        C++: double *GetMaxDataBounds()
        """
        ...
    
    def GetMaxID(self):
        """
        V.GetMaxID() -> int
        C++: virtual int GetMaxID()
        
        If this node is not a leaf node, there are leaf nodes below it
        whose regions represent a partitioning of this region.  The IDs
        of these leaf nodes form a contiguous set.  Set/Get the range of
        the IDs of the leaf nodes below this node.  If this is already a
        leaf node, these values should be the same as the ID.
        """
        ...
    
    def GetMinBounds(self):
        """
        V.GetMinBounds() -> (float, float, float)
        C++: double *GetMinBounds()
        
        Get a pointer to the 3 bound minima (xmin, ymin and zmin) or the
        3 bound maxima (xmax, ymax, zmax).  Don't free this pointer.
        """
        ...
    
    def GetMinDataBounds(self):
        """
        V.GetMinDataBounds() -> (float, float, float)
        C++: double *GetMinDataBounds()
        
        Get a pointer to the 3 data bound minima (xmin, ymin and zmin) or
        the 3 data bound maxima (xmax, ymax, zmax).  Don't free this
        pointer.
        """
        ...
    
    def GetMinID(self):
        """
        V.GetMinID() -> int
        C++: virtual int GetMinID()
        
        If this node is not a leaf node, there are leaf nodes below it
        whose regions represent a partitioning of this region.  The IDs
        of these leaf nodes form a contiguous set.  Set/Get the range of
        the IDs of the leaf nodes below this node.  If this is already a
        leaf node, these values should be the same as the ID.
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
        
        Set/Get the number of points contained in this region.
        """
        ...
    
    def GetRight(self):
        """
        V.GetRight() -> vtkKdNode
        C++: virtual vtkKdNode *GetRight()
        
        Set/Get a pointer to the right child of this node.
        """
        ...
    
    def GetUp(self):
        """
        V.GetUp() -> vtkKdNode
        C++: virtual vtkKdNode *GetUp()
        
        Set/Get a pointer to the parent of this node.
        """
        ...
    
    def IntersectsBox(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5, p_int):
        """
        V.IntersectsBox(float, float, float, float, float, float, int)
            -> int
        C++: int IntersectsBox(double x1, double x2, double y1, double y2,
             double z1, double z2, int useDataBounds)
        
        Return 1 if this spatial region intersects the axis-aligned box
        given by the bounds passed in.  Use the possibly smaller bounds
        of the points within the region if useDataBounds is non-zero.
        """
        ...
    
    def IntersectsCell(self, vtkCell, p_int, p_int_1, *float):
        """
        V.IntersectsCell(vtkCell, int, int, [float, ...]) -> int
        C++: int IntersectsCell(vtkCell *cell, int useDataBounds,
            int cellRegion=-1, double *cellBounds=nullptr)
        
        Return 1 if the cell specified intersects this region.  If you
        already know the ID of the region containing the cell's centroid,
        provide that as an argument.  If you already know the bounds of
        the cell, provide that as well, in the form of
        xmin,xmax,ymin,ymax,zmin, zmax.  Either of these may speed the
        calculation. Use the possibly smaller bounds of the points within
        the region if useDataBounds is non-zero.
        """
        ...
    
    def IntersectsRegion(self, vtkPlanesIntersection, p_int):
        """
        V.IntersectsRegion(vtkPlanesIntersection, int) -> int
        C++: int IntersectsRegion(vtkPlanesIntersection *pi,
            int useDataBounds)
        
        A vtkPlanesIntersection object represents a convex 3D region
        bounded by planes, and it is capable of computing intersections
        of boxes with itself.  Return 1 if this spatial region intersects
        the spatial region described by the vtkPlanesIntersection object.
        Use the possibly smaller bounds of the points within the region
        if useDataBounds is non-zero.
        """
        ...
    
    def IntersectsSphere2(self, p_float, p_float_1, p_float_2, p_float_3, p_int):
        """
        V.IntersectsSphere2(float, float, float, float, int) -> int
        C++: int IntersectsSphere2(double x, double y, double z,
            double rSquared, int useDataBounds)
        
        Return 1 if this spatial region intersects a sphere described by
        it's center and the square of it's radius. Use the possibly
        smaller bounds of the points within the region if useDataBounds
        is non-zero.
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
        V.NewInstance() -> vtkKdNode
        C++: vtkKdNode *NewInstance()
        """
        ...
    
    def PrintNode(self, p_int):
        """
        V.PrintNode(int)
        C++: void PrintNode(int depth)
        
        For debugging purposes, print out this node.
        """
        ...
    
    def PrintVerboseNode(self, p_int):
        """
        V.PrintVerboseNode(int)
        C++: void PrintVerboseNode(int depth)
        
        For debugging purposes, print out this node.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkKdNode
        C++: static vtkKdNode *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetBounds(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5):
        """
        V.SetBounds(float, float, float, float, float, float)
        C++: void SetBounds(double x1, double x2, double y1, double y2,
            double z1, double z2)
        V.SetBounds((float, float, float, float, float, float))
        C++: void SetBounds(const double b[6])
        
        Set/Get the bounds of the spatial region represented by this
        node. Caller allocates storage for 6-vector in GetBounds.
        """
        ...
    
    def SetDataBounds(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5):
        """
        V.SetDataBounds(float, float, float, float, float, float)
        C++: void SetDataBounds(double x1, double x2, double y1,
            double y2, double z1, double z2)
        V.SetDataBounds([float, ...])
        C++: void SetDataBounds(float *v)
        
        Set/Get the bounds of the points contained in this spatial
        region. This may be smaller than the bounds of the region itself.
        Caller allocates storage for 6-vector in GetDataBounds.
        """
        ...
    
    def SetDim(self, p_int):
        """
        V.SetDim(int)
        C++: virtual void SetDim(int _arg)
        
        Set/Get the dimension along which this region is divided. (0 - x,
        1 - y, 2 - z, 3 - leaf node (default)).
        """
        ...
    
    def SetID(self, p_int):
        """
        V.SetID(int)
        C++: virtual void SetID(int _arg)
        
        Set/Get the ID associated with the region described by this node.
         If this is not a leaf node, this value should be -1.
        """
        ...
    
    def SetLeft(self, vtkKdNode):
        """
        V.SetLeft(vtkKdNode)
        C++: void SetLeft(vtkKdNode *left)
        
        Set/Get a pointer to the left child of this node.
        """
        ...
    
    def SetMaxBounds(self, float_tuple):
        """
        V.SetMaxBounds((float, ...))
        C++: void SetMaxBounds(const double *mb)
        
        Set the xmax, ymax and zmax value of the bounds of this region
        """
        ...
    
    def SetMaxDataBounds(self, float_tuple):
        """
        V.SetMaxDataBounds((float, ...))
        C++: void SetMaxDataBounds(const double *mb)
        
        Set the xmax, ymax and zmax value of the bounds of this data
        within this region
        """
        ...
    
    def SetMaxID(self, p_int):
        """
        V.SetMaxID(int)
        C++: virtual void SetMaxID(int _arg)
        
        If this node is not a leaf node, there are leaf nodes below it
        whose regions represent a partitioning of this region.  The IDs
        of these leaf nodes form a contiguous set.  Set/Get the range of
        the IDs of the leaf nodes below this node.  If this is already a
        leaf node, these values should be the same as the ID.
        """
        ...
    
    def SetMinBounds(self, float_tuple):
        """
        V.SetMinBounds((float, ...))
        C++: void SetMinBounds(const double *mb)
        
        Set the xmin, ymin and zmin value of the bounds of this region
        """
        ...
    
    def SetMinDataBounds(self, float_tuple):
        """
        V.SetMinDataBounds((float, ...))
        C++: void SetMinDataBounds(const double *mb)
        
        Set the xmin, ymin and zmin value of the bounds of this data
        within this region
        """
        ...
    
    def SetMinID(self, p_int):
        """
        V.SetMinID(int)
        C++: virtual void SetMinID(int _arg)
        
        If this node is not a leaf node, there are leaf nodes below it
        whose regions represent a partitioning of this region.  The IDs
        of these leaf nodes form a contiguous set.  Set/Get the range of
        the IDs of the leaf nodes below this node.  If this is already a
        leaf node, these values should be the same as the ID.
        """
        ...
    
    def SetNumberOfPoints(self, p_int):
        """
        V.SetNumberOfPoints(int)
        C++: virtual void SetNumberOfPoints(int _arg)
        
        Set/Get the number of points contained in this region.
        """
        ...
    
    def SetRight(self, vtkKdNode):
        """
        V.SetRight(vtkKdNode)
        C++: void SetRight(vtkKdNode *right)
        
        Set/Get a pointer to the right child of this node.
        """
        ...
    
    def SetUp(self, vtkKdNode):
        """
        V.SetUp(vtkKdNode)
        C++: void SetUp(vtkKdNode *up)
        
        Set/Get a pointer to the parent of this node.
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


