"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkIconGlyphFilter(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkIconGlyphFilter - Filter that generates a polydata consisting of
    quads with texture coordinates referring to a set of icons within a
    sheet of icons.
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkIconGlyphFilter takes in a vtkPointSet where each point
    corresponds to the center of an icon. Scalar integer data must also
    be set to give each point an icon index. This index is a zero based
    row major index into an image that contains a grid of icons (each
    icon is the same size). You must also specify 1) the size of the icon
    in the icon sheet (in pixels), 2) the size of the icon sheet (in
    pixels), and 3) the display size of each icon (again in display
    coordinates, or pixels).
    
    Various other parameters are used to control how this data is
    combined. If UseIconSize is true then the DisplaySize is ignored. If
    PassScalars is true, then the scalar index information is passed to
    the output. Also, there is an optional IconScale array which, if
    UseIconScaling is on, will scale each icon independently.
    
    @sa
    vtkPolyDataAlgorithm vtkGlyph3D vtkGlyph2D
    """
    def GetDisplaySize(self):
        """
        V.GetDisplaySize() -> (int, int)
        C++: virtual int *GetDisplaySize()
        
        Specify the Width and Height, in pixels, of the size of the icon
        when it is rendered. By default, the IconSize is used to set the
        display size (i.e., UseIconSize is true by default). Note that
        assumes that IconScaling is disabled, or if enabled, the scale of
        a particular icon is 1.
        """
        ...
    
    def GetGravity(self):
        """
        V.GetGravity() -> int
        C++: virtual int GetGravity()
        
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
        ...
    
    def GetIconScaling(self):
        """
        V.GetIconScaling() -> int
        C++: virtual int GetIconScaling()
        
        Specify how to specify individual icons. By default, icon scaling
        is off, but if it is on, then the filter looks for an array named
        "IconScale" to control individual icon size.
        """
        ...
    
    def GetIconSheetSize(self):
        """
        V.GetIconSheetSize() -> (int, int)
        C++: virtual int *GetIconSheetSize()
        
        Specify the Width and Height, in pixels, of an icon in the icon
        sheet.
        """
        ...
    
    def GetIconSize(self):
        """
        V.GetIconSize() -> (int, int)
        C++: virtual int *GetIconSize()
        
        Specify the Width and Height, in pixels, of an icon in the icon
        sheet.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard VTK methods.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard VTK methods.
        """
        ...
    
    def GetOffset(self):
        """
        V.GetOffset() -> (int, int)
        C++: virtual int *GetOffset()
        
        Specify an offset (in pixels or display coordinates) that offsets
        the icons from their generating points.
        """
        ...
    
    def GetPassScalars(self):
        """
        V.GetPassScalars() -> bool
        C++: virtual bool GetPassScalars()
        
        Specify whether to pass the scalar icon index to the output. By
        default this is not passed since it can affect color during the
        rendering process. Note that all other point data is passed to
        the output regardless of the value of this flag.
        """
        ...
    
    def GetUseIconSize(self):
        """
        V.GetUseIconSize() -> bool
        C++: virtual bool GetUseIconSize()
        
        Specify whether the Quad generated to place the icon on will be
        either the dimensions specified by IconSize or the DisplaySize.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard VTK methods.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard VTK methods.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkIconGlyphFilter
        C++: vtkIconGlyphFilter *NewInstance()
        
        Standard VTK methods.
        """
        ...
    
    def PassScalarsOff(self):
        """
        V.PassScalarsOff()
        C++: virtual void PassScalarsOff()
        
        Specify whether to pass the scalar icon index to the output. By
        default this is not passed since it can affect color during the
        rendering process. Note that all other point data is passed to
        the output regardless of the value of this flag.
        """
        ...
    
    def PassScalarsOn(self):
        """
        V.PassScalarsOn()
        C++: virtual void PassScalarsOn()
        
        Specify whether to pass the scalar icon index to the output. By
        default this is not passed since it can affect color during the
        rendering process. Note that all other point data is passed to
        the output regardless of the value of this flag.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkIconGlyphFilter
        C++: static vtkIconGlyphFilter *SafeDownCast(vtkObjectBase *o)
        
        Standard VTK methods.
        """
        ...
    
    def SetDisplaySize(self, p_int, p_int_1):
        """
        V.SetDisplaySize(int, int)
        C++: virtual void SetDisplaySize(int _arg1, int _arg2)
        V.SetDisplaySize((int, int))
        C++: void SetDisplaySize(const int _arg[2])
        
        Specify the Width and Height, in pixels, of the size of the icon
        when it is rendered. By default, the IconSize is used to set the
        display size (i.e., UseIconSize is true by default). Note that
        assumes that IconScaling is disabled, or if enabled, the scale of
        a particular icon is 1.
        """
        ...
    
    def SetGravity(self, p_int):
        """
        V.SetGravity(int)
        C++: virtual void SetGravity(int _arg)
        
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
        ...
    
    def SetGravityToBottomCenter(self):
        """
        V.SetGravityToBottomCenter()
        C++: void SetGravityToBottomCenter()
        
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
        ...
    
    def SetGravityToBottomLeft(self):
        """
        V.SetGravityToBottomLeft()
        C++: void SetGravityToBottomLeft()
        
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
        ...
    
    def SetGravityToBottomRight(self):
        """
        V.SetGravityToBottomRight()
        C++: void SetGravityToBottomRight()
        
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
        ...
    
    def SetGravityToCenterCenter(self):
        """
        V.SetGravityToCenterCenter()
        C++: void SetGravityToCenterCenter()
        
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
        ...
    
    def SetGravityToCenterLeft(self):
        """
        V.SetGravityToCenterLeft()
        C++: void SetGravityToCenterLeft()
        
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
        ...
    
    def SetGravityToCenterRight(self):
        """
        V.SetGravityToCenterRight()
        C++: void SetGravityToCenterRight()
        
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
        ...
    
    def SetGravityToTopCenter(self):
        """
        V.SetGravityToTopCenter()
        C++: void SetGravityToTopCenter()
        
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
        ...
    
    def SetGravityToTopLeft(self):
        """
        V.SetGravityToTopLeft()
        C++: void SetGravityToTopLeft()
        
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
        ...
    
    def SetGravityToTopRight(self):
        """
        V.SetGravityToTopRight()
        C++: void SetGravityToTopRight()
        
        Specify if the input points define the center of the icon quad or
        one of top right corner, top center, top left corner, center
        right, center, center center left, bottom right corner, bottom
        center or bottom left corner.
        """
        ...
    
    def SetIconScaling(self, p_int):
        """
        V.SetIconScaling(int)
        C++: virtual void SetIconScaling(int _arg)
        
        Specify how to specify individual icons. By default, icon scaling
        is off, but if it is on, then the filter looks for an array named
        "IconScale" to control individual icon size.
        """
        ...
    
    def SetIconScalingToScalingArray(self):
        """
        V.SetIconScalingToScalingArray()
        C++: void SetIconScalingToScalingArray()
        
        Specify how to specify individual icons. By default, icon scaling
        is off, but if it is on, then the filter looks for an array named
        "IconScale" to control individual icon size.
        """
        ...
    
    def SetIconScalingToScalingOff(self):
        """
        V.SetIconScalingToScalingOff()
        C++: void SetIconScalingToScalingOff()
        
        Specify how to specify individual icons. By default, icon scaling
        is off, but if it is on, then the filter looks for an array named
        "IconScale" to control individual icon size.
        """
        ...
    
    def SetIconSheetSize(self, p_int, p_int_1):
        """
        V.SetIconSheetSize(int, int)
        C++: virtual void SetIconSheetSize(int _arg1, int _arg2)
        V.SetIconSheetSize((int, int))
        C++: void SetIconSheetSize(const int _arg[2])
        
        Specify the Width and Height, in pixels, of an icon in the icon
        sheet.
        """
        ...
    
    def SetIconSize(self, p_int, p_int_1):
        """
        V.SetIconSize(int, int)
        C++: virtual void SetIconSize(int _arg1, int _arg2)
        V.SetIconSize((int, int))
        C++: void SetIconSize(const int _arg[2])
        
        Specify the Width and Height, in pixels, of an icon in the icon
        sheet.
        """
        ...
    
    def SetOffset(self, p_int, p_int_1):
        """
        V.SetOffset(int, int)
        C++: virtual void SetOffset(int _arg1, int _arg2)
        V.SetOffset((int, int))
        C++: void SetOffset(const int _arg[2])
        
        Specify an offset (in pixels or display coordinates) that offsets
        the icons from their generating points.
        """
        ...
    
    def SetPassScalars(self, bool):
        """
        V.SetPassScalars(bool)
        C++: virtual void SetPassScalars(bool _arg)
        
        Specify whether to pass the scalar icon index to the output. By
        default this is not passed since it can affect color during the
        rendering process. Note that all other point data is passed to
        the output regardless of the value of this flag.
        """
        ...
    
    def SetUseIconSize(self, bool):
        """
        V.SetUseIconSize(bool)
        C++: virtual void SetUseIconSize(bool _arg)
        
        Specify whether the Quad generated to place the icon on will be
        either the dimensions specified by IconSize or the DisplaySize.
        """
        ...
    
    def UseIconSizeOff(self):
        """
        V.UseIconSizeOff()
        C++: virtual void UseIconSizeOff()
        
        Specify whether the Quad generated to place the icon on will be
        either the dimensions specified by IconSize or the DisplaySize.
        """
        ...
    
    def UseIconSizeOn(self):
        """
        V.UseIconSizeOn()
        C++: virtual void UseIconSizeOn()
        
        Specify whether the Quad generated to place the icon on will be
        either the dimensions specified by IconSize or the DisplaySize.
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

