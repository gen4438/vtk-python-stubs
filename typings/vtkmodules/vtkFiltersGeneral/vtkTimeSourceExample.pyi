"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkTimeSourceExample(__vtkmodules_vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    """
    vtkTimeSourceExample - no description provided.
    
    Superclass: vtkUnstructuredGridAlgorithm
    """
    def AnalyticOff(self):
        """
        V.AnalyticOff()
        C++: virtual void AnalyticOff()
        
        When off (the default) this source produces a discrete set of
        values. When on, this source produces a value analytically for
        any queried time.
        """
        ...
    
    def AnalyticOn(self):
        """
        V.AnalyticOn()
        C++: virtual void AnalyticOn()
        
        When off (the default) this source produces a discrete set of
        values. When on, this source produces a value analytically for
        any queried time.
        """
        ...
    
    def GetAnalytic(self):
        """
        V.GetAnalytic() -> int
        C++: virtual vtkTypeBool GetAnalytic()
        
        When off (the default) this source produces a discrete set of
        values. When on, this source produces a value analytically for
        any queried time.
        """
        ...
    
    def GetAnalyticMaxValue(self):
        """
        V.GetAnalyticMaxValue() -> int
        C++: virtual vtkTypeBool GetAnalyticMaxValue()
        
        When off (the default) this source produces a discrete set of
        values. When on, this source produces a value analytically for
        any queried time.
        """
        ...
    
    def GetAnalyticMinValue(self):
        """
        V.GetAnalyticMinValue() -> int
        C++: virtual vtkTypeBool GetAnalyticMinValue()
        
        When off (the default) this source produces a discrete set of
        values. When on, this source produces a value analytically for
        any queried time.
        """
        ...
    
    def GetGrowing(self):
        """
        V.GetGrowing() -> int
        C++: virtual vtkTypeBool GetGrowing()
        
        When off (the default) this produces a single cell data set. When
        on the number of cells (in the Y direction) grows and shrinks
        over time along a hat function.
        """
        ...
    
    def GetGrowingMaxValue(self):
        """
        V.GetGrowingMaxValue() -> int
        C++: virtual vtkTypeBool GetGrowingMaxValue()
        
        When off (the default) this produces a single cell data set. When
        on the number of cells (in the Y direction) grows and shrinks
        over time along a hat function.
        """
        ...
    
    def GetGrowingMinValue(self):
        """
        V.GetGrowingMinValue() -> int
        C++: virtual vtkTypeBool GetGrowingMinValue()
        
        When off (the default) this produces a single cell data set. When
        on the number of cells (in the Y direction) grows and shrinks
        over time along a hat function.
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
    
    def GetXAmplitude(self):
        """
        V.GetXAmplitude() -> float
        C++: virtual double GetXAmplitude()
        
        When 0.0 (the default) this produces a data set that is
        stationary. When on the data set moves in the X/Y plane over a
        sin wave over time, amplified by the value.
        """
        ...
    
    def GetYAmplitude(self):
        """
        V.GetYAmplitude() -> float
        C++: virtual double GetYAmplitude()
        
        When 0.0 (the default) this produces a data set that is
        stationary. When on the data set moves in the X/Y plane over a
        sin wave over time, amplified by the value.
        """
        ...
    
    def GrowingOff(self):
        """
        V.GrowingOff()
        C++: virtual void GrowingOff()
        
        When off (the default) this produces a single cell data set. When
        on the number of cells (in the Y direction) grows and shrinks
        over time along a hat function.
        """
        ...
    
    def GrowingOn(self):
        """
        V.GrowingOn()
        C++: virtual void GrowingOn()
        
        When off (the default) this produces a single cell data set. When
        on the number of cells (in the Y direction) grows and shrinks
        over time along a hat function.
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
        V.NewInstance() -> vtkTimeSourceExample
        C++: vtkTimeSourceExample *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTimeSourceExample
        C++: static vtkTimeSourceExample *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAnalytic(self, p_int):
        """
        V.SetAnalytic(int)
        C++: virtual void SetAnalytic(vtkTypeBool _arg)
        
        When off (the default) this source produces a discrete set of
        values. When on, this source produces a value analytically for
        any queried time.
        """
        ...
    
    def SetGrowing(self, p_int):
        """
        V.SetGrowing(int)
        C++: virtual void SetGrowing(vtkTypeBool _arg)
        
        When off (the default) this produces a single cell data set. When
        on the number of cells (in the Y direction) grows and shrinks
        over time along a hat function.
        """
        ...
    
    def SetXAmplitude(self, p_float):
        """
        V.SetXAmplitude(float)
        C++: virtual void SetXAmplitude(double _arg)
        
        When 0.0 (the default) this produces a data set that is
        stationary. When on the data set moves in the X/Y plane over a
        sin wave over time, amplified by the value.
        """
        ...
    
    def SetYAmplitude(self, p_float):
        """
        V.SetYAmplitude(float)
        C++: virtual void SetYAmplitude(double _arg)
        
        When 0.0 (the default) this produces a data set that is
        stationary. When on the data set moves in the X/Y plane over a
        sin wave over time, amplified by the value.
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


