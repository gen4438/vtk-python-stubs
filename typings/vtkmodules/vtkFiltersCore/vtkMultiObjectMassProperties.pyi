"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkMultiObjectMassProperties(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkMultiObjectMassProperties - compute volume and area of objects in
    a polygonal mesh
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkMultiObjectMassProperties estimates the volume and the surface
    area of a polygonal mesh. Multiple, valid closed objects may be
    represented, and each object is assumed to be defined as a polyhedron
    defined by polygonal faces (i.e., the faces do not have to be
    triangles). The algorithm computes the total volume and area, as well
    as per object values which are placed in data arrays. Note that an
    object is valid only if it is manifold and closed (i.e., each edge is
    used exactly two times by two different polygons). Invalid objects
    are processed but may produce inaccurate results. Inconsistent
    polygon ordering is also allowed.
    
    The algorithm is composed of two basic parts. First a connected
    traversal is performed to identify objects, detect whether the
    objects are valid, and ensure that the composing polygons are ordered
    consistently. Next, in threaded execution, a parallel process of
    computing areas and volumes is performed. It is possible to skip the
    first part if the SkipValidityCheck is enabled, AND a vtkIdTypeArray
    data array named "ObjectIds" is associated with the polygon input
    (i.e., cell data) that enumerates which object every polygon belongs
    to (i.e., indictaes that it is a boundary polygon of a specified
    object).
    
    The algorithm implemented here is inspired by this paper:
    http://chenlab.ece.cornell.edu/Publication/Cha/icip01_Cha.pdf. Also
    see the Stackflow entry: https://stackoverflow.com/questions/1406029/
    how-to-calculate-the-volume-of-a-3d-mesh-object-the-surface-of-which-i
    s-made-up. The general assumption here is that the model is of closed
    surface.  Also, this approach requires triangulating the polygons so
    triangle meshes are processed much faster. Finally, the volume and
    area calculations are done in paraellel (threaded) after a
    connectivity pass is made (used to identify objects and verify that
    they are manifold and closed).
    
    The output contains six additional data arrays. The arrays
    "ObjectValidity", "ObjectVolumes" and "ObjectAreas" are placed in the
    output field data.  These are arrays which indicate which objects are
    valid; the volume of each object; and the surface area of each
    object. Three additional arrays are placed in the output cell data,
    and indicate, on a per polygons basis, which object the polygon
    bounds "ObjectIds"; the polygon area "Areas"; and the contribution of
    volume "Volumes".  Additionally, the TotalVolume and TotalArea is
    available after the filter executes (i.e., the sum of the
    ObjectVolumes and ObjectAreas arrays).
    
    Per object validity, as mentioned previously, is reported in the
    ObjectValidity array. However another variable, AllValid, is set
    after filter execution which indicates whether all objects are valid
    (!=0) or not. This information can be used as a shortcut in case you
    want to skip validity checking on an object-by-object basis.
    
    @warning
    This filter operates on the polygonal data contained in the input
    vtkPolyData. Other types (verts, lines, triangle strips) are ignored
    and not passed to the output. The input polys and points, as well as
    associated point and cell data, are passed through to the output.
    
    @warning
    This filter is similar to vtkMassProperties. However
    vtkMassProperties operates on triangle meshes and assumes only a
    single, closed, properly oriented surface is represented.
    vtkMultiObjectMassProperties performs additional topological and
    connectivity operations to identify separate objects, and confirms
    that they are manifold. It also accommodates inconsistent ordering.
    
    @warning
    This class has been threaded with vtkSMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    vtkMassProperties
    """
    def GetAllValid(self):
        """
        V.GetAllValid() -> int
        C++: vtkTypeBool GetAllValid()
        
        Return whether all objects are valid or not. This is valid only
        after the filter executes.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def GetNumberOfObjects(self):
        """
        V.GetNumberOfObjects() -> int
        C++: vtkIdType GetNumberOfObjects()
        
        Return the number of objects identified. This is valid only after
        the filter executes. Check the ObjectValidity array which
        indicates which of these identified objects are valid. Invalid
        objects may have incorrect volume and area values.
        """
        ...
    
    def GetSkipValidityCheck(self):
        """
        V.GetSkipValidityCheck() -> int
        C++: virtual vtkTypeBool GetSkipValidityCheck()
        
        Indicate whether to skip the validity check (the first part of
        the algorithm). By default this is off; however even if enabled
        validity skipping will only occur if a vtkIdTypeArray named
        "ObjectIds" is also provided on input to the filter.
        """
        ...
    
    def GetTotalArea(self):
        """
        V.GetTotalArea() -> float
        C++: double GetTotalArea()
        
        Return the summed area of all objects. This is valid only after
        the filter executes.
        """
        ...
    
    def GetTotalVolume(self):
        """
        V.GetTotalVolume() -> float
        C++: double GetTotalVolume()
        
        Return the summed volume of all objects. This is valid only after
        the filter executes.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkMultiObjectMassProperties
        C++: vtkMultiObjectMassProperties *NewInstance()
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkMultiObjectMassProperties
        C++: static vtkMultiObjectMassProperties *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def SetSkipValidityCheck(self, p_int):
        """
        V.SetSkipValidityCheck(int)
        C++: virtual void SetSkipValidityCheck(vtkTypeBool _arg)
        
        Indicate whether to skip the validity check (the first part of
        the algorithm). By default this is off; however even if enabled
        validity skipping will only occur if a vtkIdTypeArray named
        "ObjectIds" is also provided on input to the filter.
        """
        ...
    
    def SkipValidityCheckOff(self):
        """
        V.SkipValidityCheckOff()
        C++: virtual void SkipValidityCheckOff()
        
        Indicate whether to skip the validity check (the first part of
        the algorithm). By default this is off; however even if enabled
        validity skipping will only occur if a vtkIdTypeArray named
        "ObjectIds" is also provided on input to the filter.
        """
        ...
    
    def SkipValidityCheckOn(self):
        """
        V.SkipValidityCheckOn()
        C++: virtual void SkipValidityCheckOn()
        
        Indicate whether to skip the validity check (the first part of
        the algorithm). By default this is off; however even if enabled
        validity skipping will only occur if a vtkIdTypeArray named
        "ObjectIds" is also provided on input to the filter.
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

