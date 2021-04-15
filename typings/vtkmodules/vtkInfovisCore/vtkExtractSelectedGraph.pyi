"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkExtractSelectedGraph(__vtkmodules_vtkCommonExecutionModel.vtkGraphAlgorithm):
    """
    vtkExtractSelectedGraph - return a subgraph of a vtkGraph
    
    Superclass: vtkGraphAlgorithm
    
    The first input is a vtkGraph to take a subgraph from. The second
    input (optional) is a vtkSelection containing selected indices. The
    third input (optional) is a vtkAnnotationsLayers whose annotations
    contain selected specifying selected indices. The vtkSelection may
    have FIELD_TYPE set to POINTS (a vertex selection) or CELLS (an edge
    selection).  A vertex selection preserves all edges that connect
    selected vertices.  An edge selection preserves all vertices that are
    adjacent to at least one selected edge.  Alternately, you may
    indicate that an edge selection should maintain the full set of
    vertices, by turning RemoveIsolatedVertices off.
    """
    def FillInputPortInformation(self, p_int, vtkInformation):
        """
        V.FillInputPortInformation(int, vtkInformation) -> int
        C++: int FillInputPortInformation(int port, vtkInformation *info)
            override;
        
        Specify the first vtkGraph input and the second vtkSelection
        input.
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
    
    def GetRemoveIsolatedVertices(self):
        """
        V.GetRemoveIsolatedVertices() -> bool
        C++: virtual bool GetRemoveIsolatedVertices()
        
        If set, removes vertices with no adjacent edges in an edge
        selection. A vertex selection ignores this flag and always
        returns the full set of selected vertices.  Default is on.
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
        V.NewInstance() -> vtkExtractSelectedGraph
        C++: vtkExtractSelectedGraph *NewInstance()
        """
        ...
    
    def RemoveIsolatedVerticesOff(self):
        """
        V.RemoveIsolatedVerticesOff()
        C++: virtual void RemoveIsolatedVerticesOff()
        
        If set, removes vertices with no adjacent edges in an edge
        selection. A vertex selection ignores this flag and always
        returns the full set of selected vertices.  Default is on.
        """
        ...
    
    def RemoveIsolatedVerticesOn(self):
        """
        V.RemoveIsolatedVerticesOn()
        C++: virtual void RemoveIsolatedVerticesOn()
        
        If set, removes vertices with no adjacent edges in an edge
        selection. A vertex selection ignores this flag and always
        returns the full set of selected vertices.  Default is on.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtractSelectedGraph
        C++: static vtkExtractSelectedGraph *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetAnnotationLayersConnection(self, vtkAlgorithmOutput):
        """
        V.SetAnnotationLayersConnection(vtkAlgorithmOutput)
        C++: void SetAnnotationLayersConnection(vtkAlgorithmOutput *in)
        
        A convenience method for setting the third input (i.e. the
        annotation layers).
        """
        ...
    
    def SetRemoveIsolatedVertices(self, bool):
        """
        V.SetRemoveIsolatedVertices(bool)
        C++: virtual void SetRemoveIsolatedVertices(bool _arg)
        
        If set, removes vertices with no adjacent edges in an edge
        selection. A vertex selection ignores this flag and always
        returns the full set of selected vertices.  Default is on.
        """
        ...
    
    def SetSelectionConnection(self, vtkAlgorithmOutput):
        """
        V.SetSelectionConnection(vtkAlgorithmOutput)
        C++: void SetSelectionConnection(vtkAlgorithmOutput *in)
        
        A convenience method for setting the second input (i.e. the
        selection).
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

