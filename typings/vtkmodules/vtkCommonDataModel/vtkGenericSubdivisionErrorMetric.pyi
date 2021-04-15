"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkGenericSubdivisionErrorMetric(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkGenericSubdivisionErrorMetric - Objects that compute error during
    cell tessellation.
    
    Superclass: vtkObject
    
    Objects of that class answer the following question during the cell
    subdivision: "does the edge need to be subdivided?" through
    RequiresEdgeSubdivision(). The answer depends on the criterium
    actually used in the subclass of this abstract class: a
    geometric-based error metric (variation of edge from a straight
    line), an attribute-based error metric (variation of the active
    attribute/component value from a linear ramp) , a view-depend error
    metric, ... Cell subdivision is performed in the context of the
    adaptor framework: higher-order, or complex cells, are automatically
    tessellated into simplices so that they can be processed with
    conventional visualization algorithms.
    
    @sa
    vtkGenericCellTessellator
    """
    def GetDataSet(self):
        """
        V.GetDataSet() -> vtkGenericDataSet
        C++: virtual vtkGenericDataSet *GetDataSet()
        
        Set/Get the dataset to be tessellated.
        """
        ...
    
    def GetError(self, *float, **kwargs):
        """
        V.GetError([float, ...], [float, ...], [float, ...], float)
            -> float
        C++: virtual double GetError(double *leftPoint, double *midPoint,
            double *rightPoint, double alpha)
        
        Return the error at the mid-point. The type of error depends on
        the state of the concrete error metric. For instance, it can
        return an absolute or relative error metric. See
        RequiresEdgeSubdivision() for a description of the arguments.
        \pre leftPoint_exists: leftPoint!=0
        \pre midPoint_exists: midPoint!=0
        \pre rightPoint_exists: rightPoint!=0
        \pre clamped_alpha: alpha>0 && alpha<1
        \pre valid_size:
            sizeof(leftPoint)=sizeof(midPoint)=sizeof(rightPoint)
        =GetAttributeCollection()->GetNumberOfPointCenteredComponents()+6
        \post positive_result: result>=0
        """
        ...
    
    def GetGenericCell(self):
        """
        V.GetGenericCell() -> vtkGenericAdaptorCell
        C++: virtual vtkGenericAdaptorCell *GetGenericCell()
        
        The cell that the edge belongs to.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard VTK type and error macros.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard VTK type and error macros.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard VTK type and error macros.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard VTK type and error macros.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkGenericSubdivisionErrorMetric
        C++: vtkGenericSubdivisionErrorMetric *NewInstance()
        
        Standard VTK type and error macros.
        """
        ...
    
    def RequiresEdgeSubdivision(self, *float, **kwargs):
        """
        V.RequiresEdgeSubdivision([float, ...], [float, ...], [float,
            ...], float) -> int
        C++: virtual int RequiresEdgeSubdivision(double *leftPoint,
            double *midPoint, double *rightPoint, double alpha)
        
        Does the edge need to be subdivided according to the implemented
        computation? The edge is defined by its `leftPoint' and its
        `rightPoint'. `leftPoint', `midPoint' and `rightPoint' have to be
        initialized before calling RequiresEdgeSubdivision(). Their
        format is global coordinates, parametric coordinates and point
        centered attributes: xyx rst abc de... `alpha' is the normalized
        abscissa of the midpoint along the edge. (close to 0 means close
        to the left point, close to 1 means close to the right point)
        \pre leftPoint_exists: leftPoint!=0
        \pre midPoint_exists: midPoint!=0
        \pre rightPoint_exists: rightPoint!=0
        \pre clamped_alpha: alpha>0 && alpha<1
        \pre valid_size:
            sizeof(leftPoint)=sizeof(midPoint)=sizeof(rightPoint)
        =GetAttributeCollection()->GetNumberOfPointCenteredComponents()+6
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkGenericSubdivisionErrorMetric
        C++: static vtkGenericSubdivisionErrorMetric *SafeDownCast(
            vtkObjectBase *o)
        
        Standard VTK type and error macros.
        """
        ...
    
    def SetDataSet(self, vtkGenericDataSet):
        """
        V.SetDataSet(vtkGenericDataSet)
        C++: void SetDataSet(vtkGenericDataSet *ds)
        
        Set/Get the dataset to be tessellated.
        """
        ...
    
    def SetGenericCell(self, vtkGenericAdaptorCell):
        """
        V.SetGenericCell(vtkGenericAdaptorCell)
        C++: void SetGenericCell(vtkGenericAdaptorCell *cell)
        
        The cell that the edge belongs to.
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

