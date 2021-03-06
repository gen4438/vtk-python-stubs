"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkPolyPointSource(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkPolyPointSource - create points from a list of input points
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkPolyPointSource is a source object that creates a vert from
    user-specified points. The output is a vtkPolyData.
    """
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Get the mtime plus consider its Points
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
        C++: vtkIdType GetNumberOfPoints()
        
        Set the number of points in the poly line.
        """
        ...
    
    def GetPoints(self):
        """
        V.GetPoints() -> vtkPoints
        C++: virtual vtkPoints *GetPoints()
        
        Get the points.
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
        V.NewInstance() -> vtkPolyPointSource
        C++: vtkPolyPointSource *NewInstance()
        """
        ...
    
    def Resize(self, p_int):
        """
        V.Resize(int)
        C++: void Resize(vtkIdType numPoints)
        
        Resize while preserving data.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPolyPointSource
        C++: static vtkPolyPointSource *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetNumberOfPoints(self, p_int):
        """
        V.SetNumberOfPoints(int)
        C++: void SetNumberOfPoints(vtkIdType numPoints)
        
        Set the number of points in the poly line.
        """
        ...
    
    def SetPoint(self, p_int, p_float, p_float_1, p_float_2):
        """
        V.SetPoint(int, float, float, float)
        C++: void SetPoint(vtkIdType id, double x, double y, double z)
        
        Set a point location.
        """
        ...
    
    def SetPoints(self, vtkPoints):
        """
        V.SetPoints(vtkPoints)
        C++: void SetPoints(vtkPoints *points)
        
        Get the points.
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


