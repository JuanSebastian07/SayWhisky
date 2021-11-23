import pyautogui
import cv2

lista=[]

def coordenada_inicial():
    pyautogui.moveTo(830, 259, duration=0.25)
    x,y = pyautogui.position()
    #print(x,y)
    return x,y

#print(f'--->{type(coordenada_inicial())}')
coordenada_final=(830, 259)

try:
    while coordenada_inicial() == coordenada_final:
        x,y = pyautogui.position()
        positionStr = f'{x} {y}'
        print("\r [+] posicion : " + positionStr, end='')
       
        
except KeyboardInterrupt:
        exit()


for i in range(1):
    cap = cv2.VideoCapture(0)
    leido, frame = cap.read()

    if leido == True:
        cv2.imwrite("foto.png", frame)
        print("Foto tomada correctamente")
    else:
        print("Error al acceder a la cámara")
