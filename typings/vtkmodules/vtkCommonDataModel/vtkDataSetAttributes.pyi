"""
This type stub file was generated by pyright.
"""

from .vtkFieldData import vtkFieldData

class vtkDataSetAttributes(vtkFieldData):
    """
    vtkDataSetAttributes - represent and manipulate attribute data in a
    dataset
    
    Superclass: vtkFieldData
    
    vtkDataSetAttributes is a class that is used to represent and
    manipulate attribute data (e.g., scalars, vectors, normals, texture
    coordinates, tensors, global ids, pedigree ids, and field data).
    
    This adds to vtkFieldData the ability to pick one of the arrays from
    the field as the currently active array for each attribute type. In
    other words, you pick one array to be called "THE" Scalars, and then
    filters down the pipeline will treat that array specially. For
    example vtkContourFilter will contour "THE" Scalar array unless a
    different array is asked for.
    
    Additionally vtkDataSetAttributes provides methods that filters call
    to pass data through, copy data into, and interpolate from Fields.
    PassData passes entire arrays from the source to the destination.
    Copy passes through some subset of the tuples from the source to the
    destination. Interpolate interpolates from the chosen tuple(s) in the
    source data, using the provided weights, to produce new tuples in the
    destination. Each attribute type has pass, copy and interpolate
    "copy" flags that can be set in the destination to choose which
    attribute arrays will be transferred from the source to the
    destination.
    
    Finally this class provides a mechanism to determine which attributes
    a group of sources have in common, and to copy tuples from a source
    into the destination, for only those attributes that are held by all.
    """
    def CopyAllocate(self, vtkDataSetAttributes, p_int, p_int_1):
        """
        V.CopyAllocate(vtkDataSetAttributes, int, int)
        C++: void CopyAllocate(vtkDataSetAttributes *pd, vtkIdType sze=0,
            vtkIdType ext=1000)
        V.CopyAllocate(vtkDataSetAttributes, int, int, int)
        C++: void CopyAllocate(vtkDataSetAttributes *pd, vtkIdType sze,
            vtkIdType ext, int shallowCopyArrays)
        V.CopyAllocate(vtkDataSetAttributesFieldList, int, int)
        C++: void CopyAllocate(vtkDataSetAttributes::FieldList &list,
            vtkIdType sze=0, vtkIdType ext=1000)
        
        Allocates point data for point-by-point (or cell-by-cell) copy
        operation. If sze=0, then use the input DataSetAttributes to
        create (i.e., find initial size of) new objects; otherwise use
        the sze variable. Note that pd HAS to be the vtkDataSetAttributes
        object which will later be used with CopyData. If this is not the
        case, consider using the alternative forms of CopyAllocate and
        CopyData. ext is no longer used. If shallowCopyArrays is true,
        input arrays are copied to the output instead of new ones being
        allocated.
        """
        ...
    
    def CopyAllOff(self, p_int):
        """
        V.CopyAllOff(int)
        C++: void CopyAllOff(int ctype=ALLCOPY) override;
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def CopyAllOn(self, p_int):
        """
        V.CopyAllOn(int)
        C++: void CopyAllOn(int ctype=ALLCOPY) override;
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def CopyData(self, vtkDataSetAttributes, p_int, p_int_1):
        """
        V.CopyData(vtkDataSetAttributes, int, int)
        C++: void CopyData(vtkDataSetAttributes *fromPd, vtkIdType fromId,
             vtkIdType toId)
        V.CopyData(vtkDataSetAttributes, vtkIdList, vtkIdList)
        C++: void CopyData(vtkDataSetAttributes *fromPd,
            vtkIdList *fromIds, vtkIdList *toIds)
        V.CopyData(vtkDataSetAttributes, int, int, int)
        C++: void CopyData(vtkDataSetAttributes *fromPd,
            vtkIdType dstStart, vtkIdType n, vtkIdType srcStart)
        V.CopyData(vtkDataSetAttributesFieldList, vtkDataSetAttributes,
            int, int, int)
        C++: void CopyData(vtkDataSetAttributes::FieldList &list,
            vtkDataSetAttributes *dsa, int idx, vtkIdType fromId,
            vtkIdType toId)
        V.CopyData(vtkDataSetAttributesFieldList, vtkDataSetAttributes,
            int, int, int, int)
        C++: void CopyData(vtkDataSetAttributes::FieldList &list,
            vtkDataSetAttributes *dsa, int idx, vtkIdType dstStart,
            vtkIdType n, vtkIdType srcStart)
        
        Copy the attribute data from one id to another. Make sure
        CopyAllocate() has been invoked before using this method. When
        copying a field, the following copying rules are followed: 1)
        Check if a field is an attribute, if yes and if there is a
        COPYTUPLE copy flag for that attribute (on or off), obey the flag
        for that attribute, ignore (2) and (3), 2) if there is a copy
        field for that field (on or off), obey the flag, ignore (3) 3)
        obey CopyAllOn/Off
        """
        ...
    
    def CopyGlobalIdsOff(self):
        """
        V.CopyGlobalIdsOff()
        C++: virtual void CopyGlobalIdsOff()
        """
        ...
    
    def CopyGlobalIdsOn(self):
        """
        V.CopyGlobalIdsOn()
        C++: virtual void CopyGlobalIdsOn()
        """
        ...
    
    def CopyHigherOrderDegreesOff(self):
        """
        V.CopyHigherOrderDegreesOff()
        C++: virtual void CopyHigherOrderDegreesOff()
        """
        ...
    
    def CopyHigherOrderDegreesOn(self):
        """
        V.CopyHigherOrderDegreesOn()
        C++: virtual void CopyHigherOrderDegreesOn()
        """
        ...
    
    def CopyNormalsOff(self):
        """
        V.CopyNormalsOff()
        C++: virtual void CopyNormalsOff()
        """
        ...
    
    def CopyNormalsOn(self):
        """
        V.CopyNormalsOn()
        C++: virtual void CopyNormalsOn()
        """
        ...
    
    def CopyPedigreeIdsOff(self):
        """
        V.CopyPedigreeIdsOff()
        C++: virtual void CopyPedigreeIdsOff()
        """
        ...
    
    def CopyPedigreeIdsOn(self):
        """
        V.CopyPedigreeIdsOn()
        C++: virtual void CopyPedigreeIdsOn()
        """
        ...
    
    def CopyRationalWeightsOff(self):
        """
        V.CopyRationalWeightsOff()
        C++: virtual void CopyRationalWeightsOff()
        """
        ...
    
    def CopyRationalWeightsOn(self):
        """
        V.CopyRationalWeightsOn()
        C++: virtual void CopyRationalWeightsOn()
        """
        ...
    
    def CopyScalarsOff(self):
        """
        V.CopyScalarsOff()
        C++: virtual void CopyScalarsOff()
        """
        ...
    
    def CopyScalarsOn(self):
        """
        V.CopyScalarsOn()
        C++: virtual void CopyScalarsOn()
        """
        ...
    
    def CopyStructuredData(self, vtkDataSetAttributes, int_tuple, int_tuple_1, bool):
        """
        V.CopyStructuredData(vtkDataSetAttributes, (int, ...), (int, ...),
             bool)
        C++: void CopyStructuredData(vtkDataSetAttributes *inDsa,
            const int *inExt, const int *outExt, bool setSize=true)
        
        This method is used to copy data arrays in images. You should
        call CopyAllocate or SetupForCopy before calling this method. If
        setSize is true, this method will set the size of the output
        arrays according to the output extent. This is required when
        CopyAllocate() was used to setup output arrays.
        """
        ...
    
    def CopyTangentsOff(self):
        """
        V.CopyTangentsOff()
        C++: virtual void CopyTangentsOff()
        """
        ...
    
    def CopyTangentsOn(self):
        """
        V.CopyTangentsOn()
        C++: virtual void CopyTangentsOn()
        """
        ...
    
    def CopyTCoordsOff(self):
        """
        V.CopyTCoordsOff()
        C++: virtual void CopyTCoordsOff()
        """
        ...
    
    def CopyTCoordsOn(self):
        """
        V.CopyTCoordsOn()
        C++: virtual void CopyTCoordsOn()
        """
        ...
    
    def CopyTensorsOff(self):
        """
        V.CopyTensorsOff()
        C++: virtual void CopyTensorsOff()
        """
        ...
    
    def CopyTensorsOn(self):
        """
        V.CopyTensorsOn()
        C++: virtual void CopyTensorsOn()
        """
        ...
    
    def CopyTuple(self, vtkAbstractArray, vtkAbstractArray_1, p_int, p_int_1):
        """
        V.CopyTuple(vtkAbstractArray, vtkAbstractArray, int, int)
        C++: void CopyTuple(vtkAbstractArray *fromData,
            vtkAbstractArray *toData, vtkIdType fromId, vtkIdType toId)
        
        Copy a tuple (or set of tuples) of data from one data array to
        another. This method assumes that the fromData and toData objects
        are of the same type, and have the same number of components.
        This is true if you invoke CopyAllocate() or
        InterpolateAllocate().
        """
        ...
    
    def CopyTuples(self, vtkAbstractArray, vtkAbstractArray_1, vtkIdList, vtkIdList_1):
        """
        V.CopyTuples(vtkAbstractArray, vtkAbstractArray, vtkIdList,
            vtkIdList)
        C++: void CopyTuples(vtkAbstractArray *fromData,
            vtkAbstractArray *toData, vtkIdList *fromIds,
            vtkIdList *toIds)
        V.CopyTuples(vtkAbstractArray, vtkAbstractArray, int, int, int)
        C++: void CopyTuples(vtkAbstractArray *fromData,
            vtkAbstractArray *toData, vtkIdType dstStart, vtkIdType n,
            vtkIdType srcStart)
        
        Copy a tuple (or set of tuples) of data from one data array to
        another. This method assumes that the fromData and toData objects
        are of the same type, and have the same number of components.
        This is true if you invoke CopyAllocate() or
        InterpolateAllocate().
        """
        ...
    
    def CopyVectorsOff(self):
        """
        V.CopyVectorsOff()
        C++: virtual void CopyVectorsOff()
        """
        ...
    
    def CopyVectorsOn(self):
        """
        V.CopyVectorsOn()
        C++: virtual void CopyVectorsOn()
        """
        ...
    
    def DeepCopy(self, vtkFieldData):
        """
        V.DeepCopy(vtkFieldData)
        C++: void DeepCopy(vtkFieldData *pd) override;
        
        Deep copy of data (i.e., create new data arrays and copy from
        input data). Ignores the copy flags but preserves them in the
        output.
        """
        ...
    
    def GetAbstractAttribute(self, p_int):
        """
        V.GetAbstractAttribute(int) -> vtkAbstractArray
        C++: vtkAbstractArray *GetAbstractAttribute(int attributeType)
        
        Return an attribute given the attribute type (see
        vtkDataSetAttributes::AttributeTypes). This is the same as
        GetAttribute(), except that the returned array is a
        vtkAbstractArray instead of vtkDataArray. Some attributes (such
        as PEDIGREEIDS) may not be vtkDataArray subclass.
        """
        ...
    
    def GetAttribute(self, p_int):
        """
        V.GetAttribute(int) -> vtkDataArray
        C++: vtkDataArray *GetAttribute(int attributeType)
        
        Return an attribute given the attribute type (see
        vtkDataSetAttributes::AttributeTypes). Some attributes (such as
        PEDIGREEIDS) may not be vtkDataArray subclass, so in that case
        use GetAbstractAttribute().
        """
        ...
    
    def GetAttributeIndices(self, *int):
        """
        V.GetAttributeIndices([int, ...])
        C++: void GetAttributeIndices(int *indexArray)
        
        Get the field data array indices corresponding to scalars,
        vectors, tensors, etc.
        """
        ...
    
    def GetAttributeTypeAsString(self, p_int):
        """
        V.GetAttributeTypeAsString(int) -> string
        C++: static const char *GetAttributeTypeAsString(
            int attributeType)
        
        Given an integer attribute type, this static method returns a
        string type for the attribute (i.e. type = 0: returns "Scalars").
        """
        ...
    
    def GetCopyAttribute(self, p_int, p_int_1):
        """
        V.GetCopyAttribute(int, int) -> int
        C++: int GetCopyAttribute(int index, int ctype)
        
        Get the attribute copy flag for copy operation of attribute .
        """
        ...
    
    def GetCopyGlobalIds(self, p_int):
        """
        V.GetCopyGlobalIds(int) -> int
        C++: vtkTypeBool GetCopyGlobalIds(int ctype=ALLCOPY)
        """
        ...
    
    def GetCopyHigherOrderDegrees(self, p_int):
        """
        V.GetCopyHigherOrderDegrees(int) -> int
        C++: vtkTypeBool GetCopyHigherOrderDegrees(int ctype=ALLCOPY)
        """
        ...
    
    def GetCopyNormals(self, p_int):
        """
        V.GetCopyNormals(int) -> int
        C++: vtkTypeBool GetCopyNormals(int ctype=ALLCOPY)
        """
        ...
    
    def GetCopyPedigreeIds(self, p_int):
        """
        V.GetCopyPedigreeIds(int) -> int
        C++: vtkTypeBool GetCopyPedigreeIds(int ctype=ALLCOPY)
        """
        ...
    
    def GetCopyRationalWeights(self, p_int):
        """
        V.GetCopyRationalWeights(int) -> int
        C++: vtkTypeBool GetCopyRationalWeights(int ctype=ALLCOPY)
        """
        ...
    
    def GetCopyScalars(self, p_int):
        """
        V.GetCopyScalars(int) -> int
        C++: vtkTypeBool GetCopyScalars(int ctype=ALLCOPY)
        """
        ...
    
    def GetCopyTangents(self, p_int):
        """
        V.GetCopyTangents(int) -> int
        C++: vtkTypeBool GetCopyTangents(int ctype=ALLCOPY)
        """
        ...
    
    def GetCopyTCoords(self, p_int):
        """
        V.GetCopyTCoords(int) -> int
        C++: vtkTypeBool GetCopyTCoords(int ctype=ALLCOPY)
        """
        ...
    
    def GetCopyTensors(self, p_int):
        """
        V.GetCopyTensors(int) -> int
        C++: vtkTypeBool GetCopyTensors(int ctype=ALLCOPY)
        """
        ...
    
    def GetCopyVectors(self, p_int):
        """
        V.GetCopyVectors(int) -> int
        C++: vtkTypeBool GetCopyVectors(int ctype=ALLCOPY)
        """
        ...
    
    def GetGlobalIds(self):
        """
        V.GetGlobalIds() -> vtkDataArray
        C++: vtkDataArray *GetGlobalIds()
        V.GetGlobalIds(string) -> vtkDataArray
        C++: vtkDataArray *GetGlobalIds(const char *name)
        
        Set/Get the global id data.
        """
        ...
    
    def GetHigherOrderDegrees(self):
        """
        V.GetHigherOrderDegrees() -> vtkDataArray
        C++: vtkDataArray *GetHigherOrderDegrees()
        V.GetHigherOrderDegrees(string) -> vtkDataArray
        C++: vtkDataArray *GetHigherOrderDegrees(const char *name)
        
        Set/Get the rational degrees data.
        """
        ...
    
    def GetLongAttributeTypeAsString(self, p_int):
        """
        V.GetLongAttributeTypeAsString(int) -> string
        C++: static const char *GetLongAttributeTypeAsString(
            int attributeType)
        
        Given an integer attribute type, this static method returns a
        string type for the attribute (i.e. type = 0: returns "Scalars").
        """
        ...
    
    def GetNormals(self):
        """
        V.GetNormals() -> vtkDataArray
        C++: vtkDataArray *GetNormals()
        V.GetNormals(string) -> vtkDataArray
        C++: vtkDataArray *GetNormals(const char *name)
        
        Set/get the normal data.
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
    
    def GetPedigreeIds(self):
        """
        V.GetPedigreeIds() -> vtkAbstractArray
        C++: vtkAbstractArray *GetPedigreeIds()
        V.GetPedigreeIds(string) -> vtkAbstractArray
        C++: vtkAbstractArray *GetPedigreeIds(const char *name)
        
        Set/Get the pedigree id data.
        """
        ...
    
    def GetRationalWeights(self):
        """
        V.GetRationalWeights() -> vtkDataArray
        C++: vtkDataArray *GetRationalWeights()
        V.GetRationalWeights(string) -> vtkDataArray
        C++: vtkDataArray *GetRationalWeights(const char *name)
        
        Set/Get the rational weights data.
        """
        ...
    
    def GetScalars(self):
        """
        V.GetScalars() -> vtkDataArray
        C++: vtkDataArray *GetScalars()
        V.GetScalars(string) -> vtkDataArray
        C++: vtkDataArray *GetScalars(const char *name)
        
        Set/Get the scalar data.
        """
        ...
    
    def GetTangents(self):
        """
        V.GetTangents() -> vtkDataArray
        C++: vtkDataArray *GetTangents()
        V.GetTangents(string) -> vtkDataArray
        C++: vtkDataArray *GetTangents(const char *name)
        
        Set/get the tangent data.
        """
        ...
    
    def GetTCoords(self):
        """
        V.GetTCoords() -> vtkDataArray
        C++: vtkDataArray *GetTCoords()
        V.GetTCoords(string) -> vtkDataArray
        C++: vtkDataArray *GetTCoords(const char *name)
        
        Set/Get the texture coordinate data.
        """
        ...
    
    def GetTensors(self):
        """
        V.GetTensors() -> vtkDataArray
        C++: vtkDataArray *GetTensors()
        V.GetTensors(string) -> vtkDataArray
        C++: vtkDataArray *GetTensors(const char *name)
        
        Set/Get the tensor data.
        """
        ...
    
    def GetVectors(self):
        """
        V.GetVectors() -> vtkDataArray
        C++: vtkDataArray *GetVectors()
        V.GetVectors(string) -> vtkDataArray
        C++: vtkDataArray *GetVectors(const char *name)
        
        Set/Get the vector data.
        """
        ...
    
    def GhostArrayName(self):
        """
        V.GhostArrayName() -> string
        C++: static const char *GhostArrayName()
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        Initialize all of the object's data to nullptr Also, clear the
        copy flags.
        """
        ...
    
    def InterpolateAllocate(self, vtkDataSetAttributes, p_int, p_int_1):
        """
        V.InterpolateAllocate(vtkDataSetAttributes, int, int)
        C++: void InterpolateAllocate(vtkDataSetAttributes *pd,
            vtkIdType sze=0, vtkIdType ext=1000)
        V.InterpolateAllocate(vtkDataSetAttributes, int, int, int)
        C++: void InterpolateAllocate(vtkDataSetAttributes *pd,
            vtkIdType sze, vtkIdType ext, int shallowCopyArrays)
        V.InterpolateAllocate(vtkDataSetAttributesFieldList, int, int)
        C++: void InterpolateAllocate(
            vtkDataSetAttributes::FieldList &list, vtkIdType sze=0,
            vtkIdType ext=1000)
        
        Initialize point interpolation method. Note that pd HAS to be the
        vtkDataSetAttributes object which will later be used with
        InterpolatePoint or InterpolateEdge. ext is no longer used. If
        shallowCopyArrays is true, input arrays are copied to the output
        instead of new ones being allocated.
        """
        ...
    
    def InterpolateEdge(self, vtkDataSetAttributes, p_int, p_int_1, p_int_2, p_float):
        """
        V.InterpolateEdge(vtkDataSetAttributes, int, int, int, float)
        C++: void InterpolateEdge(vtkDataSetAttributes *fromPd,
            vtkIdType toId, vtkIdType p1, vtkIdType p2, double t)
        
        Interpolate data from the two points p1,p2 (forming an edge) and
        an interpolation factor, t, along the edge. The weight ranges
        from (0,1), with t=0 located at p1. Make sure that the method
        InterpolateAllocate() has been invoked before using this method.
        If the INTERPOLATION copy flag is set to 0 for an array,
        interpolation is prevented. If the flag is set to 1, weighted
        interpolation occurs. If the flag is set to 2, nearest neighbor
        interpolation is used.
        """
        ...
    
    def InterpolatePoint(self, vtkDataSetAttributes, p_int, vtkIdList, *float):
        """
        V.InterpolatePoint(vtkDataSetAttributes, int, vtkIdList, [float,
            ...])
        C++: void InterpolatePoint(vtkDataSetAttributes *fromPd,
            vtkIdType toId, vtkIdList *ids, double *weights)
        V.InterpolatePoint(vtkDataSetAttributesFieldList,
            vtkDataSetAttributes, int, int, vtkIdList, [float, ...])
        C++: void InterpolatePoint(vtkDataSetAttributes::FieldList &list,
            vtkDataSetAttributes *fromPd, int idx, vtkIdType toId,
            vtkIdList *ids, double *weights)
        
        Interpolate data set attributes from other data set attributes
        given cell or point ids and associated interpolation weights. If
        the INTERPOLATION copy flag is set to 0 for an array,
        interpolation is prevented. If the flag is set to 1, weighted
        interpolation occurs. If the flag is set to 2, nearest neighbor
        interpolation is used.
        """
        ...
    
    def InterpolateTime(self, vtkDataSetAttributes, vtkDataSetAttributes_1, p_int, p_float):
        """
        V.InterpolateTime(vtkDataSetAttributes, vtkDataSetAttributes, int,
             float)
        C++: void InterpolateTime(vtkDataSetAttributes *from1,
            vtkDataSetAttributes *from2, vtkIdType id, double t)
        
        Interpolate data from the same id (point or cell) at different
        points in time (parameter t). Two input data set attributes
        objects are input. The parameter t lies between (0<=t<=1).
        IMPORTANT: it is assumed that the number of attributes and number
        of components is the same for both from1 and from2, and the type
        of data for from1 and from2 are the same. Make sure that the
        method InterpolateAllocate() has been invoked before using this
        method. If the INTERPOLATION copy flag is set to 0 for an array,
        interpolation is prevented. If the flag is set to 1, weighted
        interpolation occurs. If the flag is set to 2, nearest neighbor
        interpolation is used.
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
    
    def IsArrayAnAttribute(self, p_int):
        """
        V.IsArrayAnAttribute(int) -> int
        C++: int IsArrayAnAttribute(int idx)
        
        Determine whether a data array of index idx is considered a data
        set attribute (i.e., scalar, vector, tensor, etc). Return
        less-than zero if it is, otherwise an index 0<=idx<NUM_ATTRIBUTES
        to indicate which attribute.
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
        V.NewInstance() -> vtkDataSetAttributes
        C++: vtkDataSetAttributes *NewInstance()
        """
        ...
    
    def PassData(self, vtkFieldData):
        """
        V.PassData(vtkFieldData)
        C++: void PassData(vtkFieldData *fd) override;
        
        Pass entire arrays of input data through to output. Obey the
        "copy" flags. When passing a field,  the following copying rules
        are followed: 1) Check if a field is an attribute, if yes and if
        there is a PASSDATA copy flag for that attribute (on or off),
        obey the flag for that attribute, ignore (2) and (3), 2) if there
        is a copy field for that field (on or off), obey the flag, ignore
        (3) 3) obey CopyAllOn/Off
        """
        ...
    
    def RemoveArray(self, p_int):
        """
        V.RemoveArray(int)
        C++: void RemoveArray(int index) override;
        V.RemoveArray(string)
        C++: virtual void RemoveArray(const char *name)
        
        Remove an array (with the given name) from the list of arrays.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDataSetAttributes
        C++: static vtkDataSetAttributes *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetActiveAttribute(self, string, p_int):
        """
        V.SetActiveAttribute(string, int) -> int
        C++: int SetActiveAttribute(const char *name, int attributeType)
        V.SetActiveAttribute(int, int) -> int
        C++: int SetActiveAttribute(int index, int attributeType)
        
        Make the array with the given name the active attribute.
        Attribute types are: vtkDataSetAttributes::SCALARS = 0
        vtkDataSetAttributes::VECTORS = 1 vtkDataSetAttributes::NORMALS =
        2 vtkDataSetAttributes::TCOORDS = 3 vtkDataSetAttributes::TENSORS
        = 4 vtkDataSetAttributes::GLOBALIDS = 5
        vtkDataSetAttributes::PEDIGREEIDS = 6
        vtkDataSetAttributes::EDGEFLAG = 7 vtkDataSetAttributes::TANGENTS
        = 8 Returns the index of the array if successful, -1 if the array
        is not in the list of arrays.
        """
        ...
    
    def SetActiveGlobalIds(self, string):
        """
        V.SetActiveGlobalIds(string) -> int
        C++: int SetActiveGlobalIds(const char *name)
        
        Set/Get the global id data.
        """
        ...
    
    def SetActiveHigherOrderDegrees(self, string):
        """
        V.SetActiveHigherOrderDegrees(string) -> int
        C++: int SetActiveHigherOrderDegrees(const char *name)
        
        Set/Get the rational degrees data.
        """
        ...
    
    def SetActiveNormals(self, string):
        """
        V.SetActiveNormals(string) -> int
        C++: int SetActiveNormals(const char *name)
        
        Set/get the normal data.
        """
        ...
    
    def SetActivePedigreeIds(self, string):
        """
        V.SetActivePedigreeIds(string) -> int
        C++: int SetActivePedigreeIds(const char *name)
        
        Set/Get the pedigree id data.
        """
        ...
    
    def SetActiveRationalWeights(self, string):
        """
        V.SetActiveRationalWeights(string) -> int
        C++: int SetActiveRationalWeights(const char *name)
        
        Set/Get the rational weights data.
        """
        ...
    
    def SetActiveScalars(self, string):
        """
        V.SetActiveScalars(string) -> int
        C++: int SetActiveScalars(const char *name)
        
        Set/Get the scalar data.
        """
        ...
    
    def SetActiveTangents(self, string):
        """
        V.SetActiveTangents(string) -> int
        C++: int SetActiveTangents(const char *name)
        
        Set/get the tangent data.
        """
        ...
    
    def SetActiveTCoords(self, string):
        """
        V.SetActiveTCoords(string) -> int
        C++: int SetActiveTCoords(const char *name)
        
        Set/Get the texture coordinate data.
        """
        ...
    
    def SetActiveTensors(self, string):
        """
        V.SetActiveTensors(string) -> int
        C++: int SetActiveTensors(const char *name)
        
        Set/Get the tensor data.
        """
        ...
    
    def SetActiveVectors(self, string):
        """
        V.SetActiveVectors(string) -> int
        C++: int SetActiveVectors(const char *name)
        
        Set/Get the vector data.
        """
        ...
    
    def SetAttribute(self, vtkAbstractArray, p_int):
        """
        V.SetAttribute(vtkAbstractArray, int) -> int
        C++: int SetAttribute(vtkAbstractArray *aa, int attributeType)
        
        Set an array to use as the given attribute type (i.e.,
        vtkDataSetAttributes::SCALAR, vtkDataSetAttributes::VECTOR,
        vtkDataSetAttributes::TENSOR, etc.). If this attribute was
        previously set to another array, that array is removed from the
        vtkDataSetAttributes object and the array aa is used as the
        attribute.
        
        * Returns the index of aa within the vtkDataSetAttributes object
        * (i.e., the index to pass to the method GetArray(int) to obtain
        * aa) if the attribute was set to aa successfully. If aa was
        * already set as the given attributeType, returns the index of
        * aa.
        
        * Returns -1 in the following cases:
        
        * - aa is nullptr (used to unset an attribute; not an error
          indicator)
        * - aa is not a subclass of vtkDataArray, unless the
          attributeType
        * is vtkDataSetAttributes::PEDIGREEIDS (error indicator)
        * - aa has a number of components incompatible with the attribute
        type
        * (error indicator)
        """
        ...
    
    def SetCopyAttribute(self, p_int, p_int_1, p_int_2):
        """
        V.SetCopyAttribute(int, int, int)
        C++: void SetCopyAttribute(int index, int value,
            int ctype=ALLCOPY)
        
        Turn on/off the copying of attribute data. ctype is one of the
        AttributeCopyOperations, and controls copy, interpolate and
        passdata behavior. For set, ctype=ALLCOPY means set all three
        flags to the same value. For get, ctype=ALLCOPY returns true only
        if all three flags are true.
        
        * During copying, interpolation and passdata, the following rules
        are
        * followed for each array:
        * 1. If the copy/interpolate/pass flag for an attribute is set
          (on or off),
        * it is applied. This overrides rules 2 and 3.
        * 2. If the copy flag for an array is set (on or off), it is
          applied
        * This overrides rule 3.
        * 3. If CopyAllOn is set, copy the array.
        * If CopyAllOff is set, do not copy the array
        
        * For interpolation, the flag values can be as follows:
        * 0: Do not interpolate.
        * 1: Weighted interpolation.
        * 2: Nearest neighbor interpolation.
        """
        ...
    
    def SetCopyGlobalIds(self, p_int, p_int_1):
        """
        V.SetCopyGlobalIds(int, int)
        C++: void SetCopyGlobalIds(vtkTypeBool i, int ctype=ALLCOPY)
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def SetCopyHigherOrderDegrees(self, p_int, p_int_1):
        """
        V.SetCopyHigherOrderDegrees(int, int)
        C++: void SetCopyHigherOrderDegrees(vtkTypeBool i,
            int ctype=ALLCOPY)
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def SetCopyNormals(self, p_int, p_int_1):
        """
        V.SetCopyNormals(int, int)
        C++: void SetCopyNormals(vtkTypeBool i, int ctype=ALLCOPY)
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def SetCopyPedigreeIds(self, p_int, p_int_1):
        """
        V.SetCopyPedigreeIds(int, int)
        C++: void SetCopyPedigreeIds(vtkTypeBool i, int ctype=ALLCOPY)
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def SetCopyRationalWeights(self, p_int, p_int_1):
        """
        V.SetCopyRationalWeights(int, int)
        C++: void SetCopyRationalWeights(vtkTypeBool i, int ctype=ALLCOPY)
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def SetCopyScalars(self, p_int, p_int_1):
        """
        V.SetCopyScalars(int, int)
        C++: void SetCopyScalars(vtkTypeBool i, int ctype=ALLCOPY)
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def SetCopyTangents(self, p_int, p_int_1):
        """
        V.SetCopyTangents(int, int)
        C++: void SetCopyTangents(vtkTypeBool i, int ctype=ALLCOPY)
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def SetCopyTCoords(self, p_int, p_int_1):
        """
        V.SetCopyTCoords(int, int)
        C++: void SetCopyTCoords(vtkTypeBool i, int ctype=ALLCOPY)
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def SetCopyTensors(self, p_int, p_int_1):
        """
        V.SetCopyTensors(int, int)
        C++: void SetCopyTensors(vtkTypeBool i, int ctype=ALLCOPY)
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def SetCopyVectors(self, p_int, p_int_1):
        """
        V.SetCopyVectors(int, int)
        C++: void SetCopyVectors(vtkTypeBool i, int ctype=ALLCOPY)
        
        @copydoc vtkDataSetAttributes::SetCopyAttribute()
        """
        ...
    
    def SetGlobalIds(self, vtkDataArray):
        """
        V.SetGlobalIds(vtkDataArray) -> int
        C++: int SetGlobalIds(vtkDataArray *da)
        
        Set/Get the global id data.
        """
        ...
    
    def SetHigherOrderDegrees(self, vtkDataArray):
        """
        V.SetHigherOrderDegrees(vtkDataArray) -> int
        C++: int SetHigherOrderDegrees(vtkDataArray *da)
        
        Set/Get the rational degrees data.
        """
        ...
    
    def SetNormals(self, vtkDataArray):
        """
        V.SetNormals(vtkDataArray) -> int
        C++: int SetNormals(vtkDataArray *da)
        
        Set/get the normal data.
        """
        ...
    
    def SetPedigreeIds(self, vtkAbstractArray):
        """
        V.SetPedigreeIds(vtkAbstractArray) -> int
        C++: int SetPedigreeIds(vtkAbstractArray *da)
        
        Set/Get the pedigree id data.
        """
        ...
    
    def SetRationalWeights(self, vtkDataArray):
        """
        V.SetRationalWeights(vtkDataArray) -> int
        C++: int SetRationalWeights(vtkDataArray *da)
        
        Set/Get the rational weights data.
        """
        ...
    
    def SetScalars(self, vtkDataArray):
        """
        V.SetScalars(vtkDataArray) -> int
        C++: int SetScalars(vtkDataArray *da)
        
        Set/Get the scalar data.
        """
        ...
    
    def SetTangents(self, vtkDataArray):
        """
        V.SetTangents(vtkDataArray) -> int
        C++: int SetTangents(vtkDataArray *da)
        
        Set/get the tangent data.
        """
        ...
    
    def SetTCoords(self, vtkDataArray):
        """
        V.SetTCoords(vtkDataArray) -> int
        C++: int SetTCoords(vtkDataArray *da)
        
        Set/Get the texture coordinate data.
        """
        ...
    
    def SetTensors(self, vtkDataArray):
        """
        V.SetTensors(vtkDataArray) -> int
        C++: int SetTensors(vtkDataArray *da)
        
        Set/Get the tensor data.
        """
        ...
    
    def SetupForCopy(self, vtkDataSetAttributes):
        """
        V.SetupForCopy(vtkDataSetAttributes)
        C++: void SetupForCopy(vtkDataSetAttributes *pd)
        
        Create a mapping between the input attributes and this object so
        that methods like CopyData() and CopyStructuredData() can be
        called. This method assumes that this object has the same arrays
        as the input and that they are ordered the same way (same array
        indices).
        """
        ...
    
    def SetVectors(self, vtkDataArray):
        """
        V.SetVectors(vtkDataArray) -> int
        C++: int SetVectors(vtkDataArray *da)
        
        Set/Get the vector data.
        """
        ...
    
    def ShallowCopy(self, vtkFieldData):
        """
        V.ShallowCopy(vtkFieldData)
        C++: void ShallowCopy(vtkFieldData *pd) override;
        
        Shallow copy of data (i.e., use reference counting). Ignores the
        copy flags but preserves them in the output.
        """
        ...
    
    def Update(self):
        """
        V.Update()
        C++: virtual void Update()
        
        Attributes have a chance to bring themselves up to date; right
        now this is ignored.
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
    ALLCOPY = ...
    AttributeCopyOperations = ...
    AttributeLimitTypes = ...
    AttributeTypes = ...
    CellGhostTypes = ...
    COPYTUPLE = ...
    DUPLICATECELL = ...
    DUPLICATEPOINT = ...
    EDGEFLAG = ...
    EXACT = ...
    EXTERIORCELL = ...
    GLOBALIDS = ...
    HIDDENCELL = ...
    HIDDENPOINT = ...
    HIGHCONNECTIVITYCELL = ...
    HIGHERORDERDEGREES = ...
    INTERPOLATE = ...
    LOWCONNECTIVITYCELL = ...
    MAX = ...
    NOLIMIT = ...
    NORMALS = ...
    NUM_ATTRIBUTES = ...
    PASSDATA = ...
    PEDIGREEIDS = ...
    PointGhostTypes = ...
    RATIONALWEIGHTS = ...
    REFINEDCELL = ...
    SCALARS = ...
    TANGENTS = ...
    TCOORDS = ...
    TENSORS = ...
    VECTORS = ...
    __dict__ = ...
    __vtkname__ = ...


