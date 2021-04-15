"""
This type stub file was generated by pyright.
"""

from .vtkXMLWriter import vtkXMLWriter

class vtkXMLTableWriter(vtkXMLWriter):
    """
    vtkXMLTableWriter - Write VTK XML Table files.
    
    Superclass: vtkXMLWriter
    
    vtkXMLTableWriter provides a functionality for writing vtTable as XML
    .vtt files.
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
    
    def GetNumberOfPieces(self):
        """
        V.GetNumberOfPieces() -> int
        C++: virtual int GetNumberOfPieces()
        
        Get/Set the number of pieces used to stream the table through the
        pipeline while writing to the file.
        """
        ...
    
    def GetWritePiece(self):
        """
        V.GetWritePiece() -> int
        C++: virtual int GetWritePiece()
        
        Get/Set the piece to write to the file.  If this is negative or
        equal to the NumberOfPieces, all pieces will be written.
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
        V.NewInstance() -> vtkXMLTableWriter
        C++: vtkXMLTableWriter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkXMLTableWriter
        C++: static vtkXMLTableWriter *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetNumberOfPieces(self, p_int):
        """
        V.SetNumberOfPieces(int)
        C++: virtual void SetNumberOfPieces(int _arg)
        
        Get/Set the number of pieces used to stream the table through the
        pipeline while writing to the file.
        """
        ...
    
    def SetWritePiece(self, p_int):
        """
        V.SetWritePiece(int)
        C++: virtual void SetWritePiece(int _arg)
        
        Get/Set the piece to write to the file.  If this is negative or
        equal to the NumberOfPieces, all pieces will be written.
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

