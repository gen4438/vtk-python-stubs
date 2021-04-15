"""
This type stub file was generated by pyright.
"""

from .vtkAbstractMapper import vtkAbstractMapper

class vtkAbstractMapper3D(vtkAbstractMapper):
    """
    vtkAbstractMapper3D - abstract class specifies interface to map 3D
    data
    
    Superclass: vtkAbstractMapper
    
    vtkAbstractMapper3D is an abstract class to specify interface between
    3D data and graphics primitives or software rendering techniques.
    Subclasses of vtkAbstractMapper3D can be used for rendering geometry
    or rendering volumetric data.
    
    This class also defines an API to support hardware clipping planes
    (at most six planes can be defined). It also provides geometric data
    about the input data it maps, such as the bounding box and center.
    
    @sa
    vtkAbstractMapper vtkMapper vtkPolyDataMapper vtkVolumeMapper
    """
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: virtual double *GetBounds()
        V.GetBounds([float, float, float, float, float, float])
        C++: virtual void GetBounds(double bounds[6])
        
        Return bounding box (array of six doubles) of data expressed as
        (xmin,xmax, ymin,ymax, zmin,zmax). Update this->Bounds as a side
        effect.
        """
        ...
    
    def GetCenter(self):
        """
        V.GetCenter() -> (float, float, float)
        C++: double *GetCenter()
        V.GetCenter([float, float, float])
        C++: void GetCenter(double center[3])
        
        Return the Center of this mapper's data.
        """
        ...
    
    def GetClippingPlaneInDataCoords(self, vtkMatrix4x4, p_int, p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetClippingPlaneInDataCoords(vtkMatrix4x4, int, [float, float,
            float, float])
        C++: void GetClippingPlaneInDataCoords(vtkMatrix4x4 *propMatrix,
            int i, double planeEquation[4])
        
        Get the ith clipping plane as a homogeneous plane equation. Use
        GetNumberOfClippingPlanes to get the number of planes.
        """
        ...
    
    def GetLength(self):
        """
        V.GetLength() -> float
        C++: double GetLength()
        
        Return the diagonal length of this mappers bounding box.
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
    
    def IsARayCastMapper(self):
        """
        V.IsARayCastMapper() -> int
        C++: virtual vtkTypeBool IsARayCastMapper()
        
        Is this a ray cast mapper? A subclass would return 1 if the ray
        caster is needed to generate an image from this mapper.
        """
        ...
    
    def IsARenderIntoImageMapper(self):
        """
        V.IsARenderIntoImageMapper() -> int
        C++: virtual vtkTypeBool IsARenderIntoImageMapper()
        
        Is this a "render into image" mapper? A subclass would return 1
        if the mapper produces an image by rendering into a software
        image buffer.
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
        V.NewInstance() -> vtkAbstractMapper3D
        C++: vtkAbstractMapper3D *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAbstractMapper3D
        C++: static vtkAbstractMapper3D *SafeDownCast(vtkObjectBase *o)
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


