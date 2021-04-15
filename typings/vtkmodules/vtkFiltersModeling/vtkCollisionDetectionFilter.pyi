"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkCollisionDetectionFilter(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkCollisionDetectionFilter - performs collision determination
    between two polyhedral surfaces
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkCollisionDetectionFilter performs collision determination between
     two polyhedral surfaces using two instances of vtkOBBTree. Set the
     polydata inputs, the tolerance and transforms or matrices. If
     CollisionMode is set to AllContacts, the Contacts output will be
    lines
     of contact.  If CollisionMode is FirstContact or HalfContacts then
    the
     Contacts output will be vertices.  See below for an explanation of
     these options.
    
    
     This class can be used to clip one polydata surface with another,
     using the Contacts output as a loop set in vtkSelectPolyData
    
    @authors Goodwin Lawlor, Bill Lorensen
    """
    def GenerateScalarsOff(self):
        """
        V.GenerateScalarsOff()
        C++: virtual void GenerateScalarsOff()
        """
        ...
    
    def GenerateScalarsOn(self):
        """
        V.GenerateScalarsOn()
        C++: virtual void GenerateScalarsOn()
        """
        ...
    
    def GetBoxTolerance(self):
        """
        V.GetBoxTolerance() -> float
        C++: virtual float GetBoxTolerance()
        """
        ...
    
    def GetCellTolerance(self):
        """
        V.GetCellTolerance() -> float
        C++: virtual double GetCellTolerance()
        """
        ...
    
    def GetCollisionMode(self):
        """
        V.GetCollisionMode() -> int
        C++: virtual int GetCollisionMode()
        
        Set the collision mode to VTK_ALL_CONTACTS to find all the
        contacting cell pairs with two points per collision, or
        VTK_HALF_CONTACTS to find all the contacting cell pairs with one
        point per collision, or VTK_FIRST_CONTACT to quickly find the
        first contact point.
        """
        ...
    
    def GetCollisionModeAsString(self):
        """
        V.GetCollisionModeAsString() -> string
        C++: const char *GetCollisionModeAsString(void)
        
        Set the collision mode to VTK_ALL_CONTACTS to find all the
        contacting cell pairs with two points per collision, or
        VTK_HALF_CONTACTS to find all the contacting cell pairs with one
        point per collision, or VTK_FIRST_CONTACT to quickly find the
        first contact point.
        """
        ...
    
    def GetCollisionModeMaxValue(self):
        """
        V.GetCollisionModeMaxValue() -> int
        C++: virtual int GetCollisionModeMaxValue()
        
        Set the collision mode to VTK_ALL_CONTACTS to find all the
        contacting cell pairs with two points per collision, or
        VTK_HALF_CONTACTS to find all the contacting cell pairs with one
        point per collision, or VTK_FIRST_CONTACT to quickly find the
        first contact point.
        """
        ...
    
    def GetCollisionModeMinValue(self):
        """
        V.GetCollisionModeMinValue() -> int
        C++: virtual int GetCollisionModeMinValue()
        
        Set the collision mode to VTK_ALL_CONTACTS to find all the
        contacting cell pairs with two points per collision, or
        VTK_HALF_CONTACTS to find all the contacting cell pairs with one
        point per collision, or VTK_FIRST_CONTACT to quickly find the
        first contact point.
        """
        ...
    
    def GetContactCells(self, p_int):
        """
        V.GetContactCells(int) -> vtkIdTypeArray
        C++: vtkIdTypeArray *GetContactCells(int i)
        
        Get an array of the contacting cells. This is a convenience
        method to access the "ContactCells" field array in outputs 0 and
        1. These arrays index contacting cells (eg) index 50 of array 0
        points to a cell (triangle) which contacts/intersects a cell at
        index 50 of array 1. This method is equivalent to
        GetOutput(i)->GetFieldData()->GetArray("ContactCells")
        """
        ...
    
    def GetContactsOutput(self):
        """
        V.GetContactsOutput() -> vtkPolyData
        C++: vtkPolyData *GetContactsOutput()
        
        Get the output with the points where the contacting cells
        intersect. This method is is equivalent to
        GetOutputPort(2)/GetOutput(2)
        """
        ...
    
    def GetContactsOutputPort(self):
        """
        V.GetContactsOutputPort() -> vtkAlgorithmOutput
        C++: vtkAlgorithmOutput *GetContactsOutputPort()
        
        Get the output with the points where the contacting cells
        intersect. This method is is equivalent to
        GetOutputPort(2)/GetOutput(2)
        """
        ...
    
    def GetGenerateScalars(self):
        """
        V.GetGenerateScalars() -> int
        C++: virtual int GetGenerateScalars()
        """
        ...
    
    def GetInputData(self, p_int):
        """
        V.GetInputData(int) -> vtkPolyData
        C++: vtkPolyData *GetInputData(int i)
        
        Set and Get the input vtk polydata models
        """
        ...
    
    def GetMatrix(self, p_int):
        """
        V.GetMatrix(int) -> vtkMatrix4x4
        C++: vtkMatrix4x4 *GetMatrix(int i)
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Return this object's modified time.
        """
        ...
    
    def GetNumberOfBoxTests(self):
        """
        V.GetNumberOfBoxTests() -> int
        C++: virtual int GetNumberOfBoxTests()
        """
        ...
    
    def GetNumberOfCellsPerNode(self):
        """
        V.GetNumberOfCellsPerNode() -> int
        C++: virtual int GetNumberOfCellsPerNode()
        """
        ...
    
    def GetNumberOfContacts(self):
        """
        V.GetNumberOfContacts() -> int
        C++: int GetNumberOfContacts()
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def GetOpacity(self):
        """
        V.GetOpacity() -> float
        C++: virtual float GetOpacity()
        """
        ...
    
    def GetOpacityMaxValue(self):
        """
        V.GetOpacityMaxValue() -> float
        C++: virtual float GetOpacityMaxValue()
        """
        ...
    
    def GetOpacityMinValue(self):
        """
        V.GetOpacityMinValue() -> float
        C++: virtual float GetOpacityMinValue()
        """
        ...
    
    def GetTransform(self, p_int):
        """
        V.GetTransform(int) -> vtkLinearTransform
        C++: vtkLinearTransform *GetTransform(int i)
        """
        ...
    
    def IntersectPolygonWithPolygon(self, p_int, *float, **kwargs):
        """
        V.IntersectPolygonWithPolygon(int, [float, ...], [float, float,
            float, float, float, float], int, [float, ...], [float, float,
             float, float, float, float], float, [float, float], [float,
            float, float], int) -> int
        C++: int IntersectPolygonWithPolygon(int npts, double *pts,
            double bounds[6], int npts2, double *pts2, double bounds2[6],
            double tol2, double x1[2], double x2[3], int CollisionMode)
        
        Description: Intersect two polygons, return x1 and x2 as the two
        points of intersection. If CollisionMode = VTK_ALL_CONTACTS, both
        contact points are found. If CollisionMode = VTK_FIRST_CONTACT or
        VTK_HALF_CONTACTS, only one contact point is found.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkCollisionDetectionFilter
        C++: vtkCollisionDetectionFilter *NewInstance()
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCollisionDetectionFilter
        C++: static vtkCollisionDetectionFilter *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for construction, type and printing.
        """
        ...
    
    def SetBoxTolerance(self, p_float):
        """
        V.SetBoxTolerance(float)
        C++: virtual void SetBoxTolerance(float _arg)
        """
        ...
    
    def SetCellTolerance(self, p_float):
        """
        V.SetCellTolerance(float)
        C++: virtual void SetCellTolerance(double _arg)
        """
        ...
    
    def SetCollisionMode(self, p_int):
        """
        V.SetCollisionMode(int)
        C++: virtual void SetCollisionMode(int _arg)
        
        Set the collision mode to VTK_ALL_CONTACTS to find all the
        contacting cell pairs with two points per collision, or
        VTK_HALF_CONTACTS to find all the contacting cell pairs with one
        point per collision, or VTK_FIRST_CONTACT to quickly find the
        first contact point.
        """
        ...
    
    def SetCollisionModeToAllContacts(self):
        """
        V.SetCollisionModeToAllContacts()
        C++: void SetCollisionModeToAllContacts()
        
        Set the collision mode to VTK_ALL_CONTACTS to find all the
        contacting cell pairs with two points per collision, or
        VTK_HALF_CONTACTS to find all the contacting cell pairs with one
        point per collision, or VTK_FIRST_CONTACT to quickly find the
        first contact point.
        """
        ...
    
    def SetCollisionModeToFirstContact(self):
        """
        V.SetCollisionModeToFirstContact()
        C++: void SetCollisionModeToFirstContact()
        
        Set the collision mode to VTK_ALL_CONTACTS to find all the
        contacting cell pairs with two points per collision, or
        VTK_HALF_CONTACTS to find all the contacting cell pairs with one
        point per collision, or VTK_FIRST_CONTACT to quickly find the
        first contact point.
        """
        ...
    
    def SetCollisionModeToHalfContacts(self):
        """
        V.SetCollisionModeToHalfContacts()
        C++: void SetCollisionModeToHalfContacts()
        
        Set the collision mode to VTK_ALL_CONTACTS to find all the
        contacting cell pairs with two points per collision, or
        VTK_HALF_CONTACTS to find all the contacting cell pairs with one
        point per collision, or VTK_FIRST_CONTACT to quickly find the
        first contact point.
        """
        ...
    
    def SetGenerateScalars(self, p_int):
        """
        V.SetGenerateScalars(int)
        C++: virtual void SetGenerateScalars(int _arg)
        """
        ...
    
    def SetInputData(self, p_int, vtkPolyData):
        """
        V.SetInputData(int, vtkPolyData)
        C++: void SetInputData(int i, vtkPolyData *model)
        
        Set and Get the input vtk polydata models
        """
        ...
    
    def SetMatrix(self, p_int, vtkMatrix4x4):
        """
        V.SetMatrix(int, vtkMatrix4x4)
        C++: void SetMatrix(int i, vtkMatrix4x4 *matrix)
        """
        ...
    
    def SetNumberOfCellsPerNode(self, p_int):
        """
        V.SetNumberOfCellsPerNode(int)
        C++: virtual void SetNumberOfCellsPerNode(int _arg)
        """
        ...
    
    def SetOpacity(self, p_float):
        """
        V.SetOpacity(float)
        C++: virtual void SetOpacity(float _arg)
        """
        ...
    
    def SetTransform(self, p_int, vtkLinearTransform):
        """
        V.SetTransform(int, vtkLinearTransform)
        C++: void SetTransform(int i, vtkLinearTransform *transform)
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
    CollisionModes = ...
    VTK_ALL_CONTACTS = ...
    VTK_FIRST_CONTACT = ...
    VTK_HALF_CONTACTS = ...
    __dict__ = ...
    __vtkname__ = ...


