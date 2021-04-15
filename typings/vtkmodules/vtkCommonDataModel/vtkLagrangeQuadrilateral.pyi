"""
This type stub file was generated by pyright.
"""

from .vtkHigherOrderQuadrilateral import vtkHigherOrderQuadrilateral

class vtkLagrangeQuadrilateral(vtkHigherOrderQuadrilateral):
    """
    vtkLagrangeQuadrilateral
    
    Superclass: vtkHigherOrderQuadrilateral
    
    See Also:
    """
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
        V.NewInstance() -> vtkLagrangeQuadrilateral
        C++: vtkLagrangeQuadrilateral *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkLagrangeQuadrilateral
        C++: static vtkLagrangeQuadrilateral *SafeDownCast(
            vtkObjectBase *o)
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


