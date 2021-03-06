"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkStructuredGridAppend(__vtkmodules_vtkCommonExecutionModel.vtkStructuredGridAlgorithm):
    """
    vtkStructuredGridAppend - Collects data from multiple inputs into one
    structured grid.
    
    Superclass: vtkStructuredGridAlgorithm
    
    vtkStructuredGridAppend takes the components from multiple inputs and
    merges them into one output. All inputs must have the same number of
    scalar components. All inputs must have the same scalar type.
    """
    def GetInput(self, p_int):
        """
        V.GetInput(int) -> vtkDataObject
        C++: vtkDataObject *GetInput(int num)
        V.GetInput() -> vtkDataObject
        C++: vtkDataObject *GetInput()
        
        Get one input to this filter. This method is only for support of
        old-style pipeline connections.  When writing new code you should
        use vtkAlgorithm::GetInputConnection(0, num).
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
    
    def GetNumberOfInputs(self):
        """
        V.GetNumberOfInputs() -> int
        C++: int GetNumberOfInputs()
        
        Get the number of inputs to this filter. This method is only for
        support of old-style pipeline connections.  When writing new code
        you should use vtkAlgorithm::GetNumberOfInputConnections(0).
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
        V.NewInstance() -> vtkStructuredGridAppend
        C++: vtkStructuredGridAppend *NewInstance()
        """
        ...
    
    def ReplaceNthInputConnection(self, p_int, vtkAlgorithmOutput):
        """
        V.ReplaceNthInputConnection(int, vtkAlgorithmOutput)
        C++: virtual void ReplaceNthInputConnection(int idx,
            vtkAlgorithmOutput *input)
        
        Replace one of the input connections with a new input.  You can
        only replace input connections that you previously created with
        AddInputConnection() or, in the case of the first input, with
        SetInputConnection().
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkStructuredGridAppend
        C++: static vtkStructuredGridAppend *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetInputData(self, p_int, vtkDataObject):
        """
        V.SetInputData(int, vtkDataObject)
        C++: void SetInputData(int num, vtkDataObject *input)
        V.SetInputData(vtkDataObject)
        C++: void SetInputData(vtkDataObject *input)
        
        Assign a data object as input. Note that this method does not
        establish a pipeline connection. Use SetInputConnection() to
        setup a pipeline connection.
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


