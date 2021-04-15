"""
This type stub file was generated by pyright.
"""

from .vtkObject import vtkObject

class vtkByteSwap(vtkObject):
    """
    vtkByteSwap - perform machine dependent byte swapping
    
    Superclass: vtkObject
    
    vtkByteSwap is used by other classes to perform machine dependent
    byte swapping. Byte swapping is often used when reading or writing
    binary files.
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
        V.NewInstance() -> vtkByteSwap
        C++: vtkByteSwap *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkByteSwap
        C++: static vtkByteSwap *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def Swap2BE(self, void):
        """
        V.Swap2BE(void)
        C++: static void Swap2BE(void *p)
        
        Swap 2, 4, or 8 bytes for storage as Big Endian.
        """
        ...
    
    def Swap2BERange(self, void, p_int):
        """
        V.Swap2BERange(void, int)
        C++: static void Swap2BERange(void *p, size_t num)
        
        Swap a block of 2-, 4-, or 8-byte segments for storage as Big
        Endian.
        """
        ...
    
    def Swap2LE(self, void):
        """
        V.Swap2LE(void)
        C++: static void Swap2LE(void *p)
        
        Swap 2, 4, or 8 bytes for storage as Little Endian.
        """
        ...
    
    def Swap2LERange(self, void, p_int):
        """
        V.Swap2LERange(void, int)
        C++: static void Swap2LERange(void *p, size_t num)
        
        Swap a block of 2-, 4-, or 8-byte segments for storage as Little
        Endian.
        """
        ...
    
    def Swap4BE(self, void):
        """
        V.Swap4BE(void)
        C++: static void Swap4BE(void *p)
        
        Swap 2, 4, or 8 bytes for storage as Big Endian.
        """
        ...
    
    def Swap4BERange(self, void, p_int):
        """
        V.Swap4BERange(void, int)
        C++: static void Swap4BERange(void *p, size_t num)
        
        Swap a block of 2-, 4-, or 8-byte segments for storage as Big
        Endian.
        """
        ...
    
    def Swap4LE(self, void):
        """
        V.Swap4LE(void)
        C++: static void Swap4LE(void *p)
        
        Swap 2, 4, or 8 bytes for storage as Little Endian.
        """
        ...
    
    def Swap4LERange(self, void, p_int):
        """
        V.Swap4LERange(void, int)
        C++: static void Swap4LERange(void *p, size_t num)
        
        Swap a block of 2-, 4-, or 8-byte segments for storage as Little
        Endian.
        """
        ...
    
    def Swap8BE(self, void):
        """
        V.Swap8BE(void)
        C++: static void Swap8BE(void *p)
        
        Swap 2, 4, or 8 bytes for storage as Big Endian.
        """
        ...
    
    def Swap8BERange(self, void, p_int):
        """
        V.Swap8BERange(void, int)
        C++: static void Swap8BERange(void *p, size_t num)
        
        Swap a block of 2-, 4-, or 8-byte segments for storage as Big
        Endian.
        """
        ...
    
    def Swap8LE(self, void):
        """
        V.Swap8LE(void)
        C++: static void Swap8LE(void *p)
        
        Swap 2, 4, or 8 bytes for storage as Little Endian.
        """
        ...
    
    def Swap8LERange(self, void, p_int):
        """
        V.Swap8LERange(void, int)
        C++: static void Swap8LERange(void *p, size_t num)
        
        Swap a block of 2-, 4-, or 8-byte segments for storage as Little
        Endian.
        """
        ...
    
    def SwapBE(self, *float):
        """
        V.SwapBE([float, ...])
        C++: static void SwapBE(double *p)
        V.SwapBE(string)
        C++: static void SwapBE(char *p)
        V.SwapBE([int, ...])
        C++: static void SwapBE(int *p)
        V.SwapBE([int, ...])
        C++: static void SwapBE(long *p)
        V.SwapBE([int, ...])
        C++: static void SwapBE(long long *p)
        
        Type-safe swap signatures to swap for storage in either Little
        Endian or Big Endian format.  Swapping is performed according to
        the true size of the type given.
        """
        ...
    
    def SwapBERange(self, *float, **kwargs):
        """
        V.SwapBERange([float, ...], int)
        C++: static void SwapBERange(double *p, size_t num)
        V.SwapBERange(string, int)
        C++: static void SwapBERange(char *p, size_t num)
        V.SwapBERange([int, ...], int)
        C++: static void SwapBERange(int *p, size_t num)
        V.SwapBERange([int, ...], int)
        C++: static void SwapBERange(long *p, size_t num)
        V.SwapBERange([int, ...], int)
        C++: static void SwapBERange(long long *p, size_t num)
        
        Type-safe swap signatures to swap for storage in either Little
        Endian or Big Endian format.  Swapping is performed according to
        the true size of the type given.
        """
        ...
    
    def SwapLE(self, *float):
        """
        V.SwapLE([float, ...])
        C++: static void SwapLE(double *p)
        V.SwapLE(string)
        C++: static void SwapLE(char *p)
        V.SwapLE([int, ...])
        C++: static void SwapLE(int *p)
        V.SwapLE([int, ...])
        C++: static void SwapLE(long *p)
        V.SwapLE([int, ...])
        C++: static void SwapLE(long long *p)
        
        Type-safe swap signatures to swap for storage in either Little
        Endian or Big Endian format.  Swapping is performed according to
        the true size of the type given.
        """
        ...
    
    def SwapLERange(self, *float, **kwargs):
        """
        V.SwapLERange([float, ...], int)
        C++: static void SwapLERange(double *p, size_t num)
        V.SwapLERange(string, int)
        C++: static void SwapLERange(char *p, size_t num)
        V.SwapLERange([int, ...], int)
        C++: static void SwapLERange(int *p, size_t num)
        V.SwapLERange([int, ...], int)
        C++: static void SwapLERange(long *p, size_t num)
        V.SwapLERange([int, ...], int)
        C++: static void SwapLERange(long long *p, size_t num)
        
        Type-safe swap signatures to swap for storage in either Little
        Endian or Big Endian format.  Swapping is performed according to
        the true size of the type given.
        """
        ...
    
    def SwapVoidRange(self, void, p_int, p_int_1):
        """
        V.SwapVoidRange(void, int, int)
        C++: static void SwapVoidRange(void *buffer, size_t numWords,
            size_t wordSize)
        
        Swaps the bytes of a buffer.  Uses an arbitrary word size, but
        assumes the word size is divisible by two.
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


