"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkBoundedPointSource(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkBoundedPointSource - create a random cloud of points within a
    specified bounding box
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkBoundedPointSource is a source object that creates a
    user-specified number of points within a specified bounding box. The
    points are scattered randomly throughout the box. Optionally, the
    user can produce a vtkPolyVertex cell as well as random scalar values
    within a specified range. The class is typically used for debugging
    and testing, as well as seeding streamlines.
    """
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: virtual double *GetBounds()
        
        Set the bounding box for the point distribution. By default the
        bounds is (-1,1,-1,1,-1,1).
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiation, type information and
        printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiation, type information and
        printing.
        """
        ...
    
    def GetNumberOfPoints(self):
        """
        V.GetNumberOfPoints() -> int
        C++: virtual vtkIdType GetNumberOfPoints()
        
        Set the number of points to generate.
        """
        ...
    
    def GetNumberOfPointsMaxValue(self):
        """
        V.GetNumberOfPointsMaxValue() -> int
        C++: virtual vtkIdType GetNumberOfPointsMaxValue()
        
        Set the number of points to generate.
        """
        ...
    
    def GetNumberOfPointsMinValue(self):
        """
        V.GetNumberOfPointsMinValue() -> int
        C++: virtual vtkIdType GetNumberOfPointsMinValue()
        
        Set the number of points to generate.
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
    
    def GetProduceCellOutput(self):
        """
        V.GetProduceCellOutput() -> bool
        C++: virtual bool GetProduceCellOutput()
        
        Indicate whether to produce a vtkPolyVertex cell to go along with
        the output vtkPoints generated. By default a cell is NOT
        produced. Some filters do not need the vtkPolyVertex which just
        consumes a lot of memory.
        """
        ...
    
    def GetProduceRandomScalars(self):
        """
        V.GetProduceRandomScalars() -> bool
        C++: virtual bool GetProduceRandomScalars()
        
        Indicate whether to produce random point scalars in the output.
        By default this is off.
        """
        ...
    
    def GetScalarRange(self):
        """
        V.GetScalarRange() -> (float, float)
        C++: virtual double *GetScalarRange()
        
        Set the range in which the random scalars should be produced. By
        default the scalar range is (0,1).
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiation, type information and
        printing.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiation, type information and
        printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkBoundedPointSource
        C++: vtkBoundedPointSource *NewInstance()
        
        Standard methods for instantiation, type information and
        printing.
        """
        ...
    
    def ProduceCellOutputOff(self):
        """
        V.ProduceCellOutputOff()
        C++: virtual void ProduceCellOutputOff()
        
        Indicate whether to produce a vtkPolyVertex cell to go along with
        the output vtkPoints generated. By default a cell is NOT
        produced. Some filters do not need the vtkPolyVertex which just
        consumes a lot of memory.
        """
        ...
    
    def ProduceCellOutputOn(self):
        """
        V.ProduceCellOutputOn()
        C++: virtual void ProduceCellOutputOn()
        
        Indicate whether to produce a vtkPolyVertex cell to go along with
        the output vtkPoints generated. By default a cell is NOT
        produced. Some filters do not need the vtkPolyVertex which just
        consumes a lot of memory.
        """
        ...
    
    def ProduceRandomScalarsOff(self):
        """
        V.ProduceRandomScalarsOff()
        C++: virtual void ProduceRandomScalarsOff()
        
        Indicate whether to produce random point scalars in the output.
        By default this is off.
        """
        ...
    
    def ProduceRandomScalarsOn(self):
        """
        V.ProduceRandomScalarsOn()
        C++: virtual void ProduceRandomScalarsOn()
        
        Indicate whether to produce random point scalars in the output.
        By default this is off.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkBoundedPointSource
        C++: static vtkBoundedPointSource *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for instantiation, type information and
        printing.
        """
        ...
    
    def SetBounds(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5):
        """
        V.SetBounds(float, float, float, float, float, float)
        C++: virtual void SetBounds(double _arg1, double _arg2,
            double _arg3, double _arg4, double _arg5, double _arg6)
        V.SetBounds((float, float, float, float, float, float))
        C++: virtual void SetBounds(const double _arg[6])
        
        Set the bounding box for the point distribution. By default the
        bounds is (-1,1,-1,1,-1,1).
        """
        ...
    
    def SetNumberOfPoints(self, p_int):
        """
        V.SetNumberOfPoints(int)
        C++: virtual void SetNumberOfPoints(vtkIdType _arg)
        
        Set the number of points to generate.
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
    
    def SetProduceCellOutput(self, bool):
        """
        V.SetProduceCellOutput(bool)
        C++: virtual void SetProduceCellOutput(bool _arg)
        
        Indicate whether to produce a vtkPolyVertex cell to go along with
        the output vtkPoints generated. By default a cell is NOT
        produced. Some filters do not need the vtkPolyVertex which just
        consumes a lot of memory.
        """
        ...
    
    def SetProduceRandomScalars(self, bool):
        """
        V.SetProduceRandomScalars(bool)
        C++: virtual void SetProduceRandomScalars(bool _arg)
        
        Indicate whether to produce random point scalars in the output.
        By default this is off.
        """
        ...
    
    def SetScalarRange(self, p_float, p_float_1):
        """
        V.SetScalarRange(float, float)
        C++: virtual void SetScalarRange(double _arg1, double _arg2)
        V.SetScalarRange((float, float))
        C++: void SetScalarRange(const double _arg[2])
        
        Set the range in which the random scalars should be produced. By
        default the scalar range is (0,1).
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


