"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkInformationExecutivePortVectorKey(__vtkmodules_vtkCommonCore.vtkInformationKey):
    """
    vtkInformationExecutivePortVectorKey - Key for vtkExecutive/Port
    value pair vectors.
    
    Superclass: vtkInformationKey
    
    vtkInformationExecutivePortVectorKey is used to represent keys in
    vtkInformation for values that are vectors of vtkExecutive instances
    paired with port numbers.
    """
    def Append(self, vtkInformation, vtkExecutive, p_int):
        """
        V.Append(vtkInformation, vtkExecutive, int)
        C++: void Append(vtkInformation *info, vtkExecutive *executive,
            int port)
        
        Get/Set the value associated with this key in the given
        information object.
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
    
    def GetPorts(self, vtkInformation):
        """
        V.GetPorts(vtkInformation) -> (int, ...)
        C++: int *GetPorts(vtkInformation *info)
        
        Get/Set the value associated with this key in the given
        information object.
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
    
    def Length(self, vtkInformation):
        """
        V.Length(vtkInformation) -> int
        C++: int Length(vtkInformation *info)
        
        Get/Set the value associated with this key in the given
        information object.
        """
        ...
    
    def MakeKey(self, string, string_1):
        """
        V.MakeKey(string, string) -> vtkInformationExecutivePortVectorKey
        C++: static vtkInformationExecutivePortVectorKey *MakeKey(
            const char *name, const char *location)
        
        This method simply returns a new
        vtkInformationExecutivePortVectorKey, given a name and a
        location. This method is provided for wrappers. Use the
        constructor directly from C++ instead.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkInformationExecutivePortVectorKey
        C++: vtkInformationExecutivePortVectorKey *NewInstance()
        """
        ...
    
    def Remove(self, vtkInformation, vtkExecutive, p_int):
        """
        V.Remove(vtkInformation, vtkExecutive, int)
        C++: void Remove(vtkInformation *info, vtkExecutive *executive,
            int port)
        V.Remove(vtkInformation)
        C++: void Remove(vtkInformation *info) override;
        
        Get/Set the value associated with this key in the given
        information object.
        """
        ...
    
    def Report(self, vtkInformation, vtkGarbageCollector):
        """
        V.Report(vtkInformation, vtkGarbageCollector)
        C++: void Report(vtkInformation *info,
            vtkGarbageCollector *collector) override;
        
        Report a reference this key has in the given information object.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkInformationExecutivePortVectorKey
        C++: static vtkInformationExecutivePortVectorKey *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def ShallowCopy(self, vtkInformation, vtkInformation_1):
        """
        V.ShallowCopy(vtkInformation, vtkInformation)
        C++: void ShallowCopy(vtkInformation *from, vtkInformation *to)
            override;
        
        Copy the entry associated with this key from one information
        object to another.  If there is no entry in the first information
        object for this key, the value is removed from the second.
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

