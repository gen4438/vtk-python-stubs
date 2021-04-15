"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkXMLDataElement(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkXMLDataElement - Represents an XML element and those nested inside.
    
    Superclass: vtkObject
    
    vtkXMLDataElement is used by vtkXMLDataParser to represent an XML
    element.  It provides methods to access the element's attributes and
    nested elements in a convenient manner.  This allows easy traversal
    of an input XML file by vtkXMLReader and its subclasses.
    
    @sa
    vtkXMLDataParser
    """
    def AddCharacterData(self, string, p_int):
        """
        V.AddCharacterData(string, int)
        C++: void AddCharacterData(const char *c, size_t length)
        
        Set/Get the character data between XML start/end tags.
        """
        ...
    
    def AddNestedElement(self, vtkXMLDataElement):
        """
        V.AddNestedElement(vtkXMLDataElement)
        C++: void AddNestedElement(vtkXMLDataElement *element)
        
        Add nested element
        """
        ...
    
    def DeepCopy(self, vtkXMLDataElement):
        """
        V.DeepCopy(vtkXMLDataElement)
        C++: virtual void DeepCopy(vtkXMLDataElement *elem)
        
        Copy this element from another of the same type (elem),
        recursively. Old attributes and nested elements are removed, new
        ones are created given the contents of 'elem'. Warning: Parent is
        ignored.
        """
        ...
    
    def FindNestedElement(self, string):
        """
        V.FindNestedElement(string) -> vtkXMLDataElement
        C++: vtkXMLDataElement *FindNestedElement(const char *id)
        
        Find the first nested element with the given id, given name, or
        given name and id. WARNING: the search is only performed on the
        children, not the grand-children.
        """
        ...
    
    def FindNestedElementWithName(self, string):
        """
        V.FindNestedElementWithName(string) -> vtkXMLDataElement
        C++: vtkXMLDataElement *FindNestedElementWithName(
            const char *name)
        
        Find the first nested element with the given id, given name, or
        given name and id. WARNING: the search is only performed on the
        children, not the grand-children.
        """
        ...
    
    def FindNestedElementWithNameAndAttribute(self, string, string_1, string_2):
        """
        V.FindNestedElementWithNameAndAttribute(string, string, string)
            -> vtkXMLDataElement
        C++: vtkXMLDataElement *FindNestedElementWithNameAndAttribute(
            const char *name, const char *att_name, const char *att_value)
        
        Find the first nested element with the given id, given name, or
        given name and id. WARNING: the search is only performed on the
        children, not the grand-children.
        """
        ...
    
    def FindNestedElementWithNameAndId(self, string, string_1):
        """
        V.FindNestedElementWithNameAndId(string, string)
            -> vtkXMLDataElement
        C++: vtkXMLDataElement *FindNestedElementWithNameAndId(
            const char *name, const char *id)
        
        Find the first nested element with the given id, given name, or
        given name and id. WARNING: the search is only performed on the
        children, not the grand-children.
        """
        ...
    
    def GetAttribute(self, string):
        """
        V.GetAttribute(string) -> string
        C++: const char *GetAttribute(const char *name)
        
        Get the attribute with the given name.  If it doesn't exist,
        returns 0.
        """
        ...
    
    def GetAttributeEncoding(self):
        """
        V.GetAttributeEncoding() -> int
        C++: virtual int GetAttributeEncoding()
        
        Get/Set the internal character encoding of the attributes.
        Default type is VTK_ENCODING_UTF_8. Note that a vtkXMLDataParser
        has its own AttributesEncoding ivar. If this ivar is set to
        something other than VTK_ENCODING_NONE, it will be used to set
        the attribute encoding of each vtkXMLDataElement created by this
        vtkXMLDataParser.
        """
        ...
    
    def GetAttributeEncodingMaxValue(self):
        """
        V.GetAttributeEncodingMaxValue() -> int
        C++: virtual int GetAttributeEncodingMaxValue()
        
        Get/Set the internal character encoding of the attributes.
        Default type is VTK_ENCODING_UTF_8. Note that a vtkXMLDataParser
        has its own AttributesEncoding ivar. If this ivar is set to
        something other than VTK_ENCODING_NONE, it will be used to set
        the attribute encoding of each vtkXMLDataElement created by this
        vtkXMLDataParser.
        """
        ...
    
    def GetAttributeEncodingMinValue(self):
        """
        V.GetAttributeEncodingMinValue() -> int
        C++: virtual int GetAttributeEncodingMinValue()
        
        Get/Set the internal character encoding of the attributes.
        Default type is VTK_ENCODING_UTF_8. Note that a vtkXMLDataParser
        has its own AttributesEncoding ivar. If this ivar is set to
        something other than VTK_ENCODING_NONE, it will be used to set
        the attribute encoding of each vtkXMLDataElement created by this
        vtkXMLDataParser.
        """
        ...
    
    def GetAttributeName(self, p_int):
        """
        V.GetAttributeName(int) -> string
        C++: const char *GetAttributeName(int idx)
        
        Get the n-th attribute name. Returns 0 if there is no such
        attribute.
        """
        ...
    
    def GetAttributeValue(self, p_int):
        """
        V.GetAttributeValue(int) -> string
        C++: const char *GetAttributeValue(int idx)
        
        Get the n-th attribute value. Returns 0 if there is no such
        attribute.
        """
        ...
    
    def GetCharacterData(self):
        """
        V.GetCharacterData() -> string
        C++: virtual char *GetCharacterData()
        
        Set/Get the character data between XML start/end tags.
        """
        ...
    
    def GetCharacterDataWidth(self):
        """
        V.GetCharacterDataWidth() -> int
        C++: virtual int GetCharacterDataWidth()
        
        Get/Set the width (in number of fields) that character data (that
        between open and closing tags ie. ... ) is printed. If the width
        is less than one the tag's character data is printed all on one
        line. If it is greater than one the character data is streamed
        insterting line feeds every width number of fields. See PrintXML.
        """
        ...
    
    def GetId(self):
        """
        V.GetId() -> string
        C++: virtual char *GetId()
        
        Set/Get the value of the id attribute of the element, if any.
        """
        ...
    
    def GetName(self):
        """
        V.GetName() -> string
        C++: virtual char *GetName()
        
        Set/Get the name of the element.  This is its XML tag.
        """
        ...
    
    def GetNestedElement(self, p_int):
        """
        V.GetNestedElement(int) -> vtkXMLDataElement
        C++: vtkXMLDataElement *GetNestedElement(int index)
        
        Get the element nested in this one at the given index.
        """
        ...
    
    def GetNumberOfAttributes(self):
        """
        V.GetNumberOfAttributes() -> int
        C++: virtual int GetNumberOfAttributes()
        
        Get the number of attributes.
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
    
    def GetNumberOfNestedElements(self):
        """
        V.GetNumberOfNestedElements() -> int
        C++: int GetNumberOfNestedElements()
        
        Get the number of elements nested in this one.
        """
        ...
    
    def GetParent(self):
        """
        V.GetParent() -> vtkXMLDataElement
        C++: vtkXMLDataElement *GetParent()
        
        Set/Get the parent of this element.
        """
        ...
    
    def GetRoot(self):
        """
        V.GetRoot() -> vtkXMLDataElement
        C++: virtual vtkXMLDataElement *GetRoot()
        
        Get root of the XML tree this element is part of.
        """
        ...
    
    def GetScalarAttribute(self, string, p_int):
        """
        V.GetScalarAttribute(string, int) -> int
        C++: int GetScalarAttribute(const char *name, int &value)
        V.GetScalarAttribute(string, float) -> int
        C++: int GetScalarAttribute(const char *name, double &value)
        V.GetScalarAttribute(string, int) -> int
        C++: int GetScalarAttribute(const char *name, long &value)
        V.GetScalarAttribute(string, int) -> int
        C++: int GetScalarAttribute(const char *name, long long &value)
        
        Get the attribute with the given name and converted to a scalar
        value.  Returns whether value was extracted.
        """
        ...
    
    def GetVectorAttribute(self, string, p_int, *int):
        """
        V.GetVectorAttribute(string, int, [int, ...]) -> int
        C++: int GetVectorAttribute(const char *name, int length,
            int *value)
        V.GetVectorAttribute(string, int, [float, ...]) -> int
        C++: int GetVectorAttribute(const char *name, int length,
            double *value)
        V.GetVectorAttribute(string, int, [int, ...]) -> int
        C++: int GetVectorAttribute(const char *name, int length,
            long *value)
        V.GetVectorAttribute(string, int, [int, ...]) -> int
        C++: int GetVectorAttribute(const char *name, int length,
            long long *value)
        
        Get the attribute with the given name and converted to a scalar
        value.  Returns length of vector read.
        """
        ...
    
    def GetWordTypeAttribute(self, string, p_int):
        """
        V.GetWordTypeAttribute(string, int) -> int
        C++: int GetWordTypeAttribute(const char *name, int &value)
        
        Get the attribute with the given name and converted to a word
        type such as VTK_FLOAT or VTK_UNSIGNED_LONG.
        """
        ...
    
    def GetXMLByteIndex(self):
        """
        V.GetXMLByteIndex() -> int
        C++: virtual vtkTypeInt64 GetXMLByteIndex()
        
        Set/Get the offset from the beginning of the XML document to this
        element.
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
    
    def IsEqualTo(self, vtkXMLDataElement):
        """
        V.IsEqualTo(vtkXMLDataElement) -> int
        C++: virtual int IsEqualTo(vtkXMLDataElement *elem)
        
        Check if the instance has the same name, attributes, character
        data and nested elements contents than the given element (this
        method is applied recursively on the nested elements, and they
        must be stored in the same order). Warning: Id, Parent,
        XMLByteIndex are ignored.
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
    
    def LookupElement(self, string):
        """
        V.LookupElement(string) -> vtkXMLDataElement
        C++: vtkXMLDataElement *LookupElement(const char *id)
        
        Lookup the element with the given id, starting at this scope.
        """
        ...
    
    def LookupElementWithName(self, string):
        """
        V.LookupElementWithName(string) -> vtkXMLDataElement
        C++: vtkXMLDataElement *LookupElementWithName(const char *name)
        
        Find the first nested element with given name. WARNING: the
        search is performed on the whole XML tree.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkXMLDataElement
        C++: vtkXMLDataElement *NewInstance()
        """
        ...
    
    def PrintXML(self, string):
        """
        V.PrintXML(string)
        C++: void PrintXML(const char *fname)
        
        Prints element tree as XML.
        """
        ...
    
    def RemoveAllAttributes(self):
        """
        V.RemoveAllAttributes()
        C++: virtual void RemoveAllAttributes()
        
        Remove one or all attributes.
        """
        ...
    
    def RemoveAllNestedElements(self):
        """
        V.RemoveAllNestedElements()
        C++: virtual void RemoveAllNestedElements()
        
        Remove all nested elements.
        """
        ...
    
    def RemoveAttribute(self, string):
        """
        V.RemoveAttribute(string)
        C++: virtual void RemoveAttribute(const char *name)
        
        Remove one or all attributes.
        """
        ...
    
    def RemoveNestedElement(self, vtkXMLDataElement):
        """
        V.RemoveNestedElement(vtkXMLDataElement)
        C++: virtual void RemoveNestedElement(vtkXMLDataElement *)
        
        Remove nested element.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkXMLDataElement
        C++: static vtkXMLDataElement *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAttribute(self, string, string_1):
        """
        V.SetAttribute(string, string)
        C++: void SetAttribute(const char *name, const char *value)
        
        Set the attribute with the given name and value. If it doesn't
        exist, adds it.
        """
        ...
    
    def SetAttributeEncoding(self, p_int):
        """
        V.SetAttributeEncoding(int)
        C++: virtual void SetAttributeEncoding(int _arg)
        
        Get/Set the internal character encoding of the attributes.
        Default type is VTK_ENCODING_UTF_8. Note that a vtkXMLDataParser
        has its own AttributesEncoding ivar. If this ivar is set to
        something other than VTK_ENCODING_NONE, it will be used to set
        the attribute encoding of each vtkXMLDataElement created by this
        vtkXMLDataParser.
        """
        ...
    
    def SetCharacterData(self, string, p_int):
        """
        V.SetCharacterData(string, int)
        C++: void SetCharacterData(const char *c, int length)
        
        Set/Get the character data between XML start/end tags.
        """
        ...
    
    def SetCharacterDataWidth(self, p_int):
        """
        V.SetCharacterDataWidth(int)
        C++: virtual void SetCharacterDataWidth(int _arg)
        
        Get/Set the width (in number of fields) that character data (that
        between open and closing tags ie. ... ) is printed. If the width
        is less than one the tag's character data is printed all on one
        line. If it is greater than one the character data is streamed
        insterting line feeds every width number of fields. See PrintXML.
        """
        ...
    
    def SetDoubleAttribute(self, string, p_float):
        """
        V.SetDoubleAttribute(string, float)
        C++: void SetDoubleAttribute(const char *name, double value)
        
        Set the attribute with the given name. We can not use the same
        GetScalarAttribute() construct since the compiler will not be
        able to resolve between SetAttribute(..., int) and
        SetAttribute(..., unsigned long).
        """
        ...
    
    def SetFloatAttribute(self, string, p_float):
        """
        V.SetFloatAttribute(string, float)
        C++: void SetFloatAttribute(const char *name, float value)
        
        Set the attribute with the given name. We can not use the same
        GetScalarAttribute() construct since the compiler will not be
        able to resolve between SetAttribute(..., int) and
        SetAttribute(..., unsigned long).
        """
        ...
    
    def SetId(self, string):
        """
        V.SetId(string)
        C++: virtual void SetId(const char *_arg)
        
        Set/Get the value of the id attribute of the element, if any.
        """
        ...
    
    def SetIntAttribute(self, string, p_int):
        """
        V.SetIntAttribute(string, int)
        C++: void SetIntAttribute(const char *name, int value)
        
        Set the attribute with the given name. We can not use the same
        GetScalarAttribute() construct since the compiler will not be
        able to resolve between SetAttribute(..., int) and
        SetAttribute(..., unsigned long).
        """
        ...
    
    def SetName(self, string):
        """
        V.SetName(string)
        C++: virtual void SetName(const char *_arg)
        
        Set/Get the name of the element.  This is its XML tag.
        """
        ...
    
    def SetParent(self, vtkXMLDataElement):
        """
        V.SetParent(vtkXMLDataElement)
        C++: void SetParent(vtkXMLDataElement *parent)
        
        Set/Get the parent of this element.
        """
        ...
    
    def SetUnsignedLongAttribute(self, string, p_int):
        """
        V.SetUnsignedLongAttribute(string, int)
        C++: void SetUnsignedLongAttribute(const char *name,
            unsigned long value)
        
        Set the attribute with the given name. We can not use the same
        GetScalarAttribute() construct since the compiler will not be
        able to resolve between SetAttribute(..., int) and
        SetAttribute(..., unsigned long).
        """
        ...
    
    def SetVectorAttribute(self, string, p_int, int_tuple):
        """
        V.SetVectorAttribute(string, int, (int, ...))
        C++: void SetVectorAttribute(const char *name, int length,
            const int *value)
        V.SetVectorAttribute(string, int, (float, ...))
        C++: void SetVectorAttribute(const char *name, int length,
            const double *value)
        V.SetVectorAttribute(string, int, (int, ...))
        C++: void SetVectorAttribute(const char *name, int length,
            const unsigned long *value)
        V.SetVectorAttribute(string, int, (int, ...))
        C++: void SetVectorAttribute(const char *name, int length,
            long long const *value)
        
        Set the attribute with the given name.
        """
        ...
    
    def SetXMLByteIndex(self, p_int):
        """
        V.SetXMLByteIndex(int)
        C++: virtual void SetXMLByteIndex(vtkTypeInt64 _arg)
        
        Set/Get the offset from the beginning of the XML document to this
        element.
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


