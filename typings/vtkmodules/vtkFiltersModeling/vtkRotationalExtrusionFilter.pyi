"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkRotationalExtrusionFilter(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkRotationalExtrusionFilter - sweep polygonal data creating "skirt"
    from free edges and lines, and lines from vertices
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkRotationalExtrusionFilter is a modeling filter. It takes polygonal
    data as input and generates polygonal data on output. The input
    dataset is swept around the z-axis to create new polygonal
    primitives. These primitives form a "skirt" or swept surface. For
    example, sweeping a line results in a cylindrical shell, and sweeping
    a circle creates a torus.
    
    There are a number of control parameters for this filter. You can
    control whether the sweep of a 2D object (i.e., polygon or triangle
    strip) is capped with the generating geometry via the "Capping"
    instance variable. Also, you can control the angle of rotation, and
    whether translation along the z-axis is performed along with the
    rotation. (Translation is useful for creating "springs".) You also
    can adjust the radius of the generating geometry using the
    "DeltaRotation" instance variable.
    
    The skirt is generated by locating certain topological features. Free
    edges (edges of polygons or triangle strips only used by one polygon
    or triangle strips) generate surfaces. This is true also of lines or
    polylines. Vertices generate lines.
    
    This filter can be used to model axisymmetric objects like cylinders,
    bottles, and wine glasses; or translational/rotational symmetric
    objects like springs or corkscrews.
    
    @warning
    If the object sweeps 360 degrees, radius does not vary, and the
    object does not translate, capping is not performed. This is because
    the cap is unnecessary.
    
    @warning
    Some polygonal objects have no free edges (e.g., sphere). When swept,
    this will result in two separate surfaces if capping is on, or no
    surface if capping is off.
    
    @sa
    vtkLinearExtrusionFilter
    """
    def CappingOff(self):
        """
        V.CappingOff()
        C++: virtual void CappingOff()
        
        Turn on/off the capping of the skirt.
        """
        ...
    
    def CappingOn(self):
        """
        V.CappingOn()
        C++: virtual void CappingOn()
        
        Turn on/off the capping of the skirt.
        """
        ...
    
    def GetAngle(self):
        """
        V.GetAngle() -> float
        C++: virtual double GetAngle()
        
        Set/Get angle of rotation.
        """
        ...
    
    def GetCapping(self):
        """
        V.GetCapping() -> int
        C++: virtual vtkTypeBool GetCapping()
        
        Turn on/off the capping of the skirt.
        """
        ...
    
    def GetDeltaRadius(self):
        """
        V.GetDeltaRadius() -> float
        C++: virtual double GetDeltaRadius()
        
        Set/Get change in radius during sweep process.
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
    
    def GetTranslation(self):
        """
        V.GetTranslation() -> float
        C++: virtual double GetTranslation()
        
        Set/Get total amount of translation along the z-axis.
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
        V.NewInstance() -> vtkRotationalExtrusionFilter
        C++: vtkRotationalExtrusionFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkRotationalExtrusionFilter
        C++: static vtkRotationalExtrusionFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetAngle(self, p_float):
        """
        V.SetAngle(float)
        C++: virtual void SetAngle(double _arg)
        
        Set/Get angle of rotation.
        """
        ...
    
    def SetCapping(self, p_int):
        """
        V.SetCapping(int)
        C++: virtual void SetCapping(vtkTypeBool _arg)
        
        Turn on/off the capping of the skirt.
        """
        ...
    
    def SetDeltaRadius(self, p_float):
        """
        V.SetDeltaRadius(float)
        C++: virtual void SetDeltaRadius(double _arg)
        
        Set/Get change in radius during sweep process.
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
    
    def SetTranslation(self, p_float):
        """
        V.SetTranslation(float)
        C++: virtual void SetTranslation(double _arg)
        
        Set/Get total amount of translation along the z-axis.
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


