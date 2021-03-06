"""
This type stub file was generated by pyright.
"""

from .vtkXMLDataReader import vtkXMLDataReader

class vtkXMLStructuredDataReader(vtkXMLDataReader):
    """
    vtkXMLStructuredDataReader - Superclass for structured data XML
    readers.
    
    Superclass: vtkXMLDataReader
    
    vtkXMLStructuredDataReader provides functionality common to all
    structured data format readers.
    
    @sa
    vtkXMLImageDataReader vtkXMLStructuredGridReader
    vtkXMLRectilinearGridReader
    """
    def CopyOutputInformation(self, vtkInformation, p_int):
        """
        V.CopyOutputInformation(vtkInformation, int)
        C++: void CopyOutputInformation(vtkInformation *outInfo, int port)
             override;
        
        For the specified port, copy the information this reader sets up
        in SetupOutputInformation to outInfo
        """
        ...
    
    def GetNumberOfCells(self):
        """
        V.GetNumberOfCells() -> int
        C++: vtkIdType GetNumberOfCells() override;
        
        Get the number of cells in the output.
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
        
        Get the number of points in the output.
        """
        ...
    
    def GetWholeSlices(self):
        """
        V.GetWholeSlices() -> int
        C++: virtual vtkTypeBool GetWholeSlices()
        
        Get/Set whether the reader gets a whole slice from disk when only
        a rectangle inside it is needed.  This mode reads more data than
        necessary, but prevents many short reads from interacting poorly
        with the compression and encoding schemes.
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
        V.NewInstance() -> vtkXMLStructuredDataReader
        C++: vtkXMLStructuredDataReader *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkXMLStructuredDataReader
        C++: static vtkXMLStructuredDataReader *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetWholeSlices(self, p_int):
        """
        V.SetWholeSlices(int)
        C++: virtual void SetWholeSlices(vtkTypeBool _arg)
        
        Get/Set whether the reader gets a whole slice from disk when only
        a rectangle inside it is needed.  This mode reads more data than
        necessary, but prevents many short reads from interacting poorly
        with the compression and encoding schemes.
        """
        ...
    
    def WholeSlicesOff(self):
        """
        V.WholeSlicesOff()
        C++: virtual void WholeSlicesOff()
        
        Get/Set whether the reader gets a whole slice from disk when only
        a rectangle inside it is needed.  This mode reads more data than
        necessary, but prevents many short reads from interacting poorly
        with the compression and encoding schemes.
        """
        ...
    
    def WholeSlicesOn(self):
        """
        V.WholeSlicesOn()
        C++: virtual void WholeSlicesOn()
        
        Get/Set whether the reader gets a whole slice from disk when only
        a rectangle inside it is needed.  This mode reads more data than
        necessary, but prevents many short reads from interacting poorly
        with the compression and encoding schemes.
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


