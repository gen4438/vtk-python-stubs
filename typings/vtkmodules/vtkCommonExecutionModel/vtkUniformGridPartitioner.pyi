"""
This type stub file was generated by pyright.
"""

from .vtkMultiBlockDataSetAlgorithm import vtkMultiBlockDataSetAlgorithm

class vtkUniformGridPartitioner(vtkMultiBlockDataSetAlgorithm):
    """
    vtkUniformGridPartitioner -  A concrete implementation of
    vtkMultiBlockDataSetAlgorithm that provides
     functionality for partitioning a uniform grid.
    
    Superclass: vtkMultiBlockDataSetAlgorithm
    
    The partitioning method
     that is used is Recursive Coordinate Bisection (RCB) where each time
     the longest dimension is split.
    
    @sa
    vtkStructuredGridPartitioner vtkRectilinearGridPartitioner
    """
    def DuplicateNodesOff(self):
        """
        V.DuplicateNodesOff()
        C++: virtual void DuplicateNodesOff()
        """
        ...
    
    def DuplicateNodesOn(self):
        """
        V.DuplicateNodesOn()
        C++: virtual void DuplicateNodesOn()
        """
        ...
    
    def GetDuplicateNodes(self):
        """
        V.GetDuplicateNodes() -> int
        C++: virtual vtkTypeBool GetDuplicateNodes()
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
    
    def GetNumberOfGhostLayers(self):
        """
        V.GetNumberOfGhostLayers() -> int
        C++: virtual int GetNumberOfGhostLayers()
        
        Set/Get macro for the number of ghost layers.
        """
        ...
    
    def GetNumberOfPartitions(self):
        """
        V.GetNumberOfPartitions() -> int
        C++: virtual int GetNumberOfPartitions()
        
        Set/Get macro for the number of subdivisions.
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
        V.NewInstance() -> vtkUniformGridPartitioner
        C++: vtkUniformGridPartitioner *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkUniformGridPartitioner
        C++: static vtkUniformGridPartitioner *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetDuplicateNodes(self, p_int):
        """
        V.SetDuplicateNodes(int)
        C++: virtual void SetDuplicateNodes(vtkTypeBool _arg)
        """
        ...
    
    def SetNumberOfGhostLayers(self, p_int):
        """
        V.SetNumberOfGhostLayers(int)
        C++: virtual void SetNumberOfGhostLayers(int _arg)
        
        Set/Get macro for the number of ghost layers.
        """
        ...
    
    def SetNumberOfPartitions(self, p_int):
        """
        V.SetNumberOfPartitions(int)
        C++: virtual void SetNumberOfPartitions(int _arg)
        
        Set/Get macro for the number of subdivisions.
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


