"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkExtractVectorComponents(__vtkmodules_vtkCommonExecutionModel.vtkDataSetAlgorithm):
    """
    vtkExtractVectorComponents - extract components of vector as separate
    scalars
    
    Superclass: vtkDataSetAlgorithm
    
    vtkExtractVectorComponents is a filter that extracts vector
    components as separate scalars. This is accomplished by creating
    three different outputs. Each output is the same as the input, except
    that the scalar values will be one of the three components of the
    vector. These can be found in the VxComponent, VyComponent, and
    VzComponent. Alternatively, if the ExtractToFieldData flag is set,
    the filter will put all the components in the field data. The first
    component will be the scalar and the others will be non-attribute
    arrays.
    
    @warning
    This filter is unusual in that it creates multiple outputs. If you
    use the GetOutput() method, you will be retrieving the x vector
    component.
    """
    def ExtractToFieldDataOff(self):
        """
        V.ExtractToFieldDataOff()
        C++: virtual void ExtractToFieldDataOff()
        
        Determines whether the vector components will be put in separate
        outputs or in the first output's field data
        """
        ...
    
    def ExtractToFieldDataOn(self):
        """
        V.ExtractToFieldDataOn()
        C++: virtual void ExtractToFieldDataOn()
        
        Determines whether the vector components will be put in separate
        outputs or in the first output's field data
        """
        ...
    
    def GetExtractToFieldData(self):
        """
        V.GetExtractToFieldData() -> int
        C++: virtual vtkTypeBool GetExtractToFieldData()
        
        Determines whether the vector components will be put in separate
        outputs or in the first output's field data
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
    
    def GetVxComponent(self):
        """
        V.GetVxComponent() -> vtkDataSet
        C++: vtkDataSet *GetVxComponent()
        
        Get the output dataset representing velocity x-component. If
        output is nullptr then input hasn't been set, which is necessary
        for abstract objects. (Note: this method returns the same
        information as the GetOutput() method with an index of 0.)
        """
        ...
    
    def GetVyComponent(self):
        """
        V.GetVyComponent() -> vtkDataSet
        C++: vtkDataSet *GetVyComponent()
        
        Get the output dataset representing velocity y-component. If
        output is nullptr then input hasn't been set, which is necessary
        for abstract objects. (Note: this method returns the same
        information as the GetOutput() method with an index of 1.) Note
        that if ExtractToFieldData is true, this output will be empty.
        """
        ...
    
    def GetVzComponent(self):
        """
        V.GetVzComponent() -> vtkDataSet
        C++: vtkDataSet *GetVzComponent()
        
        Get the output dataset representing velocity z-component. If
        output is nullptr then input hasn't been set, which is necessary
        for abstract objects. (Note: this method returns the same
        information as the GetOutput() method with an index of 2.) Note
        that if ExtractToFieldData is true, this output will be empty.
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
        V.NewInstance() -> vtkExtractVectorComponents
        C++: vtkExtractVectorComponents *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtractVectorComponents
        C++: static vtkExtractVectorComponents *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetExtractToFieldData(self, p_int):
        """
        V.SetExtractToFieldData(int)
        C++: virtual void SetExtractToFieldData(vtkTypeBool _arg)
        
        Determines whether the vector components will be put in separate
        outputs or in the first output's field data
        """
        ...
    
    def SetInputData(self, vtkDataSet):
        """
        V.SetInputData(vtkDataSet)
        C++: virtual void SetInputData(vtkDataSet *input)
        
        Specify the input data or filter.
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


