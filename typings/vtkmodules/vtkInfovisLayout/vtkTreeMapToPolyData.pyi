"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkTreeMapToPolyData(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkTreeMapToPolyData - converts a tree to a polygonal data
    representing a tree map
    
    Superclass: vtkPolyDataAlgorithm
    
    This algorithm requires that the vtkTreeMapLayout filter has already
    applied to the data in order to create the quadruple array (min x,
    max x, min y, max y) of bounds for each vertex of the tree.
    """
    def FillInputPortInformation(self, p_int, vtkInformation):
        """
        V.FillInputPortInformation(int, vtkInformation) -> int
        C++: int FillInputPortInformation(int port, vtkInformation *info)
            override;
        
        Fill the input port information objects for this algorithm.  This
        is invoked by the first call to GetInputPortInformation for each
        port so subclasses can specify what they can handle.
        """
        ...
    
    def GetAddNormals(self):
        """
        V.GetAddNormals() -> bool
        C++: virtual bool GetAddNormals()
        
        The spacing along the z-axis between tree map levels.
        """
        ...
    
    def GetLevelDeltaZ(self):
        """
        V.GetLevelDeltaZ() -> float
        C++: virtual double GetLevelDeltaZ()
        
        The spacing along the z-axis between tree map levels.
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
        V.NewInstance() -> vtkTreeMapToPolyData
        C++: vtkTreeMapToPolyData *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTreeMapToPolyData
        C++: static vtkTreeMapToPolyData *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAddNormals(self, bool):
        """
        V.SetAddNormals(bool)
        C++: virtual void SetAddNormals(bool _arg)
        
        The spacing along the z-axis between tree map levels.
        """
        ...
    
    def SetLevelArrayName(self, string):
        """
        V.SetLevelArrayName(string)
        C++: virtual void SetLevelArrayName(const char *name)
        
        The field containing the level of each tree node. This can be
        added using vtkTreeLevelsFilter before this filter. If this is
        not present, the filter simply calls tree->GetLevel(v) for each
        vertex, which will produce the same result, but may not be as
        efficient.
        """
        ...
    
    def SetLevelDeltaZ(self, p_float):
        """
        V.SetLevelDeltaZ(float)
        C++: virtual void SetLevelDeltaZ(double _arg)
        
        The spacing along the z-axis between tree map levels.
        """
        ...
    
    def SetRectanglesArrayName(self, string):
        """
        V.SetRectanglesArrayName(string)
        C++: virtual void SetRectanglesArrayName(const char *name)
        
        The field containing quadruples of the form (min x, max x, min y,
        max y) representing the bounds of the rectangles for each vertex.
        This array may be added to the tree using vtkTreeMapLayout.
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


