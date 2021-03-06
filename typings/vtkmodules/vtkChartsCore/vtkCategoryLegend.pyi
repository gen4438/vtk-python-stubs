"""
This type stub file was generated by pyright.
"""

from .vtkChartLegend import vtkChartLegend

class vtkCategoryLegend(vtkChartLegend):
    """
    vtkCategoryLegend - Legend item to display categorical data.
    
    Superclass: vtkChartLegend
    
    vtkCategoryLegend will display a label and color patch for each value
    in a categorical data set.  To use this class, you must first
    populate a vtkScalarsToColors by using the SetAnnotation() method. 
    The other input to this class is a vtkVariantArray.  This should
    contain the annotated values from the vtkScalarsToColors that you
    wish to include within the legend.
    """
    def GetBoundingRect(self, vtkContext2D):
        """
        V.GetBoundingRect(vtkContext2D) -> vtkRectf
        C++: vtkRectf GetBoundingRect(vtkContext2D *painter) override;
        
        Compute and return the lower left corner of this legend, along
        with its width and height.
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
    
    def GetOutlierLabel(self):
        """
        V.GetOutlierLabel() -> string
        C++: virtual vtkStdString GetOutlierLabel()
        
        Get/set the label to use for outlier data.
        """
        ...
    
    def GetScalarsToColors(self):
        """
        V.GetScalarsToColors() -> vtkScalarsToColors
        C++: virtual vtkScalarsToColors *GetScalarsToColors()
        
        Get/Set the vtkScalarsToColors used to draw this legend. Since
        this legend represents categorical data, this vtkScalarsToColors
        must have been populated using SetAnnotation().
        """
        ...
    
    def GetTitle(self):
        """
        V.GetTitle() -> string
        C++: virtual vtkStdString GetTitle()
        
        Get/set the title text of the legend.
        """
        ...
    
    def GetValues(self):
        """
        V.GetValues() -> vtkVariantArray
        C++: virtual vtkVariantArray *GetValues()
        
        Get/Set the array of values that will be represented by this
        legend. This array must contain distinct annotated values from
        the ScalarsToColors. Each value in this array will be drawn as a
        separate entry within this legend.
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
        V.NewInstance() -> vtkCategoryLegend
        C++: vtkCategoryLegend *NewInstance()
        """
        ...
    
    def Paint(self, vtkContext2D):
        """
        V.Paint(vtkContext2D) -> bool
        C++: bool Paint(vtkContext2D *painter) override;
        
        Paint the legend into a rectangle defined by the bounds.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCategoryLegend
        C++: static vtkCategoryLegend *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetOutlierLabel(self, string):
        """
        V.SetOutlierLabel(string)
        C++: virtual void SetOutlierLabel(vtkStdString _arg)
        
        Get/set the label to use for outlier data.
        """
        ...
    
    def SetScalarsToColors(self, vtkScalarsToColors):
        """
        V.SetScalarsToColors(vtkScalarsToColors)
        C++: virtual void SetScalarsToColors(vtkScalarsToColors *stc)
        
        Get/Set the vtkScalarsToColors used to draw this legend. Since
        this legend represents categorical data, this vtkScalarsToColors
        must have been populated using SetAnnotation().
        """
        ...
    
    def SetTitle(self, string):
        """
        V.SetTitle(string)
        C++: virtual void SetTitle(const vtkStdString &title)
        
        Get/set the title text of the legend.
        """
        ...
    
    def SetValues(self, vtkVariantArray):
        """
        V.SetValues(vtkVariantArray)
        C++: virtual void SetValues(vtkVariantArray *_arg)
        
        Get/Set the array of values that will be represented by this
        legend. This array must contain distinct annotated values from
        the ScalarsToColors. Each value in this array will be drawn as a
        separate entry within this legend.
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
    HORIZONTAL = ...
    VERTICAL = ...
    __dict__ = ...
    __vtkname__ = ...


