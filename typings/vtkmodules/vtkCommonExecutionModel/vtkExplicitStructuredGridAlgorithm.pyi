"""
This type stub file was generated by pyright.
"""

from .vtkAlgorithm import vtkAlgorithm

class vtkExplicitStructuredGridAlgorithm(vtkAlgorithm):
    """
    vtkExplicitStructuredGridAlgorithm - Superclass for algorithms that
    produce only explicit structured grid as output.
    
    Superclass: vtkAlgorithm
    """
    def AddInputData(self, vtkDataObject):
        """
        V.AddInputData(vtkDataObject)
        C++: void AddInputData(vtkDataObject *)
        V.AddInputData(int, vtkDataObject)
        C++: void AddInputData(int, vtkDataObject *)
        
        Assign a data object as input. Note that this method does not
        establish a pipeline connection. Use AddInputConnection() to
        setup a pipeline connection.
        """
        ...
    
    def GetExplicitStructuredGridInput(self, p_int):
        """
        V.GetExplicitStructuredGridInput(int) -> vtkExplicitStructuredGrid
        C++: vtkExplicitStructuredGrid *GetExplicitStructuredGridInput(
            int port)
        """
        ...
    
    def GetInput(self):
        """
        V.GetInput() -> vtkDataObject
        C++: vtkDataObject *GetInput()
        V.GetInput(int) -> vtkDataObject
        C++: vtkDataObject *GetInput(int port)
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
    
    def GetOutput(self):
        """
        V.GetOutput() -> vtkExplicitStructuredGrid
        C++: vtkExplicitStructuredGrid *GetOutput()
        V.GetOutput(int) -> vtkExplicitStructuredGrid
        C++: vtkExplicitStructuredGrid *GetOutput(int)
        
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
        V.NewInstance() -> vtkExplicitStructuredGridAlgorithm
        C++: vtkExplicitStructuredGridAlgorithm *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkExplicitStructuredGridAlgorithm
        C++: static vtkExplicitStructuredGridAlgorithm *SafeDownCast(
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
    
    def SetOutput(self, vtkDataObject):
        """
        V.SetOutput(vtkDataObject)
        C++: virtual void SetOutput(vtkDataObject *d)
        
        Get the output data object for a port on this algorithm.
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


