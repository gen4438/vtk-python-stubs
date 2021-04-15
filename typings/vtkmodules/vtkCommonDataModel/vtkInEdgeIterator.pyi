"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkInEdgeIterator(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkInEdgeIterator - Iterates through all incoming edges to a vertex.
    
    Superclass: vtkObject
    
    vtkInEdgeIterator iterates through all edges whose target is a
    particular vertex. Instantiate this class directly and call
    Initialize() to traverse the vertex of a graph. Alternately, use
    GetInEdges() on the graph to initialize the iterator. it->Next()
    returns a vtkInEdgeType structure, which contains Id, the edge's id, and Source, the
    edge's source vertex.
    
    @sa
    vtkGraph vtkOutEdgeIterator
    """
    def GetGraph(self):
        """
        V.GetGraph() -> vtkGraph
        C++: virtual vtkGraph *GetGraph()
        
        Get the graph and vertex associated with this iterator.
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
    
    def GetVertex(self):
        """
        V.GetVertex() -> int
        C++: virtual vtkIdType GetVertex()
        
        Get the graph and vertex associated with this iterator.
        """
        ...
    
    def HasNext(self):
        """
        V.HasNext() -> bool
        C++: bool HasNext()
        
        Whether this iterator has more edges.
        """
        ...
    
    def Initialize(self, vtkGraph, p_int):
        """
        V.Initialize(vtkGraph, int)
        C++: void Initialize(vtkGraph *g, vtkIdType v)
        
        Initialize the iterator with a graph and vertex.
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
        V.NewInstance() -> vtkInEdgeIterator
        C++: vtkInEdgeIterator *NewInstance()
        """
        ...
    
    def Next(self):
        """
        V.Next() -> vtkInEdgeType
        C++: vtkInEdgeType Next()
        
        Returns the next edge in the graph.
        """
        ...
    
    def NextGraphEdge(self):
        """
        V.NextGraphEdge() -> vtkGraphEdge
        C++: vtkGraphEdge *NextGraphEdge()
        
        Just like Next(), but returns heavy-weight vtkGraphEdge object
        instead of the vtkEdgeType struct, for use with wrappers. The
        graph edge is owned by this iterator, and changes after each call
        to NextGraphEdge().
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkInEdgeIterator
        C++: static vtkInEdgeIterator *SafeDownCast(vtkObjectBase *o)
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

