"""
This type stub file was generated by pyright.
"""

from .vtkAbstractPropPicker import vtkAbstractPropPicker

class vtkAreaPicker(vtkAbstractPropPicker):
    """
    vtkAreaPicker - Picks props behind a selection rectangle on a
    viewport.
    
    Superclass: vtkAbstractPropPicker
    
    The vtkAreaPicker picks all vtkProp3Ds that lie behind the screen
    space rectangle from x0,y0 and x1,y1. The selection is based upon the
    bounding box of the prop and is thus not exact.
    
    Like vtkPicker, a pick results in a list of Prop3Ds because many
    props may lie within the pick frustum. You can also get an
    AssemblyPath, which in this case is defined to be the path to the one
    particular prop in the Prop3D list that lies nearest to the near
    plane.
    
    This picker also returns the selection frustum, defined as either a
    vtkPlanes, or a set of eight corner vertices in world space. The
    vtkPlanes version is an ImplicitFunction, which is suitable for use
    with the vtkExtractGeometry. The six frustum planes are in order:
    left, right, bottom, top, near, far
    
    Because this picker picks everything within a volume, the world pick
    point result is ill-defined. Therefore if you ask this class for the
    world pick position, you will get the centroid of the pick frustum.
    This may be outside of all props in the prop list.
    
    @sa
    vtkInteractorStyleRubberBandPick, vtkExtractSelectedFrustum.
    """
    def AreaPick(self, p_float, p_float_1, p_float_2, p_float_3, vtkRenderer):
        """
        V.AreaPick(float, float, float, float, vtkRenderer) -> int
        C++: virtual int AreaPick(double x0, double y0, double x1,
            double y1, vtkRenderer *renderer=nullptr)
        
        Perform pick operation in volume behind the given screen
        coordinates. Props intersecting the selection frustum will be
        accessible via GetProp3D. GetPlanes returns a vtkImplicitFunction
        suitable for vtkExtractGeometry.
        """
        ...
    
    def GetClipPoints(self):
        """
        V.GetClipPoints() -> vtkPoints
        C++: virtual vtkPoints *GetClipPoints()
        
        Return eight points that define the selection frustum.
        """
        ...
    
    def GetDataSet(self):
        """
        V.GetDataSet() -> vtkDataSet
        C++: virtual vtkDataSet *GetDataSet()
        
        Get a pointer to the dataset that was picked (if any). If nothing
        was picked then NULL is returned.
        """
        ...
    
    def GetFrustum(self):
        """
        V.GetFrustum() -> vtkPlanes
        C++: virtual vtkPlanes *GetFrustum()
        
        Return the six planes that define the selection frustum. The
        implicit function defined by the planes evaluates to negative
        inside and positive outside.
        """
        ...
    
    def GetMapper(self):
        """
        V.GetMapper() -> vtkAbstractMapper3D
        C++: virtual vtkAbstractMapper3D *GetMapper()
        
        Return mapper that was picked (if any).
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
    
    def GetProp3Ds(self):
        """
        V.GetProp3Ds() -> vtkProp3DCollection
        C++: vtkProp3DCollection *GetProp3Ds()
        
        Return a collection of all the prop 3D's that were intersected by
        the pick ray. This collection is not sorted.
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
        V.NewInstance() -> vtkAreaPicker
        C++: vtkAreaPicker *NewInstance()
        """
        ...
    
    def Pick(self):
        """
        V.Pick() -> int
        C++: virtual int Pick()
        V.Pick(float, float, float, vtkRenderer) -> int
        C++: int Pick(double x0, double y0, double z0,
            vtkRenderer *renderer=nullptr) override;
        
        Perform an AreaPick within the default screen rectangle and
        renderer.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAreaPicker
        C++: static vtkAreaPicker *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetPickCoords(self, p_float, p_float_1, p_float_2, p_float_3):
        """
        V.SetPickCoords(float, float, float, float)
        C++: void SetPickCoords(double x0, double y0, double x1,
            double y1)
        
        Set the default screen rectangle to pick in.
        """
        ...
    
    def SetRenderer(self, vtkRenderer):
        """
        V.SetRenderer(vtkRenderer)
        C++: void SetRenderer(vtkRenderer *)
        
        Set the default renderer to pick on.
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


