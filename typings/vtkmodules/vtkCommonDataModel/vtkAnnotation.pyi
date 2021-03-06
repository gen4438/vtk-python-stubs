"""
This type stub file was generated by pyright.
"""

from .vtkDataObject import vtkDataObject

class vtkAnnotation(vtkDataObject):
    """
    vtkAnnotation - Stores a collection of annotation artifacts.
    
    Superclass: vtkDataObject
    
    vtkAnnotation is a collection of annotation properties along with an
    associated selection indicating the portion of data the annotation
    refers to.
    
    @par Thanks: Timothy M. Shead (tshead@sandia.gov) at Sandia National
    Laboratories contributed code to this class.
    """
    def COLOR(self):
        """
        V.COLOR() -> vtkInformationDoubleVectorKey
        C++: static vtkInformationDoubleVectorKey *COLOR()
        
        The color for this annotation. This is stored as an RGB triple
        with values between 0 and 1.
        """
        ...
    
    def DATA(self):
        """
        V.DATA() -> vtkInformationDataObjectKey
        C++: static vtkInformationDataObjectKey *DATA()
        
        Associate a vtkDataObject with this annotation
        """
        ...
    
    def DeepCopy(self, vtkDataObject):
        """
        V.DeepCopy(vtkDataObject)
        C++: void DeepCopy(vtkDataObject *other) override;
        
        Make this annotation have the same properties and have a copy of
        the selection of another annotation.
        """
        ...
    
    def ENABLE(self):
        """
        V.ENABLE() -> vtkInformationIntegerKey
        C++: static vtkInformationIntegerKey *ENABLE()
        
        Whether or not this annotation is enabled. A value of 1 means
        enabled, 0 disabled.
        """
        ...
    
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkAnnotation
        C++: static vtkAnnotation *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkAnnotation
        C++: static vtkAnnotation *GetData(vtkInformationVector *v,
            int i=0)
        
        Retrieve a vtkAnnotation stored inside an information object.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Get the modified time of this object.
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
    
    def GetSelection(self):
        """
        V.GetSelection() -> vtkSelection
        C++: virtual vtkSelection *GetSelection()
        
        The selection to which this set of annotations will apply.
        """
        ...
    
    def HIDE(self):
        """
        V.HIDE() -> vtkInformationIntegerKey
        C++: static vtkInformationIntegerKey *HIDE()
        
        Whether or not this annotation is visible.
        """
        ...
    
    def ICON_INDEX(self):
        """
        V.ICON_INDEX() -> vtkInformationIntegerKey
        C++: static vtkInformationIntegerKey *ICON_INDEX()
        
        An icon index for this annotation.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        Initialize the annotation to an empty state.
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
    
    def LABEL(self):
        """
        V.LABEL() -> vtkInformationStringKey
        C++: static vtkInformationStringKey *LABEL()
        
        The label for this annotation.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkAnnotation
        C++: vtkAnnotation *NewInstance()
        """
        ...
    
    def OPACITY(self):
        """
        V.OPACITY() -> vtkInformationDoubleKey
        C++: static vtkInformationDoubleKey *OPACITY()
        
        The color for this annotation. This is stored as a value between
        0 and 1.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAnnotation
        C++: static vtkAnnotation *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetSelection(self, vtkSelection):
        """
        V.SetSelection(vtkSelection)
        C++: virtual void SetSelection(vtkSelection *selection)
        
        The selection to which this set of annotations will apply.
        """
        ...
    
    def ShallowCopy(self, vtkDataObject):
        """
        V.ShallowCopy(vtkDataObject)
        C++: void ShallowCopy(vtkDataObject *other) override;
        
        Make this annotation have the same properties and have the same
        selection of another annotation.
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


