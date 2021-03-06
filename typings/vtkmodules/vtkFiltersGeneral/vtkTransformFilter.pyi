"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkTransformFilter(__vtkmodules_vtkCommonExecutionModel.vtkPointSetAlgorithm):
    """
    vtkTransformFilter - transform points and associated normals and
    vectors
    
    Superclass: vtkPointSetAlgorithm
    
    vtkTransformFilter is a filter to transform point coordinates, and
    associated point normals and vectors, as well as cell normals and
    vectors. Transformed data array will be stored in a float array or a
    double array. Other point and cel data are passed through the filter,
    unless TransformAllInputVectors is set to true, in this case all
    other 3 components arrays from point and cell data will be
    transformed as well.
    
    An alternative method of transformation is to use vtkActor's methods
    to scale, rotate, and translate objects. The difference between the
    two methods is that vtkActor's transformation simply effects where
    objects are rendered (via the graphics pipeline), whereas
    vtkTransformFilter actually modifies point coordinates in the
    visualization pipeline. This is necessary for some objects (e.g.,
    vtkProbeFilter) that require point coordinates as input.
    
    @sa
    vtkAbstractTransform vtkTransformPolyDataFilter vtkActor
    """
    def FillInputPortInformation(self, p_int, vtkInformation):
        """
        V.FillInputPortInformation(int, vtkInformation) -> int
        C++: int FillInputPortInformation(int port, vtkInformation *info)
            override;
        
        Fill the input port information objects for this algorithm.  This
        is invoked by the first call to GetInputPortInformation for each
        port so subclasses can specify what they can handle.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Return the MTime also considering the transform.
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
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
        ...
    
    def GetTransform(self):
        """
        V.GetTransform() -> vtkAbstractTransform
        C++: virtual vtkAbstractTransform *GetTransform()
        
        Specify the transform object used to transform points.
        """
        ...
    
    def GetTransformAllInputVectors(self):
        """
        V.GetTransformAllInputVectors() -> bool
        C++: virtual bool GetTransformAllInputVectors()
        
        If off (the default), only Vectors and Normals will be
        transformed. If on, all 3-component data arrays ( considered as
        3D vectors) will be transformed All other won't be flipped and
        will only be copied.
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
        V.NewInstance() -> vtkTransformFilter
        C++: vtkTransformFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTransformFilter
        C++: static vtkTransformFilter *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetOutputPointsPrecision(self, p_int):
        """
        V.SetOutputPointsPrecision(int)
        C++: virtual void SetOutputPointsPrecision(int _arg)
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
        ...
    
    def SetTransform(self, vtkAbstractTransform):
        """
        V.SetTransform(vtkAbstractTransform)
        C++: virtual void SetTransform(vtkAbstractTransform *)
        
        Specify the transform object used to transform points.
        """
        ...
    
    def SetTransformAllInputVectors(self, bool):
        """
        V.SetTransformAllInputVectors(bool)
        C++: virtual void SetTransformAllInputVectors(bool _arg)
        
        If off (the default), only Vectors and Normals will be
        transformed. If on, all 3-component data arrays ( considered as
        3D vectors) will be transformed All other won't be flipped and
        will only be copied.
        """
        ...
    
    def TransformAllInputVectorsOff(self):
        """
        V.TransformAllInputVectorsOff()
        C++: virtual void TransformAllInputVectorsOff()
        
        If off (the default), only Vectors and Normals will be
        transformed. If on, all 3-component data arrays ( considered as
        3D vectors) will be transformed All other won't be flipped and
        will only be copied.
        """
        ...
    
    def TransformAllInputVectorsOn(self):
        """
        V.TransformAllInputVectorsOn()
        C++: virtual void TransformAllInputVectorsOn()
        
        If off (the default), only Vectors and Normals will be
        transformed. If on, all 3-component data arrays ( considered as
        3D vectors) will be transformed All other won't be flipped and
        will only be copied.
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


