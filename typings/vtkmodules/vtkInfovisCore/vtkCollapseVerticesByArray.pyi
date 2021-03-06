"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkCollapseVerticesByArray(__vtkmodules_vtkCommonExecutionModel.vtkGraphAlgorithm):
    """
    vtkCollapseVerticesByArray - Collapse the graph given a vertex array
    
    Superclass: vtkGraphAlgorithm
    
    vtkCollapseVerticesByArray is a class which collapses the graph using
    a vertex array as the key. So if the graph has vertices sharing
    common traits then this class combines all these vertices into one.
    This class does not perform aggregation on vertex data but allow to
    do so for edge data. Users can choose one or more edge data arrays
    for aggregation using AddAggregateEdgeArray function.
    """
    def AddAggregateEdgeArray(self, string):
        """
        V.AddAggregateEdgeArray(string)
        C++: void AddAggregateEdgeArray(const char *arrName)
        
        Add arrays on which aggregation of data is allowed. Default if
        replaced by the last value.
        """
        ...
    
    def AllowSelfLoopsOff(self):
        """
        V.AllowSelfLoopsOff()
        C++: virtual void AllowSelfLoopsOff()
        
        Boolean to allow self loops during collapse.
        """
        ...
    
    def AllowSelfLoopsOn(self):
        """
        V.AllowSelfLoopsOn()
        C++: virtual void AllowSelfLoopsOn()
        
        Boolean to allow self loops during collapse.
        """
        ...
    
    def ClearAggregateEdgeArray(self):
        """
        V.ClearAggregateEdgeArray()
        C++: void ClearAggregateEdgeArray()
        
        Clear the list of arrays on which aggregation was set to allow.
        """
        ...
    
    def CountEdgesCollapsedOff(self):
        """
        V.CountEdgesCollapsedOff()
        C++: virtual void CountEdgesCollapsedOff()
        
        Set if count should be made of how many edges collapsed.
        """
        ...
    
    def CountEdgesCollapsedOn(self):
        """
        V.CountEdgesCollapsedOn()
        C++: virtual void CountEdgesCollapsedOn()
        
        Set if count should be made of how many edges collapsed.
        """
        ...
    
    def CountVerticesCollapsedOff(self):
        """
        V.CountVerticesCollapsedOff()
        C++: virtual void CountVerticesCollapsedOff()
        
        Get/Set if count should be made of how many vertices collapsed.
        """
        ...
    
    def CountVerticesCollapsedOn(self):
        """
        V.CountVerticesCollapsedOn()
        C++: virtual void CountVerticesCollapsedOn()
        
        Get/Set if count should be made of how many vertices collapsed.
        """
        ...
    
    def GetAllowSelfLoops(self):
        """
        V.GetAllowSelfLoops() -> bool
        C++: virtual bool GetAllowSelfLoops()
        
        Boolean to allow self loops during collapse.
        """
        ...
    
    def GetCountEdgesCollapsed(self):
        """
        V.GetCountEdgesCollapsed() -> bool
        C++: virtual bool GetCountEdgesCollapsed()
        
        Set if count should be made of how many edges collapsed.
        """
        ...
    
    def GetCountVerticesCollapsed(self):
        """
        V.GetCountVerticesCollapsed() -> bool
        C++: virtual bool GetCountVerticesCollapsed()
        
        Get/Set if count should be made of how many vertices collapsed.
        """
        ...
    
    def GetEdgesCollapsedArray(self):
        """
        V.GetEdgesCollapsedArray() -> string
        C++: virtual char *GetEdgesCollapsedArray()
        
        Name of the array where the count of how many edges collapsed
        will be stored.By default the name of array is
        "EdgesCollapsedCountArray".
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
    
    def GetVertexArray(self):
        """
        V.GetVertexArray() -> string
        C++: virtual char *GetVertexArray()
        
        Set the array using which perform the collapse.
        """
        ...
    
    def GetVerticesCollapsedArray(self):
        """
        V.GetVerticesCollapsedArray() -> string
        C++: virtual char *GetVerticesCollapsedArray()
        
        Name of the array where the count of how many vertices collapsed
        will be stored. By default name of the array is
        "VerticesCollapsedCountArray".
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
        V.NewInstance() -> vtkCollapseVerticesByArray
        C++: vtkCollapseVerticesByArray *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCollapseVerticesByArray
        C++: static vtkCollapseVerticesByArray *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetAllowSelfLoops(self, bool):
        """
        V.SetAllowSelfLoops(bool)
        C++: virtual void SetAllowSelfLoops(bool _arg)
        
        Boolean to allow self loops during collapse.
        """
        ...
    
    def SetCountEdgesCollapsed(self, bool):
        """
        V.SetCountEdgesCollapsed(bool)
        C++: virtual void SetCountEdgesCollapsed(bool _arg)
        
        Set if count should be made of how many edges collapsed.
        """
        ...
    
    def SetCountVerticesCollapsed(self, bool):
        """
        V.SetCountVerticesCollapsed(bool)
        C++: virtual void SetCountVerticesCollapsed(bool _arg)
        
        Get/Set if count should be made of how many vertices collapsed.
        """
        ...
    
    def SetEdgesCollapsedArray(self, string):
        """
        V.SetEdgesCollapsedArray(string)
        C++: virtual void SetEdgesCollapsedArray(const char *_arg)
        
        Name of the array where the count of how many edges collapsed
        will be stored.By default the name of array is
        "EdgesCollapsedCountArray".
        """
        ...
    
    def SetVertexArray(self, string):
        """
        V.SetVertexArray(string)
        C++: virtual void SetVertexArray(const char *_arg)
        
        Set the array using which perform the collapse.
        """
        ...
    
    def SetVerticesCollapsedArray(self, string):
        """
        V.SetVerticesCollapsedArray(string)
        C++: virtual void SetVerticesCollapsedArray(const char *_arg)
        
        Name of the array where the count of how many vertices collapsed
        will be stored. By default name of the array is
        "VerticesCollapsedCountArray".
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


