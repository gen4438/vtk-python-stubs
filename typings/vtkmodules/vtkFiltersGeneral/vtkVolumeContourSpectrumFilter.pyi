"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkVolumeContourSpectrumFilter(__vtkmodules_vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    """
    vtkVolumeContourSpectrumFilter - compute an approximation of the
    volume contour signature (evolution of the volume of the input
    tet-mesh along an arc of the Reeb graph).
    
    Superclass: vtkDataObjectAlgorithm
    
    The filter takes a vtkUnstructuredGrid as an input (port 0), along
    with a vtkReebGraph (port 1). The Reeb graph arc to consider can be
    specified with SetArcId() (default: 0). The number of (evenly
    distributed) samples of the signature can be defined with
    SetNumberOfSamples() (default value: 100). The filter will first try
    to pull as a scalar field the vtkDataArray with Id 'FieldId' of the
    vtkUnstructuredGrid, see SetFieldId (default: 0). The filter will
    abort if this field does not exist.
    
    The filter outputs a vtkTable with the volume contour signature
    approximation, each sample being evenly distributed in the function
    span of the arc.
    
    This filter is a typical example for designing your own contour
    signature filter (with customized metrics). It also shows typical
    vtkReebGraph traversals.
    
    Reference: C. Bajaj, V. Pascucci, D. Schikore, "The contour
    spectrum", IEEE Visualization, 167-174, 1997.
    """
    def GetArcId(self):
        """
        V.GetArcId() -> int
        C++: virtual vtkIdType GetArcId()
        
        Set the arc Id for which the contour signature has to be
        computed. Default value: 0
        """
        ...
    
    def GetFieldId(self):
        """
        V.GetFieldId() -> int
        C++: virtual vtkIdType GetFieldId()
        
        Set the scalar field Id Default value: 0
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
    
    def GetNumberOfSamples(self):
        """
        V.GetNumberOfSamples() -> int
        C++: virtual int GetNumberOfSamples()
        
        Set the number of samples in the output signature Default value:
        100
        """
        ...
    
    def GetOutput(self):
        """
        V.GetOutput() -> vtkTable
        C++: vtkTable *GetOutput()
        
        Get the output data object for a port on this algorithm.
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
        V.NewInstance() -> vtkVolumeContourSpectrumFilter
        C++: vtkVolumeContourSpectrumFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkVolumeContourSpectrumFilter
        C++: static vtkVolumeContourSpectrumFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetArcId(self, p_int):
        """
        V.SetArcId(int)
        C++: virtual void SetArcId(vtkIdType _arg)
        
        Set the arc Id for which the contour signature has to be
        computed. Default value: 0
        """
        ...
    
    def SetFieldId(self, p_int):
        """
        V.SetFieldId(int)
        C++: virtual void SetFieldId(vtkIdType _arg)
        
        Set the scalar field Id Default value: 0
        """
        ...
    
    def SetNumberOfSamples(self, p_int):
        """
        V.SetNumberOfSamples(int)
        C++: virtual void SetNumberOfSamples(int _arg)
        
        Set the number of samples in the output signature Default value:
        100
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

