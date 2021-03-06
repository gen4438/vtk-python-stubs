"""
This type stub file was generated by pyright.
"""

from .vtkXMLDataReader import vtkXMLDataReader

class vtkXMLGenericDataObjectReader(vtkXMLDataReader):
    """
    vtkXMLGenericDataObjectReader - Read any type of vtk data object
    
    Superclass: vtkXMLDataReader
    
    vtkXMLGenericDataObjectReader reads any type of vtk data object
    encoded in XML format.
    
    @sa
    vtkGenericDataObjectReader
    """
    def GetHierarchicalBoxDataSetOutput(self):
        """
        V.GetHierarchicalBoxDataSetOutput() -> vtkHierarchicalBoxDataSet
        C++: vtkHierarchicalBoxDataSet *GetHierarchicalBoxDataSetOutput()
        
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general GetOutput() method. If the
        wrong type is used nullptr is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
        ...
    
    def GetImageDataOutput(self):
        """
        V.GetImageDataOutput() -> vtkImageData
        C++: vtkImageData *GetImageDataOutput()
        
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general GetOutput() method. If the
        wrong type is used nullptr is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
        ...
    
    def GetMultiBlockDataSetOutput(self):
        """
        V.GetMultiBlockDataSetOutput() -> vtkMultiBlockDataSet
        C++: vtkMultiBlockDataSet *GetMultiBlockDataSetOutput()
        
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general GetOutput() method. If the
        wrong type is used nullptr is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
        ...
    
    def GetNumberOfCells(self):
        """
        V.GetNumberOfCells() -> int
        C++: vtkIdType GetNumberOfCells() override;
        
        Overridden method.
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
    
    def GetNumberOfPoints(self):
        """
        V.GetNumberOfPoints() -> int
        C++: vtkIdType GetNumberOfPoints() override;
        
        Overridden method.
        """
        ...
    
    def GetOutput(self):
        """
        V.GetOutput() -> vtkDataObject
        C++: vtkDataObject *GetOutput()
        V.GetOutput(int) -> vtkDataObject
        C++: vtkDataObject *GetOutput(int idx)
        
        Get the reader's output.
        """
        ...
    
    def GetPolyDataOutput(self):
        """
        V.GetPolyDataOutput() -> vtkPolyData
        C++: vtkPolyData *GetPolyDataOutput()
        
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general GetOutput() method. If the
        wrong type is used nullptr is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
        ...
    
    def GetRectilinearGridOutput(self):
        """
        V.GetRectilinearGridOutput() -> vtkRectilinearGrid
        C++: vtkRectilinearGrid *GetRectilinearGridOutput()
        
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general GetOutput() method. If the
        wrong type is used nullptr is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
        ...
    
    def GetStructuredGridOutput(self):
        """
        V.GetStructuredGridOutput() -> vtkStructuredGrid
        C++: vtkStructuredGrid *GetStructuredGridOutput()
        
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general GetOutput() method. If the
        wrong type is used nullptr is returned.  (You must also set the
        filename of the object prior to getting the output.)
        """
        ...
    
    def GetUnstructuredGridOutput(self):
        """
        V.GetUnstructuredGridOutput() -> vtkUnstructuredGrid
        C++: vtkUnstructuredGrid *GetUnstructuredGridOutput()
        
        Get the output as various concrete types. This method is
        typically used when you know exactly what type of data is being
        read.  Otherwise, use the general GetOutput() method. If the
        wrong type is used nullptr is returned.  (You must also set the
        filename of the object prior to getting the output.)
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
        V.NewInstance() -> vtkXMLGenericDataObjectReader
        C++: vtkXMLGenericDataObjectReader *NewInstance()
        """
        ...
    
    def ReadOutputType(self, string, bool):
        """
        V.ReadOutputType(string, bool) -> int
        C++: virtual int ReadOutputType(const char *name, bool &parallel)
        
        This method can be used to find out the type of output expected
        without needing to read the whole file.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkXMLGenericDataObjectReader
        C++: static vtkXMLGenericDataObjectReader *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetupEmptyOutput(self):
        """
        V.SetupEmptyOutput()
        C++: void SetupEmptyOutput() override;
        
        Overridden method. Not Used. Delegated.
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


