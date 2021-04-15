"""
This type stub file was generated by pyright.
"""

from .vtkPolyDataMapper import vtkPolyDataMapper

class vtkPointGaussianMapper(vtkPolyDataMapper):
    """
    vtkPointGaussianMapper - draw PointGaussians using imposters
    
    Superclass: vtkPolyDataMapper
    
    A mapper that uses imposters to draw gaussian splats or other shapes
    if custom shader code is set. Supports transparency and picking as
    well. It draws all the points and does not require cell arrays. If
    cell arrays are provided it will only draw the points used by the
    Verts cell array. The shape of the imposter is a triangle.
    """
    def EmissiveOff(self):
        """
        V.EmissiveOff()
        C++: virtual void EmissiveOff()
        
        Treat the points/splats as emissive light sources. The default is
        true.
        """
        ...
    
    def EmissiveOn(self):
        """
        V.EmissiveOn()
        C++: virtual void EmissiveOn()
        
        Treat the points/splats as emissive light sources. The default is
        true.
        """
        ...
    
    def GetEmissive(self):
        """
        V.GetEmissive() -> int
        C++: virtual vtkTypeBool GetEmissive()
        
        Treat the points/splats as emissive light sources. The default is
        true.
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
    
    def GetOpacityArray(self):
        """
        V.GetOpacityArray() -> string
        C++: virtual char *GetOpacityArray()
        
        Method to set the optional opacity array.  If specified this
        array will be used to generate the opacity values.
        """
        ...
    
    def GetOpacityArrayComponent(self):
        """
        V.GetOpacityArrayComponent() -> int
        C++: virtual int GetOpacityArrayComponent()
        
        Convenience method to set the component of the array to opacify
        with.
        """
        ...
    
    def GetOpacityTableSize(self):
        """
        V.GetOpacityTableSize() -> int
        C++: virtual int GetOpacityTableSize()
        
        The size of the table used in computing opacities, used when
        converting a vtkPiecewiseFunction to a table
        """
        ...
    
    def GetScalarOpacityFunction(self):
        """
        V.GetScalarOpacityFunction() -> vtkPiecewiseFunction
        C++: virtual vtkPiecewiseFunction *GetScalarOpacityFunction()
        
        Set/Get the optional opacity transfer function. This is only used
        when an OpacityArray is also specified.
        """
        ...
    
    def GetScaleArray(self):
        """
        V.GetScaleArray() -> string
        C++: virtual char *GetScaleArray()
        
        Convenience method to set the array to scale with.
        """
        ...
    
    def GetScaleArrayComponent(self):
        """
        V.GetScaleArrayComponent() -> int
        C++: virtual int GetScaleArrayComponent()
        
        Convenience method to set the component of the array to scale
        with.
        """
        ...
    
    def GetScaleFactor(self):
        """
        V.GetScaleFactor() -> float
        C++: virtual double GetScaleFactor()
        
        Set the default scale factor of the point gaussians.  This
        defaults to 1.0. All radius computations will be scaled by the
        factor including the ScaleArray. If a vtkPiecewideFunction is
        used the scaling happens prior to the function lookup. A scale
        factor of 0.0 indicates that the splats should be rendered as
        simple points.
        """
        ...
    
    def GetScaleFunction(self):
        """
        V.GetScaleFunction() -> vtkPiecewiseFunction
        C++: virtual vtkPiecewiseFunction *GetScaleFunction()
        
        Set/Get the optional scale transfer function. This is only used
        when a ScaleArray is also specified.
        """
        ...
    
    def GetScaleTableSize(self):
        """
        V.GetScaleTableSize() -> int
        C++: virtual int GetScaleTableSize()
        
        The size of the table used in computing scale, used when
        converting a vtkPiecewiseFunction to a table
        """
        ...
    
    def GetSplatShaderCode(self):
        """
        V.GetSplatShaderCode() -> string
        C++: virtual char *GetSplatShaderCode()
        
        Method to override the fragment shader code for the splat.  You
        can set this to draw other shapes. For the OPenGL2 backend some
        of the variables you can use and/or modify include, opacity - 0.0
        to 1.0 diffuseColor - vec3 ambientColor - vec3 offsetVCVSOutput -
        vec2 offset in view coordinates from the splat center
        """
        ...
    
    def GetSupportsSelection(self):
        """
        V.GetSupportsSelection() -> bool
        C++: bool GetSupportsSelection() override;
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS Used by
        vtkHardwareSelector to determine if the prop supports hardware
        selection.
        """
        ...
    
    def GetTriangleScale(self):
        """
        V.GetTriangleScale() -> float
        C++: virtual float GetTriangleScale()
        
        When drawing triangles as opposed too point mode (triangles are
        for splats shaders that are bigger than a pixel) this controls
        how large the triangle will be. By default it is large enough to
        contain a cicle of radius 3.0*scale which works well for gaussian
        splats as after 3.0 standard deviations the opacity is near zero.
        For custom shader codes a different value can be used. Generally
        you should use the lowest value you can as it will result in
        fewer fragments. For example if your custom shader only draws a
        disc of radius 1.0*scale, then set this to 1.0 to avoid sending
        many fragments to the shader that will just get discarded.
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
        V.NewInstance() -> vtkPointGaussianMapper
        C++: vtkPointGaussianMapper *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPointGaussianMapper
        C++: static vtkPointGaussianMapper *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetEmissive(self, p_int):
        """
        V.SetEmissive(int)
        C++: virtual void SetEmissive(vtkTypeBool _arg)
        
        Treat the points/splats as emissive light sources. The default is
        true.
        """
        ...
    
    def SetOpacityArray(self, string):
        """
        V.SetOpacityArray(string)
        C++: virtual void SetOpacityArray(const char *_arg)
        
        Method to set the optional opacity array.  If specified this
        array will be used to generate the opacity values.
        """
        ...
    
    def SetOpacityArrayComponent(self, p_int):
        """
        V.SetOpacityArrayComponent(int)
        C++: virtual void SetOpacityArrayComponent(int _arg)
        
        Convenience method to set the component of the array to opacify
        with.
        """
        ...
    
    def SetOpacityTableSize(self, p_int):
        """
        V.SetOpacityTableSize(int)
        C++: virtual void SetOpacityTableSize(int _arg)
        
        The size of the table used in computing opacities, used when
        converting a vtkPiecewiseFunction to a table
        """
        ...
    
    def SetScalarOpacityFunction(self, vtkPiecewiseFunction):
        """
        V.SetScalarOpacityFunction(vtkPiecewiseFunction)
        C++: void SetScalarOpacityFunction(vtkPiecewiseFunction *)
        
        Set/Get the optional opacity transfer function. This is only used
        when an OpacityArray is also specified.
        """
        ...
    
    def SetScaleArray(self, string):
        """
        V.SetScaleArray(string)
        C++: virtual void SetScaleArray(const char *_arg)
        
        Convenience method to set the array to scale with.
        """
        ...
    
    def SetScaleArrayComponent(self, p_int):
        """
        V.SetScaleArrayComponent(int)
        C++: virtual void SetScaleArrayComponent(int _arg)
        
        Convenience method to set the component of the array to scale
        with.
        """
        ...
    
    def SetScaleFactor(self, p_float):
        """
        V.SetScaleFactor(float)
        C++: virtual void SetScaleFactor(double _arg)
        
        Set the default scale factor of the point gaussians.  This
        defaults to 1.0. All radius computations will be scaled by the
        factor including the ScaleArray. If a vtkPiecewideFunction is
        used the scaling happens prior to the function lookup. A scale
        factor of 0.0 indicates that the splats should be rendered as
        simple points.
        """
        ...
    
    def SetScaleFunction(self, vtkPiecewiseFunction):
        """
        V.SetScaleFunction(vtkPiecewiseFunction)
        C++: void SetScaleFunction(vtkPiecewiseFunction *)
        
        Set/Get the optional scale transfer function. This is only used
        when a ScaleArray is also specified.
        """
        ...
    
    def SetScaleTableSize(self, p_int):
        """
        V.SetScaleTableSize(int)
        C++: virtual void SetScaleTableSize(int _arg)
        
        The size of the table used in computing scale, used when
        converting a vtkPiecewiseFunction to a table
        """
        ...
    
    def SetSplatShaderCode(self, string):
        """
        V.SetSplatShaderCode(string)
        C++: virtual void SetSplatShaderCode(const char *_arg)
        
        Method to override the fragment shader code for the splat.  You
        can set this to draw other shapes. For the OPenGL2 backend some
        of the variables you can use and/or modify include, opacity - 0.0
        to 1.0 diffuseColor - vec3 ambientColor - vec3 offsetVCVSOutput -
        vec2 offset in view coordinates from the splat center
        """
        ...
    
    def SetTriangleScale(self, p_float):
        """
        V.SetTriangleScale(float)
        C++: virtual void SetTriangleScale(float _arg)
        
        When drawing triangles as opposed too point mode (triangles are
        for splats shaders that are bigger than a pixel) this controls
        how large the triangle will be. By default it is large enough to
        contain a cicle of radius 3.0*scale which works well for gaussian
        splats as after 3.0 standard deviations the opacity is near zero.
        For custom shader codes a different value can be used. Generally
        you should use the lowest value you can as it will result in
        fewer fragments. For example if your custom shader only draws a
        disc of radius 1.0*scale, then set this to 1.0 to avoid sending
        many fragments to the shader that will just get discarded.
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


