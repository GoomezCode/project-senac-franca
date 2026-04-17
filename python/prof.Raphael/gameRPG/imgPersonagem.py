# Artes em ASCII usando raw strings (r"")
guerreiro = r"""
     ___
    [___]   /)
    (o_o)  //
    /] [\_//
   //| |\//
  // | | /
 (/  | |
    /   \
   /_____\
"""

mago = r"""
      *
      A
     /_\
    (o_o)   |
    / | \_  |
   /  |   \ |
  |___|___| O
   |     |
   |_____|
    /   \
   /_____\
"""

arqueiro = r"""
     ___
    /   \    )
   (o_o)    /
   / | \_  /
  /  |   \ \
 |___|___|  )
    /  \   /
   /____\ /
"""

aventureiro = r"""
     ___
    / _ \    (
   (o_o)    )\
   /] [\_ _//
  [X]| | \//
  [X]| |  /
 (_//   \
   /_____\
"""

# Função simples para testar a exibição no console
def mostrar_classes(nStatus):
    
    if nStatus.lower() == "guerreiro":
        return guerreiro    
    if nStatus.lower() == "mago":
        return mago
    if nStatus.lower() == "arqueiro":
        return arqueiro
    if nStatus.lower() == "aventureiro":
        return aventureiro
