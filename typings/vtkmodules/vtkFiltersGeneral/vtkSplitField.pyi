"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkSplitField(__vtkmodules_vtkCommonExecutionModel.vtkDataSetAlgorithm):
    """
    vtkSplitField - Split a field into single component fields
    
    Superclass: vtkDataSetAlgorithm
    
    vtkSplitField is used to split a multi-component field (vtkDataArray)
    into multiple single component fields. The new fields are put in the
    same field data as the original field. The output arrays are of the
    same type as the input array. Example:
     sf->SetInputField("gradient", vtkSplitField::POINT_DATA);
     sf->Split(0, "firstcomponent");
      tells vtkSplitField to extract the first component of the field
    called gradient and create an array called firstcomponent (the new
    field will be in the output's point data). Note that, by default, the
    original array is also passed through.
    
    @warning
    When using Java, Python or Visual Basic bindings, the array name can
    not be one of the  AttributeTypes when calling Split() which takes
    strings as arguments. The wrapped command will always assume the
    string corresponds to an attribute type when the argument is one of
    the AttributeTypes. In this situation, use the Split() which takes
    enums.
    
    @sa
    vtkFieldData vtkDataSet vtkDataObjectToDataSetFilter
    vtkDataSetAttributes vtkDataArray vtkRearrangeFields
    vtkAssignAttribute vtkMergeFields
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
        V.NewInstance() -> vtkSplitField
        C++: vtkSplitField *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSplitField
        C++: static vtkSplitField *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetInputField(self, p_int, p_int_1):
        """
        V.SetInputField(int, int)
        C++: void SetInputField(int attributeType, int fieldLoc)
        V.SetInputField(string, int)
        C++: void SetInputField(const char *name, int fieldLoc)
        V.SetInputField(string, string)
        C++: void SetInputField(const char *name, const char *fieldLoc)
        
        Use the given attribute in the field data given by fieldLoc as
        input.
        """
        ...
    
    def Split(self, p_int, string):
        """
        V.Split(int, string)
        C++: void Split(int component, const char *arrayName)
        
        Create a new array with the given component.
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
    CELL_DATA = ...
    DATA_OBJECT = ...
    FieldLocations = ...
    POINT_DATA = ...
    __dict__ = ...
    __vtkname__ = ...


