"""
This type stub file was generated by pyright.
"""

from .vtkInteractorObserver import vtkInteractorObserver

class vtkInteractorStyle(vtkInteractorObserver):
    """
    vtkInteractorStyle - provide event-driven interface to the rendering
    window (defines trackball mode)
    
    Superclass: vtkInteractorObserver
    
    vtkInteractorStyle is a base class implementing the majority of
    motion control routines and defines an event driven interface to
    support vtkRenderWindowInteractor. vtkRenderWindowInteractor
    implements platform dependent key/mouse routing and timer control,
    which forwards events in a neutral form to vtkInteractorStyle.
    
    vtkInteractorStyle implements the "joystick" style of interaction.
    That is, holding down the mouse keys generates a stream of events
    that cause continuous actions (e.g., rotate, translate, pan, zoom).
    (The class vtkInteractorStyleTrackball implements a grab and move
    style.) The event bindings for this class include the following:
    - Keypress j / Keypress t: toggle between joystick (position
      sensitive) and trackball (motion sensitive) styles. In joystick
      style, motion occurs continuously as long as a mouse button is
      pressed. In trackball style, motion occurs when the mouse button is
    pressed and the mouse pointer moves.
    - Keypress c / Keypress a: toggle between camera and actor modes. In
      camera mode, mouse events affect the camera position and focal
      point. In actor mode, mouse events affect the actor that is under
      the mouse pointer.
    - Button 1: rotate the camera around its focal point (if camera mode)
    or rotate the actor around its origin (if actor mode). The rotation
      is in the direction defined from the center of the renderer's
      viewport towards the mouse position. In joystick mode, the
      magnitude of the rotation is determined by the distance the mouse
      is from the center of the render window.
    - Button 2: pan the camera (if camera mode) or translate the actor
      (if actor mode). In joystick mode, the direction of pan or
      translation is from the center of the viewport towards the mouse
      position. In trackball mode, the direction of motion is the
      direction the mouse moves. (Note: with 2-button mice, pan is
      defined as <Shift>-Button 1.)
    - Button 3: zoom the camera (if camera mode) or scale the actor (if
      actor mode). Zoom in/increase scale if the mouse position is in the
    top half of the viewport; zoom out/decrease scale if the mouse
      position is in the bottom half. In joystick mode, the amount of
      zoom is controlled by the distance of the mouse pointer from the
      horizontal centerline of the window.
    - Keypress 3: toggle the render window into and out of stereo mode.
      By default, red-blue stereo pairs are created. Some systems support
    Crystal Eyes LCD stereo glasses; you have to invoke
      SetStereoTypeToCrystalEyes() on the rendering window.
    - Keypress e: exit the application.
    - Keypress f: fly to the picked point
    - Keypress p: perform a pick operation. The render window interactor
      has an internal instance of vtkCellPicker that it uses to pick.
    - Keypress r: reset the camera view along the current view direction.
    Centers the actors and moves the camera so that all actors are
      visible.
    - Keypress s: modify the representation of all actors so that they
      are surfaces.
    - Keypress u: invoke the user-defined function. Typically, this
      keypress will bring up an interactor that you can type commands in.
      Typing u calls UserCallBack() on the vtkRenderWindowInteractor,
      which invokes a vtkCommand::UserEvent. In other words, to define a
      user-defined callback, just add an observer to the
      vtkCommand::UserEvent on the vtkRenderWindowInteractor object.
    - Keypress w: modify the representation of all actors so that they
      are wireframe.
    
    vtkInteractorStyle can be subclassed to provide new interaction
    styles and a facility to override any of the default mouse/key
    operations which currently handle trackball or joystick styles is
    provided. Note that this class will fire a variety of events that can
    be watched using an observer, such as LeftButtonPressEvent,
    LeftButtonReleaseEvent, MiddleButtonPressEvent,
    MiddleButtonReleaseEvent, RightButtonPressEvent,
    RightButtonReleaseEvent, EnterEvent, LeaveEvent, KeyPressEvent,
    KeyReleaseEvent, CharEvent, ExposeEvent, ConfigureEvent, TimerEvent,
    MouseMoveEvent,
    
    @sa
    vtkInteractorStyleTrackball
    """
    def AutoAdjustCameraClippingRangeOff(self):
        """
        V.AutoAdjustCameraClippingRangeOff()
        C++: virtual void AutoAdjustCameraClippingRangeOff()
        
        If AutoAdjustCameraClippingRange is on, then before each render
        the camera clipping range will be adjusted to "fit" the whole
        scene. Clipping will still occur if objects in the scene are
        behind the camera or come very close. If
        AutoAdjustCameraClippingRange is off, no adjustment will be made
        per render, but the camera clipping range will still be reset
        when the camera is reset.
        """
        ...
    
    def AutoAdjustCameraClippingRangeOn(self):
        """
        V.AutoAdjustCameraClippingRangeOn()
        C++: virtual void AutoAdjustCameraClippingRangeOn()
        
        If AutoAdjustCameraClippingRange is on, then before each render
        the camera clipping range will be adjusted to "fit" the whole
        scene. Clipping will still occur if objects in the scene are
        behind the camera or come very close. If
        AutoAdjustCameraClippingRange is off, no adjustment will be made
        per render, but the camera clipping range will still be reset
        when the camera is reset.
        """
        ...
    
    def DelegateTDxEvent(self, p_int, void):
        """
        V.DelegateTDxEvent(int, void)
        C++: void DelegateTDxEvent(unsigned long event, void *calldata)
        
        Called by the callback to process 3DConnexion device events.
        """
        ...
    
    def Dolly(self):
        """
        V.Dolly()
        C++: virtual void Dolly()
        """
        ...
    
    def EndDolly(self):
        """
        V.EndDolly()
        C++: virtual void EndDolly()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def EndEnvRotate(self):
        """
        V.EndEnvRotate()
        C++: virtual void EndEnvRotate()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def EndGesture(self):
        """
        V.EndGesture()
        C++: virtual void EndGesture()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def EndPan(self):
        """
        V.EndPan()
        C++: virtual void EndPan()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def EndRotate(self):
        """
        V.EndRotate()
        C++: virtual void EndRotate()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def EndSpin(self):
        """
        V.EndSpin()
        C++: virtual void EndSpin()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def EndTimer(self):
        """
        V.EndTimer()
        C++: virtual void EndTimer()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def EndTwoPointer(self):
        """
        V.EndTwoPointer()
        C++: virtual void EndTwoPointer()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def EndUniformScale(self):
        """
        V.EndUniformScale()
        C++: virtual void EndUniformScale()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def EndZoom(self):
        """
        V.EndZoom()
        C++: virtual void EndZoom()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def EnvironmentRotate(self):
        """
        V.EnvironmentRotate()
        C++: virtual void EnvironmentRotate()
        """
        ...
    
    def FindPokedRenderer(self, p_int, p_int_1):
        """
        V.FindPokedRenderer(int, int)
        C++: void FindPokedRenderer(int, int)
        
        When an event occurs, we must determine which Renderer the event
        occurred within, since one RenderWindow may contain multiple
        renderers.
        """
        ...
    
    def GetAutoAdjustCameraClippingRange(self):
        """
        V.GetAutoAdjustCameraClippingRange() -> int
        C++: virtual vtkTypeBool GetAutoAdjustCameraClippingRange()
        
        If AutoAdjustCameraClippingRange is on, then before each render
        the camera clipping range will be adjusted to "fit" the whole
        scene. Clipping will still occur if objects in the scene are
        behind the camera or come very close. If
        AutoAdjustCameraClippingRange is off, no adjustment will be made
        per render, but the camera clipping range will still be reset
        when the camera is reset.
        """
        ...
    
    def GetAutoAdjustCameraClippingRangeMaxValue(self):
        """
        V.GetAutoAdjustCameraClippingRangeMaxValue() -> int
        C++: virtual vtkTypeBool GetAutoAdjustCameraClippingRangeMaxValue(
            )
        
        If AutoAdjustCameraClippingRange is on, then before each render
        the camera clipping range will be adjusted to "fit" the whole
        scene. Clipping will still occur if objects in the scene are
        behind the camera or come very close. If
        AutoAdjustCameraClippingRange is off, no adjustment will be made
        per render, but the camera clipping range will still be reset
        when the camera is reset.
        """
        ...
    
    def GetAutoAdjustCameraClippingRangeMinValue(self):
        """
        V.GetAutoAdjustCameraClippingRangeMinValue() -> int
        C++: virtual vtkTypeBool GetAutoAdjustCameraClippingRangeMinValue(
            )
        
        If AutoAdjustCameraClippingRange is on, then before each render
        the camera clipping range will be adjusted to "fit" the whole
        scene. Clipping will still occur if objects in the scene are
        behind the camera or come very close. If
        AutoAdjustCameraClippingRange is off, no adjustment will be made
        per render, but the camera clipping range will still be reset
        when the camera is reset.
        """
        ...
    
    def GetHandleObservers(self):
        """
        V.GetHandleObservers() -> int
        C++: virtual vtkTypeBool GetHandleObservers()
        
        Does ProcessEvents handle observers on this class or not
        """
        ...
    
    def GetMouseWheelMotionFactor(self):
        """
        V.GetMouseWheelMotionFactor() -> float
        C++: virtual double GetMouseWheelMotionFactor()
        
        Set/Get the mouse wheel motion factor. Default to 1.0. Set it to
        a different value to emphasize or de-emphasize the action
        triggered by mouse wheel motion.
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
    
    def GetPickColor(self):
        """
        V.GetPickColor() -> (float, float, float)
        C++: virtual double *GetPickColor()
        
        Set/Get the pick color (used by default to color vtkActor2D's).
        The color is expressed as red/green/blue values between
        (0.0,1.0).
        """
        ...
    
    def GetState(self):
        """
        V.GetState() -> int
        C++: virtual int GetState()
        
        Some useful information for interaction
        """
        ...
    
    def GetTDxStyle(self):
        """
        V.GetTDxStyle() -> vtkTDxInteractorStyle
        C++: virtual vtkTDxInteractorStyle *GetTDxStyle()
        
        3Dconnexion device interactor style. Initial value is a pointer
        to an object of class vtkTdxInteractorStyleCamera.
        """
        ...
    
    def GetTimerDuration(self):
        """
        V.GetTimerDuration() -> int
        C++: virtual unsigned long GetTimerDuration()
        
        If using timers, specify the default timer interval (in
        milliseconds). Care must be taken when adjusting the timer
        interval from the default value of 10 milliseconds--it may
        adversely affect the interactors.
        """
        ...
    
    def GetTimerDurationMaxValue(self):
        """
        V.GetTimerDurationMaxValue() -> int
        C++: virtual unsigned long GetTimerDurationMaxValue()
        
        If using timers, specify the default timer interval (in
        milliseconds). Care must be taken when adjusting the timer
        interval from the default value of 10 milliseconds--it may
        adversely affect the interactors.
        """
        ...
    
    def GetTimerDurationMinValue(self):
        """
        V.GetTimerDurationMinValue() -> int
        C++: virtual unsigned long GetTimerDurationMinValue()
        
        If using timers, specify the default timer interval (in
        milliseconds). Care must be taken when adjusting the timer
        interval from the default value of 10 milliseconds--it may
        adversely affect the interactors.
        """
        ...
    
    def GetUseTimers(self):
        """
        V.GetUseTimers() -> int
        C++: virtual vtkTypeBool GetUseTimers()
        
        Set/Get timer hint
        """
        ...
    
    def HandleObserversOff(self):
        """
        V.HandleObserversOff()
        C++: virtual void HandleObserversOff()
        
        Does ProcessEvents handle observers on this class or not
        """
        ...
    
    def HandleObserversOn(self):
        """
        V.HandleObserversOn()
        C++: virtual void HandleObserversOn()
        
        Does ProcessEvents handle observers on this class or not
        """
        ...
    
    def HighlightActor2D(self, vtkActor2D):
        """
        V.HighlightActor2D(vtkActor2D)
        C++: virtual void HighlightActor2D(vtkActor2D *actor2D)
        
        When picking successfully selects an actor, this method
        highlights the picked prop appropriately. Currently this is done
        by placing a bounding box around a picked vtkProp3D, and using
        the PickColor to highlight a vtkProp2D.
        """
        ...
    
    def HighlightProp(self, vtkProp):
        """
        V.HighlightProp(vtkProp)
        C++: virtual void HighlightProp(vtkProp *prop)
        
        When picking successfully selects an actor, this method
        highlights the picked prop appropriately. Currently this is done
        by placing a bounding box around a picked vtkProp3D, and using
        the PickColor to highlight a vtkProp2D.
        """
        ...
    
    def HighlightProp3D(self, vtkProp3D):
        """
        V.HighlightProp3D(vtkProp3D)
        C++: virtual void HighlightProp3D(vtkProp3D *prop3D)
        
        When picking successfully selects an actor, this method
        highlights the picked prop appropriately. Currently this is done
        by placing a bounding box around a picked vtkProp3D, and using
        the PickColor to highlight a vtkProp2D.
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
        V.NewInstance() -> vtkInteractorStyle
        C++: vtkInteractorStyle *NewInstance()
        """
        ...
    
    def OnButton3D(self, vtkEventData):
        """
        V.OnButton3D(vtkEventData)
        C++: virtual void OnButton3D(vtkEventData *)
        """
        ...
    
    def OnChar(self):
        """
        V.OnChar()
        C++: void OnChar() override;
        
        OnChar is triggered when an ASCII key is pressed. Some basic key
        presses are handled here ('q' for Quit, 'p' for Pick, etc)
        """
        ...
    
    def OnConfigure(self):
        """
        V.OnConfigure()
        C++: virtual void OnConfigure()
        """
        ...
    
    def OnDropFiles(self, vtkStringArray):
        """
        V.OnDropFiles(vtkStringArray)
        C++: virtual void OnDropFiles(vtkStringArray *filePaths)
        
        When files are dropped on the render window. The argument
        contains the list of file paths dropped. It is called after
        OnDropLocation.
        """
        ...
    
    def OnDropLocation(self, *float):
        """
        V.OnDropLocation([float, ...])
        C++: virtual void OnDropLocation(double *position)
        
        When the mouse location is updated while dragging files. The
        argument contains the position relative to the window of the
        mouse where the files are dropped. It is called before
        OnDropFiles.
        """
        ...
    
    def OnEndPan(self):
        """
        V.OnEndPan()
        C++: virtual void OnEndPan()
        """
        ...
    
    def OnEndPinch(self):
        """
        V.OnEndPinch()
        C++: virtual void OnEndPinch()
        """
        ...
    
    def OnEndRotate(self):
        """
        V.OnEndRotate()
        C++: virtual void OnEndRotate()
        """
        ...
    
    def OnEndSwipe(self):
        """
        V.OnEndSwipe()
        C++: virtual void OnEndSwipe()
        """
        ...
    
    def OnEnter(self):
        """
        V.OnEnter()
        C++: virtual void OnEnter()
        """
        ...
    
    def OnExpose(self):
        """
        V.OnExpose()
        C++: virtual void OnExpose()
        
        These are more esoteric events, but are useful in some cases.
        """
        ...
    
    def OnFifthButtonDown(self):
        """
        V.OnFifthButtonDown()
        C++: virtual void OnFifthButtonDown()
        """
        ...
    
    def OnFifthButtonUp(self):
        """
        V.OnFifthButtonUp()
        C++: virtual void OnFifthButtonUp()
        """
        ...
    
    def OnFourthButtonDown(self):
        """
        V.OnFourthButtonDown()
        C++: virtual void OnFourthButtonDown()
        """
        ...
    
    def OnFourthButtonUp(self):
        """
        V.OnFourthButtonUp()
        C++: virtual void OnFourthButtonUp()
        """
        ...
    
    def OnKeyDown(self):
        """
        V.OnKeyDown()
        C++: virtual void OnKeyDown()
        """
        ...
    
    def OnKeyPress(self):
        """
        V.OnKeyPress()
        C++: virtual void OnKeyPress()
        """
        ...
    
    def OnKeyRelease(self):
        """
        V.OnKeyRelease()
        C++: virtual void OnKeyRelease()
        """
        ...
    
    def OnKeyUp(self):
        """
        V.OnKeyUp()
        C++: virtual void OnKeyUp()
        """
        ...
    
    def OnLeave(self):
        """
        V.OnLeave()
        C++: virtual void OnLeave()
        """
        ...
    
    def OnLeftButtonDown(self):
        """
        V.OnLeftButtonDown()
        C++: virtual void OnLeftButtonDown()
        """
        ...
    
    def OnLeftButtonUp(self):
        """
        V.OnLeftButtonUp()
        C++: virtual void OnLeftButtonUp()
        """
        ...
    
    def OnLongTap(self):
        """
        V.OnLongTap()
        C++: virtual void OnLongTap()
        """
        ...
    
    def OnMiddleButtonDown(self):
        """
        V.OnMiddleButtonDown()
        C++: virtual void OnMiddleButtonDown()
        """
        ...
    
    def OnMiddleButtonUp(self):
        """
        V.OnMiddleButtonUp()
        C++: virtual void OnMiddleButtonUp()
        """
        ...
    
    def OnMouseMove(self):
        """
        V.OnMouseMove()
        C++: virtual void OnMouseMove()
        
        Generic event bindings can be overridden in subclasses
        """
        ...
    
    def OnMouseWheelBackward(self):
        """
        V.OnMouseWheelBackward()
        C++: virtual void OnMouseWheelBackward()
        """
        ...
    
    def OnMouseWheelForward(self):
        """
        V.OnMouseWheelForward()
        C++: virtual void OnMouseWheelForward()
        """
        ...
    
    def OnMove3D(self, vtkEventData):
        """
        V.OnMove3D(vtkEventData)
        C++: virtual void OnMove3D(vtkEventData *)
        
        Generic 3D event bindings can be overridden in subclasses
        """
        ...
    
    def OnPan(self):
        """
        V.OnPan()
        C++: virtual void OnPan()
        """
        ...
    
    def OnPinch(self):
        """
        V.OnPinch()
        C++: virtual void OnPinch()
        """
        ...
    
    def OnRightButtonDown(self):
        """
        V.OnRightButtonDown()
        C++: virtual void OnRightButtonDown()
        """
        ...
    
    def OnRightButtonUp(self):
        """
        V.OnRightButtonUp()
        C++: virtual void OnRightButtonUp()
        """
        ...
    
    def OnRotate(self):
        """
        V.OnRotate()
        C++: virtual void OnRotate()
        """
        ...
    
    def OnStartPan(self):
        """
        V.OnStartPan()
        C++: virtual void OnStartPan()
        """
        ...
    
    def OnStartPinch(self):
        """
        V.OnStartPinch()
        C++: virtual void OnStartPinch()
        """
        ...
    
    def OnStartRotate(self):
        """
        V.OnStartRotate()
        C++: virtual void OnStartRotate()
        """
        ...
    
    def OnStartSwipe(self):
        """
        V.OnStartSwipe()
        C++: virtual void OnStartSwipe()
        
        gesture based events
        """
        ...
    
    def OnSwipe(self):
        """
        V.OnSwipe()
        C++: virtual void OnSwipe()
        """
        ...
    
    def OnTap(self):
        """
        V.OnTap()
        C++: virtual void OnTap()
        """
        ...
    
    def OnTimer(self):
        """
        V.OnTimer()
        C++: virtual void OnTimer()
        
        OnTimer calls Rotate, Rotate etc which should be overridden by
        style subclasses.
        """
        ...
    
    def Pan(self):
        """
        V.Pan()
        C++: virtual void Pan()
        """
        ...
    
    def Rotate(self):
        """
        V.Rotate()
        C++: virtual void Rotate()
        
        These methods for the different interactions in different modes
        are overridden in subclasses to perform the correct motion. Since
        they might be called from OnTimer, they do not have mouse coord
        parameters (use interactor's GetEventPosition and
        GetLastEventPosition)
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkInteractorStyle
        C++: static vtkInteractorStyle *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAutoAdjustCameraClippingRange(self, p_int):
        """
        V.SetAutoAdjustCameraClippingRange(int)
        C++: virtual void SetAutoAdjustCameraClippingRange(
            vtkTypeBool _arg)
        
        If AutoAdjustCameraClippingRange is on, then before each render
        the camera clipping range will be adjusted to "fit" the whole
        scene. Clipping will still occur if objects in the scene are
        behind the camera or come very close. If
        AutoAdjustCameraClippingRange is off, no adjustment will be made
        per render, but the camera clipping range will still be reset
        when the camera is reset.
        """
        ...
    
    def SetEnabled(self, p_int):
        """
        V.SetEnabled(int)
        C++: void SetEnabled(int) override;
        
        Turn on/off this interactor. Interactor styles operate a little
        bit differently than other types of interactor observers. When
        the SetInteractor() method is invoked, the automatically enable
        themselves. This is a legacy requirement, and convenient for the
        user.
        """
        ...
    
    def SetHandleObservers(self, p_int):
        """
        V.SetHandleObservers(int)
        C++: virtual void SetHandleObservers(vtkTypeBool _arg)
        
        Does ProcessEvents handle observers on this class or not
        """
        ...
    
    def SetInteractor(self, vtkRenderWindowInteractor):
        """
        V.SetInteractor(vtkRenderWindowInteractor)
        C++: void SetInteractor(vtkRenderWindowInteractor *interactor)
            override;
        
        Set/Get the Interactor wrapper being controlled by this object.
        (Satisfy superclass API.)
        """
        ...
    
    def SetMouseWheelMotionFactor(self, p_float):
        """
        V.SetMouseWheelMotionFactor(float)
        C++: virtual void SetMouseWheelMotionFactor(double _arg)
        
        Set/Get the mouse wheel motion factor. Default to 1.0. Set it to
        a different value to emphasize or de-emphasize the action
        triggered by mouse wheel motion.
        """
        ...
    
    def SetPickColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetPickColor(float, float, float)
        C++: virtual void SetPickColor(double _arg1, double _arg2,
            double _arg3)
        V.SetPickColor((float, float, float))
        C++: virtual void SetPickColor(const double _arg[3])
        
        Set/Get the pick color (used by default to color vtkActor2D's).
        The color is expressed as red/green/blue values between
        (0.0,1.0).
        """
        ...
    
    def SetTDxStyle(self, vtkTDxInteractorStyle):
        """
        V.SetTDxStyle(vtkTDxInteractorStyle)
        C++: virtual void SetTDxStyle(vtkTDxInteractorStyle *tdxStyle)
        
        3Dconnexion device interactor style. Initial value is a pointer
        to an object of class vtkTdxInteractorStyleCamera.
        """
        ...
    
    def SetTimerDuration(self, p_int):
        """
        V.SetTimerDuration(int)
        C++: virtual void SetTimerDuration(unsigned long _arg)
        
        If using timers, specify the default timer interval (in
        milliseconds). Care must be taken when adjusting the timer
        interval from the default value of 10 milliseconds--it may
        adversely affect the interactors.
        """
        ...
    
    def SetUseTimers(self, p_int):
        """
        V.SetUseTimers(int)
        C++: virtual void SetUseTimers(vtkTypeBool _arg)
        
        Set/Get timer hint
        """
        ...
    
    def Spin(self):
        """
        V.Spin()
        C++: virtual void Spin()
        """
        ...
    
    def StartAnimate(self):
        """
        V.StartAnimate()
        C++: virtual void StartAnimate()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StartDolly(self):
        """
        V.StartDolly()
        C++: virtual void StartDolly()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StartEnvRotate(self):
        """
        V.StartEnvRotate()
        C++: virtual void StartEnvRotate()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StartGesture(self):
        """
        V.StartGesture()
        C++: virtual void StartGesture()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StartPan(self):
        """
        V.StartPan()
        C++: virtual void StartPan()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StartRotate(self):
        """
        V.StartRotate()
        C++: virtual void StartRotate()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StartSpin(self):
        """
        V.StartSpin()
        C++: virtual void StartSpin()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StartState(self, p_int):
        """
        V.StartState(int)
        C++: virtual void StartState(int newstate)
        
        utility routines used by state changes
        """
        ...
    
    def StartTimer(self):
        """
        V.StartTimer()
        C++: virtual void StartTimer()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StartTwoPointer(self):
        """
        V.StartTwoPointer()
        C++: virtual void StartTwoPointer()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StartUniformScale(self):
        """
        V.StartUniformScale()
        C++: virtual void StartUniformScale()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StartZoom(self):
        """
        V.StartZoom()
        C++: virtual void StartZoom()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StopAnimate(self):
        """
        V.StopAnimate()
        C++: virtual void StopAnimate()
        
        Interaction mode entry points used internally.
        """
        ...
    
    def StopState(self):
        """
        V.StopState()
        C++: virtual void StopState()
        
        utility routines used by state changes
        """
        ...
    
    def UniformScale(self):
        """
        V.UniformScale()
        C++: virtual void UniformScale()
        """
        ...
    
    def UseTimersOff(self):
        """
        V.UseTimersOff()
        C++: virtual void UseTimersOff()
        
        Set/Get timer hint
        """
        ...
    
    def UseTimersOn(self):
        """
        V.UseTimersOn()
        C++: virtual void UseTimersOn()
        
        Set/Get timer hint
        """
        ...
    
    def Zoom(self):
        """
        V.Zoom()
        C++: virtual void Zoom()
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


