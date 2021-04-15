"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkTableToPolyData(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkTableToPolyData - filter used to convert a vtkTable to a
    vtkPolyData consisting of vertices.
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkTableToPolyData is a filter used to convert a vtkTable  to a
    vtkPolyData consisting of vertices.
    """
    def Create2DPointsOff(self):
        """
        V.Create2DPointsOff()
        C++: virtual void Create2DPointsOff()
        
        Specify whether the points of the polydata are 3D or 2D. If this
        is set to true then the Z Column will be ignored and the z value
        of each point on the polydata will be set to 0. By default this
        will be off.
        """
        ...
    
    def Create2DPointsOn(self):
        """
        V.Create2DPointsOn()
        C++: virtual void Create2DPointsOn()
        
        Specify whether the points of the polydata are 3D or 2D. If this
        is set to true then the Z Column will be ignored and the z value
        of each point on the polydata will be set to 0. By default this
        will be off.
        """
        ...
    
    def GetCreate2DPoints(self):
        """
        V.GetCreate2DPoints() -> bool
        C++: virtual bool GetCreate2DPoints()
        
        Specify whether the points of the polydata are 3D or 2D. If this
        is set to true then the Z Column will be ignored and the z value
        of each point on the polydata will be set to 0. By default this
        will be off.
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
    
    def GetPreserveCoordinateColumnsAsDataArrays(self):
        """
        V.GetPreserveCoordinateColumnsAsDataArrays() -> bool
        C++: virtual bool GetPreserveCoordinateColumnsAsDataArrays()
        
        Allow user to keep columns specified as X,Y,Z as Data arrays. By
        default this will be off.
        """
        ...
    
    def GetXColumn(self):
        """
        V.GetXColumn() -> string
        C++: virtual char *GetXColumn()
        
        Set the name of the column to use as the X coordinate for the
        points.
        """
        ...
    
    def GetXColumnIndex(self):
        """
        V.GetXColumnIndex() -> int
        C++: virtual int GetXColumnIndex()
        
        Set the index of the column to use as the X coordinate for the
        points.
        """
        ...
    
    def GetXColumnIndexMaxValue(self):
        """
        V.GetXColumnIndexMaxValue() -> int
        C++: virtual int GetXColumnIndexMaxValue()
        
        Set the index of the column to use as the X coordinate for the
        points.
        """
        ...
    
    def GetXColumnIndexMinValue(self):
        """
        V.GetXColumnIndexMinValue() -> int
        C++: virtual int GetXColumnIndexMinValue()
        
        Set the index of the column to use as the X coordinate for the
        points.
        """
        ...
    
    def GetXComponent(self):
        """
        V.GetXComponent() -> int
        C++: virtual int GetXComponent()
        
        Specify the component for the column specified using SetXColumn()
        to use as the xcoordinate in case the column is a multi-component
        array. Default is 0.
        """
        ...
    
    def GetXComponentMaxValue(self):
        """
        V.GetXComponentMaxValue() -> int
        C++: virtual int GetXComponentMaxValue()
        
        Specify the component for the column specified using SetXColumn()
        to use as the xcoordinate in case the column is a multi-component
        array. Default is 0.
        """
        ...
    
    def GetXComponentMinValue(self):
        """
        V.GetXComponentMinValue() -> int
        C++: virtual int GetXComponentMinValue()
        
        Specify the component for the column specified using SetXColumn()
        to use as the xcoordinate in case the column is a multi-component
        array. Default is 0.
        """
        ...
    
    def GetYColumn(self):
        """
        V.GetYColumn() -> string
        C++: virtual char *GetYColumn()
        
        Set the name of the column to use as the Y coordinate for the
        points. Default is 0.
        """
        ...
    
    def GetYColumnIndex(self):
        """
        V.GetYColumnIndex() -> int
        C++: virtual int GetYColumnIndex()
        
        Set the index of the column to use as the Y coordinate for the
        points.
        """
        ...
    
    def GetYColumnIndexMaxValue(self):
        """
        V.GetYColumnIndexMaxValue() -> int
        C++: virtual int GetYColumnIndexMaxValue()
        
        Set the index of the column to use as the Y coordinate for the
        points.
        """
        ...
    
    def GetYColumnIndexMinValue(self):
        """
        V.GetYColumnIndexMinValue() -> int
        C++: virtual int GetYColumnIndexMinValue()
        
        Set the index of the column to use as the Y coordinate for the
        points.
        """
        ...
    
    def GetYComponent(self):
        """
        V.GetYComponent() -> int
        C++: virtual int GetYComponent()
        
        Specify the component for the column specified using SetYColumn()
        to use as the Ycoordinate in case the column is a multi-component
        array.
        """
        ...
    
    def GetYComponentMaxValue(self):
        """
        V.GetYComponentMaxValue() -> int
        C++: virtual int GetYComponentMaxValue()
        
        Specify the component for the column specified using SetYColumn()
        to use as the Ycoordinate in case the column is a multi-component
        array.
        """
        ...
    
    def GetYComponentMinValue(self):
        """
        V.GetYComponentMinValue() -> int
        C++: virtual int GetYComponentMinValue()
        
        Specify the component for the column specified using SetYColumn()
        to use as the Ycoordinate in case the column is a multi-component
        array.
        """
        ...
    
    def GetZColumn(self):
        """
        V.GetZColumn() -> string
        C++: virtual char *GetZColumn()
        
        Set the name of the column to use as the Z coordinate for the
        points. Default is 0.
        """
        ...
    
    def GetZColumnIndex(self):
        """
        V.GetZColumnIndex() -> int
        C++: virtual int GetZColumnIndex()
        
        Set the index of the column to use as the Z coordinate for the
        points.
        """
        ...
    
    def GetZColumnIndexMaxValue(self):
        """
        V.GetZColumnIndexMaxValue() -> int
        C++: virtual int GetZColumnIndexMaxValue()
        
        Set the index of the column to use as the Z coordinate for the
        points.
        """
        ...
    
    def GetZColumnIndexMinValue(self):
        """
        V.GetZColumnIndexMinValue() -> int
        C++: virtual int GetZColumnIndexMinValue()
        
        Set the index of the column to use as the Z coordinate for the
        points.
        """
        ...
    
    def GetZComponent(self):
        """
        V.GetZComponent() -> int
        C++: virtual int GetZComponent()
        
        Specify the component for the column specified using SetZColumn()
        to use as the Zcoordinate in case the column is a multi-component
        array.
        """
        ...
    
    def GetZComponentMaxValue(self):
        """
        V.GetZComponentMaxValue() -> int
        C++: virtual int GetZComponentMaxValue()
        
        Specify the component for the column specified using SetZColumn()
        to use as the Zcoordinate in case the column is a multi-component
        array.
        """
        ...
    
    def GetZComponentMinValue(self):
        """
        V.GetZComponentMinValue() -> int
        C++: virtual int GetZComponentMinValue()
        
        Specify the component for the column specified using SetZColumn()
        to use as the Zcoordinate in case the column is a multi-component
        array.
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
        V.NewInstance() -> vtkTableToPolyData
        C++: vtkTableToPolyData *NewInstance()
        """
        ...
    
    def PreserveCoordinateColumnsAsDataArraysOff(self):
        """
        V.PreserveCoordinateColumnsAsDataArraysOff()
        C++: virtual void PreserveCoordinateColumnsAsDataArraysOff()
        
        Allow user to keep columns specified as X,Y,Z as Data arrays. By
        default this will be off.
        """
        ...
    
    def PreserveCoordinateColumnsAsDataArraysOn(self):
        """
        V.PreserveCoordinateColumnsAsDataArraysOn()
        C++: virtual void PreserveCoordinateColumnsAsDataArraysOn()
        
        Allow user to keep columns specified as X,Y,Z as Data arrays. By
        default this will be off.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTableToPolyData
        C++: static vtkTableToPolyData *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCreate2DPoints(self, bool):
        """
        V.SetCreate2DPoints(bool)
        C++: virtual void SetCreate2DPoints(bool _arg)
        
        Specify whether the points of the polydata are 3D or 2D. If this
        is set to true then the Z Column will be ignored and the z value
        of each point on the polydata will be set to 0. By default this
        will be off.
        """
        ...
    
    def SetPreserveCoordinateColumnsAsDataArrays(self, bool):
        """
        V.SetPreserveCoordinateColumnsAsDataArrays(bool)
        C++: virtual void SetPreserveCoordinateColumnsAsDataArrays(
            bool _arg)
        
        Allow user to keep columns specified as X,Y,Z as Data arrays. By
        default this will be off.
        """
        ...
    
    def SetXColumn(self, string):
        """
        V.SetXColumn(string)
        C++: virtual void SetXColumn(const char *_arg)
        
        Set the name of the column to use as the X coordinate for the
        points.
        """
        ...
    
    def SetXColumnIndex(self, p_int):
        """
        V.SetXColumnIndex(int)
        C++: virtual void SetXColumnIndex(int _arg)
        
        Set the index of the column to use as the X coordinate for the
        points.
        """
        ...
    
    def SetXComponent(self, p_int):
        """
        V.SetXComponent(int)
        C++: virtual void SetXComponent(int _arg)
        
        Specify the component for the column specified using SetXColumn()
        to use as the xcoordinate in case the column is a multi-component
        array. Default is 0.
        """
        ...
    
    def SetYColumn(self, string):
        """
        V.SetYColumn(string)
        C++: virtual void SetYColumn(const char *_arg)
        
        Set the name of the column to use as the Y coordinate for the
        points. Default is 0.
        """
        ...
    
    def SetYColumnIndex(self, p_int):
        """
        V.SetYColumnIndex(int)
        C++: virtual void SetYColumnIndex(int _arg)
        
        Set the index of the column to use as the Y coordinate for the
        points.
        """
        ...
    
    def SetYComponent(self, p_int):
        """
        V.SetYComponent(int)
        C++: virtual void SetYComponent(int _arg)
        
        Specify the component for the column specified using SetYColumn()
        to use as the Ycoordinate in case the column is a multi-component
        array.
        """
        ...
    
    def SetZColumn(self, string):
        """
        V.SetZColumn(string)
        C++: virtual void SetZColumn(const char *_arg)
        
        Set the name of the column to use as the Z coordinate for the
        points. Default is 0.
        """
        ...
    
    def SetZColumnIndex(self, p_int):
        """
        V.SetZColumnIndex(int)
        C++: virtual void SetZColumnIndex(int _arg)
        
        Set the index of the column to use as the Z coordinate for the
        points.
        """
        ...
    
    def SetZComponent(self, p_int):
        """
        V.SetZComponent(int)
        C++: virtual void SetZComponent(int _arg)
        
        Specify the component for the column specified using SetZColumn()
        to use as the Zcoordinate in case the column is a multi-component
        array.
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


