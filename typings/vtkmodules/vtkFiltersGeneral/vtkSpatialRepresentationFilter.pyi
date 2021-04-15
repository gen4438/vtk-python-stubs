"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkSpatialRepresentationFilter(__vtkmodules_vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    """
    vtkSpatialRepresentationFilter - generate polygonal model of spatial
    search object (i.e., a vtkLocator)
    
    Superclass: vtkMultiBlockDataSetAlgorithm
    
    vtkSpatialRepresentationFilter generates an polygonal representation
    of a spatial search (vtkLocator) object. The representation varies
    depending upon the nature of the spatial search object. For example,
    the representation for vtkOBBTree is a collection of oriented
    bounding boxes. This input to this filter is a dataset of any type,
    and the output is polygonal data. You must also specify the spatial
    search object to use.
    
    Generally spatial search objects are used for collision detection and
    other geometric operations, but in this filter one or more levels of
    spatial searchers can be generated to form a geometric approximation
    to the input data. This is a form of data simplification, generally
    used to accelerate the rendering process. Or, this filter can be used
    as a debugging/ visualization aid for spatial search objects.
    
    This filter can generate one or more  vtkPolyData blocks
    corresponding to different levels in the spatial search tree. The
    block ids range from 0 (root level) to MaximumLevel. Note that the
    block for level "id" is not computed unless a AddLevel(id) method is
    issued. Thus, if you desire three levels of output (say 2,4,7), you
    would have to invoke AddLevel(2), AddLevel(4), and AddLevel(7). If
    GenerateLeaves is set to true (off by default), all leaf nodes of the
    locator (which may be at different levels) are computed and stored in
    block with id MaximumLevel + 1.
    
    @sa
    vtkLocator vtkPointLocator vtkCellLocator vtkOBBTree
    """
    def AddLevel(self, p_int):
        """
        V.AddLevel(int)
        C++: void AddLevel(int level)
        
        Add a level to be computed.
        """
        ...
    
    def GenerateLeavesOff(self):
        """
        V.GenerateLeavesOff()
        C++: virtual void GenerateLeavesOff()
        
        Turn on/off the generation of leaf nodes. Off by default.
        """
        ...
    
    def GenerateLeavesOn(self):
        """
        V.GenerateLeavesOn()
        C++: virtual void GenerateLeavesOn()
        
        Turn on/off the generation of leaf nodes. Off by default.
        """
        ...
    
    def GetGenerateLeaves(self):
        """
        V.GetGenerateLeaves() -> bool
        C++: virtual bool GetGenerateLeaves()
        
        Turn on/off the generation of leaf nodes. Off by default.
        """
        ...
    
    def GetMaximumLevel(self):
        """
        V.GetMaximumLevel() -> int
        C++: virtual int GetMaximumLevel()
        
        Get the maximum level that is available. Populated during
        RequestData().
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
    
    def GetSpatialRepresentation(self):
        """
        V.GetSpatialRepresentation() -> vtkLocator
        C++: virtual vtkLocator *GetSpatialRepresentation()
        
        Set/Get the locator that will be used to generate the
        representation.
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
        V.NewInstance() -> vtkSpatialRepresentationFilter
        C++: vtkSpatialRepresentationFilter *NewInstance()
        """
        ...
    
    def ResetLevels(self):
        """
        V.ResetLevels()
        C++: void ResetLevels()
        
        Remove all levels.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSpatialRepresentationFilter
        C++: static vtkSpatialRepresentationFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetGenerateLeaves(self, bool):
        """
        V.SetGenerateLeaves(bool)
        C++: virtual void SetGenerateLeaves(bool _arg)
        
        Turn on/off the generation of leaf nodes. Off by default.
        """
        ...
    
    def SetSpatialRepresentation(self, vtkLocator):
        """
        V.SetSpatialRepresentation(vtkLocator)
        C++: virtual void SetSpatialRepresentation(vtkLocator *)
        
        Set/Get the locator that will be used to generate the
        representation.
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

