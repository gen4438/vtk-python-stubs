"""
This type stub file was generated by pyright.
"""

from .vtkAlgorithm import vtkAlgorithm

class vtkCompositeDataSetAlgorithm(vtkAlgorithm):
    """
    vtkCompositeDataSetAlgorithm - Superclass for algorithms that produce
    only vtkCompositeDataSet as output
    
    Superclass: vtkAlgorithm
    
    Algorithms that take any type of data object (including composite
    dataset) and produce a vtkCompositeDataSet in the output can subclass
    from this class.
    """
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
    
    def GetOutput(self):
        """
        V.GetOutput() -> vtkCompositeDataSet
        C++: vtkCompositeDataSet *GetOutput()
        V.GetOutput(int) -> vtkCompositeDataSet
        C++: vtkCompositeDataSet *GetOutput(int)
        
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
        V.NewInstance() -> vtkCompositeDataSetAlgorithm
        C++: vtkCompositeDataSetAlgorithm *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCompositeDataSetAlgorithm
        C++: static vtkCompositeDataSetAlgorithm *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetInputData(self, vtkDataObject):
        """
        V.SetInputData(vtkDataObject)
        C++: void SetInputData(vtkDataObject *)
        V.SetInputData(int, vtkDataObject)
        C++: void SetInputData(int, vtkDataObject *)
        
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


