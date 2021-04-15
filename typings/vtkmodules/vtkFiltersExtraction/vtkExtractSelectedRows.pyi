"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkExtractSelectedRows(__vtkmodules_vtkCommonExecutionModel.vtkTableAlgorithm):
    """
    vtkExtractSelectedRows - return selected rows of a table
    
    Superclass: vtkTableAlgorithm
    
    The first input is a vtkTable to extract rows from. The second input
    is a vtkSelection containing the selected indices. The third input is
    a vtkAnnotationLayers containing selected indices. The field type of
    the input selection is ignored when converted to row indices.
    """
    def AddOriginalRowIdsArrayOff(self):
        """
        V.AddOriginalRowIdsArrayOff()
        C++: virtual void AddOriginalRowIdsArrayOff()
        
        When set, a column named vtkOriginalRowIds will be added to the
        output. False by default.
        """
        ...
    
    def AddOriginalRowIdsArrayOn(self):
        """
        V.AddOriginalRowIdsArrayOn()
        C++: virtual void AddOriginalRowIdsArrayOn()
        
        When set, a column named vtkOriginalRowIds will be added to the
        output. False by default.
        """
        ...
    
    def FillInputPortInformation(self, p_int, vtkInformation):
        """
        V.FillInputPortInformation(int, vtkInformation) -> int
        C++: int FillInputPortInformation(int port, vtkInformation *info)
            override;
        
        Specify the first vtkGraph input and the second vtkSelection
        input.
        """
        ...
    
    def GetAddOriginalRowIdsArray(self):
        """
        V.GetAddOriginalRowIdsArray() -> bool
        C++: virtual bool GetAddOriginalRowIdsArray()
        
        When set, a column named vtkOriginalRowIds will be added to the
        output. False by default.
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
        V.NewInstance() -> vtkExtractSelectedRows
        C++: vtkExtractSelectedRows *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtractSelectedRows
        C++: static vtkExtractSelectedRows *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAddOriginalRowIdsArray(self, bool):
        """
        V.SetAddOriginalRowIdsArray(bool)
        C++: virtual void SetAddOriginalRowIdsArray(bool _arg)
        
        When set, a column named vtkOriginalRowIds will be added to the
        output. False by default.
        """
        ...
    
    def SetAnnotationLayersConnection(self, vtkAlgorithmOutput):
        """
        V.SetAnnotationLayersConnection(vtkAlgorithmOutput)
        C++: void SetAnnotationLayersConnection(vtkAlgorithmOutput *in)
        
        A convenience method for setting the third input (i.e. the
        annotation layers).
        """
        ...
    
    def SetSelectionConnection(self, vtkAlgorithmOutput):
        """
        V.SetSelectionConnection(vtkAlgorithmOutput)
        C++: void SetSelectionConnection(vtkAlgorithmOutput *in)
        
        A convenience method for setting the second input (i.e. the
        selection).
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

