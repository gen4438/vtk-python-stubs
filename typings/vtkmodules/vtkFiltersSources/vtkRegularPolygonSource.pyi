"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkRegularPolygonSource(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkRegularPolygonSource - create a regular, n-sided polygon and/or
    polyline
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkRegularPolygonSource is a source object that creates a single
    n-sided polygon and/or polyline. The polygon is centered at a
    specified point, orthogonal to a specified normal, and with a
    circumscribing radius set by the user. The user can also specify the
    number of sides of the polygon ranging from [3,N].
    
    This object can be used for seeding streamlines or defining regions
    for clipping/cutting.
    """
    def GeneratePolygonOff(self):
        """
        V.GeneratePolygonOff()
        C++: virtual void GeneratePolygonOff()
        
        Control whether a polygon is produced. By default,
        GeneratePolygon is enabled.
        """
        ...
    
    def GeneratePolygonOn(self):
        """
        V.GeneratePolygonOn()
        C++: virtual void GeneratePolygonOn()
        
        Control whether a polygon is produced. By default,
        GeneratePolygon is enabled.
        """
        ...
    
    def GeneratePolylineOff(self):
        """
        V.GeneratePolylineOff()
        C++: virtual void GeneratePolylineOff()
        
        Control whether a polyline is produced. By default,
        GeneratePolyline is enabled.
        """
        ...
    
    def GeneratePolylineOn(self):
        """
        V.GeneratePolylineOn()
        C++: virtual void GeneratePolylineOn()
        
        Control whether a polyline is produced. By default,
        GeneratePolyline is enabled.
        """
        ...
    
    def GetCenter(self):
        """
        V.GetCenter() -> (float, float, float)
        C++: virtual double *GetCenter()
        
        Set/Get the center of the polygon. By default, the center is set
        at the origin (0,0,0).
        """
        ...
    
    def GetGeneratePolygon(self):
        """
        V.GetGeneratePolygon() -> int
        C++: virtual vtkTypeBool GetGeneratePolygon()
        
        Control whether a polygon is produced. By default,
        GeneratePolygon is enabled.
        """
        ...
    
    def GetGeneratePolyline(self):
        """
        V.GetGeneratePolyline() -> int
        C++: virtual vtkTypeBool GetGeneratePolyline()
        
        Control whether a polyline is produced. By default,
        GeneratePolyline is enabled.
        """
        ...
    
    def GetNormal(self):
        """
        V.GetNormal() -> (float, float, float)
        C++: virtual double *GetNormal()
        
        Set/Get the normal to the polygon. The ordering of the polygon
        will be counter-clockwise around the normal (i.e., using the
        right-hand rule). By default, the normal is set to (0,0,1).
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiation, obtaining type and printing
        instance values.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiation, obtaining type and printing
        instance values.
        """
        ...
    
    def GetNumberOfSides(self):
        """
        V.GetNumberOfSides() -> int
        C++: virtual int GetNumberOfSides()
        
        Set/Get the number of sides of the polygon. By default, the
        number of sides is set to six.
        """
        ...
    
    def GetNumberOfSidesMaxValue(self):
        """
        V.GetNumberOfSidesMaxValue() -> int
        C++: virtual int GetNumberOfSidesMaxValue()
        
        Set/Get the number of sides of the polygon. By default, the
        number of sides is set to six.
        """
        ...
    
    def GetNumberOfSidesMinValue(self):
        """
        V.GetNumberOfSidesMinValue() -> int
        C++: virtual int GetNumberOfSidesMinValue()
        
        Set/Get the number of sides of the polygon. By default, the
        number of sides is set to six.
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
        
        Set/Get the radius of the polygon. By default, the radius is set
        to 0.5.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiation, obtaining type and printing
        instance values.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiation, obtaining type and printing
        instance values.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkRegularPolygonSource
        C++: vtkRegularPolygonSource *NewInstance()
        
        Standard methods for instantiation, obtaining type and printing
        instance values.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkRegularPolygonSource
        C++: static vtkRegularPolygonSource *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instantiation, obtaining type and printing
        instance values.
        """
        ...
    
    def SetCenter(self, p_float, p_float_1, p_float_2):
        """
        V.SetCenter(float, float, float)
        C++: virtual void SetCenter(double _arg1, double _arg2,
            double _arg3)
        V.SetCenter((float, float, float))
        C++: virtual void SetCenter(const double _arg[3])
        
        Set/Get the center of the polygon. By default, the center is set
        at the origin (0,0,0).
        """
        ...
    
    def SetGeneratePolygon(self, p_int):
        """
        V.SetGeneratePolygon(int)
        C++: virtual void SetGeneratePolygon(vtkTypeBool _arg)
        
        Control whether a polygon is produced. By default,
        GeneratePolygon is enabled.
        """
        ...
    
    def SetGeneratePolyline(self, p_int):
        """
        V.SetGeneratePolyline(int)
        C++: virtual void SetGeneratePolyline(vtkTypeBool _arg)
        
        Control whether a polyline is produced. By default,
        GeneratePolyline is enabled.
        """
        ...
    
    def SetNormal(self, p_float, p_float_1, p_float_2):
        """
        V.SetNormal(float, float, float)
        C++: virtual void SetNormal(double _arg1, double _arg2,
            double _arg3)
        V.SetNormal((float, float, float))
        C++: virtual void SetNormal(const double _arg[3])
        
        Set/Get the normal to the polygon. The ordering of the polygon
        will be counter-clockwise around the normal (i.e., using the
        right-hand rule). By default, the normal is set to (0,0,1).
        """
        ...
    
    def SetNumberOfSides(self, p_int):
        """
        V.SetNumberOfSides(int)
        C++: virtual void SetNumberOfSides(int _arg)
        
        Set/Get the number of sides of the polygon. By default, the
        number of sides is set to six.
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
        
        Set/Get the radius of the polygon. By default, the radius is set
        to 0.5.
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

