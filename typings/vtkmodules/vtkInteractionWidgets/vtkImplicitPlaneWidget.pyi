"""
This type stub file was generated by pyright.
"""

from .vtkPolyDataSourceWidget import vtkPolyDataSourceWidget

class vtkImplicitPlaneWidget(vtkPolyDataSourceWidget):
    """
    vtkImplicitPlaneWidget - 3D widget for manipulating an infinite plane
    
    Superclass: vtkPolyDataSourceWidget
    
    This 3D widget defines an infinite plane that can be interactively
    placed in a scene. The widget is represented by a plane with a normal
    vector; the plane is contained by a bounding box, and where the plane
    intersects the bounding box the edges are shown (possibly tubed). The
    normal can be selected and moved to rotate the plane; the plane
    itself can be selected and translated in various directions. As the
    plane is moved, the implicit plane function and polygon (representing
    the plane cut against the bounding box) is updated.
    
    To use this object, just invoke SetInteractor() with the argument of
    the method a vtkRenderWindowInteractor.  You may also wish to invoke
    "PlaceWidget()" to initially position the widget. If the "i" key (for
    "interactor") is pressed, the vtkImplicitPlaneWidget will appear.
    (See superclass documentation for information about changing this
    behavior.) If you select the normal vector, the plane can be
    arbitrarily rotated. The plane can be translated along the normal by
    selecting the plane and moving it. The plane (the plane origin) can
    also be arbitrary moved by selecting the plane with the middle mouse
    button. The right mouse button can be used to uniformly scale the
    bounding box (moving "up" the box scales larger; moving "down" the
    box scales smaller). Events that occur outside of the widget (i.e.,
    no part of the widget is picked) are propagated to any other
    registered obsevers (such as the interaction style).  Turn off the
    widget by pressing the "i" key again (or invoke the Off() method).
    
    The vtkImplicitPlaneWidget has several methods that can be used in
    conjunction with other VTK objects.  The GetPolyData() method can be
    used to get a polygonal representation (the single polygon clipped by
    the bounding box).  Typical usage of the widget is to make use of the
    StartInteractionEvent, InteractionEvent, and EndInteractionEvent
    events. The InteractionEvent is called on mouse motion; the other two
    events are called on button down and button up (either left or right
    button). (Note: there is also a PlaceWidgetEvent that is invoked when
    the widget is placed with PlaceWidget().)
    
    Some additional features of this class include the ability to control
    the properties of the widget. You do this by setting property values
    on the normal vector (selected and unselected properties); the plane
    (selected and unselected properties); the outline (selected and
    unselected properties); and the edges. The edges may also be tubed or
    not.
    
    @sa
    vtk3DWidget vtkBoxWidget vtkPlaneWidget vtkLineWidget vtkPointWidget
    vtkSphereWidget vtkImagePlaneWidget
    """
    def DrawPlaneOff(self):
        """
        V.DrawPlaneOff()
        C++: virtual void DrawPlaneOff()
        
        Enable/disable the drawing of the plane. In some cases the plane
        interferes with the object that it is operating on (i.e., the
        plane interferes with the cut surface it produces producing
        z-buffer artifacts.)
        """
        ...
    
    def DrawPlaneOn(self):
        """
        V.DrawPlaneOn()
        C++: virtual void DrawPlaneOn()
        
        Enable/disable the drawing of the plane. In some cases the plane
        interferes with the object that it is operating on (i.e., the
        plane interferes with the cut surface it produces producing
        z-buffer artifacts.)
        """
        ...
    
    def GetDiagonalRatio(self):
        """
        V.GetDiagonalRatio() -> float
        C++: virtual double GetDiagonalRatio()
        
        By default the arrow is 30% of the diagonal length. DiagonalRatio
        control this ratio in the interval [0-2]
        """
        ...
    
    def GetDiagonalRatioMaxValue(self):
        """
        V.GetDiagonalRatioMaxValue() -> float
        C++: virtual double GetDiagonalRatioMaxValue()
        
        By default the arrow is 30% of the diagonal length. DiagonalRatio
        control this ratio in the interval [0-2]
        """
        ...
    
    def GetDiagonalRatioMinValue(self):
        """
        V.GetDiagonalRatioMinValue() -> float
        C++: virtual double GetDiagonalRatioMinValue()
        
        By default the arrow is 30% of the diagonal length. DiagonalRatio
        control this ratio in the interval [0-2]
        """
        ...
    
    def GetDrawPlane(self):
        """
        V.GetDrawPlane() -> int
        C++: virtual vtkTypeBool GetDrawPlane()
        
        Enable/disable the drawing of the plane. In some cases the plane
        interferes with the object that it is operating on (i.e., the
        plane interferes with the cut surface it produces producing
        z-buffer artifacts.)
        """
        ...
    
    def GetEdgesProperty(self):
        """
        V.GetEdgesProperty() -> vtkProperty
        C++: virtual vtkProperty *GetEdgesProperty()
        
        Get the property of the intersection edges. (This property also
        applies to the edges when tubed.)
        """
        ...
    
    def GetNormal(self):
        """
        V.GetNormal() -> (float, float, float)
        C++: double *GetNormal()
        V.GetNormal([float, float, float])
        C++: void GetNormal(double xyz[3])
        
        Get the normal to the plane.
        """
        ...
    
    def GetNormalProperty(self):
        """
        V.GetNormalProperty() -> vtkProperty
        C++: virtual vtkProperty *GetNormalProperty()
        
        Get the properties on the normal (line and cone).
        """
        ...
    
    def GetNormalToXAxis(self):
        """
        V.GetNormalToXAxis() -> int
        C++: virtual vtkTypeBool GetNormalToXAxis()
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
        ...
    
    def GetNormalToYAxis(self):
        """
        V.GetNormalToYAxis() -> int
        C++: virtual vtkTypeBool GetNormalToYAxis()
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
        ...
    
    def GetNormalToZAxis(self):
        """
        V.GetNormalToZAxis() -> int
        C++: virtual vtkTypeBool GetNormalToZAxis()
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
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
    
    def GetOrigin(self):
        """
        V.GetOrigin() -> (float, float, float)
        C++: double *GetOrigin()
        V.GetOrigin([float, float, float])
        C++: void GetOrigin(double xyz[3])
        
        Get the origin of the plane.
        """
        ...
    
    def GetOriginTranslation(self):
        """
        V.GetOriginTranslation() -> int
        C++: virtual vtkTypeBool GetOriginTranslation()
        
        Turn on/off the ability to translate the origin (sphere) with the
        left mouse button.
        """
        ...
    
    def GetOutlineProperty(self):
        """
        V.GetOutlineProperty() -> vtkProperty
        C++: virtual vtkProperty *GetOutlineProperty()
        
        Get the property of the outline.
        """
        ...
    
    def GetOutlineTranslation(self):
        """
        V.GetOutlineTranslation() -> int
        C++: virtual vtkTypeBool GetOutlineTranslation()
        
        Turn on/off the ability to translate the bounding box by grabbing
        it with the left mouse button.
        """
        ...
    
    def GetOutsideBounds(self):
        """
        V.GetOutsideBounds() -> int
        C++: virtual vtkTypeBool GetOutsideBounds()
        
        Turn on/off the ability to move the widget outside of the input's
        bound
        """
        ...
    
    def GetPlane(self, vtkPlane):
        """
        V.GetPlane(vtkPlane)
        C++: void GetPlane(vtkPlane *plane)
        
        Get the implicit function for the plane. The user must provide
        the instance of the class vtkPlane. Note that vtkPlane is a
        subclass of vtkImplicitFunction, meaning that it can be used by a
        variety of filters to perform clipping, cutting, and selection of
        data.
        """
        ...
    
    def GetPlaneProperty(self):
        """
        V.GetPlaneProperty() -> vtkProperty
        C++: virtual vtkProperty *GetPlaneProperty()
        
        Get the plane properties. The properties of the plane when
        selected and unselected can be manipulated.
        """
        ...
    
    def GetPolyData(self, vtkPolyData):
        """
        V.GetPolyData(vtkPolyData)
        C++: void GetPolyData(vtkPolyData *pd)
        
        Grab the polydata that defines the plane. The polydata contains a
        single polygon that is clipped by the bounding box.
        """
        ...
    
    def GetPolyDataAlgorithm(self):
        """
        V.GetPolyDataAlgorithm() -> vtkPolyDataAlgorithm
        C++: vtkPolyDataAlgorithm *GetPolyDataAlgorithm() override;
        
        Satisfies superclass API.  This returns a pointer to the
        underlying PolyData (which represents the plane).
        """
        ...
    
    def GetScaleEnabled(self):
        """
        V.GetScaleEnabled() -> int
        C++: virtual vtkTypeBool GetScaleEnabled()
        
        Turn on/off the ability to scale with the mouse
        """
        ...
    
    def GetSelectedNormalProperty(self):
        """
        V.GetSelectedNormalProperty() -> vtkProperty
        C++: virtual vtkProperty *GetSelectedNormalProperty()
        
        Get the properties on the normal (line and cone).
        """
        ...
    
    def GetSelectedOutlineProperty(self):
        """
        V.GetSelectedOutlineProperty() -> vtkProperty
        C++: virtual vtkProperty *GetSelectedOutlineProperty()
        
        Get the property of the outline.
        """
        ...
    
    def GetSelectedPlaneProperty(self):
        """
        V.GetSelectedPlaneProperty() -> vtkProperty
        C++: virtual vtkProperty *GetSelectedPlaneProperty()
        
        Get the plane properties. The properties of the plane when
        selected and unselected can be manipulated.
        """
        ...
    
    def GetTubing(self):
        """
        V.GetTubing() -> int
        C++: virtual vtkTypeBool GetTubing()
        
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a vtkTubeFilter.
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
        V.NewInstance() -> vtkImplicitPlaneWidget
        C++: vtkImplicitPlaneWidget *NewInstance()
        """
        ...
    
    def NormalToXAxisOff(self):
        """
        V.NormalToXAxisOff()
        C++: virtual void NormalToXAxisOff()
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
        ...
    
    def NormalToXAxisOn(self):
        """
        V.NormalToXAxisOn()
        C++: virtual void NormalToXAxisOn()
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
        ...
    
    def NormalToYAxisOff(self):
        """
        V.NormalToYAxisOff()
        C++: virtual void NormalToYAxisOff()
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
        ...
    
    def NormalToYAxisOn(self):
        """
        V.NormalToYAxisOn()
        C++: virtual void NormalToYAxisOn()
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
        ...
    
    def NormalToZAxisOff(self):
        """
        V.NormalToZAxisOff()
        C++: virtual void NormalToZAxisOff()
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
        ...
    
    def NormalToZAxisOn(self):
        """
        V.NormalToZAxisOn()
        C++: virtual void NormalToZAxisOn()
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
        ...
    
    def OriginTranslationOff(self):
        """
        V.OriginTranslationOff()
        C++: virtual void OriginTranslationOff()
        
        Turn on/off the ability to translate the origin (sphere) with the
        left mouse button.
        """
        ...
    
    def OriginTranslationOn(self):
        """
        V.OriginTranslationOn()
        C++: virtual void OriginTranslationOn()
        
        Turn on/off the ability to translate the origin (sphere) with the
        left mouse button.
        """
        ...
    
    def OutlineTranslationOff(self):
        """
        V.OutlineTranslationOff()
        C++: virtual void OutlineTranslationOff()
        
        Turn on/off the ability to translate the bounding box by grabbing
        it with the left mouse button.
        """
        ...
    
    def OutlineTranslationOn(self):
        """
        V.OutlineTranslationOn()
        C++: virtual void OutlineTranslationOn()
        
        Turn on/off the ability to translate the bounding box by grabbing
        it with the left mouse button.
        """
        ...
    
    def OutsideBoundsOff(self):
        """
        V.OutsideBoundsOff()
        C++: virtual void OutsideBoundsOff()
        
        Turn on/off the ability to move the widget outside of the input's
        bound
        """
        ...
    
    def OutsideBoundsOn(self):
        """
        V.OutsideBoundsOn()
        C++: virtual void OutsideBoundsOn()
        
        Turn on/off the ability to move the widget outside of the input's
        bound
        """
        ...
    
    def PlaceWidget(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.PlaceWidget([float, float, float, float, float, float])
        C++: void PlaceWidget(double bounds[6]) override;
        V.PlaceWidget()
        C++: void PlaceWidget() override;
        V.PlaceWidget(float, float, float, float, float, float)
        C++: void PlaceWidget(double xmin, double xmax, double ymin,
            double ymax, double zmin, double zmax) override;
        
        Methods that satisfy the superclass' API.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImplicitPlaneWidget
        C++: static vtkImplicitPlaneWidget *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def ScaleEnabledOff(self):
        """
        V.ScaleEnabledOff()
        C++: virtual void ScaleEnabledOff()
        
        Turn on/off the ability to scale with the mouse
        """
        ...
    
    def ScaleEnabledOn(self):
        """
        V.ScaleEnabledOn()
        C++: virtual void ScaleEnabledOn()
        
        Turn on/off the ability to scale with the mouse
        """
        ...
    
    def SetDiagonalRatio(self, p_float):
        """
        V.SetDiagonalRatio(float)
        C++: virtual void SetDiagonalRatio(double _arg)
        
        By default the arrow is 30% of the diagonal length. DiagonalRatio
        control this ratio in the interval [0-2]
        """
        ...
    
    def SetDrawPlane(self, p_int):
        """
        V.SetDrawPlane(int)
        C++: void SetDrawPlane(vtkTypeBool plane)
        
        Enable/disable the drawing of the plane. In some cases the plane
        interferes with the object that it is operating on (i.e., the
        plane interferes with the cut surface it produces producing
        z-buffer artifacts.)
        """
        ...
    
    def SetEnabled(self, p_int):
        """
        V.SetEnabled(int)
        C++: void SetEnabled(int) override;
        
        Methods that satisfy the superclass' API.
        """
        ...
    
    def SetNormal(self, p_float, p_float_1, p_float_2):
        """
        V.SetNormal(float, float, float)
        C++: void SetNormal(double x, double y, double z)
        V.SetNormal([float, float, float])
        C++: void SetNormal(double x[3])
        
        Get the normal to the plane.
        """
        ...
    
    def SetNormalToXAxis(self, p_int):
        """
        V.SetNormalToXAxis(int)
        C++: void SetNormalToXAxis(vtkTypeBool)
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
        ...
    
    def SetNormalToYAxis(self, p_int):
        """
        V.SetNormalToYAxis(int)
        C++: void SetNormalToYAxis(vtkTypeBool)
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
        ...
    
    def SetNormalToZAxis(self, p_int):
        """
        V.SetNormalToZAxis(int)
        C++: void SetNormalToZAxis(vtkTypeBool)
        
        Force the plane widget to be aligned with one of the x-y-z axes.
        If one axis is set on, the other two will be set off. Remember
        that when the state changes, a ModifiedEvent is invoked. This can
        be used to snap the plane to the axes if it is originally not
        aligned.
        """
        ...
    
    def SetOrigin(self, p_float, p_float_1, p_float_2):
        """
        V.SetOrigin(float, float, float)
        C++: virtual void SetOrigin(double x, double y, double z)
        V.SetOrigin([float, float, float])
        C++: virtual void SetOrigin(double x[3])
        
        Get the origin of the plane.
        """
        ...
    
    def SetOriginTranslation(self, p_int):
        """
        V.SetOriginTranslation(int)
        C++: virtual void SetOriginTranslation(vtkTypeBool _arg)
        
        Turn on/off the ability to translate the origin (sphere) with the
        left mouse button.
        """
        ...
    
    def SetOutlineTranslation(self, p_int):
        """
        V.SetOutlineTranslation(int)
        C++: virtual void SetOutlineTranslation(vtkTypeBool _arg)
        
        Turn on/off the ability to translate the bounding box by grabbing
        it with the left mouse button.
        """
        ...
    
    def SetOutsideBounds(self, p_int):
        """
        V.SetOutsideBounds(int)
        C++: virtual void SetOutsideBounds(vtkTypeBool _arg)
        
        Turn on/off the ability to move the widget outside of the input's
        bound
        """
        ...
    
    def SetScaleEnabled(self, p_int):
        """
        V.SetScaleEnabled(int)
        C++: virtual void SetScaleEnabled(vtkTypeBool _arg)
        
        Turn on/off the ability to scale with the mouse
        """
        ...
    
    def SetTubing(self, p_int):
        """
        V.SetTubing(int)
        C++: virtual void SetTubing(vtkTypeBool _arg)
        
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a vtkTubeFilter.
        """
        ...
    
    def SizeHandles(self):
        """
        V.SizeHandles()
        C++: void SizeHandles() override;
        
        Control widget appearance
        """
        ...
    
    def TubingOff(self):
        """
        V.TubingOff()
        C++: virtual void TubingOff()
        
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a vtkTubeFilter.
        """
        ...
    
    def TubingOn(self):
        """
        V.TubingOn()
        C++: virtual void TubingOn()
        
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a vtkTubeFilter.
        """
        ...
    
    def UpdatePlacement(self):
        """
        V.UpdatePlacement()
        C++: void UpdatePlacement() override;
        
        Satisfies the superclass API.  This will change the state of the
        widget to match changes that have been made to the underlying
        PolyDataSource
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


