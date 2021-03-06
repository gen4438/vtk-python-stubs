"""
This type stub file was generated by pyright.
"""

from .vtkEdgeSubdivisionCriterion import vtkEdgeSubdivisionCriterion

class vtkDataSetEdgeSubdivisionCriterion(vtkEdgeSubdivisionCriterion):
    """
    vtkDataSetEdgeSubdivisionCriterion - a subclass of
    vtkEdgeSubdivisionCriterion for vtkDataSet objects.
    
    Superclass: vtkEdgeSubdivisionCriterion
    
    This is a subclass of vtkEdgeSubdivisionCriterion that is used for
    tessellating cells of a vtkDataSet, particularly nonlinear cells.
    
    It provides functions for setting the current cell being tessellated
    and a convenience routine, EvaluateFields() to evaluate field values
    at a point. You should call EvaluateFields() from inside
    EvaluateLocationAndFields() whenever the result of
    EvaluateLocationAndFields() will be true. Otherwise, do not call
    EvaluateFields() as the midpoint is about to be discarded.
    (Implementor's note</i>: This isn't true if UGLY_ASPECT_RATIO_HACK
    has been defined. But in that case, we don't want the exact field
    values; we need the linearly interpolated ones at the midpoint for
    continuity.)
    
    @sa
    vtkEdgeSubdivisionCriterion
    """
    def EvaluateCellDataField(self, *float, **kwargs):
        """
        V.EvaluateCellDataField([float, ...], [float, ...], int)
        C++: void EvaluateCellDataField(double *result, double *weights,
            int field)
        
        Evaluate either a cell or nodal field. This exists because of the
        funky way that Exodus data will be handled. Sure, it's a hack,
        but what are ya gonna do?
        """
        ...
    
    def EvaluateFields(self, *float, **kwargs):
        """
        V.EvaluateFields([float, ...], [float, ...], int) -> (float, ...)
        C++: double *EvaluateFields(double *vertex, double *weights,
            int field_start)
        
        Evaluate all of the fields that should be output with the given
        vertex and store them just past the parametric coordinates of
        vertex, at the offsets given
        byvtkEdgeSubdivisionCriterion::GetFieldOffsets() plus
        field_start.field_start contains the number of world-space
        coordinates (always 3) plus the embedding dimension (the size of
        the parameter-space in which the cell is embedded). It will range
        between 3 and 6, inclusive.
        
        * You must have called SetCellId() before calling this routine or
        there
        * will not be a mesh over which to evaluate the fields.
        
        * You must have called
          vtkEdgeSubdivisionCriterion::PassDefaultFields()
        * or vtkEdgeSubdivisionCriterion::PassField() or there will be no
        fields
        * defined for the output vertex.
        
        * This routine is public and returns its input argument so that
          it
        * may be used as an argument to
        * vtkStreamingTessellator::AdaptivelySamplekFacet():
        * 
         * vtkStreamingTessellator* t = vtkStreamingTessellator::New();
         * vtkEdgeSubdivisionCriterion* s;
         * ...
         * t->AdaptivelySample1Facet( s->EvaluateFields( p0 ), s->EvaluateFields( p1 ) );
         * ...
         * 
        * Although this will work, using EvaluateFields() in this manner
        * should be avoided. It's much more efficient to fetch the corner
        values
        * for each attribute and copy them into p0, p1, ... as opposed to
        * performing shape function evaluations. The only case where you
          wouldn't
        * want to do this is when the field you are interpolating is
          discontinuous
        * at cell borders, such as with a discontinuous galerkin method
          or when
        * all the Gauss points for quadrature are interior to the cell.
        
        * The final argument, weights, is the array of weights to apply
          to each
        * point's data when interpolating the field. This is returned by
        * vtkCell::EvaluateLocation() when evaluating the geometry.
        """
        ...
    
    def EvaluateLocationAndFields(self, *float, **kwargs):
        """
        V.EvaluateLocationAndFields([float, ...], int) -> bool
        C++: bool EvaluateLocationAndFields(double *midpt,
            int field_start) override;
        
        You must implement this member function in a subclass. It will be
        called by vtkStreamingTessellator for each edge in each primitive
        that vtkStreamingTessellator generates.
        """
        ...
    
    def EvaluatePointDataField(self, *float, **kwargs):
        """
        V.EvaluatePointDataField([float, ...], [float, ...], int)
        C++: void EvaluatePointDataField(double *result, double *weights,
            int field)
        
        Evaluate either a cell or nodal field. This exists because of the
        funky way that Exodus data will be handled. Sure, it's a hack,
        but what are ya gonna do?
        """
        ...
    
    def GetActiveFieldCriteria(self):
        """
        V.GetActiveFieldCriteria() -> int
        C++: virtual int GetActiveFieldCriteria()
        
        Return a bitfield specifying which FieldError2 criteria are
        positive (i.e., actively used to decide edge subdivisions). This
        is stored as separate state to make subdivisions go faster.
        """
        ...
    
    def GetCell(self):
        """
        V.GetCell() -> vtkCell
        C++: vtkCell *GetCell()
        """
        ...
    
    def GetCellId(self):
        """
        V.GetCellId() -> int
        C++: vtkIdType &GetCellId()
        """
        ...
    
    def GetChordError2(self):
        """
        V.GetChordError2() -> float
        C++: virtual double GetChordError2()
        
        Get/Set the square of the allowable chord error at any edge's
        midpoint. This value is used by EvaluateLocationAndFields.
        """
        ...
    
    def GetFieldError2(self, p_int):
        """
        V.GetFieldError2(int) -> float
        C++: double GetFieldError2(int s)
        
        Get/Set the square of the allowable error magnitude for the
        scalar field s at any edge's midpoint. A value less than or equal
        to 0 indicates that the field should not be used as a criterion
        for subdivision.
        """
        ...
    
    def GetMesh(self):
        """
        V.GetMesh() -> vtkDataSet
        C++: vtkDataSet *GetMesh()
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
        V.NewInstance() -> vtkDataSetEdgeSubdivisionCriterion
        C++: vtkDataSetEdgeSubdivisionCriterion *NewInstance()
        """
        ...
    
    def ResetFieldError2(self):
        """
        V.ResetFieldError2()
        C++: virtual void ResetFieldError2()
        
        Tell the subdivider not to use any field values as subdivision
        criteria. Effectively calls SetFieldError2( a, -1. ) for all
        fields.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkDataSetEdgeSubdivisionCriterion
        C++: static vtkDataSetEdgeSubdivisionCriterion *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetCellId(self, p_int):
        """
        V.SetCellId(int)
        C++: virtual void SetCellId(vtkIdType cell)
        """
        ...
    
    def SetChordError2(self, p_float):
        """
        V.SetChordError2(float)
        C++: virtual void SetChordError2(double _arg)
        
        Get/Set the square of the allowable chord error at any edge's
        midpoint. This value is used by EvaluateLocationAndFields.
        """
        ...
    
    def SetFieldError2(self, p_int, p_float):
        """
        V.SetFieldError2(int, float)
        C++: virtual void SetFieldError2(int s, double err)
        
        Get/Set the square of the allowable error magnitude for the
        scalar field s at any edge's midpoint. A value less than or equal
        to 0 indicates that the field should not be used as a criterion
        for subdivision.
        """
        ...
    
    def SetMesh(self, vtkDataSet):
        """
        V.SetMesh(vtkDataSet)
        C++: virtual void SetMesh(vtkDataSet *)
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


