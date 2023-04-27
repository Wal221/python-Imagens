import cv2
# abrindo a imagem
img = cv2.imread("folha.jpg")
# Detectando as bordas da imagem
bordas = cv2.Canny(img, 200, 300, True)
# Mostrando as imagens
cv2.imshow('Imagem original', img)
cv2.imshow('Bordas da imagem', bordas)

# Esperando alguma tecla ser pressionada
cv2.waitKey(0)
# Destruindo as janelas com as imagens
cv2.destroyAllWindows()

