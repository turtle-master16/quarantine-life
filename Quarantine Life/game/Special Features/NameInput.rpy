# Python init
init python:
    text_list1=["0","1","2","3","4","5","6","7","8","9", ".",
                    "Q","W","E","R","T","Y","U","I","O","P",".",
                      "A","S","D","F","G","H","J","K","L",".",
                      "Z","X","C","V","B","N","M",".",
                      "@","&", "!", "#", "$", "%", "*", "(", ")","."]
    text_list2=["0","1","2","3","4","5","6","7","8","9", ".",
                    "q","w","e","r","t","y","u","i","o","p",".",
                      "a","s","d","f","g","h","j","k","l",".",
                      "z","x","c","v","b","n","m",".",
                      "@","&", "!", "#", "$", "%", "*", "(", ")","."]
    input_text = 'Coby'
    text_limit = 10
    text_list=text_list1
    text_group=1

label inputter:
    if text_group==1:
          $text_list=text_list1
    elif text_group==2:
          $text_list=text_list2

    $ ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0, xsize=800)
    $ ui.vbox(xalign=0.5)
    $ ui.text(input_text, yoffset=20, size=50, xalign=0.5)
    $ ui.null(height=30)
    $ ui.hbox(xalign=0.5)
    if text_group==1:
        $ ui.textbutton("Upper Case", xpadding=40, text_size=30)
        $ ui.textbutton("Lower Case", clicked=ui.returns("locase"), xpadding=40, text_size=30)
    elif text_group==2:
        $ ui.textbutton("Upper Case", clicked=ui.returns("upcase"), xpadding=40, text_size=30)
        $ ui.textbutton("Lower Case", xpadding=40, text_size=30)
    $ ui.close()

    if input_text:
        $ ui.hbox(xalign=0.5)
        $ ui.textbutton("Done", clicked=ui.returns("Done"), xpadding=40, text_size=30)
        $ui.textbutton("Backspace", clicked=ui.returns("Backspace"), xpadding=40, text_size=30)
        $ui.textbutton("Delete all", clicked=ui.returns("Deleteall"), xpadding=40, text_size=30)
        $ ui.close()
    else:
        $ ui.hbox(xalign=0.5)
        $ ui.textbutton("Done", xpadding=40, text_size=30)
        $ui.textbutton("Backspace", clicked=ui.returns("Backspace"), xpadding=40, text_size=30)
        $ui.textbutton("Delete all", clicked=ui.returns("Deleteall"), xpadding=40, text_size=30)
        $ ui.close()

    $ ui.hbox(xalign=0.5, spacing=40)
    python:
        for text_code in text_list:
                if text_code==".":
                    ui.close()
                    ui.hbox(xalign= 0.5, spacing=40, background="images/bg/bg livingroom back.png")
                elif  len(input_text)<=text_limit-1:
                    ui.textbutton(text_code, clicked=ui.returns(text_code), text_size=50)
    $ ui.close()
    $ ui.close()
    $ button_selection=ui.interact()

    if button_selection=="Backspace":
            $ input_text=input_text[:-1]
            jump inputter
    elif button_selection=="Deleteall":
            $ input_text=''
            jump inputter
    elif button_selection=="upcase":
           $text_group=1
           jump inputter
    elif button_selection=="locase":
           $text_group=2
           jump inputter
    elif button_selection=="Done":
           return
    $ select_text=button_selection

    python:
            for text_code in text_list:
                    if select_text==text_code:
                        input_text += text_code
    jump inputter
