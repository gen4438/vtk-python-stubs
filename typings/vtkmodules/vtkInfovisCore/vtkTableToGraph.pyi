"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkTableToGraph(__vtkmodules_vtkCommonExecutionModel.vtkGraphAlgorithm):
    """
    vtkTableToGraph - convert a vtkTable into a vtkGraph
    
    Superclass: vtkGraphAlgorithm
    
    vtkTableToGraph converts a table to a graph using an auxiliary link
    graph.  The link graph specifies how each row in the table should be
    converted to an edge, or a collection of edges.  It also specifies
    which columns of the table should be considered part of the same
    domain, and which columns should be hidden.
    
    A second, optional, table may be provided as the vertex table. This
    vertex table must have one or more domain columns whose values match
    values in the edge table.  The linked column name is specified in the
    domain array in the link graph.  The output graph will only contain
    vertices corresponding to a row in the vertex table.  For
    heterogeneous graphs, you may want to use vtkMergeTables to create a
    single vertex table.
    
    The link graph contains the following arrays:
    
    (1) The "column" array has the names of the columns to connect in
    each table row. This array is required.
    
    (2) The optional "domain" array provides user-defined domain names
    for each column. Matching domains in multiple columns will merge
    vertices with the same value from those columns.  By default, all
    columns are in the same domain. If a vertex table is supplied, the
    domain indicates the column in the vertex table that the edge table
    column associates with.  If the user provides a vertex table but no
    domain names, the output will be an empty graph. Hidden columns do
    not need valid domain names.
    
    (3) The optional "hidden" array is a bit array specifying whether the
    column should be hidden.  The resulting graph will contain edges
    representing connections "through" the hidden column, but the
    vertices for that column will not be present.  By default, no columns
    are hidden.  Hiding a column in a particular domain hides all columns
    in that domain.
    
    The output graph will contain three additional arrays in the vertex
    data. The "domain" column is a string array containing the domain of
    each vertex. The "label" column is a string version of the distinct
    value that, along with the domain, defines that vertex. The "ids"
    column also contains the distinguishing value, but as a vtkVariant
    holding the raw value instead of being converted to a string. The
    "ids" column is set as the vertex pedigree ID attribute.
    """
    def AddLinkEdge(self, string, string_1):
        """
        V.AddLinkEdge(string, string)
        C++: void AddLinkEdge(const char *column1, const char *column2)
        
        Add an edge to the link graph.  Specify the names of the columns
        to link.
        """
        ...
    
    def AddLinkVertex(self, string, string_1, p_int):
        """
        V.AddLinkVertex(string, string, int)
        C++: void AddLinkVertex(const char *column,
            const char *domain=nullptr, int hidden=0)
        
        Add a vertex to the link graph.  Specify the column name, the
        domain name for the column, and whether the column is hidden.
        """
        ...
    
    def ClearLinkEdges(self):
        """
        V.ClearLinkEdges()
        C++: void ClearLinkEdges()
        
        Clear the link graph edges.  The graph vertices will remain.
        """
        ...
    
    def ClearLinkVertices(self):
        """
        V.ClearLinkVertices()
        C++: void ClearLinkVertices()
        
        Clear the link graph vertices.  This also clears all edges.
        """
        ...
    
    def DirectedOff(self):
        """
        V.DirectedOff()
        C++: virtual void DirectedOff()
        
        Specify the directedness of the output graph.
        """
        ...
    
    def DirectedOn(self):
        """
        V.DirectedOn()
        C++: virtual void DirectedOn()
        
        Specify the directedness of the output graph.
        """
        ...
    
    def GetDirected(self):
        """
        V.GetDirected() -> bool
        C++: virtual bool GetDirected()
        
        Specify the directedness of the output graph.
        """
        ...
    
    def GetLinkGraph(self):
        """
        V.GetLinkGraph() -> vtkMutableDirectedGraph
        C++: virtual vtkMutableDirectedGraph *GetLinkGraph()
        
        The graph describing how to link the columns in the table.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Get the current modified time.
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
    
    def LinkColumnPath(self, vtkStringArray, vtkStringArray_1, vtkBitArray):
        """
        V.LinkColumnPath(vtkStringArray, vtkStringArray, vtkBitArray)
        C++: void LinkColumnPath(vtkStringArray *column,
            vtkStringArray *domain=nullptr, vtkBitArray *hidden=nullptr)
        
        Links the columns in a specific order. This creates a simple path
        as the link graph.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkTableToGraph
        C++: vtkTableToGraph *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTableToGraph
        C++: static vtkTableToGraph *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetDirected(self, bool):
        """
        V.SetDirected(bool)
        C++: virtual void SetDirected(bool _arg)
        
        Specify the directedness of the output graph.
        """
        ...
    
    def SetLinkGraph(self, vtkMutableDirectedGraph):
        """
        V.SetLinkGraph(vtkMutableDirectedGraph)
        C++: void SetLinkGraph(vtkMutableDirectedGraph *g)
        
        The graph describing how to link the columns in the table.
        """
        ...
    
    def SetVertexTableConnection(self, vtkAlgorithmOutput):
        """
        V.SetVertexTableConnection(vtkAlgorithmOutput)
        C++: void SetVertexTableConnection(vtkAlgorithmOutput *in)
        
        A convenience method for setting the vertex table input.  This is
        mainly for the benefit of the VTK client/server layer, vanilla
        VTK code should use e.g:
        
        * table_to_graph->SetInputConnection(1, vertex_table->output());
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

