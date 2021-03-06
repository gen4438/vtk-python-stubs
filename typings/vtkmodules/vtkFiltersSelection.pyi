"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkCellDistanceSelector(__vtkmodules_vtkCommonExecutionModel.vtkSelectionAlgorithm):
    """
    vtkCellDistanceSelector - select neighbor cells up to a distance
    
    Superclass: vtkSelectionAlgorithm
    
    This filter grows an input selection by iteratively selecting
    neighbor cells (a neighbor cell is a cell that shares a
    vertex/edge/face), up to a given topological distance to the selected
    neighborhood (number of times we add neighbor cells). This filter
    takes a vtkSelection and a vtkCompositeDataSet as inputs. It outputs
    a vtkSelection identifying all the selected cells.
    
    @par Thanks: This file has been initially developed in the frame of
    CEA's Love visualization software development
    
    CEA/DIF - Commissariat a l'Energie Atomique, Centre DAM Ile-De-France
    
    BP12, F-91297 Arpajon, France.
    
    Modified and integrated into VTK, Kitware SAS 2012 Implementation by
    Thierry Carrard and Philippe Pebay
    """
    def AddIntermediateOff(self):
        """
        V.AddIntermediateOff()
        C++: virtual void AddIntermediateOff()
        
        If set, intermediate cells (between seed cells and the selection
        boundary) will be included in the final selection
        """
        ...
    
    def AddIntermediateOn(self):
        """
        V.AddIntermediateOn()
        C++: virtual void AddIntermediateOn()
        
        If set, intermediate cells (between seed cells and the selection
        boundary) will be included in the final selection
        """
        ...
    
    def GetAddIntermediate(self):
        """
        V.GetAddIntermediate() -> int
        C++: virtual vtkTypeBool GetAddIntermediate()
        
        If set, intermediate cells (between seed cells and the selection
        boundary) will be included in the final selection
        """
        ...
    
    def GetDistance(self):
        """
        V.GetDistance() -> int
        C++: virtual int GetDistance()
        
        Tells how far (in term of topological distance) away from seed
        cells to expand the selection
        """
        ...
    
    def GetIncludeSeed(self):
        """
        V.GetIncludeSeed() -> int
        C++: virtual vtkTypeBool GetIncludeSeed()
        
        If set, seed cells passed with SetSeedCells will be included in
        the final selection
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
    
    def IncludeSeedOff(self):
        """
        V.IncludeSeedOff()
        C++: virtual void IncludeSeedOff()
        
        If set, seed cells passed with SetSeedCells will be included in
        the final selection
        """
        ...
    
    def IncludeSeedOn(self):
        """
        V.IncludeSeedOn()
        C++: virtual void IncludeSeedOn()
        
        If set, seed cells passed with SetSeedCells will be included in
        the final selection
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
        V.NewInstance() -> vtkCellDistanceSelector
        C++: vtkCellDistanceSelector *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCellDistanceSelector
        C++: static vtkCellDistanceSelector *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetAddIntermediate(self, p_int):
        """
        V.SetAddIntermediate(int)
        C++: virtual void SetAddIntermediate(vtkTypeBool _arg)
        
        If set, intermediate cells (between seed cells and the selection
        boundary) will be included in the final selection
        """
        ...
    
    def SetDistance(self, p_int):
        """
        V.SetDistance(int)
        C++: virtual void SetDistance(int _arg)
        
        Tells how far (in term of topological distance) away from seed
        cells to expand the selection
        """
        ...
    
    def SetIncludeSeed(self, p_int):
        """
        V.SetIncludeSeed(int)
        C++: virtual void SetIncludeSeed(vtkTypeBool _arg)
        
        If set, seed cells passed with SetSeedCells will be included in
        the final selection
        """
        ...
    
    def SetInputMesh(self, vtkDataObject):
        """
        V.SetInputMesh(vtkDataObject)
        C++: void SetInputMesh(vtkDataObject *obj)
        
        A convenience method to set the input data object
        """
        ...
    
    def SetInputMeshConnection(self, vtkAlgorithmOutput):
        """
        V.SetInputMeshConnection(vtkAlgorithmOutput)
        C++: void SetInputMeshConnection(vtkAlgorithmOutput *in)
        
        A convenience method to set the data object input connection to
        the producer output
        """
        ...
    
    def SetInputSelection(self, vtkSelection):
        """
        V.SetInputSelection(vtkSelection)
        C++: void SetInputSelection(vtkSelection *obj)
        
        A convenience method to set the input selection
        """
        ...
    
    def SetInputSelectionConnection(self, vtkAlgorithmOutput):
        """
        V.SetInputSelectionConnection(vtkAlgorithmOutput)
        C++: void SetInputSelectionConnection(vtkAlgorithmOutput *in)
        
        A convenience method to set the selection input connection to the
        producer output
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
    InputPorts = ...
    INPUT_MESH = ...
    INPUT_SELECTION = ...
    __dict__ = ...
    __vtkname__ = ...


class vtkKdTreeSelector(__vtkmodules_vtkCommonExecutionModel.vtkSelectionAlgorithm):
    """
    vtkKdTreeSelector - Selects point ids using a kd-tree.
    
    Superclass: vtkSelectionAlgorithm
    
    If SetKdTree is used, the filter ignores the input and selects based
    on that kd-tree.  If SetKdTree is not used, the filter builds a
    kd-tree using the input point set and uses that tree for selection. 
    The output is a vtkSelection containing the ids found in the kd-tree
    using the specified bounds.
    """
    def GetKdTree(self):
        """
        V.GetKdTree() -> vtkKdTree
        C++: virtual vtkKdTree *GetKdTree()
        
        The kd-tree to use to find selected ids. The kd-tree must be
        initialized with the desired set of points. When this is set, the
        optional input is ignored.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Return this object's modified time.
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
    
    def GetSelectionAttribute(self):
        """
        V.GetSelectionAttribute() -> int
        C++: virtual int GetSelectionAttribute()
        
        The field attribute to use when generating the selection. If set,
        creates a PEDIGREEIDS or GLOBALIDS selection. If not set (or is
        set to -1), creates a INDICES selection. By default this is not
        set. NOTE: This should be set a constant in vtkDataSetAttributes,
        not vtkSelection.
        """
        ...
    
    def GetSelectionBounds(self):
        """
        V.GetSelectionBounds() -> (float, float, float, float, float,
            float)
        C++: virtual double *GetSelectionBounds()
        
        The bounds of the form (xmin,xmax,ymin,ymax,zmin,zmax). To
        perform a search in 2D, use the bounds
        (xmin,xmax,ymin,ymax,VTK_DOUBLE_MIN,VTK_DOUBLE_MAX).
        """
        ...
    
    def GetSelectionFieldName(self):
        """
        V.GetSelectionFieldName() -> string
        C++: virtual char *GetSelectionFieldName()
        
        The field name to use when generating the selection. If set,
        creates a VALUES selection. If not set (or is set to nullptr),
        creates a INDICES selection. By default this is not set.
        """
        ...
    
    def GetSingleSelection(self):
        """
        V.GetSingleSelection() -> bool
        C++: virtual bool GetSingleSelection()
        
        Whether to only allow up to one value in the result. The item
        selected is closest to the center of the bounds, if there are any
        points within the selection threshold. Default is off.
        """
        ...
    
    def GetSingleSelectionThreshold(self):
        """
        V.GetSingleSelectionThreshold() -> float
        C++: virtual double GetSingleSelectionThreshold()
        
        The threshold for the single selection. A single point is added
        to the selection if it is within this threshold from the bounds
        center. Default is 1.
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
        V.NewInstance() -> vtkKdTreeSelector
        C++: vtkKdTreeSelector *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkKdTreeSelector
        C++: static vtkKdTreeSelector *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetKdTree(self, vtkKdTree):
        """
        V.SetKdTree(vtkKdTree)
        C++: void SetKdTree(vtkKdTree *tree)
        
        The kd-tree to use to find selected ids. The kd-tree must be
        initialized with the desired set of points. When this is set, the
        optional input is ignored.
        """
        ...
    
    def SetSelectionAttribute(self, p_int):
        """
        V.SetSelectionAttribute(int)
        C++: virtual void SetSelectionAttribute(int _arg)
        
        The field attribute to use when generating the selection. If set,
        creates a PEDIGREEIDS or GLOBALIDS selection. If not set (or is
        set to -1), creates a INDICES selection. By default this is not
        set. NOTE: This should be set a constant in vtkDataSetAttributes,
        not vtkSelection.
        """
        ...
    
    def SetSelectionBounds(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5):
        """
        V.SetSelectionBounds(float, float, float, float, float, float)
        C++: virtual void SetSelectionBounds(double _arg1, double _arg2,
            double _arg3, double _arg4, double _arg5, double _arg6)
        V.SetSelectionBounds((float, float, float, float, float, float))
        C++: virtual void SetSelectionBounds(const double _arg[6])
        
        The bounds of the form (xmin,xmax,ymin,ymax,zmin,zmax). To
        perform a search in 2D, use the bounds
        (xmin,xmax,ymin,ymax,VTK_DOUBLE_MIN,VTK_DOUBLE_MAX).
        """
        ...
    
    def SetSelectionFieldName(self, string):
        """
        V.SetSelectionFieldName(string)
        C++: virtual void SetSelectionFieldName(const char *_arg)
        
        The field name to use when generating the selection. If set,
        creates a VALUES selection. If not set (or is set to nullptr),
        creates a INDICES selection. By default this is not set.
        """
        ...
    
    def SetSingleSelection(self, bool):
        """
        V.SetSingleSelection(bool)
        C++: virtual void SetSingleSelection(bool _arg)
        
        Whether to only allow up to one value in the result. The item
        selected is closest to the center of the bounds, if there are any
        points within the selection threshold. Default is off.
        """
        ...
    
    def SetSingleSelectionThreshold(self, p_float):
        """
        V.SetSingleSelectionThreshold(float)
        C++: virtual void SetSingleSelectionThreshold(double _arg)
        
        The threshold for the single selection. A single point is added
        to the selection if it is within this threshold from the bounds
        center. Default is 1.
        """
        ...
    
    def SingleSelectionOff(self):
        """
        V.SingleSelectionOff()
        C++: virtual void SingleSelectionOff()
        
        Whether to only allow up to one value in the result. The item
        selected is closest to the center of the bounds, if there are any
        points within the selection threshold. Default is off.
        """
        ...
    
    def SingleSelectionOn(self):
        """
        V.SingleSelectionOn()
        C++: virtual void SingleSelectionOn()
        
        Whether to only allow up to one value in the result. The item
        selected is closest to the center of the bounds, if there are any
        points within the selection threshold. Default is off.
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


class vtkLinearSelector(__vtkmodules_vtkCommonExecutionModel.vtkSelectionAlgorithm):
    """
    vtkLinearSelector - select cells intersecting a line (possibly broken)
    
    Superclass: vtkSelectionAlgorithm
    
    This filter takes a vtkCompositeDataSet as input and a line segment
    as parameter. It outputs a vtkSelection identifying all the cells
    intersecting the given line segment.
    
    @par Thanks: This class has been initially developed in the frame of
    CEA's Love visualization software development
    
    CEA/DIF - Commissariat a l'Energie Atomique, Centre DAM Ile-De-France
    
    BP12, F-91297 Arpajon, France.
    
    Modified and integrated into VTK, Kitware SAS 2012 This class was
    implemented by Thierry Carrard, Charles Pignerol, and Philippe Pebay.
    """
    def GetEndPoint(self):
        """
        V.GetEndPoint() -> (float, float, float)
        C++: virtual double *GetEndPoint()
        
        Set/Get end point of intersecting segment
        """
        ...
    
    def GetIncludeVertices(self):
        """
        V.GetIncludeVertices() -> bool
        C++: virtual bool GetIncludeVertices()
        
        Set/Get whether lines vertice are included in selection
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
    
    def GetPoints(self):
        """
        V.GetPoints() -> vtkPoints
        C++: virtual vtkPoints *GetPoints()
        
        Set/Get the list of points defining the intersecting broken line
        """
        ...
    
    def GetStartPoint(self):
        """
        V.GetStartPoint() -> (float, float, float)
        C++: virtual double *GetStartPoint()
        
        Set/Get starting point of intersecting segment
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> float
        C++: virtual double GetTolerance()
        
        Set/Get tolerance to be used by intersection algorithm
        """
        ...
    
    def GetVertexEliminationTolerance(self):
        """
        V.GetVertexEliminationTolerance() -> float
        C++: virtual double GetVertexEliminationTolerance()
        
        Set/Get relative tolerance for vertex elimination
        """
        ...
    
    def GetVertexEliminationToleranceMaxValue(self):
        """
        V.GetVertexEliminationToleranceMaxValue() -> float
        C++: virtual double GetVertexEliminationToleranceMaxValue()
        
        Set/Get relative tolerance for vertex elimination
        """
        ...
    
    def GetVertexEliminationToleranceMinValue(self):
        """
        V.GetVertexEliminationToleranceMinValue() -> float
        C++: virtual double GetVertexEliminationToleranceMinValue()
        
        Set/Get relative tolerance for vertex elimination
        """
        ...
    
    def IncludeVerticesOff(self):
        """
        V.IncludeVerticesOff()
        C++: virtual void IncludeVerticesOff()
        
        Set/Get whether lines vertice are included in selection
        """
        ...
    
    def IncludeVerticesOn(self):
        """
        V.IncludeVerticesOn()
        C++: virtual void IncludeVerticesOn()
        
        Set/Get whether lines vertice are included in selection
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
        V.NewInstance() -> vtkLinearSelector
        C++: vtkLinearSelector *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkLinearSelector
        C++: static vtkLinearSelector *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetEndPoint(self, p_float, p_float_1, p_float_2):
        """
        V.SetEndPoint(float, float, float)
        C++: virtual void SetEndPoint(double _arg1, double _arg2,
            double _arg3)
        V.SetEndPoint((float, float, float))
        C++: virtual void SetEndPoint(const double _arg[3])
        
        Set/Get end point of intersecting segment
        """
        ...
    
    def SetIncludeVertices(self, bool):
        """
        V.SetIncludeVertices(bool)
        C++: virtual void SetIncludeVertices(bool _arg)
        
        Set/Get whether lines vertice are included in selection
        """
        ...
    
    def SetPoints(self, vtkPoints):
        """
        V.SetPoints(vtkPoints)
        C++: virtual void SetPoints(vtkPoints *)
        
        Set/Get the list of points defining the intersecting broken line
        """
        ...
    
    def SetStartPoint(self, p_float, p_float_1, p_float_2):
        """
        V.SetStartPoint(float, float, float)
        C++: virtual void SetStartPoint(double _arg1, double _arg2,
            double _arg3)
        V.SetStartPoint((float, float, float))
        C++: virtual void SetStartPoint(const double _arg[3])
        
        Set/Get starting point of intersecting segment
        """
        ...
    
    def SetTolerance(self, p_float):
        """
        V.SetTolerance(float)
        C++: virtual void SetTolerance(double _arg)
        
        Set/Get tolerance to be used by intersection algorithm
        """
        ...
    
    def SetVertexEliminationTolerance(self, p_float):
        """
        V.SetVertexEliminationTolerance(float)
        C++: virtual void SetVertexEliminationTolerance(double _arg)
        
        Set/Get relative tolerance for vertex elimination
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


__loader__ = ...
__spec__ = ...
