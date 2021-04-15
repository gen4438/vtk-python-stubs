"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkArrayCalculator(__vtkmodules_vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    """
    vtkArrayCalculator - perform mathematical operations on data in field
    data arrays
    
    Superclass: vtkPassInputTypeAlgorithm
    
    vtkArrayCalculator performs operations on vectors or scalars in field
    data arrays.  It uses vtkFunctionParser to do the parsing and to
    evaluate the function for each entry in the input arrays.  The arrays
    used in a given function must be all in point data or all in cell
    data. The resulting array will be stored as a field data array.  The
    result array can either be stored in a new array or it can overwrite
    an existing array.
    
    The functions that this array calculator understands is:
    
    standard operations: + - * / ^ . build unit vectors: iHat, jHat, kHat
    (ie (1,0,0), (0,1,0), (0,0,1)) abs acos asin atan ceil cos cosh exp
    floor log mag min max norm sign sin sinh sqrt tan tanh  Note that
    some of these operations work on scalars, some on vectors, and some
    on both (e.g., you can multiply a scalar times a vector). The
    operations are performed tuple-wise (i.e., tuple-by-tuple). The user
    must specify which arrays to use as vectors and/or scalars, and the
    name of the output data array.
    
    @sa
    vtkFunctionParser
    """
    def AddCoordinateScalarVariable(self, string, p_int):
        """
        V.AddCoordinateScalarVariable(string, int)
        C++: void AddCoordinateScalarVariable(const char *variableName,
            int component=0)
        
        Add a variable name, a corresponding array name, and which
        components of the array to use.
        """
        ...
    
    def AddCoordinateVectorVariable(self, string, p_int, p_int_1, p_int_2):
        """
        V.AddCoordinateVectorVariable(string, int, int, int)
        C++: void AddCoordinateVectorVariable(const char *variableName,
            int component0=0, int component1=1, int component2=2)
        
        Add a variable name, a corresponding array name, and which
        components of the array to use.
        """
        ...
    
    def AddScalarArrayName(self, string, p_int):
        """
        V.AddScalarArrayName(string, int)
        C++: void AddScalarArrayName(const char *arrayName,
            int component=0)
        
        Add an array name to the list of arrays used in the function and
        specify which components of the array to use in evaluating the
        function.  The array name must match the name in the function. 
        Use AddScalarVariable or AddVectorVariable to use a variable name
        different from the array name.
        """
        ...
    
    def AddScalarVariable(self, string, string_1, p_int):
        """
        V.AddScalarVariable(string, string, int)
        C++: void AddScalarVariable(const char *variableName,
            const char *arrayName, int component=0)
        
        Add a variable name, a corresponding array name, and which
        components of the array to use.
        """
        ...
    
    def AddVectorArrayName(self, string, p_int, p_int_1, p_int_2):
        """
        V.AddVectorArrayName(string, int, int, int)
        C++: void AddVectorArrayName(const char *arrayName,
            int component0=0, int component1=1, int component2=2)
        
        Add an array name to the list of arrays used in the function and
        specify which components of the array to use in evaluating the
        function.  The array name must match the name in the function. 
        Use AddScalarVariable or AddVectorVariable to use a variable name
        different from the array name.
        """
        ...
    
    def AddVectorVariable(self, string, string_1, p_int, p_int_1, p_int_2):
        """
        V.AddVectorVariable(string, string, int, int, int)
        C++: void AddVectorVariable(const char *variableName,
            const char *arrayName, int component0=0, int component1=1,
            int component2=2)
        
        Add a variable name, a corresponding array name, and which
        components of the array to use.
        """
        ...
    
    def CoordinateResultsOff(self):
        """
        V.CoordinateResultsOff()
        C++: virtual void CoordinateResultsOff()
        
        Set whether to output results as coordinates.  ResultArrayName
        will be ignored.  Outputting as coordinates is only valid with
        vector results and if the AttributeMode is
        AttributeModeToUsePointData. If a valid output can't be made, an
        error will occur.
        """
        ...
    
    def CoordinateResultsOn(self):
        """
        V.CoordinateResultsOn()
        C++: virtual void CoordinateResultsOn()
        
        Set whether to output results as coordinates.  ResultArrayName
        will be ignored.  Outputting as coordinates is only valid with
        vector results and if the AttributeMode is
        AttributeModeToUsePointData. If a valid output can't be made, an
        error will occur.
        """
        ...
    
    def GetAttributeMode(self):
        """
        V.GetAttributeMode() -> int
        C++: int GetAttributeMode()
        
        Control whether the filter operates on point data or cell data.
        By default (AttributeModeToDefault), the filter uses point data.
        Alternatively you can explicitly set the filter to use point data
        (AttributeModeToUsePointData) or cell data
        (AttributeModeToUseCellData). For graphs you can set the filter
        to use vertex data (AttributeModeToUseVertexData) or edge data
        (AttributeModeToUseEdgeData).
        
        @deprecated Replaced By GetAttributeType and SetAttributeType as
        of VTK 8.1.
        """
        ...
    
    def GetAttributeModeAsString(self):
        """
        V.GetAttributeModeAsString() -> string
        C++: const char *GetAttributeModeAsString()
        
        Control whether the filter operates on point data or cell data.
        By default (AttributeModeToDefault), the filter uses point data.
        Alternatively you can explicitly set the filter to use point data
        (AttributeModeToUsePointData) or cell data
        (AttributeModeToUseCellData). For graphs you can set the filter
        to use vertex data (AttributeModeToUseVertexData) or edge data
        (AttributeModeToUseEdgeData).
        
        @deprecated Replaced By GetAttributeType and SetAttributeType as
        of VTK 8.1.
        """
        ...
    
    def GetAttributeType(self):
        """
        V.GetAttributeType() -> int
        C++: virtual int GetAttributeType()
        
        Control which AttributeType the filter operates on (point data or
        cell data for vtkDataSets).  By default the filter uses
        Point/Vertex/Row data depending on the input data type.  The
        input value for this function should be one of the constants in
        vtkDataObject::AttributeTypes or DEFAULT_ATTRIBUTE_TYPE for 'default
        behavior'.
        """
        ...
    
    def GetAttributeTypeAsString(self):
        """
        V.GetAttributeTypeAsString() -> string
        C++: const char *GetAttributeTypeAsString()
        
        Returns a string representation of the calculator's AttributeType
        """
        ...
    
    def GetCoordinateResults(self):
        """
        V.GetCoordinateResults() -> int
        C++: virtual vtkTypeBool GetCoordinateResults()
        
        Set whether to output results as coordinates.  ResultArrayName
        will be ignored.  Outputting as coordinates is only valid with
        vector results and if the AttributeMode is
        AttributeModeToUsePointData. If a valid output can't be made, an
        error will occur.
        """
        ...
    
    def GetDataSetOutput(self):
        """
        V.GetDataSetOutput() -> vtkDataSet
        C++: vtkDataSet *GetDataSetOutput()
        
        Returns the output of the filter downcast to a vtkDataSet or
        nullptr if the cast fails.
        """
        ...
    
    def GetFunction(self):
        """
        V.GetFunction() -> string
        C++: virtual char *GetFunction()
        
        Set/Get the function to be evaluated.
        """
        ...
    
    def GetIgnoreMissingArrays(self):
        """
        V.GetIgnoreMissingArrays() -> bool
        C++: virtual bool GetIgnoreMissingArrays()
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
    
    def GetNumberOfScalarArrays(self):
        """
        V.GetNumberOfScalarArrays() -> int
        C++: virtual int GetNumberOfScalarArrays()
        
        Methods to get information about the current variables.
        """
        ...
    
    def GetNumberOfVectorArrays(self):
        """
        V.GetNumberOfVectorArrays() -> int
        C++: virtual int GetNumberOfVectorArrays()
        
        Methods to get information about the current variables.
        """
        ...
    
    def GetReplaceInvalidValues(self):
        """
        V.GetReplaceInvalidValues() -> int
        C++: virtual vtkTypeBool GetReplaceInvalidValues()
        
        When ReplaceInvalidValues is on, all invalid values (such as
        sqrt(-2), note that function parser does not handle complex
        numbers) will be replaced by ReplacementValue. Otherwise an error
        will be reported
        """
        ...
    
    def GetReplacementValue(self):
        """
        V.GetReplacementValue() -> float
        C++: virtual double GetReplacementValue()
        
        When ReplaceInvalidValues is on, all invalid values (such as
        sqrt(-2), note that function parser does not handle complex
        numbers) will be replaced by ReplacementValue. Otherwise an error
        will be reported
        """
        ...
    
    def GetResultArrayName(self):
        """
        V.GetResultArrayName() -> string
        C++: virtual char *GetResultArrayName()
        
        Set the name of the array in which to store the result of
        evaluating this function.  If this is the name of an existing
        array, that array will be overwritten.  Otherwise a new array
        will be created with the specified name.
        """
        ...
    
    def GetResultArrayType(self):
        """
        V.GetResultArrayType() -> int
        C++: virtual int GetResultArrayType()
        
        Type of the result array. It is ignored if CoordinateResults is
        true. Initial value is VTK_DOUBLE.
        """
        ...
    
    def GetResultNormals(self):
        """
        V.GetResultNormals() -> bool
        C++: virtual bool GetResultNormals()
        
        Set whether to output results as point/cell normals. Outputting
        as normals is only valid with vector results. Point or cell
        normals are selected using AttributeMode.
        """
        ...
    
    def GetResultTCoords(self):
        """
        V.GetResultTCoords() -> bool
        C++: virtual bool GetResultTCoords()
        
        Set whether to output results as point/cell texture coordinates.
        Point or cell texture coordinates are selected using
        AttributeMode. 2-component texture coordinates cannot be
        generated at this time.
        """
        ...
    
    def GetScalarArrayName(self, p_int):
        """
        V.GetScalarArrayName(int) -> string
        C++: char *GetScalarArrayName(int i)
        
        Methods to get information about the current variables.
        """
        ...
    
    def GetScalarVariableName(self, p_int):
        """
        V.GetScalarVariableName(int) -> string
        C++: char *GetScalarVariableName(int i)
        
        Methods to get information about the current variables.
        """
        ...
    
    def GetSelectedScalarComponent(self, p_int):
        """
        V.GetSelectedScalarComponent(int) -> int
        C++: int GetSelectedScalarComponent(int i)
        
        Methods to get information about the current variables.
        """
        ...
    
    def GetSelectedScalarComponents(self):
        """
        V.GetSelectedScalarComponents() -> (int, ...)
        C++: int *GetSelectedScalarComponents()
        
        Methods to get information about the current variables.
        """
        ...
    
    def GetSelectedVectorComponents(self, p_int):
        """
        V.GetSelectedVectorComponents(int) -> (int, ...)
        C++: int *GetSelectedVectorComponents(int i)
        
        Methods to get information about the current variables.
        """
        ...
    
    def GetVectorArrayName(self, p_int):
        """
        V.GetVectorArrayName(int) -> string
        C++: char *GetVectorArrayName(int i)
        
        Methods to get information about the current variables.
        """
        ...
    
    def GetVectorVariableName(self, p_int):
        """
        V.GetVectorVariableName(int) -> string
        C++: char *GetVectorVariableName(int i)
        
        Methods to get information about the current variables.
        """
        ...
    
    def IgnoreMissingArraysOff(self):
        """
        V.IgnoreMissingArraysOff()
        C++: virtual void IgnoreMissingArraysOff()
        """
        ...
    
    def IgnoreMissingArraysOn(self):
        """
        V.IgnoreMissingArraysOn()
        C++: virtual void IgnoreMissingArraysOn()
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
        V.NewInstance() -> vtkArrayCalculator
        C++: vtkArrayCalculator *NewInstance()
        """
        ...
    
    def RemoveAllVariables(self):
        """
        V.RemoveAllVariables()
        C++: void RemoveAllVariables()
        
        Remove all the variable names and their associated array names.
        """
        ...
    
    def RemoveCoordinateScalarVariables(self):
        """
        V.RemoveCoordinateScalarVariables()
        C++: virtual void RemoveCoordinateScalarVariables()
        
        Remove all the coordinate variables.
        """
        ...
    
    def RemoveCoordinateVectorVariables(self):
        """
        V.RemoveCoordinateVectorVariables()
        C++: virtual void RemoveCoordinateVectorVariables()
        
        Remove all the coordinate variables.
        """
        ...
    
    def RemoveScalarVariables(self):
        """
        V.RemoveScalarVariables()
        C++: virtual void RemoveScalarVariables()
        
        Remove all the scalar variable names and their associated array
        names.
        """
        ...
    
    def RemoveVectorVariables(self):
        """
        V.RemoveVectorVariables()
        C++: virtual void RemoveVectorVariables()
        
        Remove all the scalar variable names and their associated array
        names.
        """
        ...
    
    def ReplaceInvalidValuesOff(self):
        """
        V.ReplaceInvalidValuesOff()
        C++: virtual void ReplaceInvalidValuesOff()
        
        When ReplaceInvalidValues is on, all invalid values (such as
        sqrt(-2), note that function parser does not handle complex
        numbers) will be replaced by ReplacementValue. Otherwise an error
        will be reported
        """
        ...
    
    def ReplaceInvalidValuesOn(self):
        """
        V.ReplaceInvalidValuesOn()
        C++: virtual void ReplaceInvalidValuesOn()
        
        When ReplaceInvalidValues is on, all invalid values (such as
        sqrt(-2), note that function parser does not handle complex
        numbers) will be replaced by ReplacementValue. Otherwise an error
        will be reported
        """
        ...
    
    def ResultNormalsOff(self):
        """
        V.ResultNormalsOff()
        C++: virtual void ResultNormalsOff()
        
        Set whether to output results as point/cell normals. Outputting
        as normals is only valid with vector results. Point or cell
        normals are selected using AttributeMode.
        """
        ...
    
    def ResultNormalsOn(self):
        """
        V.ResultNormalsOn()
        C++: virtual void ResultNormalsOn()
        
        Set whether to output results as point/cell normals. Outputting
        as normals is only valid with vector results. Point or cell
        normals are selected using AttributeMode.
        """
        ...
    
    def ResultTCoordsOff(self):
        """
        V.ResultTCoordsOff()
        C++: virtual void ResultTCoordsOff()
        
        Set whether to output results as point/cell texture coordinates.
        Point or cell texture coordinates are selected using
        AttributeMode. 2-component texture coordinates cannot be
        generated at this time.
        """
        ...
    
    def ResultTCoordsOn(self):
        """
        V.ResultTCoordsOn()
        C++: virtual void ResultTCoordsOn()
        
        Set whether to output results as point/cell texture coordinates.
        Point or cell texture coordinates are selected using
        AttributeMode. 2-component texture coordinates cannot be
        generated at this time.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkArrayCalculator
        C++: static vtkArrayCalculator *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAttributeMode(self, p_int):
        """
        V.SetAttributeMode(int)
        C++: void SetAttributeMode(int newMode)
        
        Control whether the filter operates on point data or cell data.
        By default (AttributeModeToDefault), the filter uses point data.
        Alternatively you can explicitly set the filter to use point data
        (AttributeModeToUsePointData) or cell data
        (AttributeModeToUseCellData). For graphs you can set the filter
        to use vertex data (AttributeModeToUseVertexData) or edge data
        (AttributeModeToUseEdgeData).
        
        @deprecated Replaced By GetAttributeType and SetAttributeType as
        of VTK 8.1.
        """
        ...
    
    def SetAttributeModeToDefault(self):
        """
        V.SetAttributeModeToDefault()
        C++: void SetAttributeModeToDefault()
        
        Control whether the filter operates on point data or cell data.
        By default (AttributeModeToDefault), the filter uses point data.
        Alternatively you can explicitly set the filter to use point data
        (AttributeModeToUsePointData) or cell data
        (AttributeModeToUseCellData). For graphs you can set the filter
        to use vertex data (AttributeModeToUseVertexData) or edge data
        (AttributeModeToUseEdgeData).
        
        @deprecated Replaced By GetAttributeType and SetAttributeType as
        of VTK 8.1.
        """
        ...
    
    def SetAttributeModeToUseCellData(self):
        """
        V.SetAttributeModeToUseCellData()
        C++: void SetAttributeModeToUseCellData()
        
        Control whether the filter operates on point data or cell data.
        By default (AttributeModeToDefault), the filter uses point data.
        Alternatively you can explicitly set the filter to use point data
        (AttributeModeToUsePointData) or cell data
        (AttributeModeToUseCellData). For graphs you can set the filter
        to use vertex data (AttributeModeToUseVertexData) or edge data
        (AttributeModeToUseEdgeData).
        
        @deprecated Replaced By GetAttributeType and SetAttributeType as
        of VTK 8.1.
        """
        ...
    
    def SetAttributeModeToUseEdgeData(self):
        """
        V.SetAttributeModeToUseEdgeData()
        C++: void SetAttributeModeToUseEdgeData()
        
        Control whether the filter operates on point data or cell data.
        By default (AttributeModeToDefault), the filter uses point data.
        Alternatively you can explicitly set the filter to use point data
        (AttributeModeToUsePointData) or cell data
        (AttributeModeToUseCellData). For graphs you can set the filter
        to use vertex data (AttributeModeToUseVertexData) or edge data
        (AttributeModeToUseEdgeData).
        
        @deprecated Replaced By GetAttributeType and SetAttributeType as
        of VTK 8.1.
        """
        ...
    
    def SetAttributeModeToUsePointData(self):
        """
        V.SetAttributeModeToUsePointData()
        C++: void SetAttributeModeToUsePointData()
        
        Control whether the filter operates on point data or cell data.
        By default (AttributeModeToDefault), the filter uses point data.
        Alternatively you can explicitly set the filter to use point data
        (AttributeModeToUsePointData) or cell data
        (AttributeModeToUseCellData). For graphs you can set the filter
        to use vertex data (AttributeModeToUseVertexData) or edge data
        (AttributeModeToUseEdgeData).
        
        @deprecated Replaced By GetAttributeType and SetAttributeType as
        of VTK 8.1.
        """
        ...
    
    def SetAttributeModeToUseVertexData(self):
        """
        V.SetAttributeModeToUseVertexData()
        C++: void SetAttributeModeToUseVertexData()
        
        Control whether the filter operates on point data or cell data.
        By default (AttributeModeToDefault), the filter uses point data.
        Alternatively you can explicitly set the filter to use point data
        (AttributeModeToUsePointData) or cell data
        (AttributeModeToUseCellData). For graphs you can set the filter
        to use vertex data (AttributeModeToUseVertexData) or edge data
        (AttributeModeToUseEdgeData).
        
        @deprecated Replaced By GetAttributeType and SetAttributeType as
        of VTK 8.1.
        """
        ...
    
    def SetAttributeType(self, p_int):
        """
        V.SetAttributeType(int)
        C++: virtual void SetAttributeType(int _arg)
        
        Control which AttributeType the filter operates on (point data or
        cell data for vtkDataSets).  By default the filter uses
        Point/Vertex/Row data depending on the input data type.  The
        input value for this function should be one of the constants in
        vtkDataObject::AttributeTypes or DEFAULT_ATTRIBUTE_TYPE for 'default
        behavior'.
        """
        ...
    
    def SetAttributeTypeToCellData(self):
        """
        V.SetAttributeTypeToCellData()
        C++: void SetAttributeTypeToCellData()
        
        Control which AttributeType the filter operates on (point data or
        cell data for vtkDataSets).  By default the filter uses
        Point/Vertex/Row data depending on the input data type.  The
        input value for this function should be one of the constants in
        vtkDataObject::AttributeTypes or DEFAULT_ATTRIBUTE_TYPE for 'default
        behavior'.
        """
        ...
    
    def SetAttributeTypeToDefault(self):
        """
        V.SetAttributeTypeToDefault()
        C++: void SetAttributeTypeToDefault()
        
        Control which AttributeType the filter operates on (point data or
        cell data for vtkDataSets).  By default the filter uses
        Point/Vertex/Row data depending on the input data type.  The
        input value for this function should be one of the constants in
        vtkDataObject::AttributeTypes or DEFAULT_ATTRIBUTE_TYPE for 'default
        behavior'.
        """
        ...
    
    def SetAttributeTypeToEdgeData(self):
        """
        V.SetAttributeTypeToEdgeData()
        C++: void SetAttributeTypeToEdgeData()
        
        Control which AttributeType the filter operates on (point data or
        cell data for vtkDataSets).  By default the filter uses
        Point/Vertex/Row data depending on the input data type.  The
        input value for this function should be one of the constants in
        vtkDataObject::AttributeTypes or DEFAULT_ATTRIBUTE_TYPE for 'default
        behavior'.
        """
        ...
    
    def SetAttributeTypeToPointData(self):
        """
        V.SetAttributeTypeToPointData()
        C++: void SetAttributeTypeToPointData()
        
        Control which AttributeType the filter operates on (point data or
        cell data for vtkDataSets).  By default the filter uses
        Point/Vertex/Row data depending on the input data type.  The
        input value for this function should be one of the constants in
        vtkDataObject::AttributeTypes or DEFAULT_ATTRIBUTE_TYPE for 'default
        behavior'.
        """
        ...
    
    def SetAttributeTypeToRowData(self):
        """
        V.SetAttributeTypeToRowData()
        C++: void SetAttributeTypeToRowData()
        
        Control which AttributeType the filter operates on (point data or
        cell data for vtkDataSets).  By default the filter uses
        Point/Vertex/Row data depending on the input data type.  The
        input value for this function should be one of the constants in
        vtkDataObject::AttributeTypes or DEFAULT_ATTRIBUTE_TYPE for 'default
        behavior'.
        """
        ...
    
    def SetAttributeTypeToVertexData(self):
        """
        V.SetAttributeTypeToVertexData()
        C++: void SetAttributeTypeToVertexData()
        
        Control which AttributeType the filter operates on (point data or
        cell data for vtkDataSets).  By default the filter uses
        Point/Vertex/Row data depending on the input data type.  The
        input value for this function should be one of the constants in
        vtkDataObject::AttributeTypes or DEFAULT_ATTRIBUTE_TYPE for 'default
        behavior'.
        """
        ...
    
    def SetCoordinateResults(self, p_int):
        """
        V.SetCoordinateResults(int)
        C++: virtual void SetCoordinateResults(vtkTypeBool _arg)
        
        Set whether to output results as coordinates.  ResultArrayName
        will be ignored.  Outputting as coordinates is only valid with
        vector results and if the AttributeMode is
        AttributeModeToUsePointData. If a valid output can't be made, an
        error will occur.
        """
        ...
    
    def SetFunction(self, string):
        """
        V.SetFunction(string)
        C++: virtual void SetFunction(const char *function)
        
        Set/Get the function to be evaluated.
        """
        ...
    
    def SetIgnoreMissingArrays(self, bool):
        """
        V.SetIgnoreMissingArrays(bool)
        C++: virtual void SetIgnoreMissingArrays(bool _arg)
        """
        ...
    
    def SetReplaceInvalidValues(self, p_int):
        """
        V.SetReplaceInvalidValues(int)
        C++: virtual void SetReplaceInvalidValues(vtkTypeBool _arg)
        
        When ReplaceInvalidValues is on, all invalid values (such as
        sqrt(-2), note that function parser does not handle complex
        numbers) will be replaced by ReplacementValue. Otherwise an error
        will be reported
        """
        ...
    
    def SetReplacementValue(self, p_float):
        """
        V.SetReplacementValue(float)
        C++: virtual void SetReplacementValue(double _arg)
        
        When ReplaceInvalidValues is on, all invalid values (such as
        sqrt(-2), note that function parser does not handle complex
        numbers) will be replaced by ReplacementValue. Otherwise an error
        will be reported
        """
        ...
    
    def SetResultArrayName(self, string):
        """
        V.SetResultArrayName(string)
        C++: void SetResultArrayName(const char *name)
        
        Set the name of the array in which to store the result of
        evaluating this function.  If this is the name of an existing
        array, that array will be overwritten.  Otherwise a new array
        will be created with the specified name.
        """
        ...
    
    def SetResultArrayType(self, p_int):
        """
        V.SetResultArrayType(int)
        C++: virtual void SetResultArrayType(int _arg)
        
        Type of the result array. It is ignored if CoordinateResults is
        true. Initial value is VTK_DOUBLE.
        """
        ...
    
    def SetResultNormals(self, bool):
        """
        V.SetResultNormals(bool)
        C++: virtual void SetResultNormals(bool _arg)
        
        Set whether to output results as point/cell normals. Outputting
        as normals is only valid with vector results. Point or cell
        normals are selected using AttributeMode.
        """
        ...
    
    def SetResultTCoords(self, bool):
        """
        V.SetResultTCoords(bool)
        C++: virtual void SetResultTCoords(bool _arg)
        
        Set whether to output results as point/cell texture coordinates.
        Point or cell texture coordinates are selected using
        AttributeMode. 2-component texture coordinates cannot be
        generated at this time.
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
    DEFAULT_ATTRIBUTE_TYPE = ...
    __dict__ = ...
    __vtkname__ = ...


