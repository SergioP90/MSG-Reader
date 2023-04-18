# pip install imapclient
# pip install extract-msg

import extract_msg
print('Especifica el nombre del archivo (debe estar en la misma carpeta e incluir el .msg): ')
f = input()

msg = extract_msg.Message(f)
msg_sender = msg.sender
msg_date = msg.date
msg_subj = msg.subject
msg_message = msg.body

print('Remitente: {}'.format(msg_sender))
print('Fecha de envio: {}'.format(msg_date))
print('Asunto: {}'.format(msg_subj))
print('Cuerpo: {}'.format(msg_message))

d = open('Contenido.txt', 'w')
d.write('Remitente: {}'.format(msg_sender))
d.write('Fecha de envio: {}'.format(msg_date))
d.write('Asunto: {}'.format(msg_subj))
d.write('Cuerpo: {}'.format(msg_message))
d.close()

print('Presiona cualquier tecla para cerrar')
input()
