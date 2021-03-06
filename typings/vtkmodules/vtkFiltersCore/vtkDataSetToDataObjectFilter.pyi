"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkDataSetToDataObjectFilter(__vtkmodules_vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    """
    vtkDataSetToDataObjectFilter - map dataset into data object (i.e., a
    field)
    
    Superclass: vtkDataObjectAlgorithm
    
    vtkDataSetToDataObjectFilter is an class that transforms a dataset
    into data object (i.e., a field). The field will have labeled data
    arrays corresponding to the topology, geometry, field data, and point
    and cell attribute data.
    
    You can control what portions of the dataset are converted into the
    output data object's field data. The instance variables Geometry,
    Topology, FieldData, PointData, and CellData are flags that control
    whether the dataset's geometry (e.g., points, spacing, origin);
    topology (e.g., cell connectivity, dimensions); the field data
    associated with the dataset's superclass data object; the dataset's
    point data attributes; and the dataset's cell data attributes. (Note:
    the data attributes include scalars, vectors, tensors, normals,
    texture coordinates, and field data.)
    
    The names used to create the field data are as follows. For
    vtkPolyData, "Points", "Verts", "Lines", "Polys", and "Strips". For
    vtkUnstructuredGrid, "Cells" and "CellTypes". For
    vtkStructuredPoints, "Dimensions", "Spacing", and "Origin". For
    vtkStructuredGrid, "Points" and "Dimensions". For vtkRectilinearGrid,
    "XCoordinates", "YCoordinates", and "ZCoordinates". for point
    attribute data, "PointScalars", "PointVectors", etc. For cell
    attribute data, "CellScalars", "CellVectors", etc. Field data arrays
    retain their original name.
    
    @sa
    vtkDataObject vtkFieldData vtkDataObjectToDataSetFilter
    """
    def CellDataOff(self):
        """
        V.CellDataOff()
        C++: virtual void CellDataOff()
        
        Turn on/off the conversion of dataset cell data to a data object.
        """
        ...
    
    def CellDataOn(self):
        """
        V.CellDataOn()
        C++: virtual void CellDataOn()
        
        Turn on/off the conversion of dataset cell data to a data object.
        """
        ...
    
    def FieldDataOff(self):
        """
        V.FieldDataOff()
        C++: virtual void FieldDataOff()
        
        Turn on/off the conversion of dataset field data to a data
        object.
        """
        ...
    
    def FieldDataOn(self):
        """
        V.FieldDataOn()
        C++: virtual void FieldDataOn()
        
        Turn on/off the conversion of dataset field data to a data
        object.
        """
        ...
    
    def GeometryOff(self):
        """
        V.GeometryOff()
        C++: virtual void GeometryOff()
        
        Turn on/off the conversion of dataset geometry to a data object.
        """
        ...
    
    def GeometryOn(self):
        """
        V.GeometryOn()
        C++: virtual void GeometryOn()
        
        Turn on/off the conversion of dataset geometry to a data object.
        """
        ...
    
    def GetCellData(self):
        """
        V.GetCellData() -> int
        C++: virtual vtkTypeBool GetCellData()
        
        Turn on/off the conversion of dataset cell data to a data object.
        """
        ...
    
    def GetFieldData(self):
        """
        V.GetFieldData() -> int
        C++: virtual vtkTypeBool GetFieldData()
        
        Turn on/off the conversion of dataset field data to a data
        object.
        """
        ...
    
    def GetGeometry(self):
        """
        V.GetGeometry() -> int
        C++: virtual vtkTypeBool GetGeometry()
        
        Turn on/off the conversion of dataset geometry to a data object.
        """
        ...
    
    def GetLegacyTopology(self):
        """
        V.GetLegacyTopology() -> int
        C++: virtual vtkTypeBool GetLegacyTopology()
        
        If LegacyTopology and Topology are both true, print out the
        legacy topology arrays. Default is true.
        """
        ...
    
    def GetModernTopology(self):
        """
        V.GetModernTopology() -> int
        C++: virtual vtkTypeBool GetModernTopology()
        
        If ModernTopology and Topology are both true, print out the
        modern topology arrays. Default is true.
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
    
    def GetPointData(self):
        """
        V.GetPointData() -> int
        C++: virtual vtkTypeBool GetPointData()
        
        Turn on/off the conversion of dataset point data to a data
        object.
        """
        ...
    
    def GetTopology(self):
        """
        V.GetTopology() -> int
        C++: virtual vtkTypeBool GetTopology()
        
        Turn on/off the conversion of dataset topology to a data object.
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
    
    def LegacyTopologyOff(self):
        """
        V.LegacyTopologyOff()
        C++: virtual void LegacyTopologyOff()
        
        If LegacyTopology and Topology are both true, print out the
        legacy topology arrays. Default is true.
        """
        ...
    
    def LegacyTopologyOn(self):
        """
        V.LegacyTopologyOn()
        C++: virtual void LegacyTopologyOn()
        
        If LegacyTopology and Topology are both true, print out the
        legacy topology arrays. Default is true.
        """
        ...
    
    def ModernTopologyOff(self):
        """
        V.ModernTopologyOff()
        C++: virtual void ModernTopologyOff()
        
        If ModernTopology and Topology are both true, print out the
        modern topology arrays. Default is true.
        """
        ...
    
    def ModernTopologyOn(self):
        """
        V.ModernTopologyOn()
        C++: virtual void ModernTopologyOn()
        
        If ModernTopology and Topology are both true, print out the
        modern topology arrays. Default is true.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkDataSetToDataObjectFilter
        C++: vtkDataSetToDataObjectFilter *NewInstance()
        """
        ...
    
    def PointDataOff(self):
        """
        V.PointDataOff()
        C++: virtual void PointDataOff()
        
        Turn on/off the conversion of dataset point data to a data
        object.
        """
        ...
    
    def PointDataOn(self):
        """
        V.PointDataOn()
        C++: virtual void PointDataOn()
        
        Turn on/off the conversion of dataset point data to a data
        object.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDataSetToDataObjectFilter
        C++: static vtkDataSetToDataObjectFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetCellData(self, p_int):
        """
        V.SetCellData(int)
        C++: virtual void SetCellData(vtkTypeBool _arg)
        
        Turn on/off the conversion of dataset cell data to a data object.
        """
        ...
    
    def SetFieldData(self, p_int):
        """
        V.SetFieldData(int)
        C++: virtual void SetFieldData(vtkTypeBool _arg)
        
        Turn on/off the conversion of dataset field data to a data
        object.
        """
        ...
    
    def SetGeometry(self, p_int):
        """
        V.SetGeometry(int)
        C++: virtual void SetGeometry(vtkTypeBool _arg)
        
        Turn on/off the conversion of dataset geometry to a data object.
        """
        ...
    
    def SetLegacyTopology(self, p_int):
        """
        V.SetLegacyTopology(int)
        C++: virtual void SetLegacyTopology(vtkTypeBool _arg)
        
        If LegacyTopology and Topology are both true, print out the
        legacy topology arrays. Default is true.
        """
        ...
    
    def SetModernTopology(self, p_int):
        """
        V.SetModernTopology(int)
        C++: virtual void SetModernTopology(vtkTypeBool _arg)
        
        If ModernTopology and Topology are both true, print out the
        modern topology arrays. Default is true.
        """
        ...
    
    def SetPointData(self, p_int):
        """
        V.SetPointData(int)
        C++: virtual void SetPointData(vtkTypeBool _arg)
        
        Turn on/off the conversion of dataset point data to a data
        object.
        """
        ...
    
    def SetTopology(self, p_int):
        """
        V.SetTopology(int)
        C++: virtual void SetTopology(vtkTypeBool _arg)
        
        Turn on/off the conversion of dataset topology to a data object.
        """
        ...
    
    def TopologyOff(self):
        """
        V.TopologyOff()
        C++: virtual void TopologyOff()
        
        Turn on/off the conversion of dataset topology to a data object.
        """
        ...
    
    def TopologyOn(self):
        """
        V.TopologyOn()
        C++: virtual void TopologyOn()
        
        Turn on/off the conversion of dataset topology to a data object.
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


