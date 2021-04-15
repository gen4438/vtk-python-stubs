"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkTextSource(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkTextSource - create polygonal text
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkTextSource converts a text string into polygons.  This way you can
    insert text into your renderings. It uses the 9x15 font from X
    Windows. You can specify if you want the background to be drawn or
    not. The characters are formed by scan converting the raster font
    into quadrilaterals. Colors are assigned to the letters using scalar
    data. To set the color of the characters with the source's actor
    property, set BackingOff on the text source and ScalarVisibilityOff
    on the associated vtkPolyDataMapper. Then, the color can be set using
    the associated actor's property.
    
    vtkVectorText generates higher quality polygonal representations of
    characters.
    
    @sa
    vtkVectorText
    """
    def BackingOff(self):
        """
        V.BackingOff()
        C++: virtual void BackingOff()
        
        Controls whether or not a background is drawn with the text.
        """
        ...
    
    def BackingOn(self):
        """
        V.BackingOn()
        C++: virtual void BackingOn()
        
        Controls whether or not a background is drawn with the text.
        """
        ...
    
    def GetBackgroundColor(self):
        """
        V.GetBackgroundColor() -> (float, float, float)
        C++: virtual double *GetBackgroundColor()
        
        Set/Get the background color. Default is black (0,0,0). Alpha is
        always 1.
        """
        ...
    
    def GetBacking(self):
        """
        V.GetBacking() -> int
        C++: virtual vtkTypeBool GetBacking()
        
        Controls whether or not a background is drawn with the text.
        """
        ...
    
    def GetForegroundColor(self):
        """
        V.GetForegroundColor() -> (float, float, float)
        C++: virtual double *GetForegroundColor()
        
        Set/Get the foreground color. Default is white (1,1,1). ALpha is
        always 1.
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
    
    def GetText(self):
        """
        V.GetText() -> string
        C++: virtual char *GetText()
        
        Set/Get the text to be drawn.
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
        V.NewInstance() -> vtkTextSource
        C++: vtkTextSource *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTextSource
        C++: static vtkTextSource *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetBackgroundColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetBackgroundColor(float, float, float)
        C++: virtual void SetBackgroundColor(double _arg1, double _arg2,
            double _arg3)
        V.SetBackgroundColor((float, float, float))
        C++: virtual void SetBackgroundColor(const double _arg[3])
        
        Set/Get the background color. Default is black (0,0,0). Alpha is
        always 1.
        """
        ...
    
    def SetBacking(self, p_int):
        """
        V.SetBacking(int)
        C++: virtual void SetBacking(vtkTypeBool _arg)
        
        Controls whether or not a background is drawn with the text.
        """
        ...
    
    def SetForegroundColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetForegroundColor(float, float, float)
        C++: virtual void SetForegroundColor(double _arg1, double _arg2,
            double _arg3)
        V.SetForegroundColor((float, float, float))
        C++: virtual void SetForegroundColor(const double _arg[3])
        
        Set/Get the foreground color. Default is white (1,1,1). ALpha is
        always 1.
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
    
    def SetText(self, string):
        """
        V.SetText(string)
        C++: virtual void SetText(const char *_arg)
        
        Set/Get the text to be drawn.
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

