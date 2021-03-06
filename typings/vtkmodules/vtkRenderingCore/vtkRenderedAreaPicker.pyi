"""
This type stub file was generated by pyright.
"""

from .vtkAreaPicker import vtkAreaPicker

class vtkRenderedAreaPicker(vtkAreaPicker):
    """
    vtkRenderedAreaPicker - Uses graphics hardware to picks props behind
    a selection rectangle on a viewport.
    
    Superclass: vtkAreaPicker
    
    Like vtkAreaPicker, this class picks all props within a selection
    area on the screen. The difference is in implementation. This class
    uses graphics hardware to perform the test where the other uses
    software bounding box/frustum intersection testing.
    
    This picker is more conservative than vtkAreaPicker. It will reject
    some objects that pass the bounding box test of vtkAreaPicker. This
    will happen, for instance, when picking through a corner of the
    bounding box when the data set does not have any visible geometry in
    that corner.
    """
    def AreaPick(self, p_float, p_float_1, p_float_2, p_float_3, vtkRenderer):
        """
        V.AreaPick(float, float, float, float, vtkRenderer) -> int
        C++: int AreaPick(double x0, double y0, double x1, double y1,
            vtkRenderer *) override;
        
        Perform pick operation in volume behind the given screen
        coordinates. Props intersecting the selection frustum will be
        accessible via GetProp3D. GetPlanes returns a vtkImplicitFunction
        suitable for vtkExtractGeometry.
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
        V.NewInstance() -> vtkRenderedAreaPicker
        C++: vtkRenderedAreaPicker *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkRenderedAreaPicker
        C++: static vtkRenderedAreaPicker *SafeDownCast(vtkObjectBase *o)
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


