"""
This type stub file was generated by pyright.
"""

from .vtkCuller import vtkCuller

class vtkFrustumCoverageCuller(vtkCuller):
    """
    vtkFrustumCoverageCuller - cull props based on frustum coverage
    
    Superclass: vtkCuller
    
    vtkFrustumCoverageCuller will cull props based on the coverage in the
    view frustum. The coverage is computed by enclosing the prop in a
    bounding sphere, projecting that to the viewing coordinate system,
    then taking a slice through the view frustum at the center of the
    sphere. This results in a circle on the plane slice through the view
    frustum. This circle is enclosed in a squared, and the fraction of
    the plane slice that this square covers is the coverage. This is a
    number between 0 and 1. If the number is less than the
    MinimumCoverage, the allocated render time for that prop is set to
    zero. If it is greater than the MaximumCoverage, the allocated render
    time is set to 1.0. In between, a linear ramp is used to convert
    coverage into allocated render time.
    
    @sa
    vtkCuller
    """
    def GetMaximumCoverage(self):
        """
        V.GetMaximumCoverage() -> float
        C++: virtual double GetMaximumCoverage()
        
        Set/Get the maximum coverage - props with more coverage than this
        are given an allocated render time of 1.0 (the maximum)
        """
        ...
    
    def GetMinimumCoverage(self):
        """
        V.GetMinimumCoverage() -> float
        C++: virtual double GetMinimumCoverage()
        
        Set/Get the minimum coverage - props with less coverage than this
        are given no time to render (they are culled)
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
    
    def GetSortingStyle(self):
        """
        V.GetSortingStyle() -> int
        C++: virtual int GetSortingStyle()
        
        Set the sorting style - none, front-to-back or back-to-front The
        default is none
        """
        ...
    
    def GetSortingStyleAsString(self):
        """
        V.GetSortingStyleAsString() -> string
        C++: const char *GetSortingStyleAsString(void)
        
        Set the sorting style - none, front-to-back or back-to-front The
        default is none
        """
        ...
    
    def GetSortingStyleMaxValue(self):
        """
        V.GetSortingStyleMaxValue() -> int
        C++: virtual int GetSortingStyleMaxValue()
        
        Set the sorting style - none, front-to-back or back-to-front The
        default is none
        """
        ...
    
    def GetSortingStyleMinValue(self):
        """
        V.GetSortingStyleMinValue() -> int
        C++: virtual int GetSortingStyleMinValue()
        
        Set the sorting style - none, front-to-back or back-to-front The
        default is none
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
        V.NewInstance() -> vtkFrustumCoverageCuller
        C++: vtkFrustumCoverageCuller *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkFrustumCoverageCuller
        C++: static vtkFrustumCoverageCuller *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetMaximumCoverage(self, p_float):
        """
        V.SetMaximumCoverage(float)
        C++: virtual void SetMaximumCoverage(double _arg)
        
        Set/Get the maximum coverage - props with more coverage than this
        are given an allocated render time of 1.0 (the maximum)
        """
        ...
    
    def SetMinimumCoverage(self, p_float):
        """
        V.SetMinimumCoverage(float)
        C++: virtual void SetMinimumCoverage(double _arg)
        
        Set/Get the minimum coverage - props with less coverage than this
        are given no time to render (they are culled)
        """
        ...
    
    def SetSortingStyle(self, p_int):
        """
        V.SetSortingStyle(int)
        C++: virtual void SetSortingStyle(int _arg)
        
        Set the sorting style - none, front-to-back or back-to-front The
        default is none
        """
        ...
    
    def SetSortingStyleToBackToFront(self):
        """
        V.SetSortingStyleToBackToFront()
        C++: void SetSortingStyleToBackToFront()
        
        Set the sorting style - none, front-to-back or back-to-front The
        default is none
        """
        ...
    
    def SetSortingStyleToFrontToBack(self):
        """
        V.SetSortingStyleToFrontToBack()
        C++: void SetSortingStyleToFrontToBack()
        
        Set the sorting style - none, front-to-back or back-to-front The
        default is none
        """
        ...
    
    def SetSortingStyleToNone(self):
        """
        V.SetSortingStyleToNone()
        C++: void SetSortingStyleToNone()
        
        Set the sorting style - none, front-to-back or back-to-front The
        default is none
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


