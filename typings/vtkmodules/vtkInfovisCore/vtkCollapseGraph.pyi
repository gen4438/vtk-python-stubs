"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkCollapseGraph(__vtkmodules_vtkCommonExecutionModel.vtkGraphAlgorithm):
    """
    vtkCollapseGraph - "Collapses" vertices onto their neighbors.
    
    Superclass: vtkGraphAlgorithm
    
    vtkCollapseGraph "collapses" vertices onto their neighbors, while
    maintaining connectivity.  Two inputs are required - a graph
    (directed or undirected), and a vertex selection that can be
    converted to indices.
    
    Conceptually, each of the vertices specified in the input selection
    expands, "swallowing" adacent vertices.  Edges to-or-from the
    "swallowed" vertices become edges to-or-from the expanding vertices,
    maintaining the overall graph connectivity.
    
    In the case of directed graphs, expanding vertices only swallow
    vertices that are connected via out edges.  This rule provides
    intuitive behavior when working with trees, so that "child" vertices
    collapse into their parents when the parents are part of the input
    selection.
    
    Input port 0: graph Input port 1: selection
    """
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
        V.NewInstance() -> vtkCollapseGraph
        C++: vtkCollapseGraph *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCollapseGraph
        C++: static vtkCollapseGraph *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetGraphConnection(self, vtkAlgorithmOutput):
        """
        V.SetGraphConnection(vtkAlgorithmOutput)
        C++: void SetGraphConnection(vtkAlgorithmOutput *)
        
        Convenience function provided for setting the graph input.
        """
        ...
    
    def SetSelectionConnection(self, vtkAlgorithmOutput):
        """
        V.SetSelectionConnection(vtkAlgorithmOutput)
        C++: void SetSelectionConnection(vtkAlgorithmOutput *)
        
        Convenience function provided for setting the selection input.
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


