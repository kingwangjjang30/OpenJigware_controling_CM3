import clr
clr.AddReference("OpenJigWare")
from OpenJigWare import Ojw

COjw = Ojw()
m_CMot = Ojw.CProtocol2()
# 통신포트 열어주기
m_CMot.Open(36, 1000000)


# 1, 2번 다이나믹셀의 위치 읽어오기
#m_CMot.SyncRead(1,2,3,4,5)

# 토크를 넣어준다.
m_CMot.SetTorq(True)
m_CMot.SyncRead(1,2,3,4,5)
m_CMot.Wait(3000)

#for i in range(0,3):
while (True):
    # 1, 2번 다이나믹셀을 둘다 90도 위치로 변경
    m_CMot.PlayFrameString("S2,1000,0,1:-90,2:30,3:30,4:-50,5:0")

    m_CMot.PlayFrameString("S2,500,0,1:-90,2:30,3:30,4:-50,5:-140")

    m_CMot.PlayFrameString("S2,500,0,1:-90,2:20,3:30,4:-50,5:-140")

    m_CMot.PlayFrameString("S2,1000,0,1:0,2:0,3:-20,4:0,5:-140")

    m_CMot.PlayFrameString("S2,1000,0,1:0,2:0,3:-60,4:0,5:-140")

    m_CMot.PlayFrameString("S2,1000,0,1:0,2:0,3:-20,4:0,5:-140")

    m_CMot.PlayFrameString("S2,1000,0,1:-90,2:20,3:30,4:-50,5:-140")

    m_CMot.PlayFrameString("S2,500,0,1:-90,2:20,3:30,4:-50,5:-140")

    m_CMot.PlayFrameString("S2,1000,0,1:-90,2:30,3:30,4:-50,5:-140")

    m_CMot.PlayFrameString("S2,500,0,1:-90,2:30,3:30,4:-50,5:-0")

    anPorts = Ojw.CSerial.GetPorts()
    for nPort in anPorts:
        print(nPort)
# 통신을 닫는다.
m_CMot.Close()

    # m_CSerial = Ojw.CSerial()
    # m_CSerial.Connect(12, 115200)
    # #m_CSerial.Send("L")
    # #m_CSerial.SendPacket("L")
    # #if (m_CSerial.IsConnect() == True):
    # m_CSerial.SendPacket(Ojw.CConvert.StrToBytes("L"))
    # # while m_CSerial.GetBuffer_Length() < 0 :
    # #     if m_CSerial.GetBuffer_Length() > 0 :
    # #         a = m_CSerial.GetByte()
    # #         if a == 'E' :
    # #             break
    # #Ojw.CTimer.Wait(2000)
    # #Time.sleep(5)
    # #m_CSerial.SendPacket(Ojw.CConvert.StrToBytes("R"))
    # m_CSerial.DisConnect()


# 위치를 0으로 변경
#m_CMot.PlayFrameString("S2,1000,0,2:0,1:0,3:30")
#m_CMot.Wait(3000)


# 1, 2번 다이나믹셀을 둘다 90도 위치로 변경
#m_CMot.PlayFrameString("S2,1000,0,1:90,2:90,3:90")

# 위치를 0으로 변경
#m_CMot.PlayFrameString("S2,1000,0,2:0,1:-30,3:30")

# PC의 Comport를 체크한다.
#strPorts = Ojw.CSerial.GetPortNames()
#for strPort in strPorts:
#    print(strPort)

    # m_CMot.PlayFrameString("S2,1000,0,1:-90,2:-30,3:60,4:-30,5:0")

    # m_CMot.PlayFrameString("S2,500,0,1:-0,2:-50,3:80,4:-50,5:-140")

    # m_CMot.PlayFrameString("S2,2000,0,1:0,2:0,3:-20,4:0,5:-140")

    # m_CMot.PlayFrameString("S2,1000,0,1:0,2:0,3:-60,4:0,5:-140")

    # m_CMot.PlayFrameString("S2,1000,0,1:0,2:0,3:-20,4:0,5:-140")

    # m_CMot.PlayFrameString("S2,2000,0,1:-50,2:-50,3:80,4:-50,5:-140")

    # m_CMot.PlayFrameString("S2,500,0,1:-50,2:-50,3:80,4:-50,5:0")