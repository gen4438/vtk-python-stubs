"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkEncodedGradientShader(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkEncodedGradientShader - Compute shading tables for encoded normals.
    
    Superclass: vtkObject
    
    vtkEncodedGradientShader computes shading tables for encoded normals
    that indicates the amount of diffuse and specular illumination that
    is received from all light sources at a surface location with that
    normal. For diffuse illumination this is accurate, but for specular
    illumination it is approximate for perspective projections since the
    center view direction is always used as the view direction. Since the
    shading table is dependent on the volume (for the transformation that
    must be applied to the normals to put them into world coordinates)
    there is a shading table per volume. This is necessary because
    multiple volumes can share a volume mapper.
    """
    def GetActiveComponent(self):
        """
        V.GetActiveComponent() -> int
        C++: virtual int GetActiveComponent()
        
        Set the active component for shading. This component's ambient /
        diffuse / specular / specular power values will be used to create
        the shading table. The default is 1.0
        """
        ...
    
    def GetActiveComponentMaxValue(self):
        """
        V.GetActiveComponentMaxValue() -> int
        C++: virtual int GetActiveComponentMaxValue()
        
        Set the active component for shading. This component's ambient /
        diffuse / specular / specular power values will be used to create
        the shading table. The default is 1.0
        """
        ...
    
    def GetActiveComponentMinValue(self):
        """
        V.GetActiveComponentMinValue() -> int
        C++: virtual int GetActiveComponentMinValue()
        
        Set the active component for shading. This component's ambient /
        diffuse / specular / specular power values will be used to create
        the shading table. The default is 1.0
        """
        ...
    
    def GetBlueDiffuseShadingTable(self, vtkVolume):
        """
        V.GetBlueDiffuseShadingTable(vtkVolume) -> (float, ...)
        C++: float *GetBlueDiffuseShadingTable(vtkVolume *vol)
        
        Get the red/green/blue shading table.
        """
        ...
    
    def GetBlueSpecularShadingTable(self, vtkVolume):
        """
        V.GetBlueSpecularShadingTable(vtkVolume) -> (float, ...)
        C++: float *GetBlueSpecularShadingTable(vtkVolume *vol)
        
        Get the red/green/blue shading table.
        """
        ...
    
    def GetGreenDiffuseShadingTable(self, vtkVolume):
        """
        V.GetGreenDiffuseShadingTable(vtkVolume) -> (float, ...)
        C++: float *GetGreenDiffuseShadingTable(vtkVolume *vol)
        
        Get the red/green/blue shading table.
        """
        ...
    
    def GetGreenSpecularShadingTable(self, vtkVolume):
        """
        V.GetGreenSpecularShadingTable(vtkVolume) -> (float, ...)
        C++: float *GetGreenSpecularShadingTable(vtkVolume *vol)
        
        Get the red/green/blue shading table.
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
    
    def GetRedDiffuseShadingTable(self, vtkVolume):
        """
        V.GetRedDiffuseShadingTable(vtkVolume) -> (float, ...)
        C++: float *GetRedDiffuseShadingTable(vtkVolume *vol)
        
        Get the red/green/blue shading table.
        """
        ...
    
    def GetRedSpecularShadingTable(self, vtkVolume):
        """
        V.GetRedSpecularShadingTable(vtkVolume) -> (float, ...)
        C++: float *GetRedSpecularShadingTable(vtkVolume *vol)
        
        Get the red/green/blue shading table.
        """
        ...
    
    def GetZeroNormalDiffuseIntensity(self):
        """
        V.GetZeroNormalDiffuseIntensity() -> float
        C++: virtual float GetZeroNormalDiffuseIntensity()
        
        Set / Get the intensity diffuse / specular light used for the
        zero normals.
        """
        ...
    
    def GetZeroNormalDiffuseIntensityMaxValue(self):
        """
        V.GetZeroNormalDiffuseIntensityMaxValue() -> float
        C++: virtual float GetZeroNormalDiffuseIntensityMaxValue()
        
        Set / Get the intensity diffuse / specular light used for the
        zero normals.
        """
        ...
    
    def GetZeroNormalDiffuseIntensityMinValue(self):
        """
        V.GetZeroNormalDiffuseIntensityMinValue() -> float
        C++: virtual float GetZeroNormalDiffuseIntensityMinValue()
        
        Set / Get the intensity diffuse / specular light used for the
        zero normals.
        """
        ...
    
    def GetZeroNormalSpecularIntensity(self):
        """
        V.GetZeroNormalSpecularIntensity() -> float
        C++: virtual float GetZeroNormalSpecularIntensity()
        
        Set / Get the intensity diffuse / specular light used for the
        zero normals.
        """
        ...
    
    def GetZeroNormalSpecularIntensityMaxValue(self):
        """
        V.GetZeroNormalSpecularIntensityMaxValue() -> float
        C++: virtual float GetZeroNormalSpecularIntensityMaxValue()
        
        Set / Get the intensity diffuse / specular light used for the
        zero normals.
        """
        ...
    
    def GetZeroNormalSpecularIntensityMinValue(self):
        """
        V.GetZeroNormalSpecularIntensityMinValue() -> float
        C++: virtual float GetZeroNormalSpecularIntensityMinValue()
        
        Set / Get the intensity diffuse / specular light used for the
        zero normals.
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
        V.NewInstance() -> vtkEncodedGradientShader
        C++: vtkEncodedGradientShader *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkEncodedGradientShader
        C++: static vtkEncodedGradientShader *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetActiveComponent(self, p_int):
        """
        V.SetActiveComponent(int)
        C++: virtual void SetActiveComponent(int _arg)
        
        Set the active component for shading. This component's ambient /
        diffuse / specular / specular power values will be used to create
        the shading table. The default is 1.0
        """
        ...
    
    def SetZeroNormalDiffuseIntensity(self, p_float):
        """
        V.SetZeroNormalDiffuseIntensity(float)
        C++: virtual void SetZeroNormalDiffuseIntensity(float _arg)
        
        Set / Get the intensity diffuse / specular light used for the
        zero normals.
        """
        ...
    
    def SetZeroNormalSpecularIntensity(self, p_float):
        """
        V.SetZeroNormalSpecularIntensity(float)
        C++: virtual void SetZeroNormalSpecularIntensity(float _arg)
        
        Set / Get the intensity diffuse / specular light used for the
        zero normals.
        """
        ...
    
    def UpdateShadingTable(self, vtkRenderer, vtkVolume, vtkEncodedGradientEstimator):
        """
        V.UpdateShadingTable(vtkRenderer, vtkVolume,
            vtkEncodedGradientEstimator)
        C++: void UpdateShadingTable(vtkRenderer *ren, vtkVolume *vol,
            vtkEncodedGradientEstimator *gradest)
        
        Cause the shading table to be updated
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

