"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkOutlineSource(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkOutlineSource - create wireframe outline around bounding box
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkOutlineSource creates a wireframe outline around a user-specified
    bounding box.  The outline may be created aligned with the {x,y,z}
    axis - in which case it is defined by the 6 bounds
    {xmin,xmax,ymin,ymax,zmin,zmax} via SetBounds(). Alternatively, the
    box may be arbitrarily aligned, in which case it should be set via
    the SetCorners() member.
    """
    def GenerateFacesOff(self):
        """
        V.GenerateFacesOff()
        C++: virtual void GenerateFacesOff()
        
        Generate solid faces for the box. This is off by default.
        """
        ...
    
    def GenerateFacesOn(self):
        """
        V.GenerateFacesOn()
        C++: virtual void GenerateFacesOn()
        
        Generate solid faces for the box. This is off by default.
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: virtual double *GetBounds()
        
        Specify the bounds of the box to be used in Axis Aligned mode.
        """
        ...
    
    def GetBoxType(self):
        """
        V.GetBoxType() -> int
        C++: virtual int GetBoxType()
        
        Set box type to AxisAligned (default) or Oriented. Use the method
        SetBounds() with AxisAligned mode, and SetCorners() with Oriented
        mode.
        """
        ...
    
    def GetCorners(self):
        """
        V.GetCorners() -> (float, float, float, float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float, float, float,
            float)
        C++: virtual double *GetCorners()
        
        Specify the corners of the outline when in Oriented mode, the
        values are supplied as 8*3 double values The correct corner
        ordering is using {x,y,z} convention for the unit cube as
        follows:
        {0,0,0},{1,0,0},{0,1,0},{1,1,0},{0,0,1},{1,0,1},{0,1,1},{1,1,1}.
        """
        ...
    
    def GetGenerateFaces(self):
        """
        V.GetGenerateFaces() -> int
        C++: virtual vtkTypeBool GetGenerateFaces()
        
        Generate solid faces for the box. This is off by default.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiation. type information, and
        printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiation. type information, and
        printing.
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
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiation. type information, and
        printing.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiation. type information, and
        printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkOutlineSource
        C++: vtkOutlineSource *NewInstance()
        
        Standard methods for instantiation. type information, and
        printing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOutlineSource
        C++: static vtkOutlineSource *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for instantiation. type information, and
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
        
        Specify the bounds of the box to be used in Axis Aligned mode.
        """
        ...
    
    def SetBoxType(self, p_int):
        """
        V.SetBoxType(int)
        C++: virtual void SetBoxType(int _arg)
        
        Set box type to AxisAligned (default) or Oriented. Use the method
        SetBounds() with AxisAligned mode, and SetCorners() with Oriented
        mode.
        """
        ...
    
    def SetBoxTypeToAxisAligned(self):
        """
        V.SetBoxTypeToAxisAligned()
        C++: void SetBoxTypeToAxisAligned()
        
        Set box type to AxisAligned (default) or Oriented. Use the method
        SetBounds() with AxisAligned mode, and SetCorners() with Oriented
        mode.
        """
        ...
    
    def SetBoxTypeToOriented(self):
        """
        V.SetBoxTypeToOriented()
        C++: void SetBoxTypeToOriented()
        
        Set box type to AxisAligned (default) or Oriented. Use the method
        SetBounds() with AxisAligned mode, and SetCorners() with Oriented
        mode.
        """
        ...
    
    def SetCorners(self, float_tuple):
        """
        V.SetCorners((float, ...))
        C++: virtual void SetCorners(const double data[])
        
        Specify the corners of the outline when in Oriented mode, the
        values are supplied as 8*3 double values The correct corner
        ordering is using {x,y,z} convention for the unit cube as
        follows:
        {0,0,0},{1,0,0},{0,1,0},{1,1,0},{0,0,1},{1,0,1},{0,1,1},{1,1,1}.
        """
        ...
    
    def SetGenerateFaces(self, p_int):
        """
        V.SetGenerateFaces(int)
        C++: virtual void SetGenerateFaces(vtkTypeBool _arg)
        
        Generate solid faces for the box. This is off by default.
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


