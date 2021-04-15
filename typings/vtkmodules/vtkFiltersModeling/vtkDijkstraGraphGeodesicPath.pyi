"""
This type stub file was generated by pyright.
"""

from .vtkGraphGeodesicPath import vtkGraphGeodesicPath

class vtkDijkstraGraphGeodesicPath(vtkGraphGeodesicPath):
    """
    vtkDijkstraGraphGeodesicPath - Dijkstra algorithm to compute the
    graph geodesic.
    
    Superclass: vtkGraphGeodesicPath
    
    Takes as input a polygonal mesh and performs a single source shortest
    path calculation. Dijkstra's algorithm is used. The implementation is
    similar to the one described in Introduction to Algorithms (Second
    Edition) by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest,
    and Cliff Stein, published by MIT Press and McGraw-Hill. Some minor
    enhancement are added though. All vertices are not pushed on the heap
    at start, instead a front set is maintained. The heap is implemented
    as a binary heap. The output of the filter is a set of lines
    describing the shortest path from StartVertex to EndVertex. If a path
    cannot be found the output will have no lines or points.
    
    @warning
    The input polydata must have only triangle cells.
    
    @par Thanks: The class was contributed by Rasmus Paulsen.
    www.imm.dtu.dk/~rrp/VTK . Also thanks to Alexandre Gouaillard and
    Shoaib Ghias for bug fixes and enhancements.
    """
    def GetCumulativeWeights(self, vtkDoubleArray):
        """
        V.GetCumulativeWeights(vtkDoubleArray)
        C++: virtual void GetCumulativeWeights(vtkDoubleArray *weights)
        
        Fill the array with the cumulative weights.
        """
        ...
    
    def GetIdList(self):
        """
        V.GetIdList() -> vtkIdList
        C++: virtual vtkIdList *GetIdList()
        
        The vertex ids (of the input polydata) on the shortest path
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for printing and determining type information.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for printing and determining type information.
        """
        ...
    
    def GetRepelPathFromVertices(self):
        """
        V.GetRepelPathFromVertices() -> int
        C++: virtual vtkTypeBool GetRepelPathFromVertices()
        
        Use the input point to repel the path by assigning high costs.
        """
        ...
    
    def GetRepelVertices(self):
        """
        V.GetRepelVertices() -> vtkPoints
        C++: virtual vtkPoints *GetRepelVertices()
        
        Specify vtkPoints to use to repel the path from.
        """
        ...
    
    def GetStopWhenEndReached(self):
        """
        V.GetStopWhenEndReached() -> int
        C++: virtual vtkTypeBool GetStopWhenEndReached()
        
        Stop when the end vertex is reached or calculate shortest path to
        all vertices
        """
        ...
    
    def GetUseScalarWeights(self):
        """
        V.GetUseScalarWeights() -> int
        C++: virtual vtkTypeBool GetUseScalarWeights()
        
        Use scalar values in the edge weight (experimental)
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for printing and determining type information.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for printing and determining type information.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkDijkstraGraphGeodesicPath
        C++: vtkDijkstraGraphGeodesicPath *NewInstance()
        
        Standard methods for printing and determining type information.
        """
        ...
    
    def RepelPathFromVerticesOff(self):
        """
        V.RepelPathFromVerticesOff()
        C++: virtual void RepelPathFromVerticesOff()
        
        Use the input point to repel the path by assigning high costs.
        """
        ...
    
    def RepelPathFromVerticesOn(self):
        """
        V.RepelPathFromVerticesOn()
        C++: virtual void RepelPathFromVerticesOn()
        
        Use the input point to repel the path by assigning high costs.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDijkstraGraphGeodesicPath
        C++: static vtkDijkstraGraphGeodesicPath *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for printing and determining type information.
        """
        ...
    
    def SetRepelPathFromVertices(self, p_int):
        """
        V.SetRepelPathFromVertices(int)
        C++: virtual void SetRepelPathFromVertices(vtkTypeBool _arg)
        
        Use the input point to repel the path by assigning high costs.
        """
        ...
    
    def SetRepelVertices(self, vtkPoints):
        """
        V.SetRepelVertices(vtkPoints)
        C++: virtual void SetRepelVertices(vtkPoints *)
        
        Specify vtkPoints to use to repel the path from.
        """
        ...
    
    def SetStopWhenEndReached(self, p_int):
        """
        V.SetStopWhenEndReached(int)
        C++: virtual void SetStopWhenEndReached(vtkTypeBool _arg)
        
        Stop when the end vertex is reached or calculate shortest path to
        all vertices
        """
        ...
    
    def SetUseScalarWeights(self, p_int):
        """
        V.SetUseScalarWeights(int)
        C++: virtual void SetUseScalarWeights(vtkTypeBool _arg)
        
        Use scalar values in the edge weight (experimental)
        """
        ...
    
    def StopWhenEndReachedOff(self):
        """
        V.StopWhenEndReachedOff()
        C++: virtual void StopWhenEndReachedOff()
        
        Stop when the end vertex is reached or calculate shortest path to
        all vertices
        """
        ...
    
    def StopWhenEndReachedOn(self):
        """
        V.StopWhenEndReachedOn()
        C++: virtual void StopWhenEndReachedOn()
        
        Stop when the end vertex is reached or calculate shortest path to
        all vertices
        """
        ...
    
    def UseScalarWeightsOff(self):
        """
        V.UseScalarWeightsOff()
        C++: virtual void UseScalarWeightsOff()
        
        Use scalar values in the edge weight (experimental)
        """
        ...
    
    def UseScalarWeightsOn(self):
        """
        V.UseScalarWeightsOn()
        C++: virtual void UseScalarWeightsOn()
        
        Use scalar values in the edge weight (experimental)
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

