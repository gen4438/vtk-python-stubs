"""
This type stub file was generated by pyright.
"""

from .vtkGraphLayoutStrategy import vtkGraphLayoutStrategy

class vtkCosmicTreeLayoutStrategy(vtkGraphLayoutStrategy):
    """
    vtkCosmicTreeLayoutStrategy - tree layout strategy reminiscent of
    astronomical systems
    
    Superclass: vtkGraphLayoutStrategy
    
    This layout strategy takes an input tree and places all the children
    of a node into a containing circle. The placement is such that each
    child placed can be represented with a circle tangent to the
    containing circle and (usually) 2 other children. The interior of the
    circle is left empty so that graph edges drawn on top of the tree
    will not obfuscate the tree. However, when one child is much larger
    than all the others, it may encroach on the center of the containing
    circle; that's OK, because it's large enough not to be obscured by
    edges drawn atop it.
    
    @par Thanks: Thanks to the galaxy and David Thompson hierarchically
    nested inside it for inspiring this layout strategy.
    """
    def GetLayoutDepth(self):
        """
        V.GetLayoutDepth() -> int
        C++: virtual int GetLayoutDepth()
        
        How many levels of the tree should be laid out? For large trees,
        you may wish to set the root and maximum depth in order to
        retrieve the layout for the visible portion of the tree. When
        this value is zero or negative, all nodes below and including the
        LayoutRoot will be presented. This defaults to 0.
        """
        ...
    
    def GetLayoutRoot(self):
        """
        V.GetLayoutRoot() -> int
        C++: virtual vtkIdType GetLayoutRoot()
        
        What is the top-most tree node to lay out? This node will become
        the largest containing circle in the layout. Use this in
        combination with SetLayoutDepth to retrieve the layout of a
        subtree of interest for rendering. Setting LayoutRoot to a
        negative number signals that the root node of the tree should be
        used as the root node of the layout. This defaults to -1.
        """
        ...
    
    def GetNodeSizeArrayName(self):
        """
        V.GetNodeSizeArrayName() -> string
        C++: virtual char *GetNodeSizeArrayName()
        
        Set the array to be used for sizing nodes. If this is set to an
        empty string or nullptr (the default), then all leaf nodes (or
        all nodes, when SizeLeafNodesOnly is false) will be assigned a
        unit size.
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
    
    def GetSizeLeafNodesOnly(self):
        """
        V.GetSizeLeafNodesOnly() -> int
        C++: virtual vtkTypeBool GetSizeLeafNodesOnly()
        
        Should node size specifications be obeyed at leaf nodes only or
        (with scaling as required to meet constraints) at every node in
        the tree? This defaults to true, so that leaf nodes are scaled
        according to the size specification provided, and the parent node
        sizes are calculated by the algorithm.
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
    
    def Layout(self):
        """
        V.Layout()
        C++: void Layout() override;
        
        Perform the layout.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkCosmicTreeLayoutStrategy
        C++: vtkCosmicTreeLayoutStrategy *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCosmicTreeLayoutStrategy
        C++: static vtkCosmicTreeLayoutStrategy *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetLayoutDepth(self, p_int):
        """
        V.SetLayoutDepth(int)
        C++: virtual void SetLayoutDepth(int _arg)
        
        How many levels of the tree should be laid out? For large trees,
        you may wish to set the root and maximum depth in order to
        retrieve the layout for the visible portion of the tree. When
        this value is zero or negative, all nodes below and including the
        LayoutRoot will be presented. This defaults to 0.
        """
        ...
    
    def SetLayoutRoot(self, p_int):
        """
        V.SetLayoutRoot(int)
        C++: virtual void SetLayoutRoot(vtkIdType _arg)
        
        What is the top-most tree node to lay out? This node will become
        the largest containing circle in the layout. Use this in
        combination with SetLayoutDepth to retrieve the layout of a
        subtree of interest for rendering. Setting LayoutRoot to a
        negative number signals that the root node of the tree should be
        used as the root node of the layout. This defaults to -1.
        """
        ...
    
    def SetNodeSizeArrayName(self, string):
        """
        V.SetNodeSizeArrayName(string)
        C++: virtual void SetNodeSizeArrayName(const char *_arg)
        
        Set the array to be used for sizing nodes. If this is set to an
        empty string or nullptr (the default), then all leaf nodes (or
        all nodes, when SizeLeafNodesOnly is false) will be assigned a
        unit size.
        """
        ...
    
    def SetSizeLeafNodesOnly(self, p_int):
        """
        V.SetSizeLeafNodesOnly(int)
        C++: virtual void SetSizeLeafNodesOnly(vtkTypeBool _arg)
        
        Should node size specifications be obeyed at leaf nodes only or
        (with scaling as required to meet constraints) at every node in
        the tree? This defaults to true, so that leaf nodes are scaled
        according to the size specification provided, and the parent node
        sizes are calculated by the algorithm.
        """
        ...
    
    def SizeLeafNodesOnlyOff(self):
        """
        V.SizeLeafNodesOnlyOff()
        C++: virtual void SizeLeafNodesOnlyOff()
        
        Should node size specifications be obeyed at leaf nodes only or
        (with scaling as required to meet constraints) at every node in
        the tree? This defaults to true, so that leaf nodes are scaled
        according to the size specification provided, and the parent node
        sizes are calculated by the algorithm.
        """
        ...
    
    def SizeLeafNodesOnlyOn(self):
        """
        V.SizeLeafNodesOnlyOn()
        C++: virtual void SizeLeafNodesOnlyOn()
        
        Should node size specifications be obeyed at leaf nodes only or
        (with scaling as required to meet constraints) at every node in
        the tree? This defaults to true, so that leaf nodes are scaled
        according to the size specification provided, and the parent node
        sizes are calculated by the algorithm.
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


