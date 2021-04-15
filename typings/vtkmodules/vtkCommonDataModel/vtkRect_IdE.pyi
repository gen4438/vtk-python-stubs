"""
This type stub file was generated by pyright.
"""

from .vtkVector_IdLi4EE import vtkVector_IdLi4EE

class vtkRect_IdE(vtkVector_IdLi4EE):
    """
    vtkRect- templated base type for storage of 2D rectangles.
    
    Superclass: vtkVector[float64,4]
    
    This class is a templated data type for storing and manipulating
    rectangles. The memory layout is a contiguous array of the specified
    type, such that a float[4] can be cast to a vtkRectf and manipulated.
    Also a float[12] could be cast and used as a vtkRectf[3].
    
    vtkRect()
    vtkRect(const double &x, const double &y, const double &width,
        const double &height)
    explicit vtkRect(const double *init)
    vtkRect(const &vtkRect<double>)
    """
    def AddPoint(self, ):
        """
        V.AddPoint((float, float))
        C++: void AddPoint(const double point[2])
        V.AddPoint(float, float)
        C++: void AddPoint(double x, double y)
        
        Expand this rect to contain the point passed in.
        """
        ...
    
    def AddRect(self, vtkRect_IdE):
        """
        V.AddRect(vtkRect_IdE)
        C++: void AddRect(const vtkRect<double> &rect)
        
        Expand this rect to contain the rect passed in.
        """
        ...
    
    def GetBottom(self):
        """
        V.GetBottom() -> float
        C++: const double &GetBottom()
        
        Get the bottom boundary of the rectangle along the Y direction.
        """
        ...
    
    def GetBottomLeft(self):
        """
        V.GetBottomLeft() -> vtkVector2_IdE
        C++: vtkVector2<double> GetBottomLeft()
        
        Get the bottom left corner of the rect as a vtkVector.
        """
        ...
    
    def GetBottomRight(self):
        """
        V.GetBottomRight() -> vtkVector_IdLi2EE
        C++: vtkVector<double, 2> GetBottomRight()
        
        Get the bottom right corner of the rect as a vtkVector.
        """
        ...
    
    def GetHeight(self):
        """
        V.GetHeight() -> float
        C++: const double &GetHeight()
        
        Get the height of the rectangle, i.e. element 3.
        """
        ...
    
    def GetLeft(self):
        """
        V.GetLeft() -> float
        C++: const double &GetLeft()
        
        Get the left boundary of the rectangle along the X direction.
        """
        ...
    
    def GetRight(self):
        """
        V.GetRight() -> float
        C++: double GetRight()
        
        Get the right boundary of the rectangle along the X direction.
        """
        ...
    
    def GetTop(self):
        """
        V.GetTop() -> float
        C++: double GetTop()
        
        Get the top boundary of the rectangle along the Y direction.
        """
        ...
    
    def GetTopLeft(self):
        """
        V.GetTopLeft() -> vtkVector_IdLi2EE
        C++: vtkVector<double, 2> GetTopLeft()
        
        Get the top left corner of the rect as a vtkVector.
        """
        ...
    
    def GetTopRight(self):
        """
        V.GetTopRight() -> vtkVector_IdLi2EE
        C++: vtkVector<double, 2> GetTopRight()
        
        Get the bottom left corner of the rect as a vtkVector.
        """
        ...
    
    def GetWidth(self):
        """
        V.GetWidth() -> float
        C++: const double &GetWidth()
        
        Get the width of the rectangle, i.e. element 2.
        """
        ...
    
    def GetX(self):
        """
        V.GetX() -> float
        C++: const double &GetX()
        
        Get the x component of the rectangle bottom corner, i.e. element
        0.
        """
        ...
    
    def GetY(self):
        """
        V.GetY() -> float
        C++: const double &GetY()
        
        Get the y component of the rectangle bottom corner, i.e. element
        1.
        """
        ...
    
    def Intersect(self, vtkRect_IdE):
        """
        V.Intersect(vtkRect_IdE) -> bool
        C++: bool Intersect(const vtkRect<double> &other)
        
        Intersect with `other` rectangle. If
        `this->IntersectsWith(other)` is true, this method will update
        this rect to the intersection of `this` and `other` and return
        true. If `this->IntersectsWith(other)` returns false, then this
        method will return false leaving this rect unchanged.
        
        Returns true if the intersection was performed otherwise false.
        """
        ...
    
    def IntersectsWith(self, vtkRect_IdE):
        """
        V.IntersectsWith(vtkRect_IdE) -> bool
        C++: bool IntersectsWith(const vtkRect<double> &rect)
        
        Returns true if the rect argument overlaps this rect. If the
        upper bound of one rect is equal to the lower bound of the other
        rect, then this will return false (in that case, the rects would
        be considered to be adjacent but not overlapping).
        """
        ...
    
    def MoveTo(self, p_float, p_float_1):
        """
        V.MoveTo(float, float)
        C++: void MoveTo(double x, double y)
        
        Move the rectangle, moving the bottom-left corner to the given
        position. The rectangles size remains unchanged.
        """
        ...
    
    def Set(self, p_float, p_float_1, p_float_2, p_float_3):
        """
        V.Set(float, float, float, float)
        C++: void Set(const double &x, const double &y,
            const double &width, const double &height)
        
        Set the x, y components of the rectangle, and the width/height.
        """
        ...
    
    def SetHeight(self, p_float):
        """
        V.SetHeight(float)
        C++: void SetHeight(const double &height)
        
        Set the height of the rectangle, i.e. element 3.
        """
        ...
    
    def SetWidth(self, p_float):
        """
        V.SetWidth(float)
        C++: void SetWidth(const double &width)
        
        Set the width of the rectanle, i.e. element 2.
        """
        ...
    
    def SetX(self, p_float):
        """
        V.SetX(float)
        C++: void SetX(const double &x)
        
        Set the x component of the rectangle bottom corner, i.e. element
        0.
        """
        ...
    
    def SetY(self, p_float):
        """
        V.SetY(float)
        C++: void SetY(const double &y)
        
        Set the y component of the rectangle bottom corner, i.e. element
        1.
        """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __hash__(self, *args, **kwargs) -> int:
        """ Return hash(self). """
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
    

