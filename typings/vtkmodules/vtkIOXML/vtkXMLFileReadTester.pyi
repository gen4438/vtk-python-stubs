"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkIOXMLParser as __vtkmodules_vtkIOXMLParser

class vtkXMLFileReadTester(__vtkmodules_vtkIOXMLParser.vtkXMLParser):
    """
    vtkXMLFileReadTester - Utility class for vtkXMLReader and subclasses.
    
    Superclass: vtkXMLParser
    
    vtkXMLFileReadTester reads the smallest part of a file necessary to
    determine whether it is a VTK XML file.  If so, it extracts the file
    type and version number.
    """
    def GetFileDataType(self):
        """
        V.GetFileDataType() -> string
        C++: virtual char *GetFileDataType()
        
        Get the data type of the XML file tested.  If the file could not
        be read, returns nullptr.
        """
        ...
    
    def GetFileVersion(self):
        """
        V.GetFileVersion() -> string
        C++: virtual char *GetFileVersion()
        
        Get the file version of the XML file tested.  If the file could
        not be read, returns nullptr.
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
        V.NewInstance() -> vtkXMLFileReadTester
        C++: vtkXMLFileReadTester *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkXMLFileReadTester
        C++: static vtkXMLFileReadTester *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def TestReadFile(self):
        """
        V.TestReadFile() -> int
        C++: int TestReadFile()
        
        Try to read the file given by FileName.  Returns 1 if the file is
        a VTK XML file, and 0 otherwise.
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


