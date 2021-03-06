"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkStringToImage(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkStringToImage - base class for classes that render supplied text
    to an image.
    
    Superclass: vtkObject
    """
    def GetBounds(self, vtkTextProperty, unicode, p_int):
        """
        V.GetBounds(vtkTextProperty, unicode, int) -> vtkVector2i
        C++: virtual vtkVector2i GetBounds(vtkTextProperty *property,
            const vtkUnicodeString &string, int dpi)
        V.GetBounds(vtkTextProperty, string, int) -> vtkVector2i
        C++: virtual vtkVector2i GetBounds(vtkTextProperty *property,
            const vtkStdString &string, int dpi)
        
        Given a text property and a string, get the bounding box [xmin,
        xmax] x [ymin, ymax]. Note that this is the bounding box of the
        area where actual pixels will be written, given a
        text/pen/baseline location of (0,0). For example, if the string
        starts with a 'space', or depending on the orientation, you can
        end up with a [-20, -10] x [5, 10] bbox (the math to get the real
        bbox is straightforward). Return 1 on success, 0 otherwise. You
        can use IsBoundingBoxValid() to test if the computed bbox is
        valid (it may not if GetBoundingBox() failed or if the string was
        empty).
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
    
    def GetScaleToPowerOfTwo(self):
        """
        V.GetScaleToPowerOfTwo() -> bool
        C++: virtual bool GetScaleToPowerOfTwo()
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
        V.NewInstance() -> vtkStringToImage
        C++: vtkStringToImage *NewInstance()
        """
        ...
    
    def RenderString(self, vtkTextProperty, unicode, p_int, vtkImageData, p_int=..., p_int=...):
        """
        V.RenderString(vtkTextProperty, unicode, int, vtkImageData, [int,
            int]) -> int
        C++: virtual int RenderString(vtkTextProperty *property,
            const vtkUnicodeString &string, int dpi, vtkImageData *data,
            int textDims[2]=nullptr)
        V.RenderString(vtkTextProperty, string, int, vtkImageData, [int,
            int]) -> int
        C++: virtual int RenderString(vtkTextProperty *property,
            const vtkStdString &string, int dpi, vtkImageData *data,
            int text_dims[2]=nullptr)
        
        Given a text property and a string, this function initializes the
        vtkImageData *data and renders it in a vtkImageData. textDims, if
        provided, will be overwritten by the pixel width and height of
        the rendered string. This is useful when ScaleToPowerOfTwo is
        true, and the image dimensions may not match the dimensions of
        the rendered text.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkStringToImage
        C++: static vtkStringToImage *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetScaleToPowerOfTwo(self, bool):
        """
        V.SetScaleToPowerOfTwo(bool)
        C++: virtual void SetScaleToPowerOfTwo(bool scale)
        
        Should we produce images at powers of 2, makes rendering on old
        OpenGL hardware easier. Default is false.
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


