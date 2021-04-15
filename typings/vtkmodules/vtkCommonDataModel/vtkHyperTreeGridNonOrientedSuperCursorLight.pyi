"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkHyperTreeGridNonOrientedSuperCursorLight(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkHyperTreeGridNonOrientedSuperCursorLight - Objects for traversal a
    HyperTreeGrid.
    
    Superclass: vtkObject
    
    JB A REVOIR Objects that can perform depth traversal of a hyper tree
    grid, take into account more parameters (related to the grid
    structure) than the compact hyper tree cursor implemented in
    vtkHyperTree can. This is an abstract class. Cursors are created by
    the HyperTreeGrid implementation.
    
    @sa
    vtkHyperTreeCursor vtkHyperTree vtkHyperTreeGrid
    
    @par Thanks: This class was written by Guenole Harel and
    Jacques-Bernard Lekien, 2014. This class was re-written by Philippe
    Pebay, 2016. This class was re-written and optimized by
    Jacques-Bernard Lekien, Guenole Harel and Jerome Dubois, 2018. This
    work was supported by Commissariat a l'Energie Atomique CEA, DAM,
    DIF, F-91297 Arpajon, France.
    """
    def Clone(self):
        """
        V.Clone() -> vtkHyperTreeGridNonOrientedSuperCursorLight
        C++: virtual vtkHyperTreeGridNonOrientedSuperCursorLight *Clone()
        
        Create a copy of `this'.
        \post results_exists:result!=0
        """
        ...
    
    def GetBounds(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetBounds([float, float, float, float, float, float])
        C++: void GetBounds(double bounds[6])
        
        JB Coordonnees de la boite englobante En light, information non
        disponible sur les voisins
        """
        ...
    
    def GetDimension(self):
        """
        V.GetDimension() -> int
        C++: unsigned char GetDimension()
        
        Return the dimension of the tree.
        \post positive_result: result>0
        """
        ...
    
    def GetGlobalNodeIndex(self):
        """
        V.GetGlobalNodeIndex() -> int
        C++: vtkIdType GetGlobalNodeIndex()
        V.GetGlobalNodeIndex(int) -> int
        C++: vtkIdType GetGlobalNodeIndex(unsigned int icursor)
        
        Return the global index (relative to the grid) of the current
        vertex in the tree.
        """
        ...
    
    def GetGrid(self):
        """
        V.GetGrid() -> vtkHyperTreeGrid
        C++: vtkHyperTreeGrid *GetGrid()
        
        Set the hyper tree grid to which the cursor is pointing.
        """
        ...
    
    def GetInformation(self, p_int, p_int_1, bool, p_int_2):
        """
        V.GetInformation(int, int, bool, int) -> vtkHyperTree
        C++: vtkHyperTree *GetInformation(unsigned int icursor,
            unsigned int &level, bool &leaf, vtkIdType &id)
        
        JB
        """
        ...
    
    def GetLevel(self):
        """
        V.GetLevel() -> int
        C++: unsigned int GetLevel()
        V.GetLevel(int) -> int
        C++: unsigned int GetLevel(unsigned int icursor)
        
        Get the level of the tree vertex pointed by the cursor.
        """
        ...
    
    def GetNumberOfChildren(self):
        """
        V.GetNumberOfChildren() -> int
        C++: unsigned char GetNumberOfChildren()
        
        Return the number of children for each node (non-vertex leaf) of
        the tree.
        \post positive_number: result>0
        """
        ...
    
    def GetNumberOfCursors(self):
        """
        V.GetNumberOfCursors() -> int
        C++: unsigned int GetNumberOfCursors()
        
        JB
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
        V.GetOrigin() -> (float, ...)
        C++: double *GetOrigin()
        
        JB
        """
        ...
    
    def GetPoint(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetPoint([float, float, float])
        C++: void GetPoint(double point[3])
        
        JB Coordonnees du centre de la maille En light, information non
        disponible sur les voisins
        """
        ...
    
    def GetSize(self):
        """
        V.GetSize() -> (float, ...)
        C++: double *GetSize()
        """
        ...
    
    def GetTree(self):
        """
        V.GetTree() -> vtkHyperTree
        C++: vtkHyperTree *GetTree()
        V.GetTree(int) -> vtkHyperTree
        C++: vtkHyperTree *GetTree(unsigned int icursor)
        
        Set the hyper tree to which the cursor is pointing.
        """
        ...
    
    def GetVertexId(self):
        """
        V.GetVertexId() -> int
        C++: vtkIdType GetVertexId()
        V.GetVertexId(int) -> int
        C++: vtkIdType GetVertexId(unsigned int icursor)
        
        Return the index of the current vertex in the tree.
        """
        ...
    
    def HasTree(self):
        """
        V.HasTree() -> bool
        C++: bool HasTree()
        V.HasTree(int) -> bool
        C++: bool HasTree(unsigned int icursor)
        
        Return if a Tree pointing exist
        """
        ...
    
    def Initialize(self, vtkHyperTreeGrid, p_int, bool):
        """
        V.Initialize(vtkHyperTreeGrid, int, bool)
        C++: virtual void Initialize(vtkHyperTreeGrid *grid,
            vtkIdType treeIndex, bool create=false)
        
        Initialize cursor at root of given tree index in grid. JB
        Attention : le create ne s'applique que sur le HT central.
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
    
    def IsLeaf(self):
        """
        V.IsLeaf() -> bool
        C++: bool IsLeaf()
        V.IsLeaf(int) -> bool
        C++: bool IsLeaf(unsigned int icursor)
        
        Is the cursor pointing to a leaf?
        """
        ...
    
    def IsMasked(self):
        """
        V.IsMasked() -> bool
        C++: bool IsMasked()
        V.IsMasked(int) -> bool
        C++: bool IsMasked(unsigned int icursor)
        
        Determine whether blanking mask is empty or not
        """
        ...
    
    def IsRoot(self):
        """
        V.IsRoot() -> bool
        C++: bool IsRoot()
        
        Is the cursor at tree root?
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
        V.NewInstance() -> vtkHyperTreeGridNonOrientedSuperCursorLight
        C++: vtkHyperTreeGridNonOrientedSuperCursorLight *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkHyperTreeGridNonOrientedSuperCursorLight
        C++: static vtkHyperTreeGridNonOrientedSuperCursorLight *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetGlobalIndexFromLocal(self, p_int):
        """
        V.SetGlobalIndexFromLocal(int)
        C++: void SetGlobalIndexFromLocal(vtkIdType index)
        
        JB
        """
        ...
    
    def SetGlobalIndexStart(self, p_int):
        """
        V.SetGlobalIndexStart(int)
        C++: void SetGlobalIndexStart(vtkIdType index)
        
        JB
        """
        ...
    
    def SetMask(self, bool):
        """
        V.SetMask(bool)
        C++: void SetMask(bool state)
        V.SetMask(int, bool)
        C++: void SetMask(unsigned int icursor, bool state)
        
        Set the blanking mask is empty or not
        \pre not_tree: tree
        """
        ...
    
    def SubdivideLeaf(self):
        """
        V.SubdivideLeaf()
        C++: void SubdivideLeaf()
        
        JB Fait chier normalement on devrait passer par GetEntry
        """
        ...
    
    def ToChild(self, p_int):
        """
        V.ToChild(int)
        C++: void ToChild(unsigned char)
        
        Move the cursor to child `child' of the current vertex.
        \pre Non_leaf: !IsLeaf()
        \pre valid_child: ichild>=0 && ichild<this->GetNumberOfChildren()
        """
        ...
    
    def ToParent(self):
        """
        V.ToParent()
        C++: void ToParent()
        
        Move the cursor to the parent of the current vertex. Authorized
        if HasHistory return true.
        \pre Non_root: !IsRoot()
        """
        ...
    
    def ToRoot(self):
        """
        V.ToRoot()
        C++: void ToRoot()
        
        Move the cursor to the root vertex.
        \pre can be root
        \post is_root: IsRoot()
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


