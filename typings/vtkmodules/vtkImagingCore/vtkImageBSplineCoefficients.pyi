"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkImageBSplineCoefficients(__vtkmodules_vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    """
    vtkImageBSplineCoefficients - convert image to b-spline knots
    
    Superclass: vtkThreadedImageAlgorithm
    
    vtkImageBSplineCoefficients prepares an image for b-spline
    interpolation by converting the image values into b-spline knot
    coefficients.  It is a necessary pre-filtering step before applying
    b-spline interpolation with vtkImageReslice.
    
    This class is based on code provided by Philippe Thevenaz of EPFL,
    Lausanne, Switzerland.  Please acknowledge his contribution by citing
    the following paper: [1] P. Thevenaz, T. Blu, M. Unser, "Interpolation
    Revisited,"
        IEEE Transactions on Medical Imaging 19(7):739-758, 2000.
    
    The clamped boundary condition (which is the default) is taken from
    code presented in the following paper: [2] D. Ruijters, P. Thevenaz,
        "GPU Prefilter for Accurate Cubic B-spline Interpolation,"
        The Computer Journal, doi: 10.1093/comjnl/bxq086, 2010.
    
    @par Thanks: This class was written by David Gobbi at the Seaman
    Family MR Research Centre, Foothills Medical Centre, Calgary,
    Alberta. DG Gobbi and YP Starreveld, "Uniform B-Splines for the VTK Imaging
    Pipeline," VTK Journal, 2011, http://hdl.handle.net/10380/3252
    """
    def BypassOff(self):
        """
        V.BypassOff()
        C++: virtual void BypassOff()
        
        Bypass the filter, do not do any processing.  If this is on, then
        the output data will reference the input data directly, and the
        output type will be the same as the input type.  This is useful a
        downstream filter sometimes uses b-spline interpolation and
        sometimes uses other forms of interpolation.
        """
        ...
    
    def BypassOn(self):
        """
        V.BypassOn()
        C++: virtual void BypassOn()
        
        Bypass the filter, do not do any processing.  If this is on, then
        the output data will reference the input data directly, and the
        output type will be the same as the input type.  This is useful a
        downstream filter sometimes uses b-spline interpolation and
        sometimes uses other forms of interpolation.
        """
        ...
    
    def CheckBounds(self, ):
        """
        V.CheckBounds((float, float, float)) -> int
        C++: int CheckBounds(const double point[3])
        
        Check a point against the image bounds.  Return 0 if out of
        bounds, and 1 if inside bounds.  Calling Evaluate on a point
        outside the bounds will not generate an error, but the value
        returned will depend on the BorderMode.
        """
        ...
    
    def Evaluate(self, , *float):
        """
        V.Evaluate((float, float, float), [float, ...])
        C++: void Evaluate(const double point[3], double *value)
        V.Evaluate(float, float, float) -> float
        C++: double Evaluate(double x, double y, double z)
        V.Evaluate((float, float, float)) -> float
        C++: double Evaluate(const double point[3])
        
        Interpolate a value from the image.  You must call Update()
        before calling this method for the first time.  The first
        signature can return multiple components, while the second
        signature is for use on single-component images.
        """
        ...
    
    def GetBorderMode(self):
        """
        V.GetBorderMode() -> int
        C++: virtual int GetBorderMode()
        
        Set the border mode.  The filter that is used to create the
        coefficients must repeat the image somehow to make a
        theoritically infinite input.  The default is to clamp values
        that are off the edge of the image, to the value at the closest
        point on the edge. The other ways of virtually extending the
        image are to produce mirrored copies, which results in optimal
        smoothness at the boundary, or to repeat the image, which results
        in a cyclic or periodic spline.
        """
        ...
    
    def GetBorderModeAsString(self):
        """
        V.GetBorderModeAsString() -> string
        C++: const char *GetBorderModeAsString()
        
        Set the border mode.  The filter that is used to create the
        coefficients must repeat the image somehow to make a
        theoritically infinite input.  The default is to clamp values
        that are off the edge of the image, to the value at the closest
        point on the edge. The other ways of virtually extending the
        image are to produce mirrored copies, which results in optimal
        smoothness at the boundary, or to repeat the image, which results
        in a cyclic or periodic spline.
        """
        ...
    
    def GetBorderModeMaxValue(self):
        """
        V.GetBorderModeMaxValue() -> int
        C++: virtual int GetBorderModeMaxValue()
        
        Set the border mode.  The filter that is used to create the
        coefficients must repeat the image somehow to make a
        theoritically infinite input.  The default is to clamp values
        that are off the edge of the image, to the value at the closest
        point on the edge. The other ways of virtually extending the
        image are to produce mirrored copies, which results in optimal
        smoothness at the boundary, or to repeat the image, which results
        in a cyclic or periodic spline.
        """
        ...
    
    def GetBorderModeMinValue(self):
        """
        V.GetBorderModeMinValue() -> int
        C++: virtual int GetBorderModeMinValue()
        
        Set the border mode.  The filter that is used to create the
        coefficients must repeat the image somehow to make a
        theoritically infinite input.  The default is to clamp values
        that are off the edge of the image, to the value at the closest
        point on the edge. The other ways of virtually extending the
        image are to produce mirrored copies, which results in optimal
        smoothness at the boundary, or to repeat the image, which results
        in a cyclic or periodic spline.
        """
        ...
    
    def GetBypass(self):
        """
        V.GetBypass() -> int
        C++: virtual vtkTypeBool GetBypass()
        
        Bypass the filter, do not do any processing.  If this is on, then
        the output data will reference the input data directly, and the
        output type will be the same as the input type.  This is useful a
        downstream filter sometimes uses b-spline interpolation and
        sometimes uses other forms of interpolation.
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
    
    def GetOutputScalarType(self):
        """
        V.GetOutputScalarType() -> int
        C++: virtual int GetOutputScalarType()
        
        Set the scalar type of the output.  Default is float.
        Floating-point output is used to avoid overflow, since the range
        of the output values is larger than the input values.
        """
        ...
    
    def GetOutputScalarTypeAsString(self):
        """
        V.GetOutputScalarTypeAsString() -> string
        C++: const char *GetOutputScalarTypeAsString()
        
        Set the scalar type of the output.  Default is float.
        Floating-point output is used to avoid overflow, since the range
        of the output values is larger than the input values.
        """
        ...
    
    def GetOutputScalarTypeMaxValue(self):
        """
        V.GetOutputScalarTypeMaxValue() -> int
        C++: virtual int GetOutputScalarTypeMaxValue()
        
        Set the scalar type of the output.  Default is float.
        Floating-point output is used to avoid overflow, since the range
        of the output values is larger than the input values.
        """
        ...
    
    def GetOutputScalarTypeMinValue(self):
        """
        V.GetOutputScalarTypeMinValue() -> int
        C++: virtual int GetOutputScalarTypeMinValue()
        
        Set the scalar type of the output.  Default is float.
        Floating-point output is used to avoid overflow, since the range
        of the output values is larger than the input values.
        """
        ...
    
    def GetSplineDegree(self):
        """
        V.GetSplineDegree() -> int
        C++: virtual int GetSplineDegree()
        
        Set the degree of the spline polynomial.  The default value is 3,
        and the maximum is 9.
        """
        ...
    
    def GetSplineDegreeMaxValue(self):
        """
        V.GetSplineDegreeMaxValue() -> int
        C++: virtual int GetSplineDegreeMaxValue()
        
        Set the degree of the spline polynomial.  The default value is 3,
        and the maximum is 9.
        """
        ...
    
    def GetSplineDegreeMinValue(self):
        """
        V.GetSplineDegreeMinValue() -> int
        C++: virtual int GetSplineDegreeMinValue()
        
        Set the degree of the spline polynomial.  The default value is 3,
        and the maximum is 9.
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
        V.NewInstance() -> vtkImageBSplineCoefficients
        C++: vtkImageBSplineCoefficients *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImageBSplineCoefficients
        C++: static vtkImageBSplineCoefficients *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetBorderMode(self, p_int):
        """
        V.SetBorderMode(int)
        C++: virtual void SetBorderMode(int _arg)
        
        Set the border mode.  The filter that is used to create the
        coefficients must repeat the image somehow to make a
        theoritically infinite input.  The default is to clamp values
        that are off the edge of the image, to the value at the closest
        point on the edge. The other ways of virtually extending the
        image are to produce mirrored copies, which results in optimal
        smoothness at the boundary, or to repeat the image, which results
        in a cyclic or periodic spline.
        """
        ...
    
    def SetBorderModeToClamp(self):
        """
        V.SetBorderModeToClamp()
        C++: void SetBorderModeToClamp()
        
        Set the border mode.  The filter that is used to create the
        coefficients must repeat the image somehow to make a
        theoritically infinite input.  The default is to clamp values
        that are off the edge of the image, to the value at the closest
        point on the edge. The other ways of virtually extending the
        image are to produce mirrored copies, which results in optimal
        smoothness at the boundary, or to repeat the image, which results
        in a cyclic or periodic spline.
        """
        ...
    
    def SetBorderModeToMirror(self):
        """
        V.SetBorderModeToMirror()
        C++: void SetBorderModeToMirror()
        
        Set the border mode.  The filter that is used to create the
        coefficients must repeat the image somehow to make a
        theoritically infinite input.  The default is to clamp values
        that are off the edge of the image, to the value at the closest
        point on the edge. The other ways of virtually extending the
        image are to produce mirrored copies, which results in optimal
        smoothness at the boundary, or to repeat the image, which results
        in a cyclic or periodic spline.
        """
        ...
    
    def SetBorderModeToRepeat(self):
        """
        V.SetBorderModeToRepeat()
        C++: void SetBorderModeToRepeat()
        
        Set the border mode.  The filter that is used to create the
        coefficients must repeat the image somehow to make a
        theoritically infinite input.  The default is to clamp values
        that are off the edge of the image, to the value at the closest
        point on the edge. The other ways of virtually extending the
        image are to produce mirrored copies, which results in optimal
        smoothness at the boundary, or to repeat the image, which results
        in a cyclic or periodic spline.
        """
        ...
    
    def SetBypass(self, p_int):
        """
        V.SetBypass(int)
        C++: virtual void SetBypass(vtkTypeBool _arg)
        
        Bypass the filter, do not do any processing.  If this is on, then
        the output data will reference the input data directly, and the
        output type will be the same as the input type.  This is useful a
        downstream filter sometimes uses b-spline interpolation and
        sometimes uses other forms of interpolation.
        """
        ...
    
    def SetOutputScalarType(self, p_int):
        """
        V.SetOutputScalarType(int)
        C++: virtual void SetOutputScalarType(int _arg)
        
        Set the scalar type of the output.  Default is float.
        Floating-point output is used to avoid overflow, since the range
        of the output values is larger than the input values.
        """
        ...
    
    def SetOutputScalarTypeToDouble(self):
        """
        V.SetOutputScalarTypeToDouble()
        C++: void SetOutputScalarTypeToDouble()
        
        Set the scalar type of the output.  Default is float.
        Floating-point output is used to avoid overflow, since the range
        of the output values is larger than the input values.
        """
        ...
    
    def SetOutputScalarTypeToFloat(self):
        """
        V.SetOutputScalarTypeToFloat()
        C++: void SetOutputScalarTypeToFloat()
        
        Set the scalar type of the output.  Default is float.
        Floating-point output is used to avoid overflow, since the range
        of the output values is larger than the input values.
        """
        ...
    
    def SetSplineDegree(self, p_int):
        """
        V.SetSplineDegree(int)
        C++: virtual void SetSplineDegree(int _arg)
        
        Set the degree of the spline polynomial.  The default value is 3,
        and the maximum is 9.
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

