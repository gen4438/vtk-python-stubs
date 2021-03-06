"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkMergeGraphs(__vtkmodules_vtkCommonExecutionModel.vtkGraphAlgorithm):
    """
    vtkMergeGraphs - combines two graphs
    
    Superclass: vtkGraphAlgorithm
    
    vtkMergeGraphs combines information from two graphs into one. Both
    graphs must have pedigree ids assigned to the vertices. The output
    will contain the vertices/edges in the first graph, in addition to:
    
    - vertices in the second graph whose pedigree id does not match a
      vertex in the first input
    
    - edges in the second graph
    
    The output will contain the same attribute structure as the input;
    fields associated only with the second input graph will not be passed
    to the output. When possible, the vertex/edge data for new vertices
    and edges will be populated with matching attributes on the second
    graph. To be considered a matching attribute, the array must have the
    same name, type, and number of components.
    
    @warning
    This filter is not "domain-aware". Pedigree ids are assumed to be
    globally unique, regardless of their domain.
    """
    def ExtendGraph(self, vtkMutableGraphHelper, vtkGraph):
        """
        V.ExtendGraph(vtkMutableGraphHelper, vtkGraph) -> int
        C++: int ExtendGraph(vtkMutableGraphHelper *g1, vtkGraph *g2)
        
        This is the core functionality of the algorithm. Adds edges and
        vertices from g2 into g1.
        """
        ...
    
    def GetEdgeWindow(self):
        """
        V.GetEdgeWindow() -> float
        C++: virtual double GetEdgeWindow()
        
        The time window amount. Edges with values lower than the maximum
        value minus this window will be removed from the graph. The
        default edge window is 10000.
        """
        ...
    
    def GetEdgeWindowArrayName(self):
        """
        V.GetEdgeWindowArrayName() -> string
        C++: virtual char *GetEdgeWindowArrayName()
        
        The edge window array. The default array name is "time".
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
    
    def GetUseEdgeWindow(self):
        """
        V.GetUseEdgeWindow() -> bool
        C++: virtual bool GetUseEdgeWindow()
        
        Whether to use an edge window array. The default is to not use a
        window array.
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
        V.NewInstance() -> vtkMergeGraphs
        C++: vtkMergeGraphs *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkMergeGraphs
        C++: static vtkMergeGraphs *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetEdgeWindow(self, p_float):
        """
        V.SetEdgeWindow(float)
        C++: virtual void SetEdgeWindow(double _arg)
        
        The time window amount. Edges with values lower than the maximum
        value minus this window will be removed from the graph. The
        default edge window is 10000.
        """
        ...
    
    def SetEdgeWindowArrayName(self, string):
        """
        V.SetEdgeWindowArrayName(string)
        C++: virtual void SetEdgeWindowArrayName(const char *_arg)
        
        The edge window array. The default array name is "time".
        """
        ...
    
    def SetUseEdgeWindow(self, bool):
        """
        V.SetUseEdgeWindow(bool)
        C++: virtual void SetUseEdgeWindow(bool _arg)
        
        Whether to use an edge window array. The default is to not use a
        window array.
        """
        ...
    
    def UseEdgeWindowOff(self):
        """
        V.UseEdgeWindowOff()
        C++: virtual void UseEdgeWindowOff()
        
        Whether to use an edge window array. The default is to not use a
        window array.
        """
        ...
    
    def UseEdgeWindowOn(self):
        """
        V.UseEdgeWindowOn()
        C++: virtual void UseEdgeWindowOn()
        
        Whether to use an edge window array. The default is to not use a
        window array.
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


