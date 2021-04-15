"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkDataSetTriangleFilter(__vtkmodules_vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    """
    vtkDataSetTriangleFilter - triangulate any type of dataset
    
    Superclass: vtkUnstructuredGridAlgorithm
    
    vtkDataSetTriangleFilter generates n-dimensional simplices from any
    input dataset. That is, 3D cells are converted to tetrahedral meshes,
    2D cells to triangles, and so on. The triangulation is guaranteed to
    be compatible.
    
    This filter uses simple 1D and 2D triangulation techniques for cells
    that are of topological dimension 2 or less. For 3D cells--due to the
    issue of face compatibility across quadrilateral faces (which way to
    orient the diagonal?)--a fancier ordered Delaunay triangulation is
    used. This approach produces templates on the fly for triangulating
    the cells. The templates are then used to do the actual
    triangulation.
    
    @sa
    vtkOrderedTriangulator vtkTriangleFilter
    """
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
    
    def GetTetrahedraOnly(self):
        """
        V.GetTetrahedraOnly() -> int
        C++: virtual vtkTypeBool GetTetrahedraOnly()
        
        When On this filter will cull all 1D and 2D cells from the
        output. The default is Off.
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
        V.NewInstance() -> vtkDataSetTriangleFilter
        C++: vtkDataSetTriangleFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDataSetTriangleFilter
        C++: static vtkDataSetTriangleFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetTetrahedraOnly(self, p_int):
        """
        V.SetTetrahedraOnly(int)
        C++: virtual void SetTetrahedraOnly(vtkTypeBool _arg)
        
        When On this filter will cull all 1D and 2D cells from the
        output. The default is Off.
        """
        ...
    
    def TetrahedraOnlyOff(self):
        """
        V.TetrahedraOnlyOff()
        C++: virtual void TetrahedraOnlyOff()
        
        When On this filter will cull all 1D and 2D cells from the
        output. The default is Off.
        """
        ...
    
    def TetrahedraOnlyOn(self):
        """
        V.TetrahedraOnlyOn()
        C++: virtual void TetrahedraOnlyOn()
        
        When On this filter will cull all 1D and 2D cells from the
        output. The default is Off.
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


