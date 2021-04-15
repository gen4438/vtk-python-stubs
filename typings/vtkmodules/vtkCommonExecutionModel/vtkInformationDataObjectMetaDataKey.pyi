"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkInformationDataObjectMetaDataKey(__vtkmodules_vtkCommonCore.vtkInformationDataObjectKey):
    """
    vtkInformationDataObjectMetaDataKey - key used to define meta-data of
    type vtkDataObject vtkInformationDataObjectMetaDataKey is a
    vtkInformationDataObjectKey that (shallow) copies itself downstream
    during the REQUEST_INFORMATION pass.
    
    Superclass: vtkInformationDataObjectKey
    
    Hence it can be used to provide meta-data of type vtkDataObject or
    any subclass.
    """
    def CopyDefaultInformation(self, vtkInformation, vtkInformation_1, vtkInformation_2):
        """
        V.CopyDefaultInformation(vtkInformation, vtkInformation,
            vtkInformation)
        C++: void CopyDefaultInformation(vtkInformation *request,
            vtkInformation *fromInfo, vtkInformation *toInfo) override;
        
        Simply shallow copies the key from fromInfo to toInfo if request
        has the REQUEST_INFORMATION() key. This is used by the pipeline
        to propagate this key downstream.
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
        V.MakeKey(string, string) -> vtkInformationDataObjectMetaDataKey
        C++: static vtkInformationDataObjectMetaDataKey *MakeKey(
            const char *name, const char *location)
        
        This method simply returns a new
        vtkInformationDataObjectMetaDataKey, given a name and a location.
        This method is provided for wrappers. Use the constructor
        directly from C++ instead.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkInformationDataObjectMetaDataKey
        C++: vtkInformationDataObjectMetaDataKey *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkInformationDataObjectMetaDataKey
        C++: static vtkInformationDataObjectMetaDataKey *SafeDownCast(
            vtkObjectBase *o)
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


