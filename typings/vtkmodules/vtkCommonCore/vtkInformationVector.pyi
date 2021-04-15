"""
This type stub file was generated by pyright.
"""

from .vtkObject import vtkObject

class vtkInformationVector(vtkObject):
    """
    vtkInformationVector - Store zero or more vtkInformation instances.
    
    Superclass: vtkObject
    
    vtkInformationVector stores a vector of zero or more vtkInformation
    objects corresponding to the input or output information for a
    vtkAlgorithm.  An instance of this class is passed to
    vtkAlgorithm::ProcessRequest calls.
    """
    def Append(self, vtkInformation):
        """
        V.Append(vtkInformation)
        C++: void Append(vtkInformation *info)
        
        Append/Remove an information object.
        """
        ...
    
    def Copy(self, vtkInformationVector, p_int):
        """
        V.Copy(vtkInformationVector, int)
        C++: void Copy(vtkInformationVector *from, int deep=0)
        
        Copy all information entries from the given vtkInformation
        instance.  Any previously existing entries are removed.  If
        deep==1, a deep copy of the information structure is performed
        (new instances of any contained vtkInformation and
        vtkInformationVector objects are created).
        """
        ...
    
    def GetInformationObject(self, p_int):
        """
        V.GetInformationObject(int) -> vtkInformation
        C++: vtkInformation *GetInformationObject(int index)
        
        Get/Set the vtkInformation instance stored at the given index in
        the vector.  The vector will automatically expand to include the
        index given if necessary.  Missing entries in-between will be
        filled with empty vtkInformation instances.
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
    
    def GetNumberOfInformationObjects(self):
        """
        V.GetNumberOfInformationObjects() -> int
        C++: int GetNumberOfInformationObjects()
        
        Get/Set the number of information objects in the vector.  Setting
        the number to larger than the current number will create empty
        vtkInformation instances.  Setting the number to smaller than the
        current number will remove entries from higher indices.
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
        V.NewInstance() -> vtkInformationVector
        C++: vtkInformationVector *NewInstance()
        """
        ...
    
    def Remove(self, vtkInformation):
        """
        V.Remove(vtkInformation)
        C++: void Remove(vtkInformation *info)
        V.Remove(int)
        C++: void Remove(int idx)
        
        Append/Remove an information object.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkInformationVector
        C++: static vtkInformationVector *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetInformationObject(self, p_int, vtkInformation):
        """
        V.SetInformationObject(int, vtkInformation)
        C++: void SetInformationObject(int index, vtkInformation *info)
        
        Get/Set the vtkInformation instance stored at the given index in
        the vector.  The vector will automatically expand to include the
        index given if necessary.  Missing entries in-between will be
        filled with empty vtkInformation instances.
        """
        ...
    
    def SetNumberOfInformationObjects(self, p_int):
        """
        V.SetNumberOfInformationObjects(int)
        C++: void SetNumberOfInformationObjects(int n)
        
        Get/Set the number of information objects in the vector.  Setting
        the number to larger than the current number will create empty
        vtkInformation instances.  Setting the number to smaller than the
        current number will remove entries from higher indices.
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


