"""
This type stub file was generated by pyright.
"""

from .vtkHigherOrderQuadrilateral import vtkHigherOrderQuadrilateral

class vtkBezierQuadrilateral(vtkHigherOrderQuadrilateral):
    """
    vtkBezierQuadrilateral
    
    Superclass: vtkHigherOrderQuadrilateral
    
    See Also:
    """
    def EvaluateLocationProjectedNode(self, p_int, p_int_1, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.EvaluateLocationProjectedNode(int, int, [float, float, float],
            [float, ...])
        C++: void EvaluateLocationProjectedNode(int &subId,
            const vtkIdType point_id, double x[3], double *weights)
        """
        ...
    
    def GetCellType(self):
        """
        V.GetCellType() -> int
        C++: int GetCellType() override;
        
        Return the type of cell.
        """
        ...
    
    def GetEdge(self, p_int):
        """
        V.GetEdge(int) -> vtkCell
        C++: vtkCell *GetEdge(int edgeId) override;
        
        Return the edge cell from the edgeId of the cell.
        """
        ...
    
    def getEdgeCell(self):
        """
        V.getEdgeCell() -> vtkHigherOrderCurve
        C++: virtual vtkHigherOrderCurve *getEdgeCell() override;
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
    
    def GetRationalWeights(self):
        """
        V.GetRationalWeights() -> vtkDoubleArray
        C++: vtkDoubleArray *GetRationalWeights()
        """
        ...
    
    def InterpolateDerivs(self, , *float):
        """
        V.InterpolateDerivs((float, float, float), [float, ...])
        C++: void InterpolateDerivs(const double pcoords[3],
            double *derivs) override;
        """
        ...
    
    def InterpolateFunctions(self, , *float):
        """
        V.InterpolateFunctions((float, float, float), [float, ...])
        C++: void InterpolateFunctions(const double pcoords[3],
            double *weights) override;
        
        Compute the interpolation functions/derivatives (aka shape
        functions/derivatives) No-ops at this level. Typically overridden
        in subclasses.
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
        V.NewInstance() -> vtkBezierQuadrilateral
        C++: vtkBezierQuadrilateral *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkBezierQuadrilateral
        C++: static vtkBezierQuadrilateral *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetRationalWeightsFromPointData(self, vtkPointData, p_int):
        """
        V.SetRationalWeightsFromPointData(vtkPointData, int)
        C++: void SetRationalWeightsFromPointData(
            vtkPointData *point_data, const vtkIdType numPts)
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

