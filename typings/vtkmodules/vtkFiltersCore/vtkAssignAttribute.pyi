"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkAssignAttribute(__vtkmodules_vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    """
    vtkAssignAttribute - Labels/marks a field as an attribute
    
    Superclass: vtkPassInputTypeAlgorithm
    
    vtkAssignAttribute is used to label/mark a field (vtkDataArray) as an
    attribute. A field name or an attribute to labeled can be specified.
    For example:
     aa->Assign("foo", vtkDataSetAttributes::SCALARS,
                vtkAssignAttribute::POINT_DATA);
      tells vtkAssignAttribute to make the array in the point data called
    "foo" the active scalars. On the other hand,
     aa->Assign(vtkDataSetAttributes::VECTORS, vtkDataSetAttributes::SCALARS,
                vtkAssignAttribute::POINT_DATA);
      tells vtkAssignAttribute to make the active vectors also the active
    scalars.
    
    @warning
    When using Java, Python or Visual Basic bindings, the array name can
    not be one of the  AttributeTypes when calling Assign() which takes
    strings as arguments. The wrapped command will always assume the
    string corresponds to an attribute type when the argument is one of
    the AttributeTypes. In this situation, use the Assign() which takes
    enums.
    
    @sa
    vtkFieldData vtkDataSet vtkDataObjectToDataSetFilter
    vtkDataSetAttributes vtkDataArray vtkRearrangeFields vtkSplitField
    vtkMergeFields
    """
    def Assign(self, p_int, p_int_1, p_int_2):
        """
        V.Assign(int, int, int)
        C++: void Assign(int inputAttributeType, int attributeType,
            int attributeLoc)
        V.Assign(string, int, int)
        C++: void Assign(const char *fieldName, int attributeType,
            int attributeLoc)
        V.Assign(string, string, string)
        C++: void Assign(const char *name, const char *attributeType,
            const char *attributeLoc)
        
        Label an attribute as another attribute.
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
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkAssignAttribute
        C++: vtkAssignAttribute *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAssignAttribute
        C++: static vtkAssignAttribute *SafeDownCast(vtkObjectBase *o)
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
    AttributeLocation = ...
    CELL_DATA = ...
    EDGE_DATA = ...
    NUM_ATTRIBUTE_LOCS = ...
    POINT_DATA = ...
    VERTEX_DATA = ...
    __dict__ = ...
    __vtkname__ = ...


