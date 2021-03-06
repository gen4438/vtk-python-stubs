"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkExtentRCBPartitioner(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkExtentRCBPartitioner -  This method partitions a global extent to
    N partitions where N is a user
     supplied parameter.
    
    Superclass: vtkObject
    """
    def DuplicateNodesOff(self):
        """
        V.DuplicateNodesOff()
        C++: virtual void DuplicateNodesOff()
        
        On/Off DuplicateNodes between partitions. Default is On.
        """
        ...
    
    def DuplicateNodesOn(self):
        """
        V.DuplicateNodesOn()
        C++: virtual void DuplicateNodesOn()
        
        On/Off DuplicateNodes between partitions. Default is On.
        """
        ...
    
    def GetDuplicateNodes(self):
        """
        V.GetDuplicateNodes() -> int
        C++: virtual vtkTypeBool GetDuplicateNodes()
        
        On/Off DuplicateNodes between partitions. Default is On.
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
    
    def GetNumExtents(self):
        """
        V.GetNumExtents() -> int
        C++: virtual int GetNumExtents()
        
        Returns the number of extents.
        """
        ...
    
    def GetPartitionExtent(self, p_int, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=...):
        """
        V.GetPartitionExtent(int, [int, int, int, int, int, int])
        C++: void GetPartitionExtent(const int idx, int ext[6])
        
        Returns the extent of the partition corresponding to the given
        ID.
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
        V.NewInstance() -> vtkExtentRCBPartitioner
        C++: vtkExtentRCBPartitioner *NewInstance()
        """
        ...
    
    def Partition(self):
        """
        V.Partition()
        C++: void Partition()
        
        Partitions the extent
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtentRCBPartitioner
        C++: static vtkExtentRCBPartitioner *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetDuplicateNodes(self, p_int):
        """
        V.SetDuplicateNodes(int)
        C++: virtual void SetDuplicateNodes(vtkTypeBool _arg)
        
        On/Off DuplicateNodes between partitions. Default is On.
        """
        ...
    
    def SetGlobalExtent(self, p_int, p_int_1, p_int_2, p_int_3, p_int_4, p_int_5):
        """
        V.SetGlobalExtent(int, int, int, int, int, int)
        C++: void SetGlobalExtent(int imin, int imax, int jmin, int jmax,
            int kmin, int kmax)
        V.SetGlobalExtent([int, int, int, int, int, int])
        C++: void SetGlobalExtent(int ext[6])
        
        Set/Get the global extent array to be partitioned. The global
        extent is packed as follows: [imin,imax,jmin,jmax,kmin,kmax]
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
        C++: void SetNumberOfPartitions(const int N)
        
        Set/Get the number of requested partitions
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


