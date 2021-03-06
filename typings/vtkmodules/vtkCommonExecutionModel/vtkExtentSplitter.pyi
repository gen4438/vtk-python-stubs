"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkExtentSplitter(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkExtentSplitter - Split an extent across other extents.
    
    Superclass: vtkObject
    
    vtkExtentSplitter splits each input extent into non-overlapping
    sub-extents that are completely contained within other "source
    extents".  A source extent corresponds to some resource providing an
    extent.  Each source extent has an integer identifier, integer
    priority, and an extent.  The input extents are split into
    sub-extents according to priority, availability, and amount of
    overlap of the source extents.  This can be used by parallel data
    readers to read as few piece files as possible.
    """
    def AddExtent(self, p_int, p_int_1, p_int_2, p_int_3, p_int_4, p_int_5):
        """
        V.AddExtent(int, int, int, int, int, int)
        C++: void AddExtent(int x0, int x1, int y0, int y1, int z0,
            int z1)
        V.AddExtent([int, ...])
        C++: void AddExtent(int *extent)
        
        Add an extent to the queue of extents to be split among the
        available sources.
        """
        ...
    
    def AddExtentSource(self, p_int, p_int_1, p_int_2, p_int_3, p_int_4, p_int_5, p_int_6, p_int_7):
        """
        V.AddExtentSource(int, int, int, int, int, int, int, int)
        C++: void AddExtentSource(int id, int priority, int x0, int x1,
            int y0, int y1, int z0, int z1)
        V.AddExtentSource(int, int, [int, ...])
        C++: void AddExtentSource(int id, int priority, int *extent)
        
        Add/Remove a source providing the given extent.  Sources with
        higher priority numbers are favored.  Source id numbers and
        priorities must be non-negative.
        """
        ...
    
    def ComputeSubExtents(self):
        """
        V.ComputeSubExtents() -> int
        C++: int ComputeSubExtents()
        
        Split the extents currently in the queue among the available
        sources.  The queue is empty when this returns.  Returns 1 if all
        extents could be read.  Returns 0 if any portion of any extent
        was not available through any source.
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
    
    def GetNumberOfSubExtents(self):
        """
        V.GetNumberOfSubExtents() -> int
        C++: int GetNumberOfSubExtents()
        
        Get the number of sub-extents into which the original set of
        extents have been split across the available sources.  Valid
        after a call to ComputeSubExtents.
        """
        ...
    
    def GetPointMode(self):
        """
        V.GetPointMode() -> int
        C++: virtual vtkTypeBool GetPointMode()
        
        Get/Set whether "point mode" is on.  In point mode, sub-extents
        are generated to ensure every point in the update request is
        read, but not necessarily every cell.  This can be used when
        point data are stored in a planar slice per piece with no cell
        data.  The default is OFF.
        """
        ...
    
    def GetSubExtent(self, p_int):
        """
        V.GetSubExtent(int) -> (int, int, int, int, int, int)
        C++: int *GetSubExtent(int index)
        V.GetSubExtent(int, [int, ...])
        C++: void GetSubExtent(int index, int *extent)
        
        Get the sub-extent associated with the given index.  Use
        GetSubExtentSource to get the id of the source from which this
        sub-extent should be read.  Valid after a call to
        ComputeSubExtents.
        """
        ...
    
    def GetSubExtentSource(self, p_int):
        """
        V.GetSubExtentSource(int) -> int
        C++: int GetSubExtentSource(int index)
        
        Get the id of the source from which the sub-extent associated
        with the given index should be read.  Returns -1 if no source
        provides the sub-extent.
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
        V.NewInstance() -> vtkExtentSplitter
        C++: vtkExtentSplitter *NewInstance()
        """
        ...
    
    def PointModeOff(self):
        """
        V.PointModeOff()
        C++: virtual void PointModeOff()
        
        Get/Set whether "point mode" is on.  In point mode, sub-extents
        are generated to ensure every point in the update request is
        read, but not necessarily every cell.  This can be used when
        point data are stored in a planar slice per piece with no cell
        data.  The default is OFF.
        """
        ...
    
    def PointModeOn(self):
        """
        V.PointModeOn()
        C++: virtual void PointModeOn()
        
        Get/Set whether "point mode" is on.  In point mode, sub-extents
        are generated to ensure every point in the update request is
        read, but not necessarily every cell.  This can be used when
        point data are stored in a planar slice per piece with no cell
        data.  The default is OFF.
        """
        ...
    
    def RemoveAllExtentSources(self):
        """
        V.RemoveAllExtentSources()
        C++: void RemoveAllExtentSources()
        
        Add/Remove a source providing the given extent.  Sources with
        higher priority numbers are favored.  Source id numbers and
        priorities must be non-negative.
        """
        ...
    
    def RemoveExtentSource(self, p_int):
        """
        V.RemoveExtentSource(int)
        C++: void RemoveExtentSource(int id)
        
        Add/Remove a source providing the given extent.  Sources with
        higher priority numbers are favored.  Source id numbers and
        priorities must be non-negative.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtentSplitter
        C++: static vtkExtentSplitter *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetPointMode(self, p_int):
        """
        V.SetPointMode(int)
        C++: virtual void SetPointMode(vtkTypeBool _arg)
        
        Get/Set whether "point mode" is on.  In point mode, sub-extents
        are generated to ensure every point in the update request is
        read, but not necessarily every cell.  This can be used when
        point data are stored in a planar slice per piece with no cell
        data.  The default is OFF.
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


