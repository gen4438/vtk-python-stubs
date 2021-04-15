"""
This type stub file was generated by pyright.
"""

from .vtkAbstractMapper3D import vtkAbstractMapper3D

class vtkAbstractVolumeMapper(vtkAbstractMapper3D):
    """
    vtkAbstractVolumeMapper - Abstract class for a volume mapper
    
    Superclass: vtkAbstractMapper3D
    
    vtkAbstractVolumeMapper is the abstract definition of a volume
    mapper. Specific subclasses deal with different specific types of
    data input
    
    @sa
    vtkVolumeMapper vtkUnstructuredGridVolumeMapper
    """
    def GetArrayAccessMode(self):
        """
        V.GetArrayAccessMode() -> int
        C++: virtual int GetArrayAccessMode()
        """
        ...
    
    def GetArrayId(self):
        """
        V.GetArrayId() -> int
        C++: virtual int GetArrayId()
        """
        ...
    
    def GetArrayName(self):
        """
        V.GetArrayName() -> string
        C++: virtual char *GetArrayName()
        
        Get the array name or number and component to use for rendering.
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: double *GetBounds() override;
        V.GetBounds([float, float, float, float, float, float])
        C++: void GetBounds(double bounds[6]) override;
        
        Return bounding box (array of six doubles) of data expressed as
        (xmin,xmax, ymin,ymax, zmin,zmax).
        """
        ...
    
    def GetDataObjectInput(self):
        """
        V.GetDataObjectInput() -> vtkDataObject
        C++: virtual vtkDataObject *GetDataObjectInput()
        
        Set/Get the input data
        """
        ...
    
    def GetDataSetInput(self):
        """
        V.GetDataSetInput() -> vtkDataSet
        C++: virtual vtkDataSet *GetDataSetInput()
        
        Set/Get the input data
        """
        ...
    
    def GetGradientMagnitudeBias(self):
        """
        V.GetGradientMagnitudeBias() -> float
        C++: virtual float GetGradientMagnitudeBias()
        V.GetGradientMagnitudeBias(int) -> float
        C++: virtual float GetGradientMagnitudeBias(int)
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE
        """
        ...
    
    def GetGradientMagnitudeScale(self):
        """
        V.GetGradientMagnitudeScale() -> float
        C++: virtual float GetGradientMagnitudeScale()
        V.GetGradientMagnitudeScale(int) -> float
        C++: virtual float GetGradientMagnitudeScale(int)
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE
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
    
    def GetScalarMode(self):
        """
        V.GetScalarMode() -> int
        C++: virtual int GetScalarMode()
        
        Control how the mapper works with scalar point data and cell
        attribute data.  By default (ScalarModeToDefault), the mapper
        will use point data, and if no point data is available, then cell
        data is used. Alternatively you can explicitly set the mapper to
        use point data (ScalarModeToUsePointData) or cell data
        (ScalarModeToUseCellData). You can also choose to get the scalars
        from an array in point field data (ScalarModeToUsePointFieldData)
        or cell field data (ScalarModeToUseCellFieldData).  If scalars
        are coming from a field data array, you must call
        SelectScalarArray.
        """
        ...
    
    def GetScalarModeAsString(self):
        """
        V.GetScalarModeAsString() -> string
        C++: const char *GetScalarModeAsString()
        
        Return the method for obtaining scalar data.
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
        V.NewInstance() -> vtkAbstractVolumeMapper
        C++: vtkAbstractVolumeMapper *NewInstance()
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
        C++: virtual void Render(vtkRenderer *ren, vtkVolume *vol)
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS Render the
        volume
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAbstractVolumeMapper
        C++: static vtkAbstractVolumeMapper *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SelectScalarArray(self, p_int):
        """
        V.SelectScalarArray(int)
        C++: virtual void SelectScalarArray(int arrayNum)
        V.SelectScalarArray(string)
        C++: virtual void SelectScalarArray(const char *arrayName)
        
        When ScalarMode is set to UsePointFieldData or UseCellFieldData,
        you can specify which scalar array to use during rendering. The
        transfer function in the vtkVolumeProperty (attached to the
        calling vtkVolume) will decide how to convert vectors to colors.
        """
        ...
    
    def SetArrayAccessMode(self, p_int):
        """
        V.SetArrayAccessMode(int)
        C++: virtual void SetArrayAccessMode(int _arg)
        
        Control how the mapper works with scalar point data and cell
        attribute data.  By default (ScalarModeToDefault), the mapper
        will use point data, and if no point data is available, then cell
        data is used. Alternatively you can explicitly set the mapper to
        use point data (ScalarModeToUsePointData) or cell data
        (ScalarModeToUseCellData). You can also choose to get the scalars
        from an array in point field data (ScalarModeToUsePointFieldData)
        or cell field data (ScalarModeToUseCellFieldData).  If scalars
        are coming from a field data array, you must call
        SelectScalarArray.
        """
        ...
    
    def SetScalarMode(self, p_int):
        """
        V.SetScalarMode(int)
        C++: virtual void SetScalarMode(int _arg)
        
        Control how the mapper works with scalar point data and cell
        attribute data.  By default (ScalarModeToDefault), the mapper
        will use point data, and if no point data is available, then cell
        data is used. Alternatively you can explicitly set the mapper to
        use point data (ScalarModeToUsePointData) or cell data
        (ScalarModeToUseCellData). You can also choose to get the scalars
        from an array in point field data (ScalarModeToUsePointFieldData)
        or cell field data (ScalarModeToUseCellFieldData).  If scalars
        are coming from a field data array, you must call
        SelectScalarArray.
        """
        ...
    
    def SetScalarModeToDefault(self):
        """
        V.SetScalarModeToDefault()
        C++: void SetScalarModeToDefault()
        
        Control how the mapper works with scalar point data and cell
        attribute data.  By default (ScalarModeToDefault), the mapper
        will use point data, and if no point data is available, then cell
        data is used. Alternatively you can explicitly set the mapper to
        use point data (ScalarModeToUsePointData) or cell data
        (ScalarModeToUseCellData). You can also choose to get the scalars
        from an array in point field data (ScalarModeToUsePointFieldData)
        or cell field data (ScalarModeToUseCellFieldData).  If scalars
        are coming from a field data array, you must call
        SelectScalarArray.
        """
        ...
    
    def SetScalarModeToUseCellData(self):
        """
        V.SetScalarModeToUseCellData()
        C++: void SetScalarModeToUseCellData()
        
        Control how the mapper works with scalar point data and cell
        attribute data.  By default (ScalarModeToDefault), the mapper
        will use point data, and if no point data is available, then cell
        data is used. Alternatively you can explicitly set the mapper to
        use point data (ScalarModeToUsePointData) or cell data
        (ScalarModeToUseCellData). You can also choose to get the scalars
        from an array in point field data (ScalarModeToUsePointFieldData)
        or cell field data (ScalarModeToUseCellFieldData).  If scalars
        are coming from a field data array, you must call
        SelectScalarArray.
        """
        ...
    
    def SetScalarModeToUseCellFieldData(self):
        """
        V.SetScalarModeToUseCellFieldData()
        C++: void SetScalarModeToUseCellFieldData()
        
        Control how the mapper works with scalar point data and cell
        attribute data.  By default (ScalarModeToDefault), the mapper
        will use point data, and if no point data is available, then cell
        data is used. Alternatively you can explicitly set the mapper to
        use point data (ScalarModeToUsePointData) or cell data
        (ScalarModeToUseCellData). You can also choose to get the scalars
        from an array in point field data (ScalarModeToUsePointFieldData)
        or cell field data (ScalarModeToUseCellFieldData).  If scalars
        are coming from a field data array, you must call
        SelectScalarArray.
        """
        ...
    
    def SetScalarModeToUsePointData(self):
        """
        V.SetScalarModeToUsePointData()
        C++: void SetScalarModeToUsePointData()
        
        Control how the mapper works with scalar point data and cell
        attribute data.  By default (ScalarModeToDefault), the mapper
        will use point data, and if no point data is available, then cell
        data is used. Alternatively you can explicitly set the mapper to
        use point data (ScalarModeToUsePointData) or cell data
        (ScalarModeToUseCellData). You can also choose to get the scalars
        from an array in point field data (ScalarModeToUsePointFieldData)
        or cell field data (ScalarModeToUseCellFieldData).  If scalars
        are coming from a field data array, you must call
        SelectScalarArray.
        """
        ...
    
    def SetScalarModeToUsePointFieldData(self):
        """
        V.SetScalarModeToUsePointFieldData()
        C++: void SetScalarModeToUsePointFieldData()
        
        Control how the mapper works with scalar point data and cell
        attribute data.  By default (ScalarModeToDefault), the mapper
        will use point data, and if no point data is available, then cell
        data is used. Alternatively you can explicitly set the mapper to
        use point data (ScalarModeToUsePointData) or cell data
        (ScalarModeToUseCellData). You can also choose to get the scalars
        from an array in point field data (ScalarModeToUsePointFieldData)
        or cell field data (ScalarModeToUseCellFieldData).  If scalars
        are coming from a field data array, you must call
        SelectScalarArray.
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


