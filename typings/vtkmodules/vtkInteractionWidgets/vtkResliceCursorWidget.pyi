"""
This type stub file was generated by pyright.
"""

from .vtkAbstractWidget import vtkAbstractWidget

class vtkResliceCursorWidget(vtkAbstractWidget):
    """
    vtkResliceCursorWidget - represent a reslice cursor
    
    Superclass: vtkAbstractWidget
    
    This class represents a reslice cursor that can be used to perform
    interactive thick slab MPR's through data. It consists of two cross
    sectional hairs, with an optional thickness. The hairs may have a
    hole in the center. These may be translated or rotated independent of
    each other in the view. The result is used to reslice the data along
    these cross sections. This allows the user to perform multi-planar
    thin or thick reformat of the data on an image view, rather than a 3D
    view. The class internally uses vtkImageSlabReslice or
    vtkImageReslice depending on the modes in vtkResliceCursor to do its
    reslicing. The slab thickness is set interactively from the widget.
    The slab resolution (ie the number of blend points) is set as the
    minimum spacing along any dimension from the dataset.
    @sa
    vtkImageSlabReslice vtkResliceCursorLineRepresentation
    vtkResliceCursor
    """
    def CreateDefaultRepresentation(self):
        """
        V.CreateDefaultRepresentation()
        C++: void CreateDefaultRepresentation() override;
        
        Create the default widget representation if one is not set.
        """
        ...
    
    def GetManageWindowLevel(self):
        """
        V.GetManageWindowLevel() -> int
        C++: virtual vtkTypeBool GetManageWindowLevel()
        
        Also perform window level ?
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard VTK class macros.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard VTK class macros.
        """
        ...
    
    def GetResliceCursorRepresentation(self):
        """
        V.GetResliceCursorRepresentation()
            -> vtkResliceCursorRepresentation
        C++: vtkResliceCursorRepresentation *GetResliceCursorRepresentation(
            )
        
        Return the representation as a vtkResliceCursorRepresentation.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard VTK class macros.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard VTK class macros.
        """
        ...
    
    def ManageWindowLevelOff(self):
        """
        V.ManageWindowLevelOff()
        C++: virtual void ManageWindowLevelOff()
        
        Also perform window level ?
        """
        ...
    
    def ManageWindowLevelOn(self):
        """
        V.ManageWindowLevelOn()
        C++: virtual void ManageWindowLevelOn()
        
        Also perform window level ?
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkResliceCursorWidget
        C++: vtkResliceCursorWidget *NewInstance()
        
        Standard VTK class macros.
        """
        ...
    
    def ResetResliceCursor(self):
        """
        V.ResetResliceCursor()
        C++: virtual void ResetResliceCursor()
        
        Reset the cursor back to its initial state
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkResliceCursorWidget
        C++: static vtkResliceCursorWidget *SafeDownCast(vtkObjectBase *o)
        
        Standard VTK class macros.
        """
        ...
    
    def SetEnabled(self, p_int):
        """
        V.SetEnabled(int)
        C++: void SetEnabled(int) override;
        
        Methods for activiating this widget. This implementation extends
        the superclasses' in order to resize the widget handles due to a
        render start event.
        """
        ...
    
    def SetManageWindowLevel(self, p_int):
        """
        V.SetManageWindowLevel(int)
        C++: virtual void SetManageWindowLevel(vtkTypeBool _arg)
        
        Also perform window level ?
        """
        ...
    
    def SetRepresentation(self, vtkResliceCursorRepresentation):
        """
        V.SetRepresentation(vtkResliceCursorRepresentation)
        C++: void SetRepresentation(vtkResliceCursorRepresentation *r)
        
        Specify an instance of vtkWidgetRepresentation used to represent
        this widget in the scene. Note that the representation is a
        subclass of vtkProp so it can be added to the renderer
        independent of the widget.
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
    ResetCursorEvent = ...
    ResliceAxesChangedEvent = ...
    ResliceThicknessChangedEvent = ...
    WindowLevelEvent = ...
    __dict__ = ...
    __vtkname__ = ...


