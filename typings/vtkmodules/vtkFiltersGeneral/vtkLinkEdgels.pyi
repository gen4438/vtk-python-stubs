"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkLinkEdgels(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkLinkEdgels - links edgels together to form digital curves.
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkLinkEdgels links edgels into digital curves which are then stored
    as polylines. The algorithm works one pixel at a time only looking at
    its immediate neighbors. There is a GradientThreshold that can be set
    that eliminates any pixels with a smaller gradient value. This can be
    used as the lower threshold of a two value edgel thresholding.
    
    For the remaining edgels, links are first tried for the four
    connected neighbors.  A successful neighbor will satisfy three tests.
    First both edgels must be above the gradient threshold. Second, the
    difference between the orientation between the two edgels (Alpha) and
    each edgels orientation (Phi) must be less than LinkThreshold. Third,
    the difference between the two edgels Phi values must be less than
    PhiThreshold. The most successful link is selected. The measure is
    simply the sum of the three angle differences (actually stored as the
    sum of the cosines). If none of the four connect neighbors succeeds,
    then the eight connect neighbors are examined using the same method.
    
    This filter requires gradient information so you will need to use a
    vtkImageGradient at some point prior to this filter.  Typically a
    vtkNonMaximumSuppression filter is also used. vtkThresholdEdgels can
    be used to complete the two value edgel thresholding as used in a
    Canny edge detector. The vtkSubpixelPositionEdgels filter can also be
    used after this filter to adjust the edgel locations.
    
    @sa
    vtkImageData vtkImageGradient vtkImageNonMaximumSuppression
    """
    def GetGradientThreshold(self):
        """
        V.GetGradientThreshold() -> float
        C++: virtual double GetGradientThreshold()
        
        Set/Get the threshold for image gradient thresholding.
        """
        ...
    
    def GetLinkThreshold(self):
        """
        V.GetLinkThreshold() -> float
        C++: virtual double GetLinkThreshold()
        
        Set/Get the threshold for Phi vs. Alpha link thresholding.
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
    
    def GetPhiThreshold(self):
        """
        V.GetPhiThreshold() -> float
        C++: virtual double GetPhiThreshold()
        
        Set/get the threshold for Phi vs. Phi link thresholding.
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
        V.NewInstance() -> vtkLinkEdgels
        C++: vtkLinkEdgels *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkLinkEdgels
        C++: static vtkLinkEdgels *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetGradientThreshold(self, p_float):
        """
        V.SetGradientThreshold(float)
        C++: virtual void SetGradientThreshold(double _arg)
        
        Set/Get the threshold for image gradient thresholding.
        """
        ...
    
    def SetLinkThreshold(self, p_float):
        """
        V.SetLinkThreshold(float)
        C++: virtual void SetLinkThreshold(double _arg)
        
        Set/Get the threshold for Phi vs. Alpha link thresholding.
        """
        ...
    
    def SetPhiThreshold(self, p_float):
        """
        V.SetPhiThreshold(float)
        C++: virtual void SetPhiThreshold(double _arg)
        
        Set/get the threshold for Phi vs. Phi link thresholding.
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


