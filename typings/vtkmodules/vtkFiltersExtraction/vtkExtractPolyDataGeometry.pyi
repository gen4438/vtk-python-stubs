"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkExtractPolyDataGeometry(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkExtractPolyDataGeometry - extract vtkPolyData cells that lies
    either entirely inside or outside of a specified implicit function
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkExtractPolyDataGeometry extracts from its input vtkPolyData all
    cells that are either completely inside or outside of a specified
    implicit function. This filter is specialized to vtkPolyData. On
    output the filter generates vtkPolyData.
    
    To use this filter you must specify an implicit function. You must
    also specify whether to extract cells laying inside or outside of the
    implicit function. (The inside of an implicit function is the
    negative values region.) An option exists to extract cells that are
    neither inside nor outside (i.e., boundary).
    
    Note that this filter also has the option to directly pass all points
    or cull the points that do not satisfy the implicit function test.
    Passing all points is a tad faster, but then points remain that do
    not pass the test and may mess up subsequent glyphing operations and
    so on. By default points are culled.
    
    A more general version of this filter is available for arbitrary
    vtkDataSet input (see vtkExtractGeometry).
    
    @sa
    vtkExtractGeometry vtkClipPolyData
    """
    def ExtractBoundaryCellsOff(self):
        """
        V.ExtractBoundaryCellsOff()
        C++: virtual void ExtractBoundaryCellsOff()
        
        Boolean controls whether to extract cells that are partially
        inside. By default, ExtractBoundaryCells is off.
        """
        ...
    
    def ExtractBoundaryCellsOn(self):
        """
        V.ExtractBoundaryCellsOn()
        C++: virtual void ExtractBoundaryCellsOn()
        
        Boolean controls whether to extract cells that are partially
        inside. By default, ExtractBoundaryCells is off.
        """
        ...
    
    def ExtractInsideOff(self):
        """
        V.ExtractInsideOff()
        C++: virtual void ExtractInsideOff()
        
        Boolean controls whether to extract cells that are inside of
        implicit function (ExtractInside == 1) or outside of implicit
        function (ExtractInside == 0).
        """
        ...
    
    def ExtractInsideOn(self):
        """
        V.ExtractInsideOn()
        C++: virtual void ExtractInsideOn()
        
        Boolean controls whether to extract cells that are inside of
        implicit function (ExtractInside == 1) or outside of implicit
        function (ExtractInside == 0).
        """
        ...
    
    def GetExtractBoundaryCells(self):
        """
        V.GetExtractBoundaryCells() -> int
        C++: virtual vtkTypeBool GetExtractBoundaryCells()
        
        Boolean controls whether to extract cells that are partially
        inside. By default, ExtractBoundaryCells is off.
        """
        ...
    
    def GetExtractInside(self):
        """
        V.GetExtractInside() -> int
        C++: virtual vtkTypeBool GetExtractInside()
        
        Boolean controls whether to extract cells that are inside of
        implicit function (ExtractInside == 1) or outside of implicit
        function (ExtractInside == 0).
        """
        ...
    
    def GetImplicitFunction(self):
        """
        V.GetImplicitFunction() -> vtkImplicitFunction
        C++: virtual vtkImplicitFunction *GetImplicitFunction()
        
        Specify the implicit function for inside/outside checks.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Return the MTime taking into account changes to the implicit
        function
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
    
    def GetPassPoints(self):
        """
        V.GetPassPoints() -> int
        C++: virtual vtkTypeBool GetPassPoints()
        
        Boolean controls whether points are culled or simply passed
        through to the output.
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
        V.NewInstance() -> vtkExtractPolyDataGeometry
        C++: vtkExtractPolyDataGeometry *NewInstance()
        """
        ...
    
    def PassPointsOff(self):
        """
        V.PassPointsOff()
        C++: virtual void PassPointsOff()
        
        Boolean controls whether points are culled or simply passed
        through to the output.
        """
        ...
    
    def PassPointsOn(self):
        """
        V.PassPointsOn()
        C++: virtual void PassPointsOn()
        
        Boolean controls whether points are culled or simply passed
        through to the output.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtractPolyDataGeometry
        C++: static vtkExtractPolyDataGeometry *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetExtractBoundaryCells(self, p_int):
        """
        V.SetExtractBoundaryCells(int)
        C++: virtual void SetExtractBoundaryCells(vtkTypeBool _arg)
        
        Boolean controls whether to extract cells that are partially
        inside. By default, ExtractBoundaryCells is off.
        """
        ...
    
    def SetExtractInside(self, p_int):
        """
        V.SetExtractInside(int)
        C++: virtual void SetExtractInside(vtkTypeBool _arg)
        
        Boolean controls whether to extract cells that are inside of
        implicit function (ExtractInside == 1) or outside of implicit
        function (ExtractInside == 0).
        """
        ...
    
    def SetImplicitFunction(self, vtkImplicitFunction):
        """
        V.SetImplicitFunction(vtkImplicitFunction)
        C++: virtual void SetImplicitFunction(vtkImplicitFunction *)
        
        Specify the implicit function for inside/outside checks.
        """
        ...
    
    def SetPassPoints(self, p_int):
        """
        V.SetPassPoints(int)
        C++: virtual void SetPassPoints(vtkTypeBool _arg)
        
        Boolean controls whether points are culled or simply passed
        through to the output.
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


