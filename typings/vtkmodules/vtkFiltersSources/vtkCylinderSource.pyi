"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkCylinderSource(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkCylinderSource - generate a cylinder centered at origin
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkCylinderSource creates a polygonal cylinder centered at Center;
    The axis of the cylinder is aligned along the global y-axis. The
    height and radius of the cylinder can be specified, as well as the
    number of sides. It is also possible to control whether the cylinder
    is open-ended or capped. If you have the end points of the cylinder,
    you should use a vtkLineSource followed by a vtkTubeFilter instead of
    the vtkCylinderSource.
    """
    def CappingOff(self):
        """
        V.CappingOff()
        C++: virtual void CappingOff()
        
        Turn on/off whether to cap cylinder with polygons. Initial value
        is true.
        """
        ...
    
    def CappingOn(self):
        """
        V.CappingOn()
        C++: virtual void CappingOn()
        
        Turn on/off whether to cap cylinder with polygons. Initial value
        is true.
        """
        ...
    
    def GetCapping(self):
        """
        V.GetCapping() -> int
        C++: virtual vtkTypeBool GetCapping()
        
        Turn on/off whether to cap cylinder with polygons. Initial value
        is true.
        """
        ...
    
    def GetCenter(self):
        """
        V.GetCenter() -> (float, float, float)
        C++: virtual double *GetCenter()
        
        Set/Get cylinder center. Initial value is (0.0,0.0,0.0)
        """
        ...
    
    def GetHeight(self):
        """
        V.GetHeight() -> float
        C++: virtual double GetHeight()
        
        Set the height of the cylinder. Initial value is 1.
        """
        ...
    
    def GetHeightMaxValue(self):
        """
        V.GetHeightMaxValue() -> float
        C++: virtual double GetHeightMaxValue()
        
        Set the height of the cylinder. Initial value is 1.
        """
        ...
    
    def GetHeightMinValue(self):
        """
        V.GetHeightMinValue() -> float
        C++: virtual double GetHeightMinValue()
        
        Set the height of the cylinder. Initial value is 1.
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
    
    def GetOutputPointsPrecision(self):
        """
        V.GetOutputPointsPrecision() -> int
        C++: virtual int GetOutputPointsPrecision()
        
        Set/get the desired precision for the output points.
        vtkAlgorithm::SINGLE_PRECISION - Output single-precision floating
        point. vtkAlgorithm::DOUBLE_PRECISION - Output double-precision
        floating point.
        """
        ...
    
    def GetRadius(self):
        """
        V.GetRadius() -> float
        C++: virtual double GetRadius()
        
        Set the radius of the cylinder. Initial value is 0.5
        """
        ...
    
    def GetRadiusMaxValue(self):
        """
        V.GetRadiusMaxValue() -> float
        C++: virtual double GetRadiusMaxValue()
        
        Set the radius of the cylinder. Initial value is 0.5
        """
        ...
    
    def GetRadiusMinValue(self):
        """
        V.GetRadiusMinValue() -> float
        C++: virtual double GetRadiusMinValue()
        
        Set the radius of the cylinder. Initial value is 0.5
        """
        ...
    
    def GetResolution(self):
        """
        V.GetResolution() -> int
        C++: virtual int GetResolution()
        
        Set the number of facets used to define cylinder. Initial value
        is 6.
        """
        ...
    
    def GetResolutionMaxValue(self):
        """
        V.GetResolutionMaxValue() -> int
        C++: virtual int GetResolutionMaxValue()
        
        Set the number of facets used to define cylinder. Initial value
        is 6.
        """
        ...
    
    def GetResolutionMinValue(self):
        """
        V.GetResolutionMinValue() -> int
        C++: virtual int GetResolutionMinValue()
        
        Set the number of facets used to define cylinder. Initial value
        is 6.
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
        V.NewInstance() -> vtkCylinderSource
        C++: vtkCylinderSource *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCylinderSource
        C++: static vtkCylinderSource *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCapping(self, p_int):
        """
        V.SetCapping(int)
        C++: virtual void SetCapping(vtkTypeBool _arg)
        
        Turn on/off whether to cap cylinder with polygons. Initial value
        is true.
        """
        ...
    
    def SetCenter(self, p_float, p_float_1, p_float_2):
        """
        V.SetCenter(float, float, float)
        C++: virtual void SetCenter(double _arg1, double _arg2,
            double _arg3)
        V.SetCenter((float, float, float))
        C++: virtual void SetCenter(const double _arg[3])
        
        Set/Get cylinder center. Initial value is (0.0,0.0,0.0)
        """
        ...
    
    def SetHeight(self, p_float):
        """
        V.SetHeight(float)
        C++: virtual void SetHeight(double _arg)
        
        Set the height of the cylinder. Initial value is 1.
        """
        ...
    
    def SetOutputPointsPrecision(self, p_int):
        """
        V.SetOutputPointsPrecision(int)
        C++: virtual void SetOutputPointsPrecision(int _arg)
        
        Set/get the desired precision for the output points.
        vtkAlgorithm::SINGLE_PRECISION - Output single-precision floating
        point. vtkAlgorithm::DOUBLE_PRECISION - Output double-precision
        floating point.
        """
        ...
    
    def SetRadius(self, p_float):
        """
        V.SetRadius(float)
        C++: virtual void SetRadius(double _arg)
        
        Set the radius of the cylinder. Initial value is 0.5
        """
        ...
    
    def SetResolution(self, p_int):
        """
        V.SetResolution(int)
        C++: virtual void SetResolution(int _arg)
        
        Set the number of facets used to define cylinder. Initial value
        is 6.
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


