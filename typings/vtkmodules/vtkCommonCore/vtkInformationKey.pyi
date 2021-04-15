"""
This type stub file was generated by pyright.
"""

from .vtkObjectBase import vtkObjectBase

class vtkInformationKey(vtkObjectBase):
    """
    vtkInformationKey - Superclass for vtkInformation keys.
    
    Superclass: vtkObjectBase
    
    vtkInformationKey is the superclass for all keys used to access the
    map represented by vtkInformation.  The vtkInformation::Set and
    vtkInformation::Get methods of vtkInformation are accessed by
    information keys.  A key is a pointer to an instance of a subclass of
    vtkInformationKey.  The type of the subclass determines the overload
    of Set/Get that is selected.  This ensures that the type of value
    stored in a vtkInformation instance corresponding to a given key
    matches the type expected for that key.
    """
    def CopyDefaultInformation(self, vtkInformation, vtkInformation_1, vtkInformation_2):
        """
        V.CopyDefaultInformation(vtkInformation, vtkInformation,
            vtkInformation)
        C++: virtual void CopyDefaultInformation(vtkInformation *request,
            vtkInformation *fromInfo, vtkInformation *toInfo)
        
        This function is only relevant when the pertaining key is used in
        a VTK pipeline. By overwriting this method, a key can decide
        if/how to copy itself downstream or upstream during a particular
        pipeline pass. For example, meta-data keys can copy themselves
        during REQUEST_INFORMATION whereas request keys can copy
        themselves during REQUEST_UPDATE_EXTENT.
        """
        ...
    
    def DeepCopy(self, vtkInformation, vtkInformation_1):
        """
        V.DeepCopy(vtkInformation, vtkInformation)
        C++: virtual void DeepCopy(vtkInformation *from,
            vtkInformation *to)
        
        Duplicate (new instance created) the entry associated with this
        key from one information object to another (new instances of any
        contained vtkInformation and vtkInformationVector objects are
        created). Default implementation simply calls ShallowCopy().
        """
        ...
    
    def GetLocation(self):
        """
        V.GetLocation() -> string
        C++: const char *GetLocation()
        
        Get the location of the key.  This is the name of the class in
        which the key is defined.
        """
        ...
    
    def GetName(self):
        """
        V.GetName() -> string
        C++: const char *GetName()
        
        Get the name of the key.  This is not the type of the key, but
        the name of the key instance.
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
    
    def Has(self, vtkInformation):
        """
        V.Has(vtkInformation) -> int
        C++: virtual int Has(vtkInformation *info)
        
        Check whether this key appears in the given information object.
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
    
    def NeedToExecute(self, vtkInformation, vtkInformation_1):
        """
        V.NeedToExecute(vtkInformation, vtkInformation) -> bool
        C++: virtual bool NeedToExecute(vtkInformation *pipelineInfo,
            vtkInformation *dobjInfo)
        
        This function is only relevant when the pertaining key is used in
        a VTK pipeline. Specific keys that handle pipeline data requests
        (for example, UPDATE_PIECE_NUMBER) can overwrite this method to
        notify the pipeline that a a filter should be (re-)executed
        because what is in the current output is different that what is
        being requested by the key. For example, DATA_PIECE_NUMBER !=
        UPDATE_PIECE_NUMBER.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkInformationKey
        C++: vtkInformationKey *NewInstance()
        """
        ...
    
    def Print(self, vtkInformation):
        """
        V.Print(vtkInformation)
        C++: void Print(vtkInformation *info)
        
        Print the key's value in an information object to a stream.
        """
        ...
    
    def Remove(self, vtkInformation):
        """
        V.Remove(vtkInformation)
        C++: virtual void Remove(vtkInformation *info)
        
        Remove this key from the given information object.
        """
        ...
    
    def Report(self, vtkInformation, vtkGarbageCollector):
        """
        V.Report(vtkInformation, vtkGarbageCollector)
        C++: virtual void Report(vtkInformation *info,
            vtkGarbageCollector *collector)
        
        Report a reference this key has in the given information object.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkInformationKey
        C++: static vtkInformationKey *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def ShallowCopy(self, vtkInformation, vtkInformation_1):
        """
        V.ShallowCopy(vtkInformation, vtkInformation)
        C++: virtual void ShallowCopy(vtkInformation *from,
            vtkInformation *to)
        
        Copy the entry associated with this key from one information
        object to another.  If there is no entry in the first information
        object for this key, the value is removed from the second.
        """
        ...
    
    def StoreMetaData(self, vtkInformation, vtkInformation_1, vtkInformation_2):
        """
        V.StoreMetaData(vtkInformation, vtkInformation, vtkInformation)
        C++: virtual void StoreMetaData(vtkInformation *request,
            vtkInformation *pipelineInfo, vtkInformation *dobjInfo)
        
        This function is only relevant when the pertaining key is used in
        a VTK pipeline. Specific keys that handle pipeline data requests
        (for example, UPDATE_PIECE_NUMBER) can overwrite this method to
        store in the data information meta-data about the request that
        led to the current filter execution. This meta-data can later be
        used to compare what is being requested to decide whether the
        filter needs to re-execute. For example, a filter may store the
        current UPDATE_PIECE_NUMBER in the data object's information as
        the DATA_PIECE_NUMBER. DATA_PIECE_NUMBER can later be compared to
        a new UPDATA_PIECE_NUMBER to decide whether a filter should
        re-execute.
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

