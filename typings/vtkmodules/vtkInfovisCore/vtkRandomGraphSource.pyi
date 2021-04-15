"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkRandomGraphSource(__vtkmodules_vtkCommonExecutionModel.vtkGraphAlgorithm):
    """
    vtkRandomGraphSource - a graph with random edges
    
    Superclass: vtkGraphAlgorithm
    
    Generates a graph with a specified number of vertices, with the
    density of edges specified by either an exact number of edges or the
    probability of an edge.  You may additionally specify whether to
    begin with a random tree (which enforces graph connectivity).
    """
    def AllowParallelEdgesOff(self):
        """
        V.AllowParallelEdgesOff()
        C++: virtual void AllowParallelEdgesOff()
        
        When set, multiple edges from a source to a target vertex are
        allowed. The default is to forbid such loops.
        """
        ...
    
    def AllowParallelEdgesOn(self):
        """
        V.AllowParallelEdgesOn()
        C++: virtual void AllowParallelEdgesOn()
        
        When set, multiple edges from a source to a target vertex are
        allowed. The default is to forbid such loops.
        """
        ...
    
    def AllowSelfLoopsOff(self):
        """
        V.AllowSelfLoopsOff()
        C++: virtual void AllowSelfLoopsOff()
        
        If this flag is set to true, edges where the source and target
        vertex are the same can be generated.  The default is to forbid
        such loops.
        """
        ...
    
    def AllowSelfLoopsOn(self):
        """
        V.AllowSelfLoopsOn()
        C++: virtual void AllowSelfLoopsOn()
        
        If this flag is set to true, edges where the source and target
        vertex are the same can be generated.  The default is to forbid
        such loops.
        """
        ...
    
    def DirectedOff(self):
        """
        V.DirectedOff()
        C++: virtual void DirectedOff()
        
        When set, creates a directed graph, as opposed to an undirected
        graph.
        """
        ...
    
    def DirectedOn(self):
        """
        V.DirectedOn()
        C++: virtual void DirectedOn()
        
        When set, creates a directed graph, as opposed to an undirected
        graph.
        """
        ...
    
    def GeneratePedigreeIdsOff(self):
        """
        V.GeneratePedigreeIdsOff()
        C++: virtual void GeneratePedigreeIdsOff()
        
        Add pedigree ids to vertex and edge data.
        """
        ...
    
    def GeneratePedigreeIdsOn(self):
        """
        V.GeneratePedigreeIdsOn()
        C++: virtual void GeneratePedigreeIdsOn()
        
        Add pedigree ids to vertex and edge data.
        """
        ...
    
    def GetAllowParallelEdges(self):
        """
        V.GetAllowParallelEdges() -> bool
        C++: virtual bool GetAllowParallelEdges()
        
        When set, multiple edges from a source to a target vertex are
        allowed. The default is to forbid such loops.
        """
        ...
    
    def GetAllowSelfLoops(self):
        """
        V.GetAllowSelfLoops() -> bool
        C++: virtual bool GetAllowSelfLoops()
        
        If this flag is set to true, edges where the source and target
        vertex are the same can be generated.  The default is to forbid
        such loops.
        """
        ...
    
    def GetDirected(self):
        """
        V.GetDirected() -> bool
        C++: virtual bool GetDirected()
        
        When set, creates a directed graph, as opposed to an undirected
        graph.
        """
        ...
    
    def GetEdgePedigreeIdArrayName(self):
        """
        V.GetEdgePedigreeIdArrayName() -> string
        C++: virtual char *GetEdgePedigreeIdArrayName()
        
        The name of the edge pedigree id array. Default "edge id".
        """
        ...
    
    def GetEdgeProbability(self):
        """
        V.GetEdgeProbability() -> float
        C++: virtual double GetEdgeProbability()
        
        If UseEdgeProbability is on, adds an edge with this probability
        between 0 and 1 for each pair of vertices in the graph.
        """
        ...
    
    def GetEdgeProbabilityMaxValue(self):
        """
        V.GetEdgeProbabilityMaxValue() -> float
        C++: virtual double GetEdgeProbabilityMaxValue()
        
        If UseEdgeProbability is on, adds an edge with this probability
        between 0 and 1 for each pair of vertices in the graph.
        """
        ...
    
    def GetEdgeProbabilityMinValue(self):
        """
        V.GetEdgeProbabilityMinValue() -> float
        C++: virtual double GetEdgeProbabilityMinValue()
        
        If UseEdgeProbability is on, adds an edge with this probability
        between 0 and 1 for each pair of vertices in the graph.
        """
        ...
    
    def GetEdgeWeightArrayName(self):
        """
        V.GetEdgeWeightArrayName() -> string
        C++: virtual char *GetEdgeWeightArrayName()
        
        The name of the edge weight array. Default "edge weight".
        """
        ...
    
    def GetGeneratePedigreeIds(self):
        """
        V.GetGeneratePedigreeIds() -> bool
        C++: virtual bool GetGeneratePedigreeIds()
        
        Add pedigree ids to vertex and edge data.
        """
        ...
    
    def GetIncludeEdgeWeights(self):
        """
        V.GetIncludeEdgeWeights() -> bool
        C++: virtual bool GetIncludeEdgeWeights()
        
        When set, includes edge weights in an array named "edge_weights".
        Defaults to off.  Weights are random between 0 and 1.
        """
        ...
    
    def GetNumberOfEdges(self):
        """
        V.GetNumberOfEdges() -> int
        C++: virtual int GetNumberOfEdges()
        
        If UseEdgeProbability is off, creates a graph with the specified
        number of edges.  Duplicate (parallel) edges are allowed.
        """
        ...
    
    def GetNumberOfEdgesMaxValue(self):
        """
        V.GetNumberOfEdgesMaxValue() -> int
        C++: virtual int GetNumberOfEdgesMaxValue()
        
        If UseEdgeProbability is off, creates a graph with the specified
        number of edges.  Duplicate (parallel) edges are allowed.
        """
        ...
    
    def GetNumberOfEdgesMinValue(self):
        """
        V.GetNumberOfEdgesMinValue() -> int
        C++: virtual int GetNumberOfEdgesMinValue()
        
        If UseEdgeProbability is off, creates a graph with the specified
        number of edges.  Duplicate (parallel) edges are allowed.
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
    
    def GetNumberOfVertices(self):
        """
        V.GetNumberOfVertices() -> int
        C++: virtual int GetNumberOfVertices()
        
        The number of vertices in the graph.
        """
        ...
    
    def GetNumberOfVerticesMaxValue(self):
        """
        V.GetNumberOfVerticesMaxValue() -> int
        C++: virtual int GetNumberOfVerticesMaxValue()
        
        The number of vertices in the graph.
        """
        ...
    
    def GetNumberOfVerticesMinValue(self):
        """
        V.GetNumberOfVerticesMinValue() -> int
        C++: virtual int GetNumberOfVerticesMinValue()
        
        The number of vertices in the graph.
        """
        ...
    
    def GetSeed(self):
        """
        V.GetSeed() -> int
        C++: virtual int GetSeed()
        
        Control the seed used for pseudo-random-number generation. This
        ensures that vtkRandomGraphSource can produce repeatable results.
        """
        ...
    
    def GetStartWithTree(self):
        """
        V.GetStartWithTree() -> bool
        C++: virtual bool GetStartWithTree()
        
        When set, builds a random tree structure first, then adds
        additional random edges.
        """
        ...
    
    def GetUseEdgeProbability(self):
        """
        V.GetUseEdgeProbability() -> bool
        C++: virtual bool GetUseEdgeProbability()
        
        When set, uses the EdgeProbability parameter to determine the
        density of edges.  Otherwise, NumberOfEdges is used.
        """
        ...
    
    def GetVertexPedigreeIdArrayName(self):
        """
        V.GetVertexPedigreeIdArrayName() -> string
        C++: virtual char *GetVertexPedigreeIdArrayName()
        
        The name of the vertex pedigree id array. Default "vertex id".
        """
        ...
    
    def IncludeEdgeWeightsOff(self):
        """
        V.IncludeEdgeWeightsOff()
        C++: virtual void IncludeEdgeWeightsOff()
        
        When set, includes edge weights in an array named "edge_weights".
        Defaults to off.  Weights are random between 0 and 1.
        """
        ...
    
    def IncludeEdgeWeightsOn(self):
        """
        V.IncludeEdgeWeightsOn()
        C++: virtual void IncludeEdgeWeightsOn()
        
        When set, includes edge weights in an array named "edge_weights".
        Defaults to off.  Weights are random between 0 and 1.
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
        V.NewInstance() -> vtkRandomGraphSource
        C++: vtkRandomGraphSource *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkRandomGraphSource
        C++: static vtkRandomGraphSource *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAllowParallelEdges(self, bool):
        """
        V.SetAllowParallelEdges(bool)
        C++: virtual void SetAllowParallelEdges(bool _arg)
        
        When set, multiple edges from a source to a target vertex are
        allowed. The default is to forbid such loops.
        """
        ...
    
    def SetAllowSelfLoops(self, bool):
        """
        V.SetAllowSelfLoops(bool)
        C++: virtual void SetAllowSelfLoops(bool _arg)
        
        If this flag is set to true, edges where the source and target
        vertex are the same can be generated.  The default is to forbid
        such loops.
        """
        ...
    
    def SetDirected(self, bool):
        """
        V.SetDirected(bool)
        C++: virtual void SetDirected(bool _arg)
        
        When set, creates a directed graph, as opposed to an undirected
        graph.
        """
        ...
    
    def SetEdgePedigreeIdArrayName(self, string):
        """
        V.SetEdgePedigreeIdArrayName(string)
        C++: virtual void SetEdgePedigreeIdArrayName(const char *_arg)
        
        The name of the edge pedigree id array. Default "edge id".
        """
        ...
    
    def SetEdgeProbability(self, p_float):
        """
        V.SetEdgeProbability(float)
        C++: virtual void SetEdgeProbability(double _arg)
        
        If UseEdgeProbability is on, adds an edge with this probability
        between 0 and 1 for each pair of vertices in the graph.
        """
        ...
    
    def SetEdgeWeightArrayName(self, string):
        """
        V.SetEdgeWeightArrayName(string)
        C++: virtual void SetEdgeWeightArrayName(const char *_arg)
        
        The name of the edge weight array. Default "edge weight".
        """
        ...
    
    def SetGeneratePedigreeIds(self, bool):
        """
        V.SetGeneratePedigreeIds(bool)
        C++: virtual void SetGeneratePedigreeIds(bool _arg)
        
        Add pedigree ids to vertex and edge data.
        """
        ...
    
    def SetIncludeEdgeWeights(self, bool):
        """
        V.SetIncludeEdgeWeights(bool)
        C++: virtual void SetIncludeEdgeWeights(bool _arg)
        
        When set, includes edge weights in an array named "edge_weights".
        Defaults to off.  Weights are random between 0 and 1.
        """
        ...
    
    def SetNumberOfEdges(self, p_int):
        """
        V.SetNumberOfEdges(int)
        C++: virtual void SetNumberOfEdges(int _arg)
        
        If UseEdgeProbability is off, creates a graph with the specified
        number of edges.  Duplicate (parallel) edges are allowed.
        """
        ...
    
    def SetNumberOfVertices(self, p_int):
        """
        V.SetNumberOfVertices(int)
        C++: virtual void SetNumberOfVertices(int _arg)
        
        The number of vertices in the graph.
        """
        ...
    
    def SetSeed(self, p_int):
        """
        V.SetSeed(int)
        C++: virtual void SetSeed(int _arg)
        
        Control the seed used for pseudo-random-number generation. This
        ensures that vtkRandomGraphSource can produce repeatable results.
        """
        ...
    
    def SetStartWithTree(self, bool):
        """
        V.SetStartWithTree(bool)
        C++: virtual void SetStartWithTree(bool _arg)
        
        When set, builds a random tree structure first, then adds
        additional random edges.
        """
        ...
    
    def SetUseEdgeProbability(self, bool):
        """
        V.SetUseEdgeProbability(bool)
        C++: virtual void SetUseEdgeProbability(bool _arg)
        
        When set, uses the EdgeProbability parameter to determine the
        density of edges.  Otherwise, NumberOfEdges is used.
        """
        ...
    
    def SetVertexPedigreeIdArrayName(self, string):
        """
        V.SetVertexPedigreeIdArrayName(string)
        C++: virtual void SetVertexPedigreeIdArrayName(const char *_arg)
        
        The name of the vertex pedigree id array. Default "vertex id".
        """
        ...
    
    def StartWithTreeOff(self):
        """
        V.StartWithTreeOff()
        C++: virtual void StartWithTreeOff()
        
        When set, builds a random tree structure first, then adds
        additional random edges.
        """
        ...
    
    def StartWithTreeOn(self):
        """
        V.StartWithTreeOn()
        C++: virtual void StartWithTreeOn()
        
        When set, builds a random tree structure first, then adds
        additional random edges.
        """
        ...
    
    def UseEdgeProbabilityOff(self):
        """
        V.UseEdgeProbabilityOff()
        C++: virtual void UseEdgeProbabilityOff()
        
        When set, uses the EdgeProbability parameter to determine the
        density of edges.  Otherwise, NumberOfEdges is used.
        """
        ...
    
    def UseEdgeProbabilityOn(self):
        """
        V.UseEdgeProbabilityOn()
        C++: virtual void UseEdgeProbabilityOn()
        
        When set, uses the EdgeProbability parameter to determine the
        density of edges.  Otherwise, NumberOfEdges is used.
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


