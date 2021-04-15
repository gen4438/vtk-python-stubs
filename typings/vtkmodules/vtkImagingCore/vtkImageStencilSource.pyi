"""
This type stub file was generated by pyright.
"""

from .vtkImageStencilAlgorithm import vtkImageStencilAlgorithm

class vtkImageStencilSource(vtkImageStencilAlgorithm):
    """
    vtkImageStencilSource - generate an image stencil
    
    Superclass: vtkImageStencilAlgorithm
    
    vtkImageStencilSource is a superclass for filters that generate image
    stencils.  Given a clipping object such as a vtkImplicitFunction, it
    will set up a list of clipping extents for each x-row through the
    image data.  The extents for each x-row can be retrieved via the
    GetNextExtent() method after the extent lists have been built with
    the BuildExtents() method.  For large images, using clipping extents
    is much more memory efficient (and slightly more time-efficient) than
    building a mask.  This class can be subclassed to allow clipping with
    objects other than vtkImplicitFunction.
    @sa
    vtkImplicitFunction vtkImageStencil vtkPolyDataToImageStencil
    """
    def GetInformationInput(self):
        """
        V.GetInformationInput() -> vtkImageData
        C++: virtual vtkImageData *GetInformationInput()
        
        Set a vtkImageData that has the Spacing, Origin, and WholeExtent
        that will be used for the stencil.  This input should be set to
        the image that you wish to apply the stencil to.  If you use this
        method, then any values set with the SetOutputSpacing,
        SetOutputOrigin, and SetOutputWholeExtent methods will be
        ignored.
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
    
    def GetOutputOrigin(self):
        """
        V.GetOutputOrigin() -> (float, float, float)
        C++: virtual double *GetOutputOrigin()
        
        Set the Origin to be used for the stencil.  It should be set to
        the Origin of the image you intend to apply the stencil to. The
        default value is (0,0,0).
        """
        ...
    
    def GetOutputSpacing(self):
        """
        V.GetOutputSpacing() -> (float, float, float)
        C++: virtual double *GetOutputSpacing()
        
        Set the Spacing to be used for the stencil. It should be set to
        the Spacing of the image you intend to apply the stencil to. The
        default value is (1,1,1)
        """
        ...
    
    def GetOutputWholeExtent(self):
        """
        V.GetOutputWholeExtent() -> (int, int, int, int, int, int)
        C++: virtual int *GetOutputWholeExtent()
        
        Set the whole extent for the stencil (anything outside this
        extent will be considered to be "outside" the stencil).
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
        V.NewInstance() -> vtkImageStencilSource
        C++: vtkImageStencilSource *NewInstance()
        """
        ...
    
    def ReportReferences(self, vtkGarbageCollector):
        """
        V.ReportReferences(vtkGarbageCollector)
        C++: void ReportReferences(vtkGarbageCollector *) override;
        
        Report object referenced by instances of this class.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImageStencilSource
        C++: static vtkImageStencilSource *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetInformationInput(self, vtkImageData):
        """
        V.SetInformationInput(vtkImageData)
        C++: virtual void SetInformationInput(vtkImageData *)
        
        Set a vtkImageData that has the Spacing, Origin, and WholeExtent
        that will be used for the stencil.  This input should be set to
        the image that you wish to apply the stencil to.  If you use this
        method, then any values set with the SetOutputSpacing,
        SetOutputOrigin, and SetOutputWholeExtent methods will be
        ignored.
        """
        ...
    
    def SetOutputOrigin(self, p_float, p_float_1, p_float_2):
        """
        V.SetOutputOrigin(float, float, float)
        C++: virtual void SetOutputOrigin(double _arg1, double _arg2,
            double _arg3)
        V.SetOutputOrigin((float, float, float))
        C++: virtual void SetOutputOrigin(const double _arg[3])
        
        Set the Origin to be used for the stencil.  It should be set to
        the Origin of the image you intend to apply the stencil to. The
        default value is (0,0,0).
        """
        ...
    
    def SetOutputSpacing(self, p_float, p_float_1, p_float_2):
        """
        V.SetOutputSpacing(float, float, float)
        C++: virtual void SetOutputSpacing(double _arg1, double _arg2,
            double _arg3)
        V.SetOutputSpacing((float, float, float))
        C++: virtual void SetOutputSpacing(const double _arg[3])
        
        Set the Spacing to be used for the stencil. It should be set to
        the Spacing of the image you intend to apply the stencil to. The
        default value is (1,1,1)
        """
        ...
    
    def SetOutputWholeExtent(self, p_int, p_int_1, p_int_2, p_int_3, p_int_4, p_int_5):
        """
        V.SetOutputWholeExtent(int, int, int, int, int, int)
        C++: virtual void SetOutputWholeExtent(int _arg1, int _arg2,
            int _arg3, int _arg4, int _arg5, int _arg6)
        V.SetOutputWholeExtent((int, int, int, int, int, int))
        C++: virtual void SetOutputWholeExtent(const int _arg[6])
        
        Set the whole extent for the stencil (anything outside this
        extent will be considered to be "outside" the stencil).
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


