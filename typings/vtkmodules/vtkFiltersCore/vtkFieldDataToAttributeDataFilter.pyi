"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkFieldDataToAttributeDataFilter(__vtkmodules_vtkCommonExecutionModel.vtkDataSetAlgorithm):
    """
    vtkFieldDataToAttributeDataFilter - map field data to dataset
    attribute data
    
    Superclass: vtkDataSetAlgorithm
    
    vtkFieldDataToAttributeDataFilter is a class that maps field data
    into dataset attributes. The input to this filter is any type of
    dataset and the output is the same dataset (geometry/topology) with
    new attribute data (attribute data is passed through if not replaced
    during filter execution).
    
    To use this filter you must specify which field data from the input
    dataset to use. There are three possibilities: the cell field data,
    the point field data, or the field data associated with the data
    object superclass. Then you specify which attribute data to create:
    either cell attribute data or point attribute data.  Finally, you
    must define how to construct the various attribute data types (e.g.,
    scalars, vectors, normals, etc.) from the arrays and the components
    of the arrays from the field data. This is done by associating
    components in the input field with components making up the attribute
    data. For example, you would specify a scalar with three components
    (RGB) by assigning components from the field for the R, then G, then
    B values of the scalars.  You may also have to specify component
    ranges (for each R-G-B) to make sure that the number of R, G, and B
    values is the same. Also, you may want to normalize the components
    which helps distribute the data uniformly.
    
    This filter is often used in conjunction with
    vtkDataObjectToDataSetFilter.  vtkDataObjectToDataSetFilter filter
    generates dataset topology and geometry and passes its input field
    data along to its output. Then this filter is used to generate the
    attribute data to go along with the dataset.
    
    @warning
    Make sure that the data you extract is consistent. That is, if you
    have N points, extract N point attributes (scalars, vectors, etc.).
    
    @sa
    vtkFieldData vtkDataSet vtkDataObjectToDataSetFilter
    vtkDataSetAttributes vtkDataArray
    """
    def ConstructArray(self, vtkDataArray, p_int, vtkDataArray_1, p_int_1, p_int_2, p_int_3, p_int_4):
        """
        V.ConstructArray(vtkDataArray, int, vtkDataArray, int, int, int,
            int) -> int
        C++: static int ConstructArray(vtkDataArray *da, int comp,
            vtkDataArray *frray, int fieldComp, vtkIdType min,
            vtkIdType max, int normalize)
        
        Construct a portion of a data array (the comp portion) from
        another data array and its component. The variables min and max
        control the range of the data to use from the other data array;
        normalize is a flag that when set will normalize the data between
        (0,1).
        """
        ...
    
    def DefaultNormalizeOff(self):
        """
        V.DefaultNormalizeOff()
        C++: virtual void DefaultNormalizeOff()
        
        Set the default Normalize() flag for those methods setting a
        default Normalize value (e.g., SetScalarComponents).
        """
        ...
    
    def DefaultNormalizeOn(self):
        """
        V.DefaultNormalizeOn()
        C++: virtual void DefaultNormalizeOn()
        
        Set the default Normalize() flag for those methods setting a
        default Normalize value (e.g., SetScalarComponents).
        """
        ...
    
    def GetDefaultNormalize(self):
        """
        V.GetDefaultNormalize() -> int
        C++: virtual vtkTypeBool GetDefaultNormalize()
        
        Set the default Normalize() flag for those methods setting a
        default Normalize value (e.g., SetScalarComponents).
        """
        ...
    
    def GetFieldArray(self, vtkFieldData, string, p_int):
        """
        V.GetFieldArray(vtkFieldData, string, int) -> vtkDataArray
        C++: static vtkDataArray *GetFieldArray(vtkFieldData *fd,
            const char *name, int comp)
        
        Return an array of a particular name from field data and do error
        checking.
        """
        ...
    
    def GetInputField(self):
        """
        V.GetInputField() -> int
        C++: virtual int GetInputField()
        
        Specify which field data to use to generate the output attribute
        data. There are three choices: the field data associated with the
        vtkDataObject superclass; the point field attribute data; and the
        cell field attribute data.
        """
        ...
    
    def GetNormalComponentArrayComponent(self, p_int):
        """
        V.GetNormalComponentArrayComponent(int) -> int
        C++: int GetNormalComponentArrayComponent(int comp)
        
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetNormalComponentArrayName(self, p_int):
        """
        V.GetNormalComponentArrayName(int) -> string
        C++: const char *GetNormalComponentArrayName(int comp)
        
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetNormalComponentMaxRange(self, p_int):
        """
        V.GetNormalComponentMaxRange(int) -> int
        C++: int GetNormalComponentMaxRange(int comp)
        
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetNormalComponentMinRange(self, p_int):
        """
        V.GetNormalComponentMinRange(int) -> int
        C++: int GetNormalComponentMinRange(int comp)
        
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetNormalComponentNormalizeFlag(self, p_int):
        """
        V.GetNormalComponentNormalizeFlag(int) -> int
        C++: int GetNormalComponentNormalizeFlag(int comp)
        
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
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
    
    def GetOutputAttributeData(self):
        """
        V.GetOutputAttributeData() -> int
        C++: virtual int GetOutputAttributeData()
        
        Specify which attribute data to output: point or cell data
        attributes.
        """
        ...
    
    def GetScalarComponentArrayComponent(self, p_int):
        """
        V.GetScalarComponentArrayComponent(int) -> int
        C++: int GetScalarComponentArrayComponent(int comp)
        
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetScalarComponentArrayName(self, p_int):
        """
        V.GetScalarComponentArrayName(int) -> string
        C++: const char *GetScalarComponentArrayName(int comp)
        
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetScalarComponentMaxRange(self, p_int):
        """
        V.GetScalarComponentMaxRange(int) -> int
        C++: int GetScalarComponentMaxRange(int comp)
        
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetScalarComponentMinRange(self, p_int):
        """
        V.GetScalarComponentMinRange(int) -> int
        C++: int GetScalarComponentMinRange(int comp)
        
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetScalarComponentNormalizeFlag(self, p_int):
        """
        V.GetScalarComponentNormalizeFlag(int) -> int
        C++: int GetScalarComponentNormalizeFlag(int comp)
        
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetTCoordComponentArrayComponent(self, p_int):
        """
        V.GetTCoordComponentArrayComponent(int) -> int
        C++: int GetTCoordComponentArrayComponent(int comp)
        
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ...
    
    def GetTCoordComponentArrayName(self, p_int):
        """
        V.GetTCoordComponentArrayName(int) -> string
        C++: const char *GetTCoordComponentArrayName(int comp)
        
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ...
    
    def GetTCoordComponentMaxRange(self, p_int):
        """
        V.GetTCoordComponentMaxRange(int) -> int
        C++: int GetTCoordComponentMaxRange(int comp)
        
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ...
    
    def GetTCoordComponentMinRange(self, p_int):
        """
        V.GetTCoordComponentMinRange(int) -> int
        C++: int GetTCoordComponentMinRange(int comp)
        
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ...
    
    def GetTCoordComponentNormalizeFlag(self, p_int):
        """
        V.GetTCoordComponentNormalizeFlag(int) -> int
        C++: int GetTCoordComponentNormalizeFlag(int comp)
        
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ...
    
    def GetTensorComponentArrayComponent(self, p_int):
        """
        V.GetTensorComponentArrayComponent(int) -> int
        C++: int GetTensorComponentArrayComponent(int comp)
        
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetTensorComponentArrayName(self, p_int):
        """
        V.GetTensorComponentArrayName(int) -> string
        C++: const char *GetTensorComponentArrayName(int comp)
        
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetTensorComponentMaxRange(self, p_int):
        """
        V.GetTensorComponentMaxRange(int) -> int
        C++: int GetTensorComponentMaxRange(int comp)
        
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetTensorComponentMinRange(self, p_int):
        """
        V.GetTensorComponentMinRange(int) -> int
        C++: int GetTensorComponentMinRange(int comp)
        
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetTensorComponentNormalizeFlag(self, p_int):
        """
        V.GetTensorComponentNormalizeFlag(int) -> int
        C++: int GetTensorComponentNormalizeFlag(int comp)
        
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetVectorComponentArrayComponent(self, p_int):
        """
        V.GetVectorComponentArrayComponent(int) -> int
        C++: int GetVectorComponentArrayComponent(int comp)
        
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetVectorComponentArrayName(self, p_int):
        """
        V.GetVectorComponentArrayName(int) -> string
        C++: const char *GetVectorComponentArrayName(int comp)
        
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetVectorComponentMaxRange(self, p_int):
        """
        V.GetVectorComponentMaxRange(int) -> int
        C++: int GetVectorComponentMaxRange(int comp)
        
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetVectorComponentMinRange(self, p_int):
        """
        V.GetVectorComponentMinRange(int) -> int
        C++: int GetVectorComponentMinRange(int comp)
        
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def GetVectorComponentNormalizeFlag(self, p_int):
        """
        V.GetVectorComponentNormalizeFlag(int) -> int
        C++: int GetVectorComponentNormalizeFlag(int comp)
        
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
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
        V.NewInstance() -> vtkFieldDataToAttributeDataFilter
        C++: vtkFieldDataToAttributeDataFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkFieldDataToAttributeDataFilter
        C++: static vtkFieldDataToAttributeDataFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetDefaultNormalize(self, p_int):
        """
        V.SetDefaultNormalize(int)
        C++: virtual void SetDefaultNormalize(vtkTypeBool _arg)
        
        Set the default Normalize() flag for those methods setting a
        default Normalize value (e.g., SetScalarComponents).
        """
        ...
    
    def SetInputField(self, p_int):
        """
        V.SetInputField(int)
        C++: virtual void SetInputField(int _arg)
        
        Specify which field data to use to generate the output attribute
        data. There are three choices: the field data associated with the
        vtkDataObject superclass; the point field attribute data; and the
        cell field attribute data.
        """
        ...
    
    def SetInputFieldToCellDataField(self):
        """
        V.SetInputFieldToCellDataField()
        C++: void SetInputFieldToCellDataField()
        
        Specify which field data to use to generate the output attribute
        data. There are three choices: the field data associated with the
        vtkDataObject superclass; the point field attribute data; and the
        cell field attribute data.
        """
        ...
    
    def SetInputFieldToDataObjectField(self):
        """
        V.SetInputFieldToDataObjectField()
        C++: void SetInputFieldToDataObjectField()
        
        Specify which field data to use to generate the output attribute
        data. There are three choices: the field data associated with the
        vtkDataObject superclass; the point field attribute data; and the
        cell field attribute data.
        """
        ...
    
    def SetInputFieldToPointDataField(self):
        """
        V.SetInputFieldToPointDataField()
        C++: void SetInputFieldToPointDataField()
        
        Specify which field data to use to generate the output attribute
        data. There are three choices: the field data associated with the
        vtkDataObject superclass; the point field attribute data; and the
        cell field attribute data.
        """
        ...
    
    def SetNormalComponent(self, p_int, string, p_int_1, p_int_2, p_int_3, p_int_4):
        """
        V.SetNormalComponent(int, string, int, int, int, int)
        C++: void SetNormalComponent(int comp, const char *arrayName,
            int arrayComp, int min, int max, int normalize)
        V.SetNormalComponent(int, string, int)
        C++: void SetNormalComponent(int comp, const char *arrayName,
            int arrayComp)
        
        Define the component(s) of the field to be used for the normal
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def SetOutputAttributeData(self, p_int):
        """
        V.SetOutputAttributeData(int)
        C++: virtual void SetOutputAttributeData(int _arg)
        
        Specify which attribute data to output: point or cell data
        attributes.
        """
        ...
    
    def SetOutputAttributeDataToCellData(self):
        """
        V.SetOutputAttributeDataToCellData()
        C++: void SetOutputAttributeDataToCellData()
        
        Specify which attribute data to output: point or cell data
        attributes.
        """
        ...
    
    def SetOutputAttributeDataToPointData(self):
        """
        V.SetOutputAttributeDataToPointData()
        C++: void SetOutputAttributeDataToPointData()
        
        Specify which attribute data to output: point or cell data
        attributes.
        """
        ...
    
    def SetScalarComponent(self, p_int, string, p_int_1, p_int_2, p_int_3, p_int_4):
        """
        V.SetScalarComponent(int, string, int, int, int, int)
        C++: void SetScalarComponent(int comp, const char *arrayName,
            int arrayComp, int min, int max, int normalize)
        V.SetScalarComponent(int, string, int)
        C++: void SetScalarComponent(int comp, const char *arrayName,
            int arrayComp)
        
        Define the component(s) of the field to be used for the scalar
        components.  Note that the parameter comp must lie between (0,4).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def SetTCoordComponent(self, p_int, string, p_int_1, p_int_2, p_int_3, p_int_4):
        """
        V.SetTCoordComponent(int, string, int, int, int, int)
        C++: void SetTCoordComponent(int comp, const char *arrayName,
            int arrayComp, int min, int max, int normalize)
        V.SetTCoordComponent(int, string, int)
        C++: void SetTCoordComponent(int comp, const char *arrayName,
            int arrayComp)
        
        Define the components of the field to be used for the cell
        texture coord components.  Note that the parameter comp must lie
        between (0,9). To define the field component to use you specify
        an array name and the component in that array. The (min,max)
        values are the range of data in the component you wish to
        extract.
        """
        ...
    
    def SetTensorComponent(self, p_int, string, p_int_1, p_int_2, p_int_3, p_int_4):
        """
        V.SetTensorComponent(int, string, int, int, int, int)
        C++: void SetTensorComponent(int comp, const char *arrayName,
            int arrayComp, int min, int max, int normalize)
        V.SetTensorComponent(int, string, int)
        C++: void SetTensorComponent(int comp, const char *arrayName,
            int arrayComp)
        
        Define the components of the field to be used for the tensor
        components.  Note that the parameter comp must lie between (0,9).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def SetVectorComponent(self, p_int, string, p_int_1, p_int_2, p_int_3, p_int_4):
        """
        V.SetVectorComponent(int, string, int, int, int, int)
        C++: void SetVectorComponent(int comp, const char *arrayName,
            int arrayComp, int min, int max, int normalize)
        V.SetVectorComponent(int, string, int)
        C++: void SetVectorComponent(int comp, const char *arrayName,
            int arrayComp)
        
        Define the component(s) of the field to be used for the vector
        components.  Note that the parameter comp must lie between (0,3).
        To define the field component to use you specify an array name
        and the component in that array. The (min,max) values are the
        range of data in the component you wish to extract.
        """
        ...
    
    def UpdateComponentRange(self, vtkDataArray, p_int=..., p_int=...):
        """
        V.UpdateComponentRange(vtkDataArray, [int, int]) -> int
        C++: static int UpdateComponentRange(vtkDataArray *da,
            vtkIdType compRange[2])
        
        Update the maximum and minimum component range values. Returns a
        flag indicating whether the range was updated.
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

