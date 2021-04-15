"""
This type stub file was generated by pyright.
"""

from .vtkDataObject import vtkDataObject

class vtkTable(vtkDataObject):
    """
    vtkTable - A table, which contains similar-typed columns of data
    
    Superclass: vtkDataObject
    
    vtkTable is a basic data structure for storing columns of data.
    Internally, columns are stored in a vtkDataSetAttributes structure
    called RowData. However, using the vtkTable API additionally ensures
    that every column has the same number of entries, and provides row
    access (using vtkVariantArray) and single entry access (using
    vtkVariant).
    
    The field data inherited from vtkDataObject may be used to store
    metadata related to the table.
    
    @warning
    You should use the vtkTable API to change the table data. Performing
    operations on the object returned by GetRowData() may yield
    unexpected results. vtkTable does allow the user to set the field
    data using SetRowData(); the number of rows in the table is
    determined by the number of tuples in the first array (it is assumed
    that all arrays are the same length).
    
    @warning
    Each column added with AddColumn musthave its name set to a unique,
    non-empty string in order for GetValue() to function properly.
    
    @par Thanks: Thanks to Patricia Crossno, Ken Moreland, Andrew Wilson
    and Brian Wylie from Sandia National Laboratories for their help in
    developing this class API.
    """
    def AddColumn(self, vtkAbstractArray):
        """
        V.AddColumn(vtkAbstractArray)
        C++: void AddColumn(vtkAbstractArray *arr)
        
        Add a column to the table.
        """
        ...
    
    def DeepCopy(self, vtkDataObject):
        """
        V.DeepCopy(vtkDataObject)
        C++: void DeepCopy(vtkDataObject *src) override;
        
        Shallow/deep copy the data from src into this object.
        """
        ...
    
    def Dump(self, p_int, p_int_1):
        """
        V.Dump(int, int)
        C++: void Dump(unsigned int colWidth=16, int rowLimit=-1)
        
        Dump table contents.  If rowLimit is -1 then the full table is
        printed out (Default).  If rowLimit is 0 then only the header row
        will be displayed.  Otherwise, if rowLimit > 0 then Dump will
        print the first rowLimit rows of data.
        """
        ...
    
    def GetActualMemorySize(self):
        """
        V.GetActualMemorySize() -> int
        C++: unsigned long GetActualMemorySize() override;
        
        Return the actual size of the data in kibibytes (1024 bytes).
        This number is valid only after the pipeline has updated. The
        memory size returned is guaranteed to be greater than or equal to
        the memory required to represent the data (e.g., extra space in
        arrays, etc. are not included in the return value).
        """
        ...
    
    def GetAttributesAsFieldData(self, p_int):
        """
        V.GetAttributesAsFieldData(int) -> vtkFieldData
        C++: vtkFieldData *GetAttributesAsFieldData(int type) override;
        
        Returns the attributes of the data object as a vtkFieldData. This
        returns non-null values in all the same cases as GetAttributes,
        in addition to the case of FIELD, which will return the field
        data for any vtkDataObject subclass.
        """
        ...
    
    def GetColumn(self, p_int):
        """
        V.GetColumn(int) -> vtkAbstractArray
        C++: vtkAbstractArray *GetColumn(vtkIdType col)
        
        Get a column of the table by its column index.
        """
        ...
    
    def GetColumnByName(self, string):
        """
        V.GetColumnByName(string) -> vtkAbstractArray
        C++: vtkAbstractArray *GetColumnByName(const char *name)
        
        Get a column of the table by its name.
        """
        ...
    
    def GetColumnName(self, p_int):
        """
        V.GetColumnName(int) -> string
        C++: const char *GetColumnName(vtkIdType col)
        """
        ...
    
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkTable
        C++: static vtkTable *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkTable
        C++: static vtkTable *GetData(vtkInformationVector *v, int i=0)
        
        Retrieve the table from vtkInformation.
        """
        ...
    
    def GetDataObjectType(self):
        """
        V.GetDataObjectType() -> int
        C++: int GetDataObjectType() override;
        
        Return what type of dataset this is.
        """
        ...
    
    def GetNumberOfColumns(self):
        """
        V.GetNumberOfColumns() -> int
        C++: vtkIdType GetNumberOfColumns()
        
        Get the number of columns in the table.
        """
        ...
    
    def GetNumberOfElements(self, p_int):
        """
        V.GetNumberOfElements(int) -> int
        C++: vtkIdType GetNumberOfElements(int type) override;
        
        Get the number of elements for a specific attribute type (ROW,
        etc.).
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
    
    def GetNumberOfRows(self):
        """
        V.GetNumberOfRows() -> int
        C++: vtkIdType GetNumberOfRows()
        
        Get the number of rows in the table.
        """
        ...
    
    def GetRow(self, p_int):
        """
        V.GetRow(int) -> vtkVariantArray
        C++: vtkVariantArray *GetRow(vtkIdType row)
        V.GetRow(int, vtkVariantArray)
        C++: void GetRow(vtkIdType row, vtkVariantArray *values)
        
        Get a row of the table as a vtkVariantArray which has one entry
        for each column. NOTE: This version of the method is NOT thread
        safe.
        """
        ...
    
    def GetRowData(self):
        """
        V.GetRowData() -> vtkDataSetAttributes
        C++: virtual vtkDataSetAttributes *GetRowData()
        
        Get/Set the main data (columns) of the table.
        """
        ...
    
    def GetValue(self, p_int, p_int_1):
        """
        V.GetValue(int, int) -> vtkVariant
        C++: vtkVariant GetValue(vtkIdType row, vtkIdType col)
        
        Retrieve a value in the table by row and column index as a
        variant. Note that this calls GetValueByName internally so that
        each column array must have its name set (and that name should be
        unique within the table).
        """
        ...
    
    def GetValueByName(self, p_int, string):
        """
        V.GetValueByName(int, string) -> vtkVariant
        C++: vtkVariant GetValueByName(vtkIdType row, const char *col)
        
        Retrieve a value in the table by row index and column name as a
        variant.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        Initialize to an empty table.
        """
        ...
    
    def InsertNextBlankRow(self, p_float):
        """
        V.InsertNextBlankRow(float) -> int
        C++: vtkIdType InsertNextBlankRow(double default_num_val=0.0)
        
        Insert a blank row at the end of the table.
        """
        ...
    
    def InsertNextRow(self, vtkVariantArray):
        """
        V.InsertNextRow(vtkVariantArray) -> int
        C++: vtkIdType InsertNextRow(vtkVariantArray *arr)
        
        Insert a row specified by a vtkVariantArray.  The number of
        entries in the array should match the number of columns in the
        table.
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
        V.NewInstance() -> vtkTable
        C++: vtkTable *NewInstance()
        """
        ...
    
    def RemoveColumn(self, p_int):
        """
        V.RemoveColumn(int)
        C++: void RemoveColumn(vtkIdType col)
        
        Remove a column from the table by its column index.
        """
        ...
    
    def RemoveColumnByName(self, string):
        """
        V.RemoveColumnByName(string)
        C++: void RemoveColumnByName(const char *name)
        
        Remove a column from the table by its name.
        """
        ...
    
    def RemoveRow(self, p_int):
        """
        V.RemoveRow(int)
        C++: void RemoveRow(vtkIdType row)
        
        Delete a row from the table.  Rows below the deleted row are
        shifted up.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTable
        C++: static vtkTable *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetNumberOfRows(self, p_int):
        """
        V.SetNumberOfRows(int)
        C++: void SetNumberOfRows(const vtkIdType)
        
        Set the number of rows in the table. Note that memory allocation
        might be performed as a result of this, but no memory will be
        released.
        """
        ...
    
    def SetRow(self, p_int, vtkVariantArray):
        """
        V.SetRow(int, vtkVariantArray)
        C++: void SetRow(vtkIdType row, vtkVariantArray *values)
        
        Set a row of the table with a vtkVariantArray which has one entry
        for each column.
        """
        ...
    
    def SetRowData(self, vtkDataSetAttributes):
        """
        V.SetRowData(vtkDataSetAttributes)
        C++: virtual void SetRowData(vtkDataSetAttributes *data)
        
        Get/Set the main data (columns) of the table.
        """
        ...
    
    def SetValue(self, p_int, p_int_1, vtkVariant):
        """
        V.SetValue(int, int, vtkVariant)
        C++: void SetValue(vtkIdType row, vtkIdType col, vtkVariant value)
        
        Set a value in the table by row and column index as a variant.
        """
        ...
    
    def SetValueByName(self, p_int, string, vtkVariant):
        """
        V.SetValueByName(int, string, vtkVariant)
        C++: void SetValueByName(vtkIdType row, const char *col,
            vtkVariant value)
        
        Set a value in the table by row index and column name as a
        variant.
        """
        ...
    
    def ShallowCopy(self, vtkDataObject):
        """
        V.ShallowCopy(vtkDataObject)
        C++: void ShallowCopy(vtkDataObject *src) override;
        
        Shallow/deep copy the data from src into this object.
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

