"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkVolumeOfRevolutionFilter(__vtkmodules_vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    """
    vtkVolumeOfRevolutionFilter - sweep data about a line to create a
    volume
    
    Superclass: vtkUnstructuredGridAlgorithm
    
    vtkVolumeOfRevolutionFilter is a modeling filter. It takes a
    2-dimensional dataset as input and generates an unstructured grid on
    output. The input dataset is swept around the axis of rotation to
    create dimension-elevated primitives. For example, sweeping a vertex
    creates a series of lines; sweeping a line creates a series of quads,
    etc.
    
    @warning
    The user must take care to ensure that the axis of revolution does
    not cross through the geometry, otherwise there will be intersecting
    cells in the output.
    
    @sa
    vtkRotationalExtrusionFilter
    """
    def GetAxisDirection(self):
        """
        V.GetAxisDirection() -> (float, float, float)
        C++: virtual double *GetAxisDirection()
        
        Set/Get the direction of the axis of revolution.
        """
        ...
    
    def GetAxisPosition(self):
        """
        V.GetAxisPosition() -> (float, float, float)
        C++: virtual double *GetAxisPosition()
        
        Set/Get the position of the axis of revolution.
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
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
        ...
    
    def GetOutputPointsPrecisionMaxValue(self):
        """
        V.GetOutputPointsPrecisionMaxValue() -> int
        C++: virtual int GetOutputPointsPrecisionMaxValue()
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
        ...
    
    def GetOutputPointsPrecisionMinValue(self):
        """
        V.GetOutputPointsPrecisionMinValue() -> int
        C++: virtual int GetOutputPointsPrecisionMinValue()
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
        ...
    
    def GetResolution(self):
        """
        V.GetResolution() -> int
        C++: virtual int GetResolution()
        
        Set/Get resolution of sweep operation. Resolution controls the
        number of intermediate node points.
        """
        ...
    
    def GetResolutionMaxValue(self):
        """
        V.GetResolutionMaxValue() -> int
        C++: virtual int GetResolutionMaxValue()
        
        Set/Get resolution of sweep operation. Resolution controls the
        number of intermediate node points.
        """
        ...
    
    def GetResolutionMinValue(self):
        """
        V.GetResolutionMinValue() -> int
        C++: virtual int GetResolutionMinValue()
        
        Set/Get resolution of sweep operation. Resolution controls the
        number of intermediate node points.
        """
        ...
    
    def GetSweepAngle(self):
        """
        V.GetSweepAngle() -> float
        C++: virtual double GetSweepAngle()
        
        Set/Get angle of rotation in degrees.
        """
        ...
    
    def GetSweepAngleMaxValue(self):
        """
        V.GetSweepAngleMaxValue() -> float
        C++: virtual double GetSweepAngleMaxValue()
        
        Set/Get angle of rotation in degrees.
        """
        ...
    
    def GetSweepAngleMinValue(self):
        """
        V.GetSweepAngleMinValue() -> float
        C++: virtual double GetSweepAngleMinValue()
        
        Set/Get angle of rotation in degrees.
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
        V.NewInstance() -> vtkVolumeOfRevolutionFilter
        C++: vtkVolumeOfRevolutionFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkVolumeOfRevolutionFilter
        C++: static vtkVolumeOfRevolutionFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetAxisDirection(self, p_float, p_float_1, p_float_2):
        """
        V.SetAxisDirection(float, float, float)
        C++: virtual void SetAxisDirection(double _arg1, double _arg2,
            double _arg3)
        V.SetAxisDirection((float, float, float))
        C++: virtual void SetAxisDirection(const double _arg[3])
        
        Set/Get the direction of the axis of revolution.
        """
        ...
    
    def SetAxisPosition(self, p_float, p_float_1, p_float_2):
        """
        V.SetAxisPosition(float, float, float)
        C++: virtual void SetAxisPosition(double _arg1, double _arg2,
            double _arg3)
        V.SetAxisPosition((float, float, float))
        C++: virtual void SetAxisPosition(const double _arg[3])
        
        Set/Get the position of the axis of revolution.
        """
        ...
    
    def SetOutputPointsPrecision(self, p_int):
        """
        V.SetOutputPointsPrecision(int)
        C++: virtual void SetOutputPointsPrecision(int _arg)
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
        ...
    
    def SetResolution(self, p_int):
        """
        V.SetResolution(int)
        C++: virtual void SetResolution(int _arg)
        
        Set/Get resolution of sweep operation. Resolution controls the
        number of intermediate node points.
        """
        ...
    
    def SetSweepAngle(self, p_float):
        """
        V.SetSweepAngle(float)
        C++: virtual void SetSweepAngle(double _arg)
        
        Set/Get angle of rotation in degrees.
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


