#tkinter MinerGUI

import tkinter

print('What is the path to the config.txt file?')
pathname = input()      
window = tkinter.Tk()
window.title("Acdop100's GUI for Claymore Miner")
window.geometry("400x550")


def callback():
    savelbl.configure(text="Saved!")
    ethpool = poolwindow.get()
    ethwallet = walletwindow.get()
    ethpswd = pswdwindow.get()
    temp = tempwindow.get()
    dual = dualwindow.get()
    dcoin = coinwindow.get()
    dpool = coinpoolwindow.get()
    dwal = coinwalletwindow.get()
    dpswd = coinpswdwindow.get()
    config = open (pathname, "w")
    config.write("-epool " + ethpool + "\n")
    config.write("-ewal "+ ethwallet + "\n")
    config.write("-epsw "+ ethpswd + "\n")
    config.write("-tt "+ temp + "\n")
    if dual == 'y':
        config.write("-mode 0" + "\n")
        config.write("-dcoin "+ dcoin + "\n")
        config.write("-dpool "+ dpool + "\n")
        config.write("-dwal "+ dwal + "\n")
        config.write("-dpswd "+ dpswd + "\n")
        
    else:
        config.write("-mode 1" + "\n")



poollbl = tkinter.Label(window, text="Pool Address")
poolwindow = tkinter.Entry(window)

walletlbl = tkinter.Label(window, text="Wallet Address")
walletwindow = tkinter.Entry(window)

pswdlbl = tkinter.Label(window, text="Pool Password")
pswdwindow = tkinter.Entry(window)

templbl = tkinter.Label(window, text="Target GPU Temperature")
tempwindow = tkinter.Entry(window)

duallbl = tkinter.Label(window, text="Are You Dual Mining? (y/n)")
dualwindow = tkinter.Entry(window)

coinlbl = tkinter.Label(window, text="If So, Which Coin?")
coinwindow = tkinter.Entry(window)

coinwalletlbl = tkinter.Label(window, text="2nd Coin Wallet Address")
coinwalletwindow = tkinter.Entry(window)

coinpoollbl = tkinter.Label(window, text="2nd Coin Pool Address")
coinpoolwindow = tkinter.Entry(window)

coinpswdlbl = tkinter.Label(window, text="2nd Coin Pool Password")
coinpswdwindow = tkinter.Entry(window)

savelbl = tkinter.Label(window, text="Ready So Save")
savewindow = tkinter.Entry(window)

savebtn = tkinter.Button(window, text ="Save To Config.txt", command=callback)


poollbl.pack()
poolwindow.pack()
walletlbl.pack()
walletwindow.pack()
pswdlbl.pack()
pswdwindow.pack()
templbl.pack()
tempwindow.pack()
duallbl.pack()
dualwindow.pack()
coinlbl.pack()
coinwindow.pack()
coinwalletlbl.pack()
coinwalletwindow.pack()
coinpoollbl.pack()
coinpoolwindow.pack()
coinpswdlbl.pack()
coinpswdwindow.pack()
savelbl.pack()
savebtn.pack()

window.mainloop()
