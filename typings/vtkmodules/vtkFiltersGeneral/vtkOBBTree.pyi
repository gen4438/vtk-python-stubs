"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonDataModel as __vtkmodules_vtkCommonDataModel

class vtkOBBTree(__vtkmodules_vtkCommonDataModel.vtkAbstractCellLocator):
    """
    vtkOBBTree - generate oriented bounding box (OBB) tree
    
    Superclass: vtkAbstractCellLocator
    
    vtkOBBTree is an object to generate oriented bounding box (OBB)
    trees. An oriented bounding box is a bounding box that does not
    necessarily line up along coordinate axes. The OBB tree is a
    hierarchical tree structure of such boxes, where deeper levels of OBB
    confine smaller regions of space.
    
    To build the OBB, a recursive, top-down process is used. First, the
    root OBB is constructed by finding the mean and covariance matrix of
    the cells (and their points) that define the dataset. The
    eigenvectors of the covariance matrix are extracted, giving a set of
    three orthogonal vectors that define the tightest-fitting OBB. To
    create the two children OBB's, a split plane is found that
    (approximately) divides the number cells in half. These are then
    assigned to the children OBB's. This process then continues until the
    MaxLevel ivar limits the recursion, or no split plane can be found.
    
    A good reference for OBB-trees is Gottschalk & Manocha in Proceedings
    of Siggraph `96.
    
    @warning
    Since this algorithms works from a list of cells, the OBB tree will
    only bound the "geometry" attached to the cells if the convex hull of
    the cells bounds the geometry.
    
    @warning
    Long, skinny cells (i.e., cells with poor aspect ratio) may cause
    unsatisfactory results. This is due to the fact that this is a
    top-down implementation of the OBB tree, requiring that one or more
    complete cells are contained in each OBB. This requirement makes it
    hard to find good split planes during the recursion process. A
    bottom-up implementation would go a long way to correcting this
    problem.
    
    @sa
    vtkLocator vtkCellLocator vtkPointLocator
    """
    def BuildLocator(self):
        """
        V.BuildLocator()
        C++: void BuildLocator() override;
        
        Satisfy locator's abstract interface, see vtkLocator.
        """
        ...
    
    def ComputeOBB(self, vtkPoints, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.ComputeOBB(vtkPoints, [float, float, float], [float, float,
            float], [float, float, float], [float, float, float], [float,
            float, float])
        C++: static void ComputeOBB(vtkPoints *pts, double corner[3],
            double max[3], double mid[3], double min[3], double size[3])
        V.ComputeOBB(vtkDataSet, [float, float, float], [float, float,
            float], [float, float, float], [float, float, float], [float,
            float, float])
        C++: void ComputeOBB(vtkDataSet *input, double corner[3],
            double max[3], double mid[3], double min[3], double size[3])
        
        Compute an OBB from the list of points given. Return the corner
        point and the three axes defining the orientation of the OBB.
        Also return a sorted list of relative "sizes" of axes for
        comparison purposes.
        """
        ...
    
    def FreeSearchStructure(self):
        """
        V.FreeSearchStructure()
        C++: void FreeSearchStructure() override;
        
        Satisfy locator's abstract interface, see vtkLocator.
        """
        ...
    
    def GenerateRepresentation(self, p_int, vtkPolyData):
        """
        V.GenerateRepresentation(int, vtkPolyData)
        C++: void GenerateRepresentation(int level, vtkPolyData *pd)
            override;
        
        Create polygonal representation for OBB tree at specified level.
        If level < 0, then the leaf OBB nodes will be gathered. The
        aspect ratio (ar) and line diameter (d) are used to control the
        building of the representation. If a OBB node edge ratio's are
        greater than ar, then the dimension of the OBB is collapsed
        (OBB->plane->line). A "line" OBB will be represented either as
        two crossed polygons, or as a line, depending on the relative
        diameter of the OBB compared to the diameter (d).
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard type and print methods.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard type and print methods.
        """
        ...
    
    def InsideOrOutside(self, ):
        """
        V.InsideOrOutside((float, float, float)) -> int
        C++: int InsideOrOutside(const double point[3])
        
        Determine whether a point is inside or outside the data used to
        build this OBB tree.  The data must be a closed surface
        vtkPolyData data set. The return value is +1 if outside, -1 if
        inside, and 0 if undecided.
        """
        ...
    
    def IntersectWithLine(self, , , vtkPoints, vtkIdList):
        """
        V.IntersectWithLine((float, float, float), (float, float, float),
            vtkPoints, vtkIdList) -> int
        C++: int IntersectWithLine(const double a0[3], const double a1[3],
             vtkPoints *points, vtkIdList *cellIds) override;
        V.IntersectWithLine((float, float, float), (float, float, float),
            float, float, [float, float, float], [float, float, float],
            int, int, vtkGenericCell) -> int
        C++: int IntersectWithLine(const double a0[3], const double a1[3],
             double tol, double &t, double x[3], double pcoords[3],
            int &subId, vtkIdType &cellId, vtkGenericCell *cell) override;
        V.IntersectWithLine((float, float, float), (float, float, float),
            float, float, [float, float, float], [float, float, float],
            int) -> int
        C++: virtual int IntersectWithLine(const double p1[3],
            const double p2[3], double tol, double &t, double x[3],
            double pcoords[3], int &subId)
        V.IntersectWithLine((float, float, float), (float, float, float),
            float, float, [float, float, float], [float, float, float],
            int, int) -> int
        C++: virtual int IntersectWithLine(const double p1[3],
            const double p2[3], double tol, double &t, double x[3],
            double pcoords[3], int &subId, vtkIdType &cellId)
        
        Take the passed line segment and intersect it with the data set.
        This method assumes that the data set is a vtkPolyData that
        describes a closed surface, and the intersection points that are
        returned in 'points' alternate between entrance points and exit
        points. The return value of the function is 0 if no intersections
        were found,
        -1 if point 'a0' lies inside the closed surface, or +1 if point
           'a0' lies outside the closed surface. Either 'points' or
           'cellIds' can be set to nullptr if you don't want to receive
           that information.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard type and print methods.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard type and print methods.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkOBBTree
        C++: vtkOBBTree *NewInstance()
        
        Standard type and print methods.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOBBTree
        C++: static vtkOBBTree *SafeDownCast(vtkObjectBase *o)
        
        Standard type and print methods.
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


