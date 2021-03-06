"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkRenderingCore as __vtkmodules_vtkRenderingCore

class vtkVolumeMapper(__vtkmodules_vtkRenderingCore.vtkAbstractVolumeMapper):
    """
    vtkVolumeMapper - Abstract class for a volume mapper
    
    Superclass: vtkAbstractVolumeMapper
    
    vtkVolumeMapper is the abstract definition of a volume mapper for
    regular rectilinear data (vtkImageData). Several basic types of
    volume mappers are supported.
    """
    def CroppingOff(self):
        """
        V.CroppingOff()
        C++: virtual void CroppingOff()
        
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
        ...
    
    def CroppingOn(self):
        """
        V.CroppingOn()
        C++: virtual void CroppingOn()
        
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
        ...
    
    def GetAverageIPScalarRange(self):
        """
        V.GetAverageIPScalarRange() -> (float, float)
        C++: virtual double *GetAverageIPScalarRange()
        
        Set/Get the scalar range to be considered for average intensity
        projection blend mode. Only scalar values between this range will
        be averaged during ray casting. This can be useful when volume
        rendering CT datasets where the areas occupied by air would
        deviate the final rendering. By default, the range is set to
        (VTK_FLOAT_MIN, VTK_FLOAT_MAX).
        \sa SetBlendModeToAverageIntensity()
        """
        ...
    
    def GetBlendMode(self):
        """
        V.GetBlendMode() -> int
        C++: virtual int GetBlendMode()
        
        Set/Get the blend mode. The default mode is Composite where the
        scalar values are sampled through the volume and composited in a
        front-to-back scheme through alpha blending. The final color and
        opacity is determined using the color and opacity transfer
        functions.
        
        Maximum and minimum intensity blend modes use the maximum and
        minimum scalar values, respectively, along the sampling ray. The
        final color and opacity is determined by passing the resultant
        value through the color and opacity transfer functions.
        
        Additive blend mode accumulates scalar values by passing each
        value through the opacity transfer function and then adding up
        the product of the value and its opacity. In other words, the
        scalar values are scaled using the opacity transfer function and
        summed to derive the final color. Note that the resulting image
        is always grayscale i.e. aggregated values are not passed through
        the color transfer function. This is because the final value is a
        derived value and not a real data value along the sampling ray.
        
        Average intensity blend mode works similar to the additive blend
        mode where the scalar values are multiplied by opacity calculated
        from the opacity transfer function and then added. The additional
        step here is to divide the sum by the number of samples taken
        through the volume. One can control the scalar range by setting
        the AverageIPScalarRange ivar to disregard scalar values, not in
        the range of interest, from the average computation. As is the
        case with the additive intensity projection, the final image will
        always be grayscale i.e. the aggregated values are not passed
        through the color transfer function. This is because the
        resultant value is a derived value and not a real data value
        along the sampling ray.
        
        IsoSurface blend mode uses contour values defined by the user in
        order to display scalar values only when the ray crosses the
        contour. It supports opacity the same way composite ble ...
         [Truncated]
        """
        ...
    
    def GetCropping(self):
        """
        V.GetCropping() -> int
        C++: virtual vtkTypeBool GetCropping()
        
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
        ...
    
    def GetCroppingMaxValue(self):
        """
        V.GetCroppingMaxValue() -> int
        C++: virtual vtkTypeBool GetCroppingMaxValue()
        
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
        ...
    
    def GetCroppingMinValue(self):
        """
        V.GetCroppingMinValue() -> int
        C++: virtual vtkTypeBool GetCroppingMinValue()
        
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
        ...
    
    def GetCroppingRegionFlags(self):
        """
        V.GetCroppingRegionFlags() -> int
        C++: virtual int GetCroppingRegionFlags()
        
        Set the flags for the cropping regions. The clipping planes
        divide the volume into 27 regions - there is one bit for each
        region. The regions start from the one containing voxel (0,0,0),
        moving along the x axis fastest, the y axis next, and the z axis
        slowest. These are represented from the lowest bit to bit number
        27 in the integer containing the flags. There are several
        convenience functions to set some common configurations -
        subvolume (the default), fence (between any of the clip plane
        pairs), inverted fence, cross (between any two of the clip plane
        pairs) and inverted cross.
        """
        ...
    
    def GetCroppingRegionFlagsMaxValue(self):
        """
        V.GetCroppingRegionFlagsMaxValue() -> int
        C++: virtual int GetCroppingRegionFlagsMaxValue()
        
        Set the flags for the cropping regions. The clipping planes
        divide the volume into 27 regions - there is one bit for each
        region. The regions start from the one containing voxel (0,0,0),
        moving along the x axis fastest, the y axis next, and the z axis
        slowest. These are represented from the lowest bit to bit number
        27 in the integer containing the flags. There are several
        convenience functions to set some common configurations -
        subvolume (the default), fence (between any of the clip plane
        pairs), inverted fence, cross (between any two of the clip plane
        pairs) and inverted cross.
        """
        ...
    
    def GetCroppingRegionFlagsMinValue(self):
        """
        V.GetCroppingRegionFlagsMinValue() -> int
        C++: virtual int GetCroppingRegionFlagsMinValue()
        
        Set the flags for the cropping regions. The clipping planes
        divide the volume into 27 regions - there is one bit for each
        region. The regions start from the one containing voxel (0,0,0),
        moving along the x axis fastest, the y axis next, and the z axis
        slowest. These are represented from the lowest bit to bit number
        27 in the integer containing the flags. There are several
        convenience functions to set some common configurations -
        subvolume (the default), fence (between any of the clip plane
        pairs), inverted fence, cross (between any two of the clip plane
        pairs) and inverted cross.
        """
        ...
    
    def GetCroppingRegionPlanes(self):
        """
        V.GetCroppingRegionPlanes() -> (float, float, float, float, float,
             float)
        C++: virtual double *GetCroppingRegionPlanes()
        
        Set/Get the Cropping Region Planes ( xmin, xmax, ymin, ymax,
        zmin, zmax ) These planes are defined in volume coordinates -
        spacing and origin are considered.
        """
        ...
    
    def GetInput(self):
        """
        V.GetInput() -> vtkImageData
        C++: virtual vtkImageData *GetInput()
        V.GetInput(int) -> vtkImageData
        C++: virtual vtkImageData *GetInput(const int port)
        
        Set/Get the input data
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
    
    def GetVoxelCroppingRegionPlanes(self):
        """
        V.GetVoxelCroppingRegionPlanes() -> (float, float, float, float,
            float, float)
        C++: virtual double *GetVoxelCroppingRegionPlanes()
        
        Get the cropping region planes in voxels. Only valid during the
        rendering process
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
        V.NewInstance() -> vtkVolumeMapper
        C++: vtkVolumeMapper *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override;
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE Release
        any graphics resources that are being consumed by this mapper.
        The parameter window could be used to determine which graphic
        resources to release.
        """
        ...
    
    def Render(self, vtkRenderer, vtkVolume):
        """
        V.Render(vtkRenderer, vtkVolume)
        C++: void Render(vtkRenderer *ren, vtkVolume *vol) override = 0;
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS Render the
        volume
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkVolumeMapper
        C++: static vtkVolumeMapper *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAverageIPScalarRange(self, p_float, p_float_1):
        """
        V.SetAverageIPScalarRange(float, float)
        C++: virtual void SetAverageIPScalarRange(double _arg1,
            double _arg2)
        V.SetAverageIPScalarRange((float, float))
        C++: void SetAverageIPScalarRange(const double _arg[2])
        
        Set/Get the scalar range to be considered for average intensity
        projection blend mode. Only scalar values between this range will
        be averaged during ray casting. This can be useful when volume
        rendering CT datasets where the areas occupied by air would
        deviate the final rendering. By default, the range is set to
        (VTK_FLOAT_MIN, VTK_FLOAT_MAX).
        \sa SetBlendModeToAverageIntensity()
        """
        ...
    
    def SetBlendMode(self, p_int):
        """
        V.SetBlendMode(int)
        C++: virtual void SetBlendMode(int _arg)
        
        Set/Get the blend mode. The default mode is Composite where the
        scalar values are sampled through the volume and composited in a
        front-to-back scheme through alpha blending. The final color and
        opacity is determined using the color and opacity transfer
        functions.
        
        Maximum and minimum intensity blend modes use the maximum and
        minimum scalar values, respectively, along the sampling ray. The
        final color and opacity is determined by passing the resultant
        value through the color and opacity transfer functions.
        
        Additive blend mode accumulates scalar values by passing each
        value through the opacity transfer function and then adding up
        the product of the value and its opacity. In other words, the
        scalar values are scaled using the opacity transfer function and
        summed to derive the final color. Note that the resulting image
        is always grayscale i.e. aggregated values are not passed through
        the color transfer function. This is because the final value is a
        derived value and not a real data value along the sampling ray.
        
        Average intensity blend mode works similar to the additive blend
        mode where the scalar values are multiplied by opacity calculated
        from the opacity transfer function and then added. The additional
        step here is to divide the sum by the number of samples taken
        through the volume. One can control the scalar range by setting
        the AverageIPScalarRange ivar to disregard scalar values, not in
        the range of interest, from the average computation. As is the
        case with the additive intensity projection, the final image will
        always be grayscale i.e. the aggregated values are not passed
        through the color transfer function. This is because the
        resultant value is a derived value and not a real data value
        along the sampling ray.
        
        IsoSurface blend mode uses contour values defined by the user in
        order to display scalar values only when the ray crosses the
        contour. It supports opacity the same way composit ...
         [Truncated]
        """
        ...
    
    def SetBlendModeToAdditive(self):
        """
        V.SetBlendModeToAdditive()
        C++: void SetBlendModeToAdditive()
        
        Set/Get the blend mode. The default mode is Composite where the
        scalar values are sampled through the volume and composited in a
        front-to-back scheme through alpha blending. The final color and
        opacity is determined using the color and opacity transfer
        functions.
        
        Maximum and minimum intensity blend modes use the maximum and
        minimum scalar values, respectively, along the sampling ray. The
        final color and opacity is determined by passing the resultant
        value through the color and opacity transfer functions.
        
        Additive blend mode accumulates scalar values by passing each
        value through the opacity transfer function and then adding up
        the product of the value and its opacity. In other words, the
        scalar values are scaled using the opacity transfer function and
        summed to derive the final color. Note that the resulting image
        is always grayscale i.e. aggregated values are not passed through
        the color transfer function. This is because the final value is a
        derived value and not a real data value along the sampling ray.
        
        Average intensity blend mode works similar to the additive blend
        mode where the scalar values are multiplied by opacity calculated
        from the opacity transfer function and then added. The additional
        step here is to divide the sum by the number of samples taken
        through the volume. One can control the scalar range by setting
        the AverageIPScalarRange ivar to disregard scalar values, not in
        the range of interest, from the average computation. As is the
        case with the additive intensity projection, the final image will
        always be grayscale i.e. the aggregated values are not passed
        through the color transfer function. This is because the
        resultant value is a derived value and not a real data value
        along the sampling ray.
        
        IsoSurface blend mode uses contour values defined by the user in
        order to display scalar values only when the ray crosses the
        contour. It supports opacity the same way composi ...
         [Truncated]
        """
        ...
    
    def SetBlendModeToAverageIntensity(self):
        """
        V.SetBlendModeToAverageIntensity()
        C++: void SetBlendModeToAverageIntensity()
        
        Set/Get the blend mode. The default mode is Composite where the
        scalar values are sampled through the volume and composited in a
        front-to-back scheme through alpha blending. The final color and
        opacity is determined using the color and opacity transfer
        functions.
        
        Maximum and minimum intensity blend modes use the maximum and
        minimum scalar values, respectively, along the sampling ray. The
        final color and opacity is determined by passing the resultant
        value through the color and opacity transfer functions.
        
        Additive blend mode accumulates scalar values by passing each
        value through the opacity transfer function and then adding up
        the product of the value and its opacity. In other words, the
        scalar values are scaled using the opacity transfer function and
        summed to derive the final color. Note that the resulting image
        is always grayscale i.e. aggregated values are not passed through
        the color transfer function. This is because the final value is a
        derived value and not a real data value along the sampling ray.
        
        Average intensity blend mode works similar to the additive blend
        mode where the scalar values are multiplied by opacity calculated
        from the opacity transfer function and then added. The additional
        step here is to divide the sum by the number of samples taken
        through the volume. One can control the scalar range by setting
        the AverageIPScalarRange ivar to disregard scalar values, not in
        the range of interest, from the average computation. As is the
        case with the additive intensity projection, the final image will
        always be grayscale i.e. the aggregated values are not passed
        through the color transfer function. This is because the
        resultant value is a derived value and not a real data value
        along the sampling ray.
        
        IsoSurface blend mode uses contour values defined by the user in
        order to display scalar values only when the ray crosses the
        contour. It supports opacity the  ...
         [Truncated]
        """
        ...
    
    def SetBlendModeToComposite(self):
        """
        V.SetBlendModeToComposite()
        C++: void SetBlendModeToComposite()
        
        Set/Get the blend mode. The default mode is Composite where the
        scalar values are sampled through the volume and composited in a
        front-to-back scheme through alpha blending. The final color and
        opacity is determined using the color and opacity transfer
        functions.
        
        Maximum and minimum intensity blend modes use the maximum and
        minimum scalar values, respectively, along the sampling ray. The
        final color and opacity is determined by passing the resultant
        value through the color and opacity transfer functions.
        
        Additive blend mode accumulates scalar values by passing each
        value through the opacity transfer function and then adding up
        the product of the value and its opacity. In other words, the
        scalar values are scaled using the opacity transfer function and
        summed to derive the final color. Note that the resulting image
        is always grayscale i.e. aggregated values are not passed through
        the color transfer function. This is because the final value is a
        derived value and not a real data value along the sampling ray.
        
        Average intensity blend mode works similar to the additive blend
        mode where the scalar values are multiplied by opacity calculated
        from the opacity transfer function and then added. The additional
        step here is to divide the sum by the number of samples taken
        through the volume. One can control the scalar range by setting
        the AverageIPScalarRange ivar to disregard scalar values, not in
        the range of interest, from the average computation. As is the
        case with the additive intensity projection, the final image will
        always be grayscale i.e. the aggregated values are not passed
        through the color transfer function. This is because the
        resultant value is a derived value and not a real data value
        along the sampling ray.
        
        IsoSurface blend mode uses contour values defined by the user in
        order to display scalar values only when the ray crosses the
        contour. It supports opacity the same way compo ...
         [Truncated]
        """
        ...
    
    def SetBlendModeToIsoSurface(self):
        """
        V.SetBlendModeToIsoSurface()
        C++: void SetBlendModeToIsoSurface()
        
        Set/Get the blend mode. The default mode is Composite where the
        scalar values are sampled through the volume and composited in a
        front-to-back scheme through alpha blending. The final color and
        opacity is determined using the color and opacity transfer
        functions.
        
        Maximum and minimum intensity blend modes use the maximum and
        minimum scalar values, respectively, along the sampling ray. The
        final color and opacity is determined by passing the resultant
        value through the color and opacity transfer functions.
        
        Additive blend mode accumulates scalar values by passing each
        value through the opacity transfer function and then adding up
        the product of the value and its opacity. In other words, the
        scalar values are scaled using the opacity transfer function and
        summed to derive the final color. Note that the resulting image
        is always grayscale i.e. aggregated values are not passed through
        the color transfer function. This is because the final value is a
        derived value and not a real data value along the sampling ray.
        
        Average intensity blend mode works similar to the additive blend
        mode where the scalar values are multiplied by opacity calculated
        from the opacity transfer function and then added. The additional
        step here is to divide the sum by the number of samples taken
        through the volume. One can control the scalar range by setting
        the AverageIPScalarRange ivar to disregard scalar values, not in
        the range of interest, from the average computation. As is the
        case with the additive intensity projection, the final image will
        always be grayscale i.e. the aggregated values are not passed
        through the color transfer function. This is because the
        resultant value is a derived value and not a real data value
        along the sampling ray.
        
        IsoSurface blend mode uses contour values defined by the user in
        order to display scalar values only when the ray crosses the
        contour. It supports opacity the same way com ...
         [Truncated]
        """
        ...
    
    def SetBlendModeToMaximumIntensity(self):
        """
        V.SetBlendModeToMaximumIntensity()
        C++: void SetBlendModeToMaximumIntensity()
        
        Set/Get the blend mode. The default mode is Composite where the
        scalar values are sampled through the volume and composited in a
        front-to-back scheme through alpha blending. The final color and
        opacity is determined using the color and opacity transfer
        functions.
        
        Maximum and minimum intensity blend modes use the maximum and
        minimum scalar values, respectively, along the sampling ray. The
        final color and opacity is determined by passing the resultant
        value through the color and opacity transfer functions.
        
        Additive blend mode accumulates scalar values by passing each
        value through the opacity transfer function and then adding up
        the product of the value and its opacity. In other words, the
        scalar values are scaled using the opacity transfer function and
        summed to derive the final color. Note that the resulting image
        is always grayscale i.e. aggregated values are not passed through
        the color transfer function. This is because the final value is a
        derived value and not a real data value along the sampling ray.
        
        Average intensity blend mode works similar to the additive blend
        mode where the scalar values are multiplied by opacity calculated
        from the opacity transfer function and then added. The additional
        step here is to divide the sum by the number of samples taken
        through the volume. One can control the scalar range by setting
        the AverageIPScalarRange ivar to disregard scalar values, not in
        the range of interest, from the average computation. As is the
        case with the additive intensity projection, the final image will
        always be grayscale i.e. the aggregated values are not passed
        through the color transfer function. This is because the
        resultant value is a derived value and not a real data value
        along the sampling ray.
        
        IsoSurface blend mode uses contour values defined by the user in
        order to display scalar values only when the ray crosses the
        contour. It supports opacity the  ...
         [Truncated]
        """
        ...
    
    def SetBlendModeToMinimumIntensity(self):
        """
        V.SetBlendModeToMinimumIntensity()
        C++: void SetBlendModeToMinimumIntensity()
        
        Set/Get the blend mode. The default mode is Composite where the
        scalar values are sampled through the volume and composited in a
        front-to-back scheme through alpha blending. The final color and
        opacity is determined using the color and opacity transfer
        functions.
        
        Maximum and minimum intensity blend modes use the maximum and
        minimum scalar values, respectively, along the sampling ray. The
        final color and opacity is determined by passing the resultant
        value through the color and opacity transfer functions.
        
        Additive blend mode accumulates scalar values by passing each
        value through the opacity transfer function and then adding up
        the product of the value and its opacity. In other words, the
        scalar values are scaled using the opacity transfer function and
        summed to derive the final color. Note that the resulting image
        is always grayscale i.e. aggregated values are not passed through
        the color transfer function. This is because the final value is a
        derived value and not a real data value along the sampling ray.
        
        Average intensity blend mode works similar to the additive blend
        mode where the scalar values are multiplied by opacity calculated
        from the opacity transfer function and then added. The additional
        step here is to divide the sum by the number of samples taken
        through the volume. One can control the scalar range by setting
        the AverageIPScalarRange ivar to disregard scalar values, not in
        the range of interest, from the average computation. As is the
        case with the additive intensity projection, the final image will
        always be grayscale i.e. the aggregated values are not passed
        through the color transfer function. This is because the
        resultant value is a derived value and not a real data value
        along the sampling ray.
        
        IsoSurface blend mode uses contour values defined by the user in
        order to display scalar values only when the ray crosses the
        contour. It supports opacity the  ...
         [Truncated]
        """
        ...
    
    def SetBlendModeToSlice(self):
        """
        V.SetBlendModeToSlice()
        C++: void SetBlendModeToSlice()
        
        Set/Get the blend mode. The default mode is Composite where the
        scalar values are sampled through the volume and composited in a
        front-to-back scheme through alpha blending. The final color and
        opacity is determined using the color and opacity transfer
        functions.
        
        Maximum and minimum intensity blend modes use the maximum and
        minimum scalar values, respectively, along the sampling ray. The
        final color and opacity is determined by passing the resultant
        value through the color and opacity transfer functions.
        
        Additive blend mode accumulates scalar values by passing each
        value through the opacity transfer function and then adding up
        the product of the value and its opacity. In other words, the
        scalar values are scaled using the opacity transfer function and
        summed to derive the final color. Note that the resulting image
        is always grayscale i.e. aggregated values are not passed through
        the color transfer function. This is because the final value is a
        derived value and not a real data value along the sampling ray.
        
        Average intensity blend mode works similar to the additive blend
        mode where the scalar values are multiplied by opacity calculated
        from the opacity transfer function and then added. The additional
        step here is to divide the sum by the number of samples taken
        through the volume. One can control the scalar range by setting
        the AverageIPScalarRange ivar to disregard scalar values, not in
        the range of interest, from the average computation. As is the
        case with the additive intensity projection, the final image will
        always be grayscale i.e. the aggregated values are not passed
        through the color transfer function. This is because the
        resultant value is a derived value and not a real data value
        along the sampling ray.
        
        IsoSurface blend mode uses contour values defined by the user in
        order to display scalar values only when the ray crosses the
        contour. It supports opacity the same way composite ble ...
         [Truncated]
        """
        ...
    
    def SetCropping(self, p_int):
        """
        V.SetCropping(int)
        C++: virtual void SetCropping(vtkTypeBool _arg)
        
        Turn On/Off orthogonal cropping. (Clipping planes are
        perpendicular to the coordinate axes.)
        """
        ...
    
    def SetCroppingRegionFlags(self, p_int):
        """
        V.SetCroppingRegionFlags(int)
        C++: virtual void SetCroppingRegionFlags(int _arg)
        
        Set the flags for the cropping regions. The clipping planes
        divide the volume into 27 regions - there is one bit for each
        region. The regions start from the one containing voxel (0,0,0),
        moving along the x axis fastest, the y axis next, and the z axis
        slowest. These are represented from the lowest bit to bit number
        27 in the integer containing the flags. There are several
        convenience functions to set some common configurations -
        subvolume (the default), fence (between any of the clip plane
        pairs), inverted fence, cross (between any two of the clip plane
        pairs) and inverted cross.
        """
        ...
    
    def SetCroppingRegionFlagsToCross(self):
        """
        V.SetCroppingRegionFlagsToCross()
        C++: void SetCroppingRegionFlagsToCross()
        
        Set the flags for the cropping regions. The clipping planes
        divide the volume into 27 regions - there is one bit for each
        region. The regions start from the one containing voxel (0,0,0),
        moving along the x axis fastest, the y axis next, and the z axis
        slowest. These are represented from the lowest bit to bit number
        27 in the integer containing the flags. There are several
        convenience functions to set some common configurations -
        subvolume (the default), fence (between any of the clip plane
        pairs), inverted fence, cross (between any two of the clip plane
        pairs) and inverted cross.
        """
        ...
    
    def SetCroppingRegionFlagsToFence(self):
        """
        V.SetCroppingRegionFlagsToFence()
        C++: void SetCroppingRegionFlagsToFence()
        
        Set the flags for the cropping regions. The clipping planes
        divide the volume into 27 regions - there is one bit for each
        region. The regions start from the one containing voxel (0,0,0),
        moving along the x axis fastest, the y axis next, and the z axis
        slowest. These are represented from the lowest bit to bit number
        27 in the integer containing the flags. There are several
        convenience functions to set some common configurations -
        subvolume (the default), fence (between any of the clip plane
        pairs), inverted fence, cross (between any two of the clip plane
        pairs) and inverted cross.
        """
        ...
    
    def SetCroppingRegionFlagsToInvertedCross(self):
        """
        V.SetCroppingRegionFlagsToInvertedCross()
        C++: void SetCroppingRegionFlagsToInvertedCross()
        
        Set the flags for the cropping regions. The clipping planes
        divide the volume into 27 regions - there is one bit for each
        region. The regions start from the one containing voxel (0,0,0),
        moving along the x axis fastest, the y axis next, and the z axis
        slowest. These are represented from the lowest bit to bit number
        27 in the integer containing the flags. There are several
        convenience functions to set some common configurations -
        subvolume (the default), fence (between any of the clip plane
        pairs), inverted fence, cross (between any two of the clip plane
        pairs) and inverted cross.
        """
        ...
    
    def SetCroppingRegionFlagsToInvertedFence(self):
        """
        V.SetCroppingRegionFlagsToInvertedFence()
        C++: void SetCroppingRegionFlagsToInvertedFence()
        
        Set the flags for the cropping regions. The clipping planes
        divide the volume into 27 regions - there is one bit for each
        region. The regions start from the one containing voxel (0,0,0),
        moving along the x axis fastest, the y axis next, and the z axis
        slowest. These are represented from the lowest bit to bit number
        27 in the integer containing the flags. There are several
        convenience functions to set some common configurations -
        subvolume (the default), fence (between any of the clip plane
        pairs), inverted fence, cross (between any two of the clip plane
        pairs) and inverted cross.
        """
        ...
    
    def SetCroppingRegionFlagsToSubVolume(self):
        """
        V.SetCroppingRegionFlagsToSubVolume()
        C++: void SetCroppingRegionFlagsToSubVolume()
        
        Set the flags for the cropping regions. The clipping planes
        divide the volume into 27 regions - there is one bit for each
        region. The regions start from the one containing voxel (0,0,0),
        moving along the x axis fastest, the y axis next, and the z axis
        slowest. These are represented from the lowest bit to bit number
        27 in the integer containing the flags. There are several
        convenience functions to set some common configurations -
        subvolume (the default), fence (between any of the clip plane
        pairs), inverted fence, cross (between any two of the clip plane
        pairs) and inverted cross.
        """
        ...
    
    def SetCroppingRegionPlanes(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5):
        """
        V.SetCroppingRegionPlanes(float, float, float, float, float,
            float)
        C++: virtual void SetCroppingRegionPlanes(double _arg1,
            double _arg2, double _arg3, double _arg4, double _arg5,
            double _arg6)
        V.SetCroppingRegionPlanes((float, float, float, float, float,
            float))
        C++: virtual void SetCroppingRegionPlanes(const double _arg[6])
        
        Set/Get the Cropping Region Planes ( xmin, xmax, ymin, ymax,
        zmin, zmax ) These planes are defined in volume coordinates -
        spacing and origin are considered.
        """
        ...
    
    def SetInputData(self, vtkImageData):
        """
        V.SetInputData(vtkImageData)
        C++: virtual void SetInputData(vtkImageData *)
        V.SetInputData(vtkDataSet)
        C++: virtual void SetInputData(vtkDataSet *)
        
        Set/Get the input data
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
    ADDITIVE_BLEND = ...
    AVERAGE_INTENSITY_BLEND = ...
    BlendModes = ...
    COMPOSITE_BLEND = ...
    ISOSURFACE_BLEND = ...
    MAXIMUM_INTENSITY_BLEND = ...
    MINIMUM_INTENSITY_BLEND = ...
    SLICE_BLEND = ...
    __dict__ = ...
    __vtkname__ = ...


