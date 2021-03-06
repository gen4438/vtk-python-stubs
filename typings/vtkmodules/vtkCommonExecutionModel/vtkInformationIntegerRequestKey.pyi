"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkInformationIntegerRequestKey(__vtkmodules_vtkCommonCore.vtkInformationIntegerKey):
    """
    vtkInformationIntegerRequestKey - key that can used to request
    integer values from the pipeline vtkInformationIntegerRequestKey is a
    vtkInformationIntegerKey that can used to request integer values from
    upstream.
    
    Superclass: vtkInformationIntegerKey
    
    A good example of this is UPDATE_NUMBER_OF_PIECES where downstream
    can request that upstream provides data partitioned into a certain
    number of pieces. There are several components that make this work.
    First, the key will copy itself upstream during
    REQUEST_UPDATE_EXTENT. Second, after a successful execution, it will
    stor its value into a data object's information using a specific key
    defined by its data member DataKey. Third, before execution, it will
    check if the requested value matched the value in the data object's
    information. If not, it will ask the pipeline to execute.
    
    The best way to use this class is to subclass it to set the DataKey
    data member. This is usually done in the subclass' constructor.
    """
    def CopyDefaultInformation(self, vtkInformation, vtkInformation_1, vtkInformation_2):
        """
        V.CopyDefaultInformation(vtkInformation, vtkInformation,
            vtkInformation)
        C++: void CopyDefaultInformation(vtkInformation *request,
            vtkInformation *fromInfo, vtkInformation *toInfo) override;
        
        Copies the value stored in fromInfo using this key into toInfo if
        request has the REQUEST_UPDATE_EXTENT key.
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
    
    def MakeKey(self, string, string_1):
        """
        V.MakeKey(string, string) -> vtkInformationIntegerRequestKey
        C++: static vtkInformationIntegerRequestKey *MakeKey(
            const char *name, const char *location)
        
        This method simply returns a new vtkInformationIntegerRequestKey,
        given a name and a location. This method is provided for
        wrappers. Use the constructor directly from C++ instead.
        """
        ...
    
    def NeedToExecute(self, vtkInformation, vtkInformation_1):
        """
        V.NeedToExecute(vtkInformation, vtkInformation) -> bool
        C++: bool NeedToExecute(vtkInformation *pipelineInfo,
            vtkInformation *dobjInfo) override;
        
        Returns true if a value of type DataKey does not exist in
        dobjInfo or if it is different that the value stored in
        pipelineInfo using this key.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkInformationIntegerRequestKey
        C++: vtkInformationIntegerRequestKey *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkInformationIntegerRequestKey
        C++: static vtkInformationIntegerRequestKey *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def StoreMetaData(self, vtkInformation, vtkInformation_1, vtkInformation_2):
        """
        V.StoreMetaData(vtkInformation, vtkInformation, vtkInformation)
        C++: void StoreMetaData(vtkInformation *request,
            vtkInformation *pipelineInfo, vtkInformation *dobjInfo)
            override;
        
        Copies the value stored in pipelineInfo using this key into
        dobjInfo.
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


