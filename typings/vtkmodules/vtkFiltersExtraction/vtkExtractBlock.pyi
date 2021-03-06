"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkExtractBlock(__vtkmodules_vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    """
    vtkExtractBlock - extracts blocks from a multiblock dataset.
    
    Superclass: vtkMultiBlockDataSetAlgorithm
    
    vtkExtractBlock is a filter that extracts blocks from a multiblock
    dataset.  Each node in the multi-block tree is identified by an \c
    index. The index can be obtained by performing a preorder traversal
    of the tree (including empty nodes). eg. A(B (D, E), C(F, G)). 
    Inorder traversal yields: A, B, D, E, C, F, G Index of A is 0, while
    index of C is 4.
    
    Note that if you specify node 0, then the input is simply shallow
    copied to the output. This is true even if other nodes are specified
    along with node 0.
    """
    def AddIndex(self, p_int):
        """
        V.AddIndex(int)
        C++: void AddIndex(unsigned int index)
        
        Select the block indices to extract.  Each node in the
        multi-block tree is identified by an index. The index can be
        obtained by performing a preorder traversal of the tree
        (including empty nodes). eg. A(B (D, E), C(F, G)).  Inorder
        traversal yields: A, B, D, E, C, F, G Index of A is 0, while
        index of C is 4. (Note: specifying node 0 means the input is
        copied to the output.)
        """
        ...
    
    def GetMaintainStructure(self):
        """
        V.GetMaintainStructure() -> int
        C++: virtual vtkTypeBool GetMaintainStructure()
        
        This is used only when PruneOutput is ON. By default, when
        pruning the output i.e. remove empty blocks, if node has only 1
        non-null child block, then that node is removed. To preserve
        these parent nodes, set this flag to true. Off by default.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def GetPruneOutput(self):
        """
        V.GetPruneOutput() -> int
        C++: virtual vtkTypeBool GetPruneOutput()
        
        When set, the output multiblock dataset will be pruned to remove
        empty nodes. On by default.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def MaintainStructureOff(self):
        """
        V.MaintainStructureOff()
        C++: virtual void MaintainStructureOff()
        
        This is used only when PruneOutput is ON. By default, when
        pruning the output i.e. remove empty blocks, if node has only 1
        non-null child block, then that node is removed. To preserve
        these parent nodes, set this flag to true. Off by default.
        """
        ...
    
    def MaintainStructureOn(self):
        """
        V.MaintainStructureOn()
        C++: virtual void MaintainStructureOn()
        
        This is used only when PruneOutput is ON. By default, when
        pruning the output i.e. remove empty blocks, if node has only 1
        non-null child block, then that node is removed. To preserve
        these parent nodes, set this flag to true. Off by default.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkExtractBlock
        C++: vtkExtractBlock *NewInstance()
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def PruneOutputOff(self):
        """
        V.PruneOutputOff()
        C++: virtual void PruneOutputOff()
        
        When set, the output multiblock dataset will be pruned to remove
        empty nodes. On by default.
        """
        ...
    
    def PruneOutputOn(self):
        """
        V.PruneOutputOn()
        C++: virtual void PruneOutputOn()
        
        When set, the output multiblock dataset will be pruned to remove
        empty nodes. On by default.
        """
        ...
    
    def RemoveAllIndices(self):
        """
        V.RemoveAllIndices()
        C++: void RemoveAllIndices()
        
        Select the block indices to extract.  Each node in the
        multi-block tree is identified by an index. The index can be
        obtained by performing a preorder traversal of the tree
        (including empty nodes). eg. A(B (D, E), C(F, G)).  Inorder
        traversal yields: A, B, D, E, C, F, G Index of A is 0, while
        index of C is 4. (Note: specifying node 0 means the input is
        copied to the output.)
        """
        ...
    
    def RemoveIndex(self, p_int):
        """
        V.RemoveIndex(int)
        C++: void RemoveIndex(unsigned int index)
        
        Select the block indices to extract.  Each node in the
        multi-block tree is identified by an index. The index can be
        obtained by performing a preorder traversal of the tree
        (including empty nodes). eg. A(B (D, E), C(F, G)).  Inorder
        traversal yields: A, B, D, E, C, F, G Index of A is 0, while
        index of C is 4. (Note: specifying node 0 means the input is
        copied to the output.)
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtractBlock
        C++: static vtkExtractBlock *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def SetMaintainStructure(self, p_int):
        """
        V.SetMaintainStructure(int)
        C++: virtual void SetMaintainStructure(vtkTypeBool _arg)
        
        This is used only when PruneOutput is ON. By default, when
        pruning the output i.e. remove empty blocks, if node has only 1
        non-null child block, then that node is removed. To preserve
        these parent nodes, set this flag to true. Off by default.
        """
        ...
    
    def SetPruneOutput(self, p_int):
        """
        V.SetPruneOutput(int)
        C++: virtual void SetPruneOutput(vtkTypeBool _arg)
        
        When set, the output multiblock dataset will be pruned to remove
        empty nodes. On by default.
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


