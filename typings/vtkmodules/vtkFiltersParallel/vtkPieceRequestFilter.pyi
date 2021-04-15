"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkPieceRequestFilter(__vtkmodules_vtkCommonExecutionModel.vtkAlgorithm):
    """
    vtkPieceRequestFilter - Sets the piece request for upstream filters.
    
    Superclass: vtkAlgorithm
    
    Sends the piece and number of pieces to upstream filters; passes the
    input to the output unmodified.
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
        
        The total number of pieces.
        """
        ...
    
    def GetNumberOfPiecesMaxValue(self):
        """
        V.GetNumberOfPiecesMaxValue() -> int
        C++: virtual int GetNumberOfPiecesMaxValue()
        
        The total number of pieces.
        """
        ...
    
    def GetNumberOfPiecesMinValue(self):
        """
        V.GetNumberOfPiecesMinValue() -> int
        C++: virtual int GetNumberOfPiecesMinValue()
        
        The total number of pieces.
        """
        ...
    
    def GetOutput(self):
        """
        V.GetOutput() -> vtkDataObject
        C++: vtkDataObject *GetOutput()
        V.GetOutput(int) -> vtkDataObject
        C++: vtkDataObject *GetOutput(int)
        
        Get the output data object for a port on this algorithm.
        """
        ...
    
    def GetPiece(self):
        """
        V.GetPiece() -> int
        C++: virtual int GetPiece()
        
        The piece to extract.
        """
        ...
    
    def GetPieceMaxValue(self):
        """
        V.GetPieceMaxValue() -> int
        C++: virtual int GetPieceMaxValue()
        
        The piece to extract.
        """
        ...
    
    def GetPieceMinValue(self):
        """
        V.GetPieceMinValue() -> int
        C++: virtual int GetPieceMinValue()
        
        The piece to extract.
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
        V.NewInstance() -> vtkPieceRequestFilter
        C++: vtkPieceRequestFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPieceRequestFilter
        C++: static vtkPieceRequestFilter *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetInputData(self, vtkDataObject):
        """
        V.SetInputData(vtkDataObject)
        C++: void SetInputData(vtkDataObject *)
        V.SetInputData(int, vtkDataObject)
        C++: void SetInputData(int, vtkDataObject *)
        
        Set an input of this algorithm.
        """
        ...
    
    def SetNumberOfPieces(self, p_int):
        """
        V.SetNumberOfPieces(int)
        C++: virtual void SetNumberOfPieces(int _arg)
        
        The total number of pieces.
        """
        ...
    
    def SetPiece(self, p_int):
        """
        V.SetPiece(int)
        C++: virtual void SetPiece(int _arg)
        
        The piece to extract.
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

