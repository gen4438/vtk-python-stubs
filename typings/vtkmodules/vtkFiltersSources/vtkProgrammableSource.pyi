"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkProgrammableSource(__vtkmodules_vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    """
    vtkProgrammableSource - generate source dataset via a user-specified
    function
    
    Superclass: vtkDataObjectAlgorithm
    
    vtkProgrammableSource is a source object that is programmable by the
    user. To use this object, you must specify a function that creates
    the output.  It is possible to generate an output dataset of any
    (concrete) type; it is up to the function to properly initialize and
    define the output. Typically, you use one of the methods to get a
    concrete output type (e.g., GetPolyDataOutput() or
    GetStructuredPointsOutput()), and then manipulate the output in the
    user-specified function.
    
    Example use of this include writing a function to read a data file or
    interface to another system. (You might want to do this in favor of
    deriving a new class.) Another important use of this class is that it
    allows users of interpreters (e.g., Java) the ability to write source
    objects without having to recompile C++ code or generate new
    libraries.
    @sa
    vtkProgrammableFilter vtkProgrammableAttributeDataFilter
    vtkProgrammableDataObjectSource
    """
    def GetGraphOutput(self):
        """
        V.GetGraphOutput() -> vtkGraph
        C++: vtkGraph *GetGraphOutput()
        
        Get the output as a concrete type. This method is typically used
        by the writer of the source function to get the output as a
        particular type (i.e., it essentially does type casting). It is
        the users responsibility to know the correct type of the output
        data.
        """
        ...
    
    def GetMoleculeOutput(self):
        """
        V.GetMoleculeOutput() -> vtkMolecule
        C++: vtkMolecule *GetMoleculeOutput()
        
        Get the output as a concrete type. This method is typically used
        by the writer of the source function to get the output as a
        particular type (i.e., it essentially does type casting). It is
        the users responsibility to know the correct type of the output
        data.
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
    
    def GetPolyDataOutput(self):
        """
        V.GetPolyDataOutput() -> vtkPolyData
        C++: vtkPolyData *GetPolyDataOutput()
        
        Get the output as a concrete type. This method is typically used
        by the writer of the source function to get the output as a
        particular type (i.e., it essentially does type casting). It is
        the users responsibility to know the correct type of the output
        data.
        """
        ...
    
    def GetRectilinearGridOutput(self):
        """
        V.GetRectilinearGridOutput() -> vtkRectilinearGrid
        C++: vtkRectilinearGrid *GetRectilinearGridOutput()
        
        Get the output as a concrete type. This method is typically used
        by the writer of the source function to get the output as a
        particular type (i.e., it essentially does type casting). It is
        the users responsibility to know the correct type of the output
        data.
        """
        ...
    
    def GetStructuredGridOutput(self):
        """
        V.GetStructuredGridOutput() -> vtkStructuredGrid
        C++: vtkStructuredGrid *GetStructuredGridOutput()
        
        Get the output as a concrete type. This method is typically used
        by the writer of the source function to get the output as a
        particular type (i.e., it essentially does type casting). It is
        the users responsibility to know the correct type of the output
        data.
        """
        ...
    
    def GetStructuredPointsOutput(self):
        """
        V.GetStructuredPointsOutput() -> vtkStructuredPoints
        C++: vtkStructuredPoints *GetStructuredPointsOutput()
        
        Get the output as a concrete type. This method is typically used
        by the writer of the source function to get the output as a
        particular type (i.e., it essentially does type casting). It is
        the users responsibility to know the correct type of the output
        data.
        """
        ...
    
    def GetTableOutput(self):
        """
        V.GetTableOutput() -> vtkTable
        C++: vtkTable *GetTableOutput()
        
        Get the output as a concrete type. This method is typically used
        by the writer of the source function to get the output as a
        particular type (i.e., it essentially does type casting). It is
        the users responsibility to know the correct type of the output
        data.
        """
        ...
    
    def GetUnstructuredGridOutput(self):
        """
        V.GetUnstructuredGridOutput() -> vtkUnstructuredGrid
        C++: vtkUnstructuredGrid *GetUnstructuredGridOutput()
        
        Get the output as a concrete type. This method is typically used
        by the writer of the source function to get the output as a
        particular type (i.e., it essentially does type casting). It is
        the users responsibility to know the correct type of the output
        data.
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
        V.NewInstance() -> vtkProgrammableSource
        C++: vtkProgrammableSource *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkProgrammableSource
        C++: static vtkProgrammableSource *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetExecuteMethod(self, function):
        """
        V.SetExecuteMethod(function)
        C++: void SetExecuteMethod(void (*f)(void *), void *arg)
        
        Specify the function to use to generate the source data. Note
        that the function takes a single (void *) argument.
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

