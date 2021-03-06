"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkCursor2D(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkCursor2D - generate a 2D cursor representation
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkCursor2D is a class that generates a 2D cursor representation. The
    cursor consists of two intersection axes lines that meet at the
    cursor focus. Several optional features are available as well. An
    optional 2D bounding box may be enabled. An inner radius, centered at
    the focal point, can be set that erases the intersecting lines (e.g.,
    it leaves a clear area under the focal point so you can see what you
    are selecting). And finally, an optional point can be enabled located
    at the focal point. All of these features can be turned on and off
    independently.
    """
    def AllOff(self):
        """
        V.AllOff()
        C++: void AllOff()
        
        Turn every part of the cursor on or off.
        """
        ...
    
    def AllOn(self):
        """
        V.AllOn()
        C++: void AllOn()
        
        Turn every part of the cursor on or off.
        """
        ...
    
    def AxesOff(self):
        """
        V.AxesOff()
        C++: virtual void AxesOff()
        
        Turn on/off the wireframe axes.
        """
        ...
    
    def AxesOn(self):
        """
        V.AxesOn()
        C++: virtual void AxesOn()
        
        Turn on/off the wireframe axes.
        """
        ...
    
    def GetAxes(self):
        """
        V.GetAxes() -> int
        C++: virtual vtkTypeBool GetAxes()
        
        Turn on/off the wireframe axes.
        """
        ...
    
    def GetFocalPoint(self):
        """
        V.GetFocalPoint() -> (float, float, float)
        C++: virtual double *GetFocalPoint()
        
        Set/Get the position of cursor focus. If translation mode is on,
        then the entire cursor (including bounding box, cursor, and
        shadows) is translated. Otherwise, the focal point will either be
        clamped to the bounding box, or wrapped, if Wrap is on. (Note:
        this behavior requires that the bounding box is set prior to the
        focal point.) Note that the method takes a 3D point but ignores
        the z-coordinate value.
        """
        ...
    
    def GetModelBounds(self):
        """
        V.GetModelBounds() -> (float, float, float, float, float, float)
        C++: virtual double *GetModelBounds()
        
        Set / get the bounding box of the 2D cursor. This defines the
        outline of the cursor, and where the focal point should lie.
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
    
    def GetOutline(self):
        """
        V.GetOutline() -> int
        C++: virtual vtkTypeBool GetOutline()
        
        Turn on/off the wireframe bounding box.
        """
        ...
    
    def GetPoint(self):
        """
        V.GetPoint() -> int
        C++: virtual vtkTypeBool GetPoint()
        
        Turn on/off the point located at the cursor focus.
        """
        ...
    
    def GetRadius(self):
        """
        V.GetRadius() -> float
        C++: virtual double GetRadius()
        
        Specify a radius for a circle. This erases the cursor lines
        around the focal point.
        """
        ...
    
    def GetRadiusMaxValue(self):
        """
        V.GetRadiusMaxValue() -> float
        C++: virtual double GetRadiusMaxValue()
        
        Specify a radius for a circle. This erases the cursor lines
        around the focal point.
        """
        ...
    
    def GetRadiusMinValue(self):
        """
        V.GetRadiusMinValue() -> float
        C++: virtual double GetRadiusMinValue()
        
        Specify a radius for a circle. This erases the cursor lines
        around the focal point.
        """
        ...
    
    def GetTranslationMode(self):
        """
        V.GetTranslationMode() -> int
        C++: virtual vtkTypeBool GetTranslationMode()
        
        Enable/disable the translation mode. If on, changes in cursor
        position cause the entire widget to translate along with the
        cursor. By default, translation mode is off.
        """
        ...
    
    def GetWrap(self):
        """
        V.GetWrap() -> int
        C++: virtual vtkTypeBool GetWrap()
        
        Turn on/off cursor wrapping. If the cursor focus moves outside
        the specified bounds, the cursor will either be restrained
        against the nearest "wall" (Wrap=off), or it will wrap around
        (Wrap=on).
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
        V.NewInstance() -> vtkCursor2D
        C++: vtkCursor2D *NewInstance()
        """
        ...
    
    def OutlineOff(self):
        """
        V.OutlineOff()
        C++: virtual void OutlineOff()
        
        Turn on/off the wireframe bounding box.
        """
        ...
    
    def OutlineOn(self):
        """
        V.OutlineOn()
        C++: virtual void OutlineOn()
        
        Turn on/off the wireframe bounding box.
        """
        ...
    
    def PointOff(self):
        """
        V.PointOff()
        C++: virtual void PointOff()
        
        Turn on/off the point located at the cursor focus.
        """
        ...
    
    def PointOn(self):
        """
        V.PointOn()
        C++: virtual void PointOn()
        
        Turn on/off the point located at the cursor focus.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCursor2D
        C++: static vtkCursor2D *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAxes(self, p_int):
        """
        V.SetAxes(int)
        C++: virtual void SetAxes(vtkTypeBool _arg)
        
        Turn on/off the wireframe axes.
        """
        ...
    
    def SetFocalPoint(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetFocalPoint([float, float, float])
        C++: void SetFocalPoint(double x[3])
        V.SetFocalPoint(float, float, float)
        C++: void SetFocalPoint(double x, double y, double z)
        
        Set/Get the position of cursor focus. If translation mode is on,
        then the entire cursor (including bounding box, cursor, and
        shadows) is translated. Otherwise, the focal point will either be
        clamped to the bounding box, or wrapped, if Wrap is on. (Note:
        this behavior requires that the bounding box is set prior to the
        focal point.) Note that the method takes a 3D point but ignores
        the z-coordinate value.
        """
        ...
    
    def SetModelBounds(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5):
        """
        V.SetModelBounds(float, float, float, float, float, float)
        C++: void SetModelBounds(double xmin, double xmax, double ymin,
            double ymax, double zmin, double zmax)
        V.SetModelBounds((float, float, float, float, float, float))
        C++: void SetModelBounds(const double bounds[6])
        
        Set / get the bounding box of the 2D cursor. This defines the
        outline of the cursor, and where the focal point should lie.
        """
        ...
    
    def SetOutline(self, p_int):
        """
        V.SetOutline(int)
        C++: virtual void SetOutline(vtkTypeBool _arg)
        
        Turn on/off the wireframe bounding box.
        """
        ...
    
    def SetPoint(self, p_int):
        """
        V.SetPoint(int)
        C++: virtual void SetPoint(vtkTypeBool _arg)
        
        Turn on/off the point located at the cursor focus.
        """
        ...
    
    def SetRadius(self, p_float):
        """
        V.SetRadius(float)
        C++: virtual void SetRadius(double _arg)
        
        Specify a radius for a circle. This erases the cursor lines
        around the focal point.
        """
        ...
    
    def SetTranslationMode(self, p_int):
        """
        V.SetTranslationMode(int)
        C++: virtual void SetTranslationMode(vtkTypeBool _arg)
        
        Enable/disable the translation mode. If on, changes in cursor
        position cause the entire widget to translate along with the
        cursor. By default, translation mode is off.
        """
        ...
    
    def SetWrap(self, p_int):
        """
        V.SetWrap(int)
        C++: virtual void SetWrap(vtkTypeBool _arg)
        
        Turn on/off cursor wrapping. If the cursor focus moves outside
        the specified bounds, the cursor will either be restrained
        against the nearest "wall" (Wrap=off), or it will wrap around
        (Wrap=on).
        """
        ...
    
    def TranslationModeOff(self):
        """
        V.TranslationModeOff()
        C++: virtual void TranslationModeOff()
        
        Enable/disable the translation mode. If on, changes in cursor
        position cause the entire widget to translate along with the
        cursor. By default, translation mode is off.
        """
        ...
    
    def TranslationModeOn(self):
        """
        V.TranslationModeOn()
        C++: virtual void TranslationModeOn()
        
        Enable/disable the translation mode. If on, changes in cursor
        position cause the entire widget to translate along with the
        cursor. By default, translation mode is off.
        """
        ...
    
    def WrapOff(self):
        """
        V.WrapOff()
        C++: virtual void WrapOff()
        
        Turn on/off cursor wrapping. If the cursor focus moves outside
        the specified bounds, the cursor will either be restrained
        against the nearest "wall" (Wrap=off), or it will wrap around
        (Wrap=on).
        """
        ...
    
    def WrapOn(self):
        """
        V.WrapOn()
        C++: virtual void WrapOn()
        
        Turn on/off cursor wrapping. If the cursor focus moves outside
        the specified bounds, the cursor will either be restrained
        against the nearest "wall" (Wrap=off), or it will wrap around
        (Wrap=on).
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


