"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkCutMaterial(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkCutMaterial - Automatically computes the cut plane for a material
    array pair.
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkCutMaterial computes a cut plane based on an up vector, center of
    the bounding box and the location of the maximum variable value.
     These computed values are available so that they can be used to set
    the camera for the best view of the plane.
    """
    def GetArrayName(self):
        """
        V.GetArrayName() -> string
        C++: virtual char *GetArrayName()
        
        For now, we just use the cell values. The array name to cut.
        """
        ...
    
    def GetCenterPoint(self):
        """
        V.GetCenterPoint() -> (float, float, float)
        C++: virtual double *GetCenterPoint()
        
        Accesses to the values computed during the execute method.  They
        could be used to get a good camera view for the resulting plane.
        """
        ...
    
    def GetMaterial(self):
        """
        V.GetMaterial() -> int
        C++: virtual int GetMaterial()
        
        Material to probe.
        """
        ...
    
    def GetMaterialArrayName(self):
        """
        V.GetMaterialArrayName() -> string
        C++: virtual char *GetMaterialArrayName()
        
        Cell array that contains the material values.
        """
        ...
    
    def GetMaximumPoint(self):
        """
        V.GetMaximumPoint() -> (float, float, float)
        C++: virtual double *GetMaximumPoint()
        
        Accesses to the values computed during the execute method.  They
        could be used to get a good camera view for the resulting plane.
        """
        ...
    
    def GetNormal(self):
        """
        V.GetNormal() -> (float, float, float)
        C++: virtual double *GetNormal()
        
        Accesses to the values computed during the execute method.  They
        could be used to get a good camera view for the resulting plane.
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
    
    def GetUpVector(self):
        """
        V.GetUpVector() -> (float, float, float)
        C++: virtual double *GetUpVector()
        
        The last piece of information that specifies the plane.
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
        V.NewInstance() -> vtkCutMaterial
        C++: vtkCutMaterial *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCutMaterial
        C++: static vtkCutMaterial *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetArrayName(self, string):
        """
        V.SetArrayName(string)
        C++: virtual void SetArrayName(const char *_arg)
        
        For now, we just use the cell values. The array name to cut.
        """
        ...
    
    def SetMaterial(self, p_int):
        """
        V.SetMaterial(int)
        C++: virtual void SetMaterial(int _arg)
        
        Material to probe.
        """
        ...
    
    def SetMaterialArrayName(self, string):
        """
        V.SetMaterialArrayName(string)
        C++: virtual void SetMaterialArrayName(const char *_arg)
        
        Cell array that contains the material values.
        """
        ...
    
    def SetUpVector(self, p_float, p_float_1, p_float_2):
        """
        V.SetUpVector(float, float, float)
        C++: virtual void SetUpVector(double _arg1, double _arg2,
            double _arg3)
        V.SetUpVector((float, float, float))
        C++: virtual void SetUpVector(const double _arg[3])
        
        The last piece of information that specifies the plane.
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


