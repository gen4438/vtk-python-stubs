"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkAxes(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkAxes - create an x-y-z axes
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkAxes creates three lines that form an x-y-z axes. The origin of
    the axes is user specified (0,0,0 is default), and the size is
    specified with a scale factor. Three scalar values are generated for
    the three lines and can be used (via color map) to indicate a
    particular coordinate axis.
    """
    def ComputeNormalsOff(self):
        """
        V.ComputeNormalsOff()
        C++: virtual void ComputeNormalsOff()
        
        Option for computing normals.  By default they are computed.
        """
        ...
    
    def ComputeNormalsOn(self):
        """
        V.ComputeNormalsOn()
        C++: virtual void ComputeNormalsOn()
        
        Option for computing normals.  By default they are computed.
        """
        ...
    
    def GetComputeNormals(self):
        """
        V.GetComputeNormals() -> int
        C++: virtual vtkTypeBool GetComputeNormals()
        
        Option for computing normals.  By default they are computed.
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
    
    def GetOrigin(self):
        """
        V.GetOrigin() -> (float, float, float)
        C++: virtual double *GetOrigin()
        
        Set the origin of the axes.
        """
        ...
    
    def GetScaleFactor(self):
        """
        V.GetScaleFactor() -> float
        C++: virtual double GetScaleFactor()
        
        Set the scale factor of the axes. Used to control size.
        """
        ...
    
    def GetSymmetric(self):
        """
        V.GetSymmetric() -> int
        C++: virtual vtkTypeBool GetSymmetric()
        
        If Symmetric is on, the axis continue to negative values.
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
        V.NewInstance() -> vtkAxes
        C++: vtkAxes *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAxes
        C++: static vtkAxes *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetComputeNormals(self, p_int):
        """
        V.SetComputeNormals(int)
        C++: virtual void SetComputeNormals(vtkTypeBool _arg)
        
        Option for computing normals.  By default they are computed.
        """
        ...
    
    def SetOrigin(self, p_float, p_float_1, p_float_2):
        """
        V.SetOrigin(float, float, float)
        C++: virtual void SetOrigin(double _arg1, double _arg2,
            double _arg3)
        V.SetOrigin((float, float, float))
        C++: virtual void SetOrigin(const double _arg[3])
        
        Set the origin of the axes.
        """
        ...
    
    def SetScaleFactor(self, p_float):
        """
        V.SetScaleFactor(float)
        C++: virtual void SetScaleFactor(double _arg)
        
        Set the scale factor of the axes. Used to control size.
        """
        ...
    
    def SetSymmetric(self, p_int):
        """
        V.SetSymmetric(int)
        C++: virtual void SetSymmetric(vtkTypeBool _arg)
        
        If Symmetric is on, the axis continue to negative values.
        """
        ...
    
    def SymmetricOff(self):
        """
        V.SymmetricOff()
        C++: virtual void SymmetricOff()
        
        If Symmetric is on, the axis continue to negative values.
        """
        ...
    
    def SymmetricOn(self):
        """
        V.SymmetricOn()
        C++: virtual void SymmetricOn()
        
        If Symmetric is on, the axis continue to negative values.
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

