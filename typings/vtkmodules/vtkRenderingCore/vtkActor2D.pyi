"""
This type stub file was generated by pyright.
"""

from .vtkProp import vtkProp

class vtkActor2D(vtkProp):
    """
    vtkActor2D - a actor that draws 2D data
    
    Superclass: vtkProp
    
    vtkActor2D is similar to vtkActor, but it is made to be used with two
    dimensional images and annotation.  vtkActor2D has a position but
    does not use a transformation matrix like vtkActor (see the
    superclass vtkProp for information on positioning vtkActor2D). 
    vtkActor2D has a reference to a vtkMapper2D object which does the
    rendering.
    
    @sa
    vtkProp  vtkMapper2D vtkProperty2D
    """
    def GetActors2D(self, vtkPropCollection):
        """
        V.GetActors2D(vtkPropCollection)
        C++: void GetActors2D(vtkPropCollection *pc) override;
        
        For some exporters and other other operations we must be able to
        collect all the actors or volumes. These methods are used in that
        process.
        """
        ...
    
    def GetActualPosition2Coordinate(self):
        """
        V.GetActualPosition2Coordinate() -> vtkCoordinate
        C++: virtual vtkCoordinate *GetActualPosition2Coordinate(void)
        
        Return the actual vtkCoordinate reference that the mapper should
        use to position the actor. This is used internally by the mappers
        and should be overridden in specialized subclasses and otherwise
        ignored.
        """
        ...
    
    def GetActualPositionCoordinate(self):
        """
        V.GetActualPositionCoordinate() -> vtkCoordinate
        C++: virtual vtkCoordinate *GetActualPositionCoordinate(void)
        
        Return the actual vtkCoordinate reference that the mapper should
        use to position the actor. This is used internally by the mappers
        and should be overridden in specialized subclasses and otherwise
        ignored.
        """
        ...
    
    def GetHeight(self):
        """
        V.GetHeight() -> float
        C++: double GetHeight()
        
        Set/Get the height and width of the Actor2D. The value is
        expressed as a fraction of the viewport. This really is just
        another way of setting the Position2 instance variable.
        """
        ...
    
    def GetLayerNumber(self):
        """
        V.GetLayerNumber() -> int
        C++: virtual int GetLayerNumber()
        
        Set/Get the layer number in the overlay planes into which to
        render.
        """
        ...
    
    def GetMapper(self):
        """
        V.GetMapper() -> vtkMapper2D
        C++: virtual vtkMapper2D *GetMapper()
        
        Set/Get the vtkMapper2D which defines the data to be drawn.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Return this objects MTime.
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
    
    def GetPosition(self):
        """
        V.GetPosition() -> (float, float)
        C++: virtual double *GetPosition()
        
        Get the PositionCoordinate instance of vtkCoordinate. This is
        used for for complicated or relative positioning. The position
        variable controls the lower left corner of the Actor2D
        """
        ...
    
    def GetPosition2(self):
        """
        V.GetPosition2() -> (float, float)
        C++: virtual double *GetPosition2()
        
        Access the Position2 instance variable. This variable controls
        the upper right corner of the Actor2D. It is by default relative
        to Position and in normalized viewport coordinates. Some 2D actor
        subclasses ignore the position2 variable
        """
        ...
    
    def GetPosition2Coordinate(self):
        """
        V.GetPosition2Coordinate() -> vtkCoordinate
        C++: virtual vtkCoordinate *GetPosition2Coordinate()
        
        Access the Position2 instance variable. This variable controls
        the upper right corner of the Actor2D. It is by default relative
        to Position and in normalized viewport coordinates. Some 2D actor
        subclasses ignore the position2 variable
        """
        ...
    
    def GetPositionCoordinate(self):
        """
        V.GetPositionCoordinate() -> vtkCoordinate
        C++: virtual vtkCoordinate *GetPositionCoordinate()
        
        Get the PositionCoordinate instance of vtkCoordinate. This is
        used for for complicated or relative positioning. The position
        variable controls the lower left corner of the Actor2D
        """
        ...
    
    def GetProperty(self):
        """
        V.GetProperty() -> vtkProperty2D
        C++: vtkProperty2D *GetProperty()
        
        Returns this actor's vtkProperty2D.  Creates a property if one
        doesn't already exist.
        """
        ...
    
    def GetWidth(self):
        """
        V.GetWidth() -> float
        C++: double GetWidth()
        
        Set/Get the height and width of the Actor2D. The value is
        expressed as a fraction of the viewport. This really is just
        another way of setting the Position2 instance variable.
        """
        ...
    
    def HasTranslucentPolygonalGeometry(self):
        """
        V.HasTranslucentPolygonalGeometry() -> int
        C++: vtkTypeBool HasTranslucentPolygonalGeometry() override;
        
        Does this prop have some translucent polygonal geometry?
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
        V.NewInstance() -> vtkActor2D
        C++: vtkActor2D *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override;
        
        Release any graphics resources that are being consumed by this
        actor. The parameter window could be used to determine which
        graphic resources to release.
        """
        ...
    
    def RenderOpaqueGeometry(self, vtkViewport):
        """
        V.RenderOpaqueGeometry(vtkViewport) -> int
        C++: int RenderOpaqueGeometry(vtkViewport *viewport) override;
        
        Support the standard render methods.
        """
        ...
    
    def RenderOverlay(self, vtkViewport):
        """
        V.RenderOverlay(vtkViewport) -> int
        C++: int RenderOverlay(vtkViewport *viewport) override;
        
        Support the standard render methods.
        """
        ...
    
    def RenderTranslucentPolygonalGeometry(self, vtkViewport):
        """
        V.RenderTranslucentPolygonalGeometry(vtkViewport) -> int
        C++: int RenderTranslucentPolygonalGeometry(vtkViewport *viewport)
             override;
        
        Support the standard render methods.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkActor2D
        C++: static vtkActor2D *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetDisplayPosition(self, p_int, p_int_1):
        """
        V.SetDisplayPosition(int, int)
        C++: void SetDisplayPosition(int, int)
        
        Set the Prop2D's position in display coordinates.
        """
        ...
    
    def SetHeight(self, p_float):
        """
        V.SetHeight(float)
        C++: void SetHeight(double h)
        
        Set/Get the height and width of the Actor2D. The value is
        expressed as a fraction of the viewport. This really is just
        another way of setting the Position2 instance variable.
        """
        ...
    
    def SetLayerNumber(self, p_int):
        """
        V.SetLayerNumber(int)
        C++: virtual void SetLayerNumber(int _arg)
        
        Set/Get the layer number in the overlay planes into which to
        render.
        """
        ...
    
    def SetMapper(self, vtkMapper2D):
        """
        V.SetMapper(vtkMapper2D)
        C++: virtual void SetMapper(vtkMapper2D *mapper)
        
        Set/Get the vtkMapper2D which defines the data to be drawn.
        """
        ...
    
    def SetPosition(self, p_float=..., p_float=...):
        """
        V.SetPosition([float, float])
        C++: virtual void SetPosition(double x[2])
        V.SetPosition(float, float)
        C++: virtual void SetPosition(double x, double y)
        
        Get the PositionCoordinate instance of vtkCoordinate. This is
        used for for complicated or relative positioning. The position
        variable controls the lower left corner of the Actor2D
        """
        ...
    
    def SetPosition2(self, p_float=..., p_float=...):
        """
        V.SetPosition2([float, float])
        C++: virtual void SetPosition2(double x[2])
        V.SetPosition2(float, float)
        C++: virtual void SetPosition2(double x, double y)
        
        Access the Position2 instance variable. This variable controls
        the upper right corner of the Actor2D. It is by default relative
        to Position and in normalized viewport coordinates. Some 2D actor
        subclasses ignore the position2 variable
        """
        ...
    
    def SetProperty(self, vtkProperty2D):
        """
        V.SetProperty(vtkProperty2D)
        C++: virtual void SetProperty(vtkProperty2D *)
        
        Set this vtkProp's vtkProperty2D.
        """
        ...
    
    def SetWidth(self, p_float):
        """
        V.SetWidth(float)
        C++: void SetWidth(double w)
        
        Set/Get the height and width of the Actor2D. The value is
        expressed as a fraction of the viewport. This really is just
        another way of setting the Position2 instance variable.
        """
        ...
    
    def ShallowCopy(self, vtkProp):
        """
        V.ShallowCopy(vtkProp)
        C++: void ShallowCopy(vtkProp *prop) override;
        
        Shallow copy of this vtkActor2D. Overloads the virtual vtkProp
        method.
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

