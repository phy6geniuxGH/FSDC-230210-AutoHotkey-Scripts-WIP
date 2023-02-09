; Mouse Click
CoordMode Mouse, Screen
MouseMove 1158, 1212, 10
MouseClick Left
Sleep, 100
Send {CtrlDown}{End}{CtrlUp}
Sleep, 100
Send {CtrlDown}{ShiftDown}{AltDown}E{CtrlUp}{ShiftUp}{AltUp}
Sleep, 100
Send {CtrlDown}V{CtrlUp}
Sleep, 100
Send {Enter}
Sleep, 100
Send {Enter}
Sleep, 100
MouseMove 178, 832, 5
SendEvent {Click 178 832 Down}{click 317 444 Up}
MouseMove 3354, 144, 5
Sleep, 100
MouseClick, Left
Sleep, 100
Send, {ShiftDown}{Tab}
Sleep, 100
Send {Down}