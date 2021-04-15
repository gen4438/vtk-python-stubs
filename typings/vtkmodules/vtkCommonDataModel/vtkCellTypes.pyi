"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkCellTypes(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkCellTypes - object provides direct access to cells in vtkCellArray
    and type information
    
    Superclass: vtkObject
    
    This class is a supplemental object to vtkCellArray to allow random
    access into cells as well as representing cell type information.  The
    "location" field is the location in the vtkCellArray list in terms of
    an integer offset.  An integer offset was used instead of a pointer
    for easy storage and inter-process communication. The type
    information is defined in the file vtkCellType.h.
    
    @warning
    Sometimes this class is used to pass type information independent of
    the random access (i.e., location) information. For example, see
    vtkDataSet::GetCellTypes(). If you use the class in this way, you can
    use a location value of -1.
    
    @sa
    vtkCellArray vtkCellLinks
    """
    def Allocate(self, p_int, p_int_1):
        """
        V.Allocate(int, int) -> int
        C++: int Allocate(vtkIdType sz=512, vtkIdType ext=1000)
        
        Allocate memory for this array. Delete old storage only if
        necessary.
        """
        ...
    
    def DeepCopy(self, vtkCellTypes):
        """
        V.DeepCopy(vtkCellTypes)
        C++: void DeepCopy(vtkCellTypes *src)
        
        Standard DeepCopy method.  Since this object contains no
        reference to other objects, there is no ShallowCopy.
        """
        ...
    
    def DeleteCell(self, p_int):
        """
        V.DeleteCell(int)
        C++: void DeleteCell(vtkIdType cellId)
        
        Delete cell by setting to nullptr cell type.
        """
        ...
    
    def GetActualMemorySize(self):
        """
        V.GetActualMemorySize() -> int
        C++: unsigned long GetActualMemorySize()
        
        Return the memory in kibibytes (1024 bytes) consumed by this cell
        type array. Used to support streaming and reading/writing data.
        The value returned is guaranteed to be greater than or equal to
        the memory required to actually represent the data represented by
        this object. The information returned is valid only after the
        pipeline has been updated.
        """
        ...
    
    def GetCellLocation(self, p_int):
        """
        V.GetCellLocation(int) -> int
        C++: vtkIdType GetCellLocation(vtkIdType cellId)
        
        Return the location of the cell in the associated vtkCellArray.
        """
        ...
    
    def GetCellLocationsArray(self):
        """
        V.GetCellLocationsArray() -> vtkIdTypeArray
        C++: vtkIdTypeArray *GetCellLocationsArray()
        
        Methods for obtaining the arrays representing types and
        locations.
        """
        ...
    
    def GetCellType(self, p_int):
        """
        V.GetCellType(int) -> int
        C++: unsigned char GetCellType(vtkIdType cellId)
        
        Return the type of cell.
        """
        ...
    
    def GetCellTypesArray(self):
        """
        V.GetCellTypesArray() -> vtkUnsignedCharArray
        C++: vtkUnsignedCharArray *GetCellTypesArray()
        
        Methods for obtaining the arrays representing types and
        locations.
        """
        ...
    
    def GetClassNameFromTypeId(self, p_int):
        """
        V.GetClassNameFromTypeId(int) -> string
        C++: static const char *GetClassNameFromTypeId(int typeId)
        
        Given an int (as defined in vtkCellType.h) identifier for a class
        return it's classname.
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
    
    def GetNumberOfTypes(self):
        """
        V.GetNumberOfTypes() -> int
        C++: vtkIdType GetNumberOfTypes()
        
        Return the number of types in the list.
        """
        ...
    
    def GetTypeIdFromClassName(self, string):
        """
        V.GetTypeIdFromClassName(string) -> int
        C++: static int GetTypeIdFromClassName(const char *classname)
        
        Given a data object classname, return it's int identified (as
        defined in vtkCellType.h)
        """
        ...
    
    def InsertCell(self, p_int, p_int_1, p_int_2):
        """
        V.InsertCell(int, int, int)
        C++: void InsertCell(vtkIdType id, unsigned char type,
            vtkIdType loc)
        
        Add a cell at specified id.
        """
        ...
    
    def InsertNextCell(self, p_int, p_int_1):
        """
        V.InsertNextCell(int, int) -> int
        C++: vtkIdType InsertNextCell(unsigned char type, vtkIdType loc)
        
        Add a cell to the object in the next available slot.
        """
        ...
    
    def InsertNextType(self, p_int):
        """
        V.InsertNextType(int) -> int
        C++: vtkIdType InsertNextType(unsigned char type)
        
        Add the type specified to the end of the list. Range checking is
        performed.
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
    
    def IsLinear(self, p_int):
        """
        V.IsLinear(int) -> int
        C++: static int IsLinear(unsigned char type)
        
        This convenience method is a fast check to determine if a cell
        type represents a linear or nonlinear cell.  This is generally
        much more efficient than getting the appropriate vtkCell and
        checking its IsLinear method.
        """
        ...
    
    def IsType(self, p_int):
        """
        V.IsType(int) -> int
        C++: int IsType(unsigned char type)
        
        Return 1 if type specified is contained in list; 0 otherwise.
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
        V.NewInstance() -> vtkCellTypes
        C++: vtkCellTypes *NewInstance()
        """
        ...
    
    def Reset(self):
        """
        V.Reset()
        C++: void Reset()
        
        Initialize object without releasing memory.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCellTypes
        C++: static vtkCellTypes *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCellTypes(self, p_int, vtkUnsignedCharArray, vtkIdTypeArray):
        """
        V.SetCellTypes(int, vtkUnsignedCharArray, vtkIdTypeArray)
        C++: void SetCellTypes(vtkIdType ncells,
            vtkUnsignedCharArray *cellTypes,
            vtkIdTypeArray *cellLocations)
        V.SetCellTypes(int, vtkUnsignedCharArray, vtkIntArray)
        C++: void SetCellTypes(vtkIdType ncells,
            vtkUnsignedCharArray *cellTypes, vtkIntArray *cellLocations)
        
        Specify a group of cell types.
        """
        ...
    
    def Squeeze(self):
        """
        V.Squeeze()
        C++: void Squeeze()
        
        Reclaim any extra memory.
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


