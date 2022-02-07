from tkinter import *
from tkinter import Tk

# LOGIN CHECK

def entrar():
    email = txtboxemail_log.get()
    senha = txtboxpass_log.get()

    if (email=="" or senha==""):
            erro_blank = Label(LoginFrame, text="Preencha os campos obrigatórios.", background='#111111', font="Segoe 20", fg="red")
            erro_blank.place(relwidth=1, relx=0.5, rely=0.65, anchor=CENTER)

    else:

        if email == "crypto_viewer_user" and senha == "senhacv123":

            # MAIN FRAME

            root.destroy()
            main = Tk()
            main.configure(background='#111111')
            main.title("Crypto Viewer")
            main.attributes('-fullscreen', True)

            # HEADER

            headerFrame = Frame(main, background='#111111')
            headerFrame.place(relwidth=1, relheight=0.2)

            logo = Label(headerFrame, text="Crypto Viewer", background='#111111', font="Segoe 30 bold", fg="white")
            logo.place(relwidth=1, relheight=1)

            def exit():
                main.destroy()

            exit_bttn = Button(headerFrame, text="X", border="0", bg='#FF0000', fg="white", font="Segoe 20 bold", cursor="hand2", command=exit)
            exit_bttn.place(relwidth=0.03, relheight=0.25, relx=0.97)

            # SELECT CRYPTO

            MainFrame = Frame(main, background='#111111')
            MainFrame.place(relwidth=1, relheight=0.6, rely=0.2)

            def sol_page():
                
                sol = Tk()
                sol.configure(background='#111111')
                sol.title("Crypto Viewer")
                sol.attributes('-fullscreen', True)

                # HEADER

                headerFrame = Frame(sol, background='#111111')
                headerFrame.place(relwidth=1, relheight=0.2)

                logo = Label(headerFrame, text="Crypto Viewer", background='#111111', font="Segoe 30 bold", fg="white")
                logo.place(relwidth=1, relheight=1)

                def exit():
                    main.destroy()
                    sol.destroy()
                    ws.close()

                exit_bttn = Button(headerFrame, text="X", border="0", bg='#FF0000', fg="white", font="Segoe 20 bold", cursor="hand2", command=exit)
                exit_bttn.place(relwidth=0.03, relheight=0.25, relx=0.97)

                # INFO SOL

                sol_frame = Frame(sol, background='#111111')
                sol_frame.place(relwidth=1, relheight=0.6, rely=0.2)

                label_sol = Label(sol_frame, text="SOLANA / DOLAR - SOLUSDT", border="0", bg='#111111', fg="white", font="Segoe 30 bold")
                label_sol.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.25)

                lb_loading_sol = Label(sol_frame, text="Carregando...", border="0", bg='#111111', fg="white", font="Segoe 30 bold")
                lb_loading_sol.place(relwidth=0.35, relheight=0.1, relx=0.325, rely=0.4)

                import json, websocket

                SOCKET = "wss://stream.binance.com:9443/ws/solusdt@kline_1m"

                def on_message(ws, message):

                    valor_sol = json.loads(message)['k']['c']

                    def show_sol():

                        lb_val_sol = Label(sol_frame, text=valor_sol, border="0", bg='#FFFFFF', fg="black", font="Segoe 30 bold")
                        lb_val_sol.place(relwidth=0.35, relheight=0.1, relx=0.325, rely=0.4)

                    show_sol()

                ws = websocket.WebSocketApp(SOCKET, on_message=on_message)

                def back_sol():
                    sol.destroy()
                    ws.close()

                sol_back = Button(sol_frame, text="Voltar", border="0", bg='black', fg="white", font="Segoe 30 bold", cursor="hand2", command=back_sol)
                sol_back.place(relwidth=0.1, relheight=0.08, relx=0.45, rely=0.6)

                # RUN WS

                def connect_to_socket():

                    ws.run_forever()

                def on_connect():
                    import threading
                    t = threading.Thread(target=connect_to_socket)
                    t.start()

                on_connect()

                # RUN SOL

                sol.mainloop()


            def btc_page():
                
                btc = Tk()
                btc.configure(background='#111111')
                btc.title("Crypto Viewer")
                btc.attributes('-fullscreen', True)

                # HEADER

                headerFrame = Frame(btc, background='#111111')
                headerFrame.place(relwidth=1, relheight=0.2)

                logo = Label(headerFrame, text="Crypto Viewer", background='#111111', font="Segoe 30 bold", fg="white")
                logo.place(relwidth=1, relheight=1)

                def exit():
                    main.destroy()
                    btc.destroy()
                    ws.close()

                exit_bttn = Button(headerFrame, text="X", border="0", bg='#FF0000', fg="white", font="Segoe 20 bold", cursor="hand2", command=exit)
                exit_bttn.place(relwidth=0.03, relheight=0.25, relx=0.97)

                # INFO BTC

                btc_frame = Frame(btc, background='#111111')
                btc_frame.place(relwidth=1, relheight=0.6, rely=0.2)

                label_btc = Label(btc_frame, text="BITCOIN / DOLAR - BTCUSDT", border="0", bg='#111111', fg="white", font="Segoe 30 bold")
                label_btc.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.25)

                lb_loading_btc = Label(btc_frame, text="Carregando...", border="0", bg='#111111', fg="white", font="Segoe 30 bold")
                lb_loading_btc.place(relwidth=0.35, relheight=0.1, relx=0.325, rely=0.4)

                import json, websocket

                SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"

                def on_message(ws, message):

                    valor_btc = json.loads(message)['k']['c']

                    def show_btc():

                        lb_val_btc = Label(btc_frame, text=valor_btc, border="0", bg='#FFFFFF', fg="black", font="Segoe 30 bold")
                        lb_val_btc.place(relwidth=0.35, relheight=0.1, relx=0.325, rely=0.4)

                    show_btc()

                ws = websocket.WebSocketApp(SOCKET, on_message=on_message)

                def back_btc():
                    btc.destroy()
                    ws.close()

                btc_back = Button(btc_frame, text="Voltar", border="0", bg='black', fg="white", font="Segoe 30 bold", cursor="hand2", command=back_btc)
                btc_back.place(relwidth=0.1, relheight=0.08, relx=0.45, rely=0.6)

                # RUN WS

                def connect_to_socket():

                    ws.run_forever()

                def on_connect():
                    import threading
                    t = threading.Thread(target=connect_to_socket)
                    t.start()

                on_connect()

                # RUN BTC

                btc.mainloop()


            def eth_page():
                eth = Tk()
                eth.configure(background='#111111')
                eth.title("Crypto Viewer")
                eth.attributes('-fullscreen', True)

                # HEADER

                headerFrame = Frame(eth, background='#111111')
                headerFrame.place(relwidth=1, relheight=0.2)

                logo = Label(headerFrame, text="Crypto Viewer", background='#111111', font="Segoe 30 bold", fg="white")
                logo.place(relwidth=1, relheight=1)

                def exit():
                    main.destroy()
                    eth.destroy()
                    ws.close()

                exit_bttn = Button(headerFrame, text="X", border="0", bg='#FF0000', fg="white", font="Segoe 20 bold", cursor="hand2", command=exit)
                exit_bttn.place(relwidth=0.03, relheight=0.25, relx=0.97)

                # INFO ETH

                eth_frame = Frame(eth, background='#111111')
                eth_frame.place(relwidth=1, relheight=0.6, rely=0.2)

                label_eth = Label(eth_frame, text="ETHEREUM / DOLAR - ETHUSDT", border="0", bg='#111111', fg="white", font="Segoe 30 bold")
                label_eth.place(relwidth=0.5, relheight=0.1, relx=0.25, rely=0.25)

                lb_loading_eth = Label(eth_frame, text="Carregando...", border="0", bg='#111111', fg="white", font="Segoe 30 bold")
                lb_loading_eth.place(relwidth=0.35, relheight=0.1, relx=0.325, rely=0.4)

                import json, websocket

                SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

                def on_message(ws, message):

                    valor_eth = json.loads(message)['k']['c']

                    def show_eth():

                        lb_val_btc = Label(eth_frame, text=valor_eth, border="0", bg='#FFFFFF', fg="black", font="Segoe 30 bold")
                        lb_val_btc.place(relwidth=0.35, relheight=0.1, relx=0.325, rely=0.4)

                    show_eth()

                ws = websocket.WebSocketApp(SOCKET, on_message=on_message)

                def back_eth():
                    eth.destroy()
                    ws.close()

                eth_back = Button(eth_frame, text="Voltar", border="0", bg='black', fg="white", font="Segoe 30 bold", cursor="hand2", command=back_eth)
                eth_back.place(relwidth=0.1, relheight=0.08, relx=0.45, rely=0.6)

                # RUN WS

                def connect_to_socket():

                    ws.run_forever()

                def on_connect():
                    import threading
                    t = threading.Thread(target=connect_to_socket)
                    t.start()

                on_connect()

                # RUN ETH

                eth.mainloop()

            btc_bttn = Button(MainFrame, text="BTC", border="1", bg='#FFFFFF', fg="black", font="Segoe 30 bold", cursor="hand2", command=btc_page)
            btc_bttn.place(relwidth=0.1, relheight=0.08, relx=0.45, rely=0.3)

            eth_bttn = Button(MainFrame, text="ETH", border="1", bg='#FFFFFF', fg="black", font="Segoe 30 bold", cursor="hand2", command=eth_page)
            eth_bttn.place(relwidth=0.1, relheight=0.08, relx=0.45, rely=0.5)

            sol_bttn = Button(MainFrame, text="SOL", border="1", bg='#FFFFFF', fg="black", font="Segoe 30 bold", cursor="hand2", command=sol_page)
            sol_bttn.place(relwidth=0.1, relheight=0.08, relx=0.45, rely=0.7)

            # RUN MAIN

            main.mainloop()

        else:
            erro_invalidade = Label(LoginFrame, text="Usuário ou senha inválidos. Tente novamente.", background='#111111', font="Segoe 20", fg="red")
            erro_invalidade.place(relwidth=1, relx=0.5, rely=0.65, anchor=CENTER)

    # DEF EXIT

    def exit():
        root.destroy()

# INFO PAGE

def info():

    txt_info_1 = "Crypto Viewer é um projeto Python desenvilvido para a visualização em tempo real do valor de criptomoedas."
    txt_info_2 = "Desenvolvido por Henrique Soriano, estudante de Análise e desenvolvimento de Sistemas - Etec Polivalente Americana"
    txt_info_3 = "email: sorianol.henrique@gmail.com"
    txt_info_4 = "LinkedIn: linkedin.com/in/henrique-soriano-b6b623226"

    # INFO FRAME

    root.destroy()
    info = Tk()
    info.configure(background='#111111')
    info.title("Crypto Viewer")
    info.attributes('-fullscreen', True)

    # HEADER

    headerFrame = Frame(info, background='#111111')
    headerFrame.place(relwidth=1, relheight=0.2)

    logo = Label(headerFrame, text="Crypto Viewer", background='#111111', font="Segoe 30 bold", fg="white")
    logo.place(relwidth=1, relheight=1)

    def exit():
        info.destroy()

    exit_bttn = Button(headerFrame, text="X", border="0", bg='#FF0000', fg="white", font="Segoe 20 bold", cursor="hand2", command=exit)
    exit_bttn.place(relwidth=0.03, relheight=0.25, relx=0.97)

    # INFO

    info_frame = Frame(info, background='#111111')
    info_frame.place(relwidth=1, relheight=0.6, rely=0.2)

    lb_loading_eth = Label(info_frame, text=txt_info_1, border="0", bg='#111111', fg="white", font="Segoe 15 bold")
    lb_loading_eth.place(relwidth=1, relheight=0.1, rely=0.3)

    lb_loading_eth = Label(info_frame, text=txt_info_2, border="0", bg='#111111', fg="white", font="Segoe 15 bold")
    lb_loading_eth.place(relwidth=1, relheight=0.1, rely=0.4)

    lb_loading_eth = Label(info_frame, text=txt_info_3, border="0", bg='#111111', fg="white", font="Segoe 15 bold")
    lb_loading_eth.place(relwidth=1, relheight=0.1, rely=0.5)

    lb_loading_eth = Label(info_frame, text=txt_info_4, border="0", bg='#111111', fg="white", font="Segoe 15 bold")
    lb_loading_eth.place(relwidth=1, relheight=0.1, rely=0.6)

# MAIN INITIAL FRAME

root = Tk()
root.configure(background='#111111')
root.title("Crypto Viewer")
root.attributes('-fullscreen', True)

# HEADER

headerFrame = Frame(root, background='#111111')
headerFrame.place(relwidth=1, relheight=0.2)

logo = Label(headerFrame, text="Crypto Viewer", background='#111111', font="Segoe 30 bold", fg="white")
logo.place(relwidth=1, relheight=1)

def exit():
        root.destroy()

exit_bttn = Button(headerFrame, text="X", border="0", bg='#FF0000', fg="white", font="Segoe 20 bold", cursor="hand2", command=exit)
exit_bttn.place(relwidth=0.03, relheight=0.25, relx=0.97)

# LOGIN

LoginFrame = Frame(root, background='#111111')
LoginFrame.place(relwidth=1, relheight=0.6, rely=0.2)


l_entrar = Label(LoginFrame, text="ENTRAR", background='#111111', font="Segoe 15 bold", fg="white")
l_entrar.place(relwidth=1, relheight=0.2)


l_email = Label(LoginFrame, text="Usuário", background='#111111', font="Segoe 15", fg="white")
l_email.place(relwidth=1, relheight=0.2, rely=0.15)

txtboxemail_log = Entry(LoginFrame, bg="#222222", border=0, fg="white", font="Segoe 15")
txtboxemail_log.place(relwidth=0.3, relheight=0.05, relx=0.35, rely=0.3)


l_pass = Label(LoginFrame, text="Senha", background='#111111', font="Segoe 15", fg="white")
l_pass.place(relwidth=1, relheight=0.2, rely=0.35)

txtboxpass_log = Entry(LoginFrame, bg="#222222", border=0, fg="white", font="Segoe 15", show="*")
txtboxpass_log.place(relwidth=0.3, relheight=0.05, relx=0.35, rely=0.5)

login_bttn = Button(LoginFrame, text="ENTRAR", border="0", bg='#222222', fg="white", font="Segoe 20 bold", cursor="hand2", command=entrar)
login_bttn.place(relwidth=0.1, relheight=0.085, relx=0.45, rely=0.75)

login_bttn = Button(LoginFrame, text="?", border="0", bg='white', fg="black", font="Segoe 16 bold", cursor="hand2", command=info)
login_bttn.place(relwidth=0.02, relheight=0.06, relx=0.8, rely=0.9)

# RUN ROOT

root.mainloop()