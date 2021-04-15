"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkSelector(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkSelector - Computes the portion of a dataset which is inside a
    selection
    
    Superclass: vtkObject
    
    This is an abstract superclass for types of selection operations.
    Subclasses generally only need to override `ComputeSelectedElements`.
    """
    def Execute(self, vtkDataObject, vtkDataObject_1):
        """
        V.Execute(vtkDataObject, vtkDataObject)
        C++: virtual void Execute(vtkDataObject *input,
            vtkDataObject *output)
        
        Given an input and the vtkSelectionNode passed into the
        Initialize() method, add to the output a vtkSignedChar attribute
        array indicating whether each element is inside (1) or outside
        (0) the selection. The attribute (point data or cell data) is
        determined by the vtkSelection that owns the vtkSelectionNode set
        in Initialize(). The insidedness array is named with the value of
        InsidednessArrayName. If input is a vtkCompositeDataSet, the
        insidedness array is added to each block.
        """
        ...
    
    def Finalize(self):
        """
        V.Finalize()
        C++: virtual void Finalize()
        
        Does any cleanup of objects created in Initialize
        """
        ...
    
    def GetInsidednessArrayName(self):
        """
        V.GetInsidednessArrayName() -> string
        C++: virtual std::string GetInsidednessArrayName()
        
        Get/Set the name of the array to use for the insidedness array to
        add to the output in `Execute` call.
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
    
    def Initialize(self, vtkSelectionNode):
        """
        V.Initialize(vtkSelectionNode)
        C++: virtual void Initialize(vtkSelectionNode *node)
        
        Sets the vtkSelectionNode used by this selection operator and
        initializes the data structures in the selection operator based
        on the selection.
        
        (for example in the vtkFrustumSelector this creates the vtkPlanes
        implicit function to represent the frustum).
        
        @param node The selection node that determines the behavior of
            this operator.
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
        V.NewInstance() -> vtkSelector
        C++: vtkSelector *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSelector
        C++: static vtkSelector *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetInsidednessArrayName(self, string):
        """
        V.SetInsidednessArrayName(string)
        C++: virtual void SetInsidednessArrayName(std::string _arg)
        
        Get/Set the name of the array to use for the insidedness array to
        add to the output in `Execute` call.
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


