"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkVertexListIterator(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkVertexListIterator - Iterates all vertices in a graph.
    
    Superclass: vtkObject
    
    vtkVertexListIterator iterates through all vertices in a graph.
    Create an instance of this and call graph->GetVertices(it) to
    initialize this iterator. You may alternately call SetGraph() to
    initialize the iterator.
    
    @sa
    vtkGraph
    """
    def GetGraph(self):
        """
        V.GetGraph() -> vtkGraph
        C++: virtual vtkGraph *GetGraph()
        
        Get the graph associated with this iterator.
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
    
    def HasNext(self):
        """
        V.HasNext() -> bool
        C++: bool HasNext()
        
        Whether this iterator has more edges.
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
        V.NewInstance() -> vtkVertexListIterator
        C++: vtkVertexListIterator *NewInstance()
        """
        ...
    
    def Next(self):
        """
        V.Next() -> int
        C++: vtkIdType Next()
        
        Returns the next edge in the graph.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkVertexListIterator
        C++: static vtkVertexListIterator *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetGraph(self, vtkGraph):
        """
        V.SetGraph(vtkGraph)
        C++: virtual void SetGraph(vtkGraph *graph)
        
        Setup the iterator with a graph.
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


